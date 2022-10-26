class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes, twos, fives = 0, 0, 0
        for i in range(1, n + 1):
            while i % 2 == 0:
                twos += 1
                i //= 2
            
            while i % 5 == 0:
                fives += 1
                i //= 5            
            
        
        zeroes += min(twos, fives)
    
        return zeroes

cases = [
    (3, 0),
    (5, 1),
    (0, 0)
]
if __name__ == "__main__":
    for input, ans in cases:
        s = Solution()
        output = s.trailingZeroes(input)
        
        if output != ans:
            print(f'input={input}, output={output}, ans={ans}')
