#Day 9
file = open("Data.txt",'r')
data = file.read()
file.close()
rows = [[int(i) for i in r] for r in data.split('\n')]
#part 1
result = 0

for y, row in enumerate(rows):
    for x, col in enumerate(row):
        minimum = 9
        if (y != 0):
            minimum = min(minimum, rows[y-1][x])
        if (y != len(rows) -1):
            minimum = min(minimum, rows[y+1][x])
        if (x != 0):
            minimum = min(minimum, rows[y][x-1])
        if (x != len(row) -1):
            minimum = min(minimum, rows[y][x+1])
        if (rows[y][x] < minimum):
            result += rows[y][x] + 1
print(result)
# part 2
# find basins

def fill():
    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            alreadyVisited = False
            if alreadyVisited:
                break
            basin = set([])
            basinAdd(y,x,basin)
            basins.append(basin)

def basinAdd(y,x,basin):
    if (rows[y][x] == 9 or (y,x) in basin):
        return
    basin.add((y,x))
    if (y != 0):
        basinAdd(y-1,x,basin)
    if (y != len(rows) -1):
        basinAdd(y+1,x,basin)
    if (x != 0):
        basinAdd(y,x-1,basin)
    if (x != len(row) -1):
        basinAdd(y,x+1,basin)

basins = []
fill()
basinSizes = [len(b) for b in basins]
basinSizes = list(set(basinSizes))
basinSizes.sort(reverse=True)
result = basinSizes[0] * basinSizes[1] * basinSizes[2]
print(basins)
print(basinSizes)
print(result)