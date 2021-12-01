newDepth = 10000000
increases = 0
oldDepth = 0

with open("sonarData.txt", "r") as f:
    for line in f:
        oldDepth = newDepth
        newDepth = int(line)
        if (newDepth > oldDepth):
            increases += 1
        

print(increases)

values = []
with open("sonarData.txt", "r") as f:
    for line in f:
        values.append(int(line))
print(values)

newDepth = 100000
increases = 0
while (len(values) >= 3):
    oldDepth = newDepth
    newDepth = values[0] + values[1] + values[2]
    if (newDepth > oldDepth):
            increases += 1
    del values[0]

print(increases)
