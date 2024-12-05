from puzzles import distances

class Solution:
    def calculate_total_distance(self, distances: str):
        rows = distances.split('\n')
        first_list = []
        second_list = []
        total_distance = 0

        for row in rows:
            first, second = row.split()
            first_list.append(int(first))
            second_list.append(int(second))
        
        first_list.sort()
        second_list.sort()

        for i in range(len(first_list)):
            total_distance += abs(first_list[i] - second_list[i])
        
        return total_distance

s = Solution()
res = s.calculate_total_distance(distances)
print(res)
