# Example:
#   split digit string into substrings of the same digit:
#   "3322251" -> 33 222 5 1 -> 2 3, 3 2, 1 5, 1 1 -> 23321511

import pdb

class Solution:
    def _countAndSay(self, cas: str) -> str:
        # pdb.set_trace()
        count_and_say = ""

        i = 0
        while i < len(cas):
            digit = cas[i]
            n_digits = 1
            
            while i + 1 < len(cas) and cas[i + 1] == digit:
                n_digits += 1
                i += 1
            
            count_and_say += str(n_digits) + str(digit)
            i += 1
                
        return count_and_say
    
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
            
        digit_string = "1"
        for i in range(n - 1):
            digit_string = self._countAndSay(digit_string)
    
        return digit_string        
        
            
        
cases = [
    (1, "1"),
    (4, "1211")
]

# 1 <= n <= 30
if __name__ == "__main__":
    for n, ans in cases:
        s = Solution()
        output = s.countAndSay(n)
        
        if output != ans:
            print(f'n={n}, output={output}, ans={ans}')