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

    def get_coords(self, rows: list):
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
            else:
                break

        return x, y, passed_lines
    
    def has_loop(self, rows: list, x: int, y: int):
        row_len = len(rows)
        col_len = len(rows[0])

        pointer = '^'
        position_and_pointer = []

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
                    if (x,y,pointer) not in position_and_pointer:
                        position_and_pointer.append((x,y,pointer))
                    else:
                        return True
            else:
                break

        return False
    
    def make_loop(self, text: str):
        rows = [[i for i in row] for row in text.split('\n')]
        x, y, coords = self.get_coords(rows)

        count = 0
        for x, y in coords:
            if rows[x][y] == '.':
                rows[x][y] = '#'
                if self.has_loop(rows, x, y):
                    print("Has hoop")
                    count += 1
                else:
                    print("Has not loop")
                rows[x][y] = '.'        
        return count

s = Solution()
res = s.make_loop(text)
print(res)
