from robot import Robot


class Dinosaur:

    def __init__(self):
        self.name = 'Sparky'
        self.health = 100
        self.attack_power = 100

    def print_dino_attack(self, health):
        health -= self.attack_power
        return health
    
    
    
   