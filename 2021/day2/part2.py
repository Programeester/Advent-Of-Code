with open("data.txt", "r") as f:
    data = f.readlines()
    data = [(i.split()[0], int(i.split()[1])) for i in data]

horizontal = 0
depth = 0
aim = 0

for dir, val in data:
    if dir == "up":
        aim -= val
    if dir == "down":
        aim += val
    if dir == "forward":
        horizontal += val
        depth += val * aim
        
print(horizontal * depth)
