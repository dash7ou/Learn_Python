class PartyAnmial:
    x = 0

    def __init__(self):
        print('iam a contructed')

    def party(self):
        self.x = self.x + 1
        print('so far', self.x)

    def __del__(self):
        print('I am destructed', self.x)


an = PartyAnmial()
an.party()
an.party()
an = 542

print(" an contains", an)

# another class
print("another class")


class PrintNames:
    x = 0
    name = ''

    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")

    def addCount(self):
        self.x = self.x + 1
        print(self.x, "Count for name", self.name)


morad = PrintNames("morad")
morad.addCount()
