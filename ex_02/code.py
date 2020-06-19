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


maxValue = max(di.values())
theWord = None

for key in di:
    if di[key] == maxValue:
        theWord = key


print(theWord, maxValue)

# Using Tuples

newFile = open("./clown.txt")

newDict = dict()
for line in newFile:
    words = line.split()
    for word in words:
        x = newDict.get(word)
        newDict[word] = newDict.get(word, 0) + 1

# lst = list()
# for k, v in newDict.items():
#     lst.append((v, k))

# lst = sorted(lst, reverse=True)

# we can get shortest version
lst = sorted([(v, k) for k, v in newDict.items()], reverse=True)
for v, k in lst:
    print(v, k)
