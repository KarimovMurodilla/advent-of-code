from puzzles import text

class Solution:
    def find_word(self, text: str):
        rows = text.split('\n')

        row_len = len(rows)
        col_len = len(rows[0])

        count = 0

        for row in range(len(rows)):
            for col in range(len(rows[row])):
                if rows[row][col] == 'A':
                    if (1 <= row < row_len - 1 and 1 <= col < col_len - 1):
                        if (
                            rows[row-1][col-1] in "MS" and
                            rows[row+1][col+1] in "MS" and
                            rows[row-1][col+1] in "MS" and
                            rows[row+1][col-1] in "MS"
                        ):
                            if (
                                rows[row-1][col-1] != rows[row+1][col+1] and 
                                rows[row-1][col+1] != rows[row+1][col-1]
                            ):
                                count += 1
        return count
    

s = Solution()
res = s.find_word(text)
print(res)
