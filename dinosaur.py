from robot import Robot


class Dinosaur:

    def __init__(self):
        self.name = 'Sparky'
        self.health = 100
        self.attack_power = 100

    def print_dino_attack(self):
        Robot.health = self.attack_power
        print(f'{Robot.name} has been attacked by {Dinosaur.name}! Health level is now at {self.dino_attack}')

    