
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
        # Display Winner
        #run_game = 
        pass
    
    
    def display_welcome(self):
        print('\nWelcome one and all, for the most epic of battles!')
        
    
    
    def battle_phase(self):
        self.battle_phase_one = Battlefield()
        
        while (self.robot_one.health > 0 and self.dinosaur_one.health > 0):
            self.robot_one.health = self.dinosaur_one.dino_attack(self.robot_one.health)
            self.dinosaur_one.health = self.robot_one.robo_attack(self.dinosaur_one.health)
            time.sleep(2)

            robot_attack_message = (f'{self.robot_one.name} has been attacked by {self.dinosaur_one.name}! Health level is now at {self.robot_one.health}')
            dinosaur_attack_message = (f'{self.dinosaur_one.name} has been attacked by {self.robot_one.name}! Health level is now at {self.dinosaur_one.health}')
            
            robot_missed_hit_message = (f'{self.robot_one.name} attempted to attack {self.dinosaur_one.name} but has missed!')
            dinosaur_missed_hit_message = (f'{self.dinosaur_one.name} tried to hit {self.robot_one.name} but missed!')
      
            if random.randint(0, 1) == 1:
                print(robot_attack_message)
            else:
                print(robot_missed_hit_message)        

            if random.randint(0, 1) == 1:
                print(dinosaur_attack_message)
            else:
                print(dinosaur_missed_hit_message)
                
                              
        # print(f'{self.dinosaur_one.name} has fought valiently, but was no match for {self.robot_one.name}! {self.dinosaur_one.name} will be laid to rest.')
        # print(f'{self.robot_one.name} has fought valiently, but was no match for {self.dinosaur_one.name}! {self.robot_one.name} will be laid to rest.')
    
    # def display_winner(self):
        # while(self.robot_one > self.dinosaur_one):
            # print (f'{self.robot_one.name} has defeated it\'s mighty competitor {self.dinosaur_one.name} and is declared the victor!')
        # else:
            # print(f'{self.dinosaur_one.name} has not gone extinct and is the winner of this battle!')

        
  