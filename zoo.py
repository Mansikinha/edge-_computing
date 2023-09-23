class Zoo:
    def __init__(self):
        self.cages = []

    def add_cages(self, *cages):
        for one_cage in cages:
            self.cages.append(one_cage)

    def __repr__(self):
        return '\n'.join(str(one_cage) for one_cage in self.cages)

    def animals_by_color(self, color):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.color == color]

    def animals_by_legs(self, number_of_legs):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.number_of_legs == number_of_legs]

    def number_of_legs(self):
        return sum(one_animal.number_of_legs
                   for one_cage in self.cages
                   for one_animal in one_cage.animals)


# Define the Animal and Cage classes (assuming these are defined elsewhere in your code)

class Animal:
    def __init__(self, color, number_of_legs):
        self.color = color
        self.number_of_legs = number_of_legs

    def __str__(self):
        return f'{self.__class__.__name__}({self.color})'


class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)  # Wolves typically have 4 legs

class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)  # Sheep typically have 4 legs

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)  # Snakes typically have 0 legs

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)  # Parrots typically have 2 legs



class Cage:
    def __init__(self, cage_number):
        self.cage_number = cage_number
        self.animals = []

    def add_animals(self, *animals):
        for animal in animals:
            self.animals.append(animal)

    def __str__(self):
        return f'Cage {self.cage_number}: {", ".join(str(animal) for animal in self.animals)}'


# Instantiate the animals and cages
wolf = Wolf('black')
sheep = Sheep('white')
snake = Snake('brown')
parrot = Parrot('green')

# Instantiate the cages and zoo
c1 = Cage(1)
c1.add_animals(wolf, sheep)

c2 = Cage(2)
c2.add_animals(snake, parrot)

z = Zoo()
z.add_cages(c1, c2)

# Test your code
# Test your code
print(wolf)
print(sheep)
print(snake)
print(parrot)

print(z)
print(z.animals_by_color('white'))
print(z.animals_by_legs(4))  # Replace 0 with the desired number of legs
print(z.number_of_legs())


