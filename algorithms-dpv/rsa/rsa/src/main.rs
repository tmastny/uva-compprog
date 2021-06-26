// "RSA keys are typically 2048 to 4096 bits long"
// https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Integer_factorization_and_RSA_problem

// Faulty key generation:
//  - Fermat factorization can work if `p` and `q` are close together
//  - p - 1 and q - 1 can also be factored if they have only small prime factors
//  - if q < p < 2q, then d > n^.25 / 3
//  - primes p,q must be generated with a strong random number generator
// https://crypto.stanford.edu/~dabo/pubs/papers/RSA-survey.pdf

use std::collections::BTreeMap;

struct Euclid {
    x: i32,
    y: i32,
    d: i32
}

struct PublicKey {
    n: i32,
    e: i32
}

fn extended_euclidean(a: i32, b: i32) -> Euclid {
    if b == 0 { return Euclid {x: 1, y: 0, d: a}; }

    let result = extended_euclidean(b, a % b);
    return Euclid {x: result.y, y: result.x - a / b * result.y, d: result.d};
}

fn gcd(a: i32, b: i32) -> i32 {
    return extended_euclidean(a, b).d;
}

fn inverse(a: i32, n: i32) -> i32 {
    return (n + extended_euclidean(a, n).x) % n;
}

fn modexp(x: i32, y: i32, n: i32) -> i32 {
    if y == 0 { return 1; }

    let z = modexp(x, y / 2, n);

    if y % 2 == 0 { return z * z % n; }

    return x * z * z % n;
}

fn factors_from_roots(n: i32, e: i32, d: i32) -> Vec<i32> {
    let exp = e * d - 1;
    let mut factors = Vec::new();

    println!("Element    Exp  Roots          gcd");
    for i in 2..n {
        let mut roots = Vec::new();
        let mut factor = 1;
        let mut root_exp = exp;
        while root_exp % 2 == 0 && root_exp / 2 >= 0 {
            let a = modexp(i, root_exp / 2, n);
            roots.push(a);
            if a != 1 && a != -1 {
                factor = gcd(a - 1, n);
                break;
            } else if a == -1 {
                break;
            }
            root_exp /= 2;
        }
        factors.push(factor);
        println!("{:<11}{:<5}{:<15}{}", i, root_exp, format!("{:?}", roots), factor);
    }

    return factors;
}

fn find_public_inverse(exp_mod: i32) -> i32 {
    for elem in 3..exp_mod {
        if gcd(elem, exp_mod) == 1 {
            return elem
        }
    }
    return 3;
}



fn main() {
    let e = extended_euclidean(25, 11);
    println!("Bezout's identity:");
    println!("{} = 25 * {} + 11 * {}", e.d, e.x, e.y);


    println!("\nProblem 1.27");
    let public_key = PublicKey {n: 391, e: 3};
    let message = 41;
    let encoded_message = modexp(message, public_key.e, public_key.n);

    let secret_key = inverse(public_key.e, (17 - 1) * (23 - 1));
    println!("Decoded message is {}", modexp(encoded_message, secret_key, public_key.n));




    println!("\nProblem 1.28");
    let p = 7;
    let q = 11;
    let n = p * q;
    let exp_mod = (p - 1) * (q - 1);
    let e = find_public_inverse(exp_mod);

    println!("Public key: (N = {}, e = {})", n, e);

    let d = inverse(e, exp_mod);
    println!("Secret key: {}", d);

    println!("\nProblem 1.42");

    let p = 3;
    let q = 5;
    let n = p * q;
    let exp_mod = (p - 1) * (q - 1);
    let e = find_public_inverse(exp_mod);
    let d = inverse(e, exp_mod);

    println!("Given (N = {}, e = {}, d = {}), find the factors of N.", n, e, d);
    let factors = factors_from_roots(n, e, d);

    let mut m = BTreeMap::new();
    for f in &factors {
        *m.entry(f).or_insert(0) += 1;
    }

    println!("Factors of n and count of roots: {:?}", m);

    println!("\nProblem 1.45(c)");
    // todo

    println!("\nProblem 1.45(d)");
    println!("{}", inverse(17, (17 - 1) * (23 - 1)));
}
