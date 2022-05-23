
from battle_weapon import Weapon

class Robot:

    def __init__(self):
        self.name = 'Gary Busey'
        self.health = 100
        self.active_weapon = Weapon()

    def robo_attack(self, health):
        health -= self.active_weapon.attack_power
        return health