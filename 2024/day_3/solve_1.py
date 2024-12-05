import re
from puzzles import text

class Solution:
    def scan_uncorrupted_mul(self, text: str):
        pattern = r'mul\(\d+,\d+\)'
        pattern2 = r'\d+,\d+'
        matches = re.findall(pattern, text)

        mul_sum = 0
        for match in matches:
            res = re.search(pattern2, match)
            first, second = map(int, res.group().split(','))
            mul_sum += first * second

        return mul_sum

s = Solution()
res = s.scan_uncorrupted_mul(text)
print(res)
