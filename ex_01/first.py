test = open("./text.txt")

for line in test:
    line = line.rstrip()
    wds = line.split()
    if len(wds) == 0 or wds[0] != "From":
        continue
    print(wds[2])
