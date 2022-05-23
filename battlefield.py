
from robot import Robot
from dinosaur import Dinosaur
import time
import random


class Battlefield:

    def __init__(self):
        self.robot_one = Robot()
        self.dinosaur_one = Dinosaur()
        
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
    
    
    def display_welcome(self):
        print('\nWelcome one and all, for the most epic of battles! ROBOT Gary VERSUS DINOSAUR Sparky!!!\n')
        
    
    def battle_phase(self):
        while (self.robot_one.health > 0 and self.dinosaur_one.health > 0):
            time.sleep(2)                     

            # Sparky
            if random.randint(0, 1) == 1:
                self.dinosaur_one.health = self.robot_one.robo_attack(self.dinosaur_one.health)
                print(f'\n{self.dinosaur_one.name} has been attacked by {self.robot_one.name}! Health level is now at {self.dinosaur_one.health}!\n')
            else:
                print(f'\n{self.robot_one.name} attempted to attack {self.dinosaur_one.name} but has missed! {self.dinosaur_one.name} health level remains at {self.dinosaur_one.health}!\n')                      

            # Gary                                                                                                      #  
            if random.randint(0, 1) == 1:
                self.robot_one.health = self.dinosaur_one.dino_attack(self.robot_one.health)
                print(f'\n{self.robot_one.name} has been attacked by {self.dinosaur_one.name}! Health level is now at {self.robot_one.health}!\n')
            else: 
                print(f'\n{self.dinosaur_one.name} tried to hit {self.robot_one.name} but missed! {self.robot_one.name} health level remains at {self.robot_one.health}!\n')

            
    def display_winner(self):
        if (self.robot_one.health > 5 and self.dinosaur_one.health < 5):
            print (f'\n{self.dinosaur_one.name} has fought valiently, but was no match for {self.robot_one.name}! {self.dinosaur_one.name} will be laid to rest. Which means {self.robot_one.name} is declared the victor!\n')
        elif (self.dinosaur_one.health > 5 and self.robot_one.health < 5):
            print(f'\n{self.robot_one.name} has fought valiently, but was no match for {self.dinosaur_one.name}! {self.robot_one.name} will be laid to rest. {self.dinosaur_one.name} has not gone extinct and is the winner of this battle!\n')
        else:
            print (f'{self.robot_one.name} and {self.dinosaur_one.name} fought hard, to their deaths! May they both rest in peace!')
        
