import random
import sys

name = input("Whomstve dost thou be of Kickstart? (Hint, your name is Tiger.): ")
health = 40
score = 0

class sodieboi:
    """Sodiebois - The Rogue Gods"""
    def __init__(self, name):
        self.name = name

    @property
    def damage(self):
        return random.randint(1,5)

    def isAlive(self):
        return self.health > 0

    def attack(self):
        damage = random.randint(0, 10)
        self.health -= damage
        return damage

sodiebois = [
    sodieboi("Ebola"),
    sodieboi("Ryan"),
    sodieboi("Colton"),
    sodieboi("Dalton"),
    sodieboi("Actual Coke Bottle"),
    sodieboi("Subway Management")
]

random.shuffle(sodiebois)


while len(sodiebois) > 1:
    sodieboi = sodiebois.pop()
    print("The Sodieboi {} approaches.".format(sodieboi.name))
    while sodieboi.isAlive():
        print("Tiger has {}HP!".format(health))
        print("Do you want to bone or bolt?")
        if input("Bone / Bolt > ").lower() == "bone":
            damage = sodieboi.attack()
            score += damage
            print("Tiger did {}HP in attack! THATSA LOTTA DAMAGE!".format(damage))
            if sodieboi.isAlive():
                damage = sodieboi.damage
                health -= damage
                print("Tiger took {}HP in damage!".format(sodieboi.damage))
        else:
            bamboozled = random.randint(1,5) == 1
            if not bamboozled:
                print("Tiger ran away like the... tiger he is.")
                print("Your score was {}".format(score))
                sys.exit(0)
            else:
                print("Can't escape!")

print("Wowza, Tiger killed everyone.")
print("Epic sick nasty.")
print("Your Score: {}".format(score))
