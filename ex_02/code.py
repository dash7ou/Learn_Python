fname = input("Enter Your File...")
if len(fname) < 1:
    fname = './clown.txt'

hand = open(fname)

di = dict()

for line in hand:
    line = line.rstrip()
    line = line.split()
    for word in line:
        count = di.get(word, 0) + 1
        di[word] = count

print(di)
