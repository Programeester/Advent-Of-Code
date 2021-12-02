with open("data.txt", "r") as f:
    data = f.readlines()
    data = [(i.split()[0], int(i.split()[1])) for i in data]

horizontal = 0
depth = 0

for dir, val in data:
    if dir == "up":
        depth -= val
    if dir == "down":
        depth += val
    if dir == "forward":
        horizontal += val
        
print(horizontal * depth)
