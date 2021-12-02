bad_letters = ["ab", "cd", "pq", "xy"]
good_letters =["a", "e", "i", "o", "u"]

with open("/home/bigbrain/Documents/python_tutorial/Advent-Of-Code-main/2015/day5/data.txt", "r") as f:
    words = f.readlines()
    for word in words:
        for bad_letter in bad_letters:
            if bad_letter in word:
                pass
        for good_letter in good_letters:
            if good_letter in word:
