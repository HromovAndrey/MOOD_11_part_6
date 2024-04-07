# Завдання 3
# Створіть базовий клас «Домашня тварина» та похідні
# класи «Пес», «Кіт», «Папуга», «Хом’як». За допомогою
# конструктора встановіть ім’я кожної тварини та її характеристики. Реалізуйте для кожного із класів наступні
# методи:
# ■ Sound — видає звук тварини (пишемо текстом в консоль);
# ■ Show — відображає ім’я тварини;
# ■ Type — відображає підвид тварини.

class HomeAnimal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass

    def show(self):
        print("Ім'я тварини:", self.name)

    def type(self):
        pass

class Dog(HomeAnimal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Гав-гав!")

    def type(self):
        print("Це порода собаки", self.breed)

class Cat(HomeAnimal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Мяу!")

    def type(self):
        print("Це кіт забарвлення", self.color)

class Parrot(HomeAnimal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def sound(self):
        print("Говорить: Привіт, я папуга!")

    def type(self):
        print("Це папуга виду", self.species)

class Hamster(HomeAnimal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print("Шуршить шинкою!")

    def type(self):
        print("Це хом'як кольору", self.color)


dog = Dog("Барсік", "дворняга")
dog.show()
dog.sound()
dog.type()

cat = Cat("Мурка", "сіра")
cat.show()
cat.sound()
cat.type()

parrot = Parrot("Кеша", "ара")
parrot.show()
parrot.sound()
parrot.type()

hamster = Hamster("Буся", "білий")
hamster.show()
hamster.sound()
hamster.type()
