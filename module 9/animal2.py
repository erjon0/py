class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print('dddd')

    def sound(self):
        print(f'ddd{self.name}.')

class Dog(Animal):
    def  __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print('ham')

    def description(self):
        super().description()

        print(f'breed:{self.breed}')

class Cat(Animal):
    def  __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print('meow')

    def description(self):
        super().description()

        print(f'color:{self.color}')

animal = Animal('33')
animal.sound()
animal.description()

dog = Dog("rex", 'ee')
dog.sound()
dog.description()

cat = Cat('black','cat')
cat.sound()
cat.description()
