from puzzles import reports

class Solution:
    def is_safe(self, levels: list):
        flag = ""
        last_level = None

        for level in levels:
            if not last_level:
                last_level = level
            else:
                if level == last_level:
                    return False, last_level

                if not flag:
                    if level > last_level:
                        flag = "increase"
                    else:
                        flag = "decrease"

                if level > last_level and flag == "decrease":
                    return False, last_level
                
                elif level < last_level and flag == "increase":
                    return False, last_level

                differ = abs(last_level - level)
                if 3 < differ or differ < 1:
                    return False, last_level
                    
            last_level = level

        return True, 1

    def is_safe_without_one(self, levels: list, target: int):
        for i in range(len(levels)):
            filtered_levels = [levels[x] for x in range(len(levels)) if x != i]
            is_safe = self.is_safe(filtered_levels)
            if is_safe[0]:
                return True


    def find_safe_reports(self, distances: str):
        rows = distances.split('\n')
        count = 0
        
        for row in rows:
            levels = list(map(int, row.split()))
            is_safe = self.is_safe(levels)
            if is_safe[0]:
                print("Safe without removing:", row)
                count += 1
            else:
                is_safe_without_one = self.is_safe_without_one(levels, is_safe[1])
                if is_safe_without_one:
                    print("Safe by removing:", row)
                    count += 1

        return count
    

s = Solution()
res = s.find_safe_reports(reports)
print(res)
