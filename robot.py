
from battle_weapon import Weapon

class Robot:

    def __init__(self):
        self.name = 'Gary Busey'
        self.health = 100
        self.active_weapon = Weapon()

    def robo_attack(self, health):
        health -= self.active_weapon.attack_power
        return health


            # Now that you have the weapon power like that, and you are returning it, what do you get when you run main.py?
            # I haven't looked at your battlefield.py to see what other changes you've made
            
            # the battlefield is now a mess because I was tearing it apart to try to find the issue :(
            # Well lets go back to it and check it out. First though, lets get rid of this extra def __init__ that you copied over for reference
            #  : = )