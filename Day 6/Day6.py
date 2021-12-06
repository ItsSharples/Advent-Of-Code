from collections import defaultdict
from typing import Any
data = [2,1,1,4,4,1,3,4,2,4,2,1,1,4,3,5,1,1,5,1,1,5,4,5,4,1,5,1,3,1,4,2,3,2,1,2,5,5,2,3,1,2,3,3,1,4,3,1,1,1,1,5,2,1,1,1,5,3,3,2,1,4,1,1,1,3,1,1,5,5,1,4,4,4,4,5,1,5,1,1,5,5,2,2,5,4,1,5,4,1,4,1,1,1,1,5,3,2,4,1,1,1,4,4,1,2,1,1,5,2,1,1,1,4,4,4,4,3,3,1,1,5,1,5,2,1,4,1,2,4,4,4,4,2,2,2,4,4,4,2,1,5,5,2,1,1,1,4,4,1,4,2,3,3,3,3,3,5,4,1,5,1,4,5,5,1,1,1,4,1,2,4,4,1,2,3,3,3,3,5,1,4,2,5,5,2,1,1,1,1,3,3,1,1,2,3,2,5,4,2,1,1,2,2,2,1,3,1,5,4,1,1,5,3,3,2,2,3,1,1,1,1,2,4,2,2,5,1,2,4,2,1,1,3,2,5,5,3,1,3,3,1,4,1,1,5,5,1,5,4,1,1,1,1,2,3,3,1,2,3,1,5,1,3,1,1,3,1,1,1,1,1,1,5,1,1,5,5,2,1,1,5,2,4,5,5,1,1,5,1,5,5,1,1,3,3,1,1,3,1]
# data = [3,4,3,1,2]
school = defaultdict(int)
for lamp in data:
    school[lamp+1] += 1



def growthRate(school: "defaultdict[Any, int]", day: int) -> int:
    if day <= 0: return 0
    countOfDay = school[day]
    if countOfDay != 0: return countOfDay
    return growthRate(school, day - 6) + growthRate(school, day - 8)

days = 256
#print(sum(map(lambda x: growthRate(school, x), range(days+2, days+9))))

logDate = lambda day: (f"Day {day}, Count: {sum([y if x > day else 0 for x,y in school.items()])}")

for day in range(days+1):
    school[day+9] = school[day]
    school[day+7] = school[day-2] + school[day]
print(logDate(days))
