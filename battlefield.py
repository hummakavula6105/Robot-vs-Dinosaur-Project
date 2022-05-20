
from robot import Robot
from dinosaur import Dinosaur


welcome_greeting = 'Welcome one and all, for the most epic of battles!'
print(welcome_greeting)

class Battlefield:

    def __init__(self):
        self.run_game()
        self.dino_attack = ({Robot.health} - 100)
        print(f'{Robot.name} has been attacked by {Dinosaur.name}! Health level is now at {Robot.health}')

        



