gamma = "0000000000"
epsilon = "0000000000"

dict = {"gamma_epsilon_stuff" : []}

with open("data.txt", "r") as f:
    bytes = f.readlines()
    for i in range(len(bytes[0])):
        for byte in bytes:
            dict["gamma_epsilon_stuff"][i].append(byte)
