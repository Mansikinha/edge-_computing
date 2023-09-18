class scoop():
    def __init__(self, flavour):
        self.flavour = flavour

def create_scoops():
    scoops = [scoop('truffle'),
              scoop('strawberry'),
              scoop('vanilla')]

    for s in scoops:
        print(s.flavour)

create_scoops()
