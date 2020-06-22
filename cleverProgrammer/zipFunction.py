firstList = [1, 2, 3, 4, 5]
secondList = ['one', 'two', 'three', 'four', 'five']

# here we zipped lists togther if list longer than another the items will be ignored
zipped = list(zip(firstList, secondList))
print(zipped)

# unzipped
unzipped = list(zip(*zipped))
print(unzipped)  # we get two touple lists

# example

for (l1, l2) in zip(firstList, secondList):
    print(l1)
    print(l2)


# example 2

items = ['apple', 'banana', 'orange']
counts = [2, 1, 3]
prices = [0.5, 0.7, 1.1]

santances = []
for(item, count, price) in zip(items, counts, prices):
    santance = f"I bought {count} {item}s at {price}."
    santances.append(santance)

print(santances)
