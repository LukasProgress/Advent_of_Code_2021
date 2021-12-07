#Day 6
import statistics as s
import math
with open("Data.txt", "r") as f:
    raw = f.read()
data = [int(i) for i in raw.split(",")]
#part 1
median = s.median(data)
target = round(median)
differences = [abs(i - target) for i in data]
solution1 = sum(differences)
print(solution1)
#part 2
target2 = math.floor(s.mean(data)) # had to floor it for some reason
differences2 = [abs(i - target2) for i in data]
costs = [round(i*(i+1)/2) for i in differences2]
solution2 = sum(costs)
print(solution2)
