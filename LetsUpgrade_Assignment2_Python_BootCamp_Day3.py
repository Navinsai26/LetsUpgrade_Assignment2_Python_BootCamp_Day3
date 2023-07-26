# Step 1: Create a base class Animal
class Animal:
    def make_sound(self):
        print("Generic animal sound")

# Step 2: Create two subclasses Dog and Cat
class Dog(Animal):
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Step 4: Implement a function animal_sound_in_zoo()
def animal_sound_in_zoo(animal):
    animal.make_sound()

# Step 5: Create instances of Dog and Cat classes and call the animal_sound_in_zoo() function
dog_instance = Dog()
cat_instance = Cat()

animal_sound_in_zoo(dog_instance)  # Output will be "Bark!"
animal_sound_in_zoo(cat_instance)  # Output will be "Meow!"
