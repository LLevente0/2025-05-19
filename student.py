class Student:
    def __init__(self, name, age, sex): #konstruktor az osztály példányosításához
        self.name = name
        self.age = age
        self.sex = sex
        self.score = 10

def introduce(self):
    print(f"Név: {self.name}, Kor: {self.age}, Pontszám: {self.score}")

def learn(self, points):
    self.score += points



tivadar = Student("El Tivadar", 16, "male")
leila = Student("Leila", 17, "female")

tivadar.name = "El Tivadar"
tivadar.age = 16
tivadar.sex = "male"
tivadar.score = 20

introduce(tivadar)
learn(tivadar, 12)
introduce(tivadar)

introduce(leila)
learn(leila, -2)
introduce(leila)