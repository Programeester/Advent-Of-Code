bigger_count = 0

with open("data.txt", "r") as f:
    values = [int(value) for value in f.readlines()]
    for i in range(len(values) - 1):
        if values[i] < values[i + 1]:
            bigger_count += 1
            
print(bigger_count)
