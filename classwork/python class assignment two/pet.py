class Pet:
    name_dict = {}
    species_dict = {}
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Pet.name_dict[name] = Pet.name_dict.get(name, 0) + 1
        Pet.species_dict[name] = Pet.species_dict.get(name, 0) + 1


        # .get is a dictionary method used to avoid a KeyError. If name is not
        # a key, then .get returns the default value provided, which is 0.
        # Pet.species_dict[name] = 


    def __str___(self):
        return "Pet: name={}, species={}".format(self.name, self.species)

    def greet(self, greeting: str):
        print(f'{self.name} says {greeting}')

    def eats(self, snack:str):
        print(f'{self.name} eats {snack}. {self.species.capitalize() + "s"} love {snack}')

def main():
    pet1 = Pet("Fluffy", "cat")
    pet2 = Pet("Fluffy", "dog")
    pet3 = Pet("Rex", "dinosaur")
    pet4 = Pet("Garfield", "cat")
    
    for k, v in Pet.name_dict.items(): # k and v are corresponding key and value
        if v == 1:
            print("There is 1 pet named {}.".format(k))
        else:
            print("There are {} pets named {}.".format(v, k))
    
    # The following code will not work until after you change the class.
    for k, v in Pet.species_dict.items():
        if v == 1:
            print("There is 1 {}.".format(k))
        else:
            print("There are {} {}s.".format(v, k))
    pet1.eats("poop")

main()