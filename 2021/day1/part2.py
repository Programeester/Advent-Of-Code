bigger_count = 0

with open("data.txt", "r") as f:
    values = [int(value) for value in f.readlines()]
    for i in range(len(values)):
        if sum(values[i : i + 3]) < sum(values[i + 1 : i + 4]):
            bigger_count += 1
            
print(bigger_count)
