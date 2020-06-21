import re

# search
file = open("./text.txt")
for line in file:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)

# findall
newString = "mohammed is 10 years old i love his good 12"
allMatch = re.findall('[0-9]+', newString)
print(allMatch)
