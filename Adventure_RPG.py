from enum import Enum
import random
import time
from Adventure_RPG_ENEMİES import *

weapons = {"name": "a long blade", "damage": 10}
potions = {"name": "red potion", "heal": 50}
Inventory = [weapons, potions]

class BATTLE(Enum):
    START = 1
    PLAYERTURN = 2
    ENEMYTURN = 3
    WIN = 4
    LOSE = 5


gordon = Gordon(50, 0, Inventory)

troll = Troll("troll", 40, 10, 3)
dragon = Dragon("dragon", 60, 10, 5)
wolf = Wolf("wolf", 20, 10, 1)

creatureList = [troll, dragon, wolf]


AreaList = ["Cave", "Forest", "Dungeon"]

dragonSkills = ["dragon attack", "fire breath"]
trollSkills = ["troll attack", "troll slam"]

Areas = {
    "cave": [troll],
    "lair": [dragon],
    "forest":[wolf]
}


def PrologueFight(gordon, creatures):  
    while(True):
        CreatureSpawn = random.choice(creatures)        
        gordon.DisplayStatus()

        print("-------------------------------------------------------------------------")
        print(f"You encounter a {CreatureSpawn.Name} with {CreatureSpawn.Health} health!")
        choice = str(input("Do you want [f]ight or [r]un?: ")).lower()
        
        if choice == "f":
            while gordon.GordonsHealth > 0 and CreatureSpawn.Health > 0:            
                if CreatureSpawn == wolf:
                    attack = str(input("You have 2 skill [a]ttack or [d]ouble attack:"))
                    if attack == "a":
                        gordon.Basic_Attack(CreatureSpawn)                      
                        wolf.Wolfbite(gordon)
                                   
                    elif attack == "d":
                        gordon.Double_Attack(CreatureSpawn)
                        gordon.Use_stamina(2)
                        wolf.Wolfbite(gordon)                        

                elif CreatureSpawn == dragon:
                    attack = str(input("You have 2 skill [a]ttack or [d]ouble attack:"))
                    randomDragon = random.choice(dragonSkills)
                    if attack == "a" :
                        gordon.Basic_Attack(CreatureSpawn)
                            
                        if randomDragon == "dragon attack":
                            dragon.DragonAttack(gordon)                    
                                                        
                        elif randomDragon == "fire breath":
                            dragon.FireBreath(gordon)
                                         
                    elif attack == "d":
                        gordon.Double_Attack(CreatureSpawn)
                        gordon.Use_stamina(2)
                            
                        if randomDragon == "dragon attack":
                            dragon.DragonAttack(gordon)  
                                                       
                        elif randomDragon == "fire breath":
                            dragon.FireBreath(gordon)
                                                     
                elif CreatureSpawn == troll:
                    attack = str(input("You have 2 skill [a]ttack or [d]ouble attack:"))
                    randomTroll = random.choice(trollSkills)
                    if attack == "a":
                        gordon.Basic_Attack(CreatureSpawn)
                            
                        if randomTroll == "troll attack":
                            troll.TrollAttack(gordon)

                        elif randomTroll == "troll slam":
                            troll.TrollSlam(gordon)      

                    elif attack == "d":
                        gordon.Double_Attack(CreatureSpawn)
                        gordon.Use_stamina(2)                     
                            
                        if randomTroll == "troll attack":
                            troll.TrollAttack(gordon)

                        elif randomTroll == "troll slam":
                            troll.TrollSlam(gordon)      
                                       
                if CreatureSpawn.Health <= 0:
                    creatures.remove(CreatureSpawn)
                    gordon.GainExp(CreatureSpawn.Exp)
                    if not creatures:
                        print("You killed all.")
                    break
                                                                           
        elif choice == "r":
            print("You running...")
            time.sleep(3)
        


def Main():
    print("**********************************************************************")
    print("Welcome to The Fate Of Gordon game.")
    print("You a knight named Gordon.")
    print("You were found unconscious in forest. You have wound you need to heal.")
    print("**********************************************************************")
    print("Your current health:", gordon.GordonsHealth)
    
    while(True):
        print("If you wanna quit inventory [q]")
        choice = str(input("take a look [i]nventory:"))
        if choice.lower() == "i":
            print("You looking inventory...")
            time.sleep(2)
            gordon.Show_Inventory()
            select = input("Select an item: ").strip().lower()
            gordon.Use_Item(select)
                      
        elif choice.lower() == "q":
            print("Exiting inventory...")
            time.sleep(1)
            break
        
        else:
            while (True):             
                answer = input("You have a wound and you're barehanded. Are you sure you want to continue? (yes/no): ")
                if answer.lower() == "yes":
                    print("Okay, you proceed.")
                    break
                
                elif answer.lower() == "no":
                    print("Good choice. You're staying cautious.")
                    break

                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                  
    
    print("**************************************************************************")
    print("You are lost in forest look around.")


Main()  
PrologueFight(gordon, creatureList)


    
