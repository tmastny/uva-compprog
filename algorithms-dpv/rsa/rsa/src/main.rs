// "RSA keys are typically 2048 to 4096 bits long"
// https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Integer_factorization_and_RSA_problem

// Faulty key generation:
//  - Fermat factorization can work if `p` and `q` are close together
//  - p - 1 and q - 1 can also be factored if they have only small prime factors
//  - if q < p < 2q, then d > n^.25 / 3
//  - primes p,q must be generated with a strong random number generator
// https://crypto.stanford.edu/~dabo/pubs/papers/RSA-survey.pdf

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

    // find public inverse
    let mut e = 3;
    for elem in [3, 5, 7, 11, 13] {
        if gcd(elem, exp_mod) == 1 {
            e = elem;
            break;
        }
    }

    println!("Public key: (N = {}, e = {})", n, e);

    let d = inverse(e, exp_mod);
    println!("Secret key: {}", d);
}
