from hashlib import md5

hashed = ""
count = 0

while not hashed.startswith("00000"):
    to_hash = "bgvyzdsv" + str(count)
    hashed = md5(to_hash.encode()).hexdigest()
    count += 1

print(count - 1)
