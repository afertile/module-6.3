from random import randint
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    def __init__(self, speed):
        self.speed = speed
    def move(self, dx, dy, dz):
        self._cords[0] = self.speed * dx
        self._cords[1] = self.speed * dy
        if self.speed * dz < 0:
            print("It's too deep, i can't dive :(")
            self._cords[2] = 0
        else:
            self._cords[2] = self.speed * dz
    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f"Here are(is) {randint(1,4)} eggs for you")
class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        if super()._cords[2]/2 - abs(dz) * self.speed < 0:
            print("It's too deep, i can't dive :(")
            super()._cords[2] = 0
        else:
            super()._cords[2] = super()._cords[2]/2 - abs(dz) * self.speed
class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8
class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    def speak(self):
        print('Click-click-click')
print(Duckbill.mro())
db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

# Немного переработал логику метода dive_in, т.к. плохо понял формулировку задания