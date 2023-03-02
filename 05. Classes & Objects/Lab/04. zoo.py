class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, specie, animal_name):

        if specie == "mammal":
            self.mammals.append(animal_name)
        elif specie == "fish":
            self.fishes.append(animal_name)
        elif specie == "bird":
            self.birds.append(animal_name)


        Zoo.__animals += 1


    def get_info(self, specie):
        if specie == "mammal":
            print(f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}")
            print(f"Total animals: {self.__animals}")
        elif specie == "fish":
            print(f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}")
            print(f"Total animals: {self.__animals}")
        elif specie == "bird":
            print(f"Birds in {self.zoo_name}: {', '.join(self.birds)}")
            print(f"Total animals: {self.__animals}")


name_of_zoo = input()
zoo = Zoo(name_of_zoo)

count = int(input())

for i in range(count):
    animal = input().split()
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)


info = input()
zoo.get_info(info)

