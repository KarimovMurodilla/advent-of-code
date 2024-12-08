from puzzles import text

class Solution:
    def rotate(self, pointer: str):
        if pointer == '^':
            return '>'
        elif pointer == '>':
            return 'v'
        elif pointer == 'v':
            return '<'
        else:
            return '^'

    def find_direction(self, text: str):
        rows = [[i for i in row] for row in text.split('\n')]
        row_len = len(rows)
        col_len = len(rows[0])

        # find pointer index
        x = y = 0
        pointer = '^'
        for row in range(len(rows)):
            for col in range(len(rows[row])):
                if rows[row][col] in ['^', '>', 'v', '<']:
                    x, y = row, col
                    pointer = rows[row][col]

        # find way
        count = 1
        passed_lines = [(x, y)]
        while True:
            old_x, old_y = x, y

            if pointer == '^':
                x = x - 1
            elif pointer == '>':
                y = y + 1
            elif pointer == 'v':
                x = x + 1
            elif pointer == '<':
                y = y - 1
            
            if (row_len > x >= 0 and col_len > y >= 0):
                if rows[x][y] == '#':
                    x, y = old_x, old_y
                    pointer = self.rotate(pointer)
                else:
                    if (x,y) not in passed_lines:
                        passed_lines.append((x,y))
                        count += 1
            else:
                break

        return count


s = Solution()
res = s.find_direction(text)
print(res)
