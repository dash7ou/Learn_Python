fname = input("Enter Your File...")
if len(fname) < 1:
    fname = './clown.txt'

hand = open(fname)

di = dict()

for line in hand:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word in di:
            di[word] = di[word] + 1
        else:
            di[word] = 1

print(di)
