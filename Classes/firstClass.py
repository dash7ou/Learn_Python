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
