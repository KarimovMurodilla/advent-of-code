from puzzles import text
from collections import defaultdict

class Solution:
    def find_word(self, text: str):
        d = {
            "rows": [],
            "cols": [],
            "left_diagonal": [],
            "right_diagonal": []
        }

        # rows collection
        rows = text.split('\n')
        d['rows'] = rows

        # cols collection
        cols = defaultdict(list)
        for row in rows:
            for i in range(len(row)):
                cols[i].append(row[i])

        d["cols"] = ["".join(i) for i in cols.values()]

        # left_diagonal collection
        left_diagonal = defaultdict(list)
        for row in range(len(rows)):
            for i in range(len(rows[row])):
                left_diagonal[i-row].append(rows[row][i])

        d["left_diagonal"] = ["".join(i) for i in left_diagonal.values()]

        # right_diagonal collection
        right_diagonal = defaultdict(list)
        for row in range(len(rows)):
            for i in range(len(rows[row])):
                right_diagonal[i+row].append(rows[row][i])

        d["right_diagonal"] = ["".join(i) for i in right_diagonal.values()]

        total_count = 0
        for key in d:
            for i in d[key]:
                data = "".join(i)
                total_count += data.count('XMAS')
                total_count += data.count('SAMX')
                # print(data)

        return total_count
    

s = Solution()
res = s.find_word(text)
print(res)
