file = open("Data.txt",'r')
data = file.read()
file.close()
rows = [[int(i) for i in r] for r in data.split('\n')]


def step(count):
    #increase all by 1
    for i, row in enumerate(rows):
        for j, c in enumerate(row):
            rows[i][j] += 1

    
    flashed = []
    for i, row in enumerate(rows):
        for j, c in enumerate(row):
            count += proliferate(i,j, 0, flashed)
    

    #reset to 0 when finished flashing:
    for i, row in enumerate(rows):
        for j, c in enumerate(row):
            if rows[i][j] > 9:
                rows[i][j] = 0

    if len(flashed) == len(rows[1]) * len(rows):
        print("iteration:")
        return -10000000

    print(rows)
    return count

def proliferate(i,j,count,flashed):
    if rows[i][j] >= 10 and (i,j) not in flashed:
        flashed.append((i,j))
        count += 1
        for x in range(-1,2):
            for y in range(-1,2):
                if (not (x== 0 and y == 0) and 0 <= j+x and 0 <= i+y and len(rows) > j+x and len(rows[i]) > i+y):
                    
                    rows[i+y][j+x] += 1
                    count += proliferate(i+y,j+x,0,flashed)
    return count

def makesteps(n, count):
    for i in range(n):
        count += step(0)
        if count < 0: 
            print(i)
            return i
    return count


count = makesteps(1000, 0)
print(count)