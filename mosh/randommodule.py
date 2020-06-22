import random

for i in range(3):
    print(random.random())
    print(random.randint(0, 15))

member = ['John', 'Mary', 'shimaa']
choice = random.choice(member)
print(choice)
