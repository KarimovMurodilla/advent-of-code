from puzzles import reports

class Solution:
    def is_safe(self, row: str):
        levels = map(int, row.split())

        flag = ""
        last_level = None

        for level in levels:
            if not last_level:
                last_level = level
            else:
                if level == last_level:
                    return False

                if not flag:
                    if level > last_level:
                        flag = "increase"
                    else:
                        flag = "decrease"

                if level > last_level and flag == "decrease":
                    return False
                
                elif level < last_level and flag == "increase":
                    return False

                differ = abs(last_level - level)
                if 3 < differ or differ < 1:
                    return False
                    
            last_level = level

        return True

    def find_safe_reports(self, distances: str):
        rows = distances.split('\n')
        count = 0
        
        for row in rows:
            is_safe = self.is_safe(row)
            if is_safe:
                print(row)
                count += 1

        return count
    

s = Solution()
res = s.find_safe_reports(reports)
print(res)
