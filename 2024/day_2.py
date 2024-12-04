from puzzles import distances

class Solution:
    def calculate_similarity_score(self, distances: str):
        rows = distances.split('\n')
        first_list = []
        second_list = []
        similarity_score = 0

        for row in rows:
            first, second = row.split()
            first_list.append(int(first))
            second_list.append(int(second))
        
        for num in first_list:
            count = second_list.count(num)
            similarity_score += (num*count)
        
        return similarity_score
    

s = Solution()
res = s.calculate_similarity_score(distances)
print(res)
