newSet = {"panana", "orange", "orange"}
print(newSet)

# add to set
newSet.add("apple")
print(newSet)

# set in python using in digram => two digram share in area
persons = {"morad", "noor", "shimaa"}
anotherPersons = {"shimaa", "hadeel"}

allPersons = persons.union(anotherPersons)
personOfBoth = persons.intersection(anotherPersons)
print(allPersons)
print(personOfBoth)
