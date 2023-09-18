class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    max_scoops = 3

    def __init__(self):
        self.scoops = [] 
    
    def add_scoops(self, *new_scoops): 
        for one_scoop in new_scoops:
            if len(self.scoops) < Bowl.max_scoops:  # Use 'Bowl.max_scoops' instead of 'bowl.max_scoops'
                self.scoops.append(one_scoop)
    
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops) 

s1 = Scoop('truffle')
s2 = Scoop('vanilla')
s3 = Scoop('strawberry')
s4 = Scoop('flavour 4')
s5 = Scoop('flavour 5')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s4, s5)  # Remove the extra space before 'add_scoops'
print(b)
