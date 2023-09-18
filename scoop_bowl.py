class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    def __init__(self):
        self.scoops = [] 
    
    def add_scoops(self, *new_scoops): 
        for one_scoop in new_scoops:
            self.scoops.append(one_scoop)
    
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops) 

s1 = Scoop('truffle')
s2 = Scoop('vanilla')
s3 = Scoop('strawberry')
s4 = Scoop ('orange')
b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3,s4)
print(b)