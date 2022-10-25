# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/815/

# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1

class Solution:
    def __init__(self):
        self.visited_n = set()
        
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        if n in self.visited_n:
            return False
        
        self.visited_n.add(n)
            
        sum_of_sq_digits = 0
        while n:
            sum_of_sq_digits += (n % 10)**2
            n //= 10
                
        return self.isHappy(sum_of_sq_digits)
        
cases = [
    (19, True), 
    (2, False)
]

if __name__ == "__main__":
    for input, ans in cases:
        s = Solution()
        output = s.isHappy(input)
        
        if output != ans:
            print(f'input={input}, output={output}')