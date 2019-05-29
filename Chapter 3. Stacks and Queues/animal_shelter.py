# form Stack import Stack
import unittest


class Animal():
    def __init__(self, name):
        self.order = 0
        self.name = name

    def set_order(self, ord):
        self.order = ord

    def get_order(self):
        return self.order

    def is_older_than(self, a):
        return self.order < a.get_order()


class AnimalQueue():
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0

    def enqueue(self, animal):
        animal.set_order(self.order)
        self.order += 1
        if animal.__class__ == Cat:
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueDog(self):
        return self.dogs.pop(0)

    def dequeueCat(self):
        return self.cats.pop(0)

    def dequeueAny(self):
        if len(self.dogs) == 0:
            return self.dequeueCat()
        elif len(self.cats) == 0:
            return self.dequeueDog()

        dog = self.dogs[0]
        cat = self.cats[0]
        if dog.is_older_than(cat):
            return self.dequeueDog()
        elif cat.is_older_than(dog):
            return self.dequeueCat()


class Cat(Animal): pass


class Dog(Animal): pass


class Test(unittest.TestCase):
    def test_animal_shelter(self):
        shelter = AnimalQueue()
        shelter.enqueue(Cat("Hanzack"))
        shelter.enqueue(Dog("Pluto"))
        shelter.enqueue(Cat("Garfield"))
        shelter.enqueue(Cat("Tony"))
        shelter.enqueue(Dog("Clifford"))
        shelter.enqueue(Dog("Blue"))
        self.assertEqual(shelter.dequeueAny().name, "Hanzack")
        self.assertEqual(shelter.dequeueAny().name, "Pluto")
        self.assertEqual(shelter.dequeueDog().name, "Clifford")
        self.assertEqual(shelter.dequeueCat().name, "Garfield")
        self.assertEqual(shelter.dequeueAny().name, "Tony")


if __name__ == "__main__":
    unittest.main()
