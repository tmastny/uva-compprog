from collections import defaultdict


def longestPalindrome(s):

    curr_lo = best_lo = 0
    curr_hi = best_hi = 1

    pali_chars = defaultdict(set, {s[0]: {0}})

    width = len(s)
    print(f'{s: <{width}} curr_lo    curr_hi')
    for i in range(1, len(s)):
        print(f'{s[0:i]: <{width}} {curr_lo}          {curr_hi}       {dict(pali_chars)}')

        updated_chars = defaultdict(set)
        if s[i] in pali_chars:
            curr_hi += 1
            curr_lo = min(pali_chars[s[i]])

            # this line shows that' it's not linear performance.
            # it has to loop through all previous indices of the value
            for x in pali_chars[s[i]]:
                if x - 1 >= 0:
                    updated_chars[s[x - 1]].add(x - 1)
        else:
            curr_hi = i + 1
            curr_lo = i

        if curr_hi - curr_lo > best_hi - best_lo:
            best_hi = curr_hi
            best_lo = curr_lo

        pali_chars.clear()
        pali_chars = updated_chars
        pali_chars[s[i]].add(i)
        pali_chars[s[i - 1]].add(i - 1)

        pali_index = curr_lo - 1
        if pali_index >= 0:
            pali_chars[s[pali_index]].add(pali_index)

    print(f'{s[0:i]: <{width}} {curr_lo}          {curr_hi}       {dict(pali_chars)}')
    return s[best_lo:best_hi]


strings = [
    #012345
    "aaaaa"
]

for s in strings:
    print(longestPalindrome(s))
