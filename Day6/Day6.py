#Day 6
with open("Data.txt", "r") as f:
    raw = f.read()
data = [int(i) for i in raw.split(",")]
#initialize fish array
fish = [0,0,0,0,0,0,0,0,0]
for f in data:
    fish[f] += 1
#solve part 1
def step(n):
    for steps in range(n):
        newfish = fish[0]
        for f in range(0,8):
            fish[f] = fish[f+1]
        fish[6] += newfish
        fish[8] = newfish
#change the call of step to desired day number
step(256)
print(sum(fish))