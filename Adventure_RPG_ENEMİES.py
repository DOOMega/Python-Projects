import time

class Creatures:

    def __init__(self, name, health, damage, exp):
        self.Name = name
        self.Health = health
        self.Damage = damage
        self.Exp = exp  
          
class Wolf(Creatures):

    def Wolfbite(self, gordon):
        if self.Health > 0:
            if (gordon.GordonsHealth > 0):
                time.sleep(1)
                gordon.GordonsHealth -= self.Damage         
                print("-------------------------------------------------------------------------------------------------")
                print("Wolf bit you Gordon's health:", gordon.GordonsHealth)

            else:
                print("Gordon cant resist to wolfs bite and die.")
        
        elif self.Health <= 0:
            print(f"You killed the {self.Name}.")
  

class Dragon(Creatures):

    def DragonAttack(self, gordon):
        if self.Health > 0:
            if gordon.GordonsHealth > 0:
                time.sleep(1)
                gordon.GordonsHealth -= self.Damage
                print("-------------------------------------------------------------------------------------------------")
                print("The dragon attacking Gordon's health:", gordon.GordonsHealth)
        
            elif gordon.GordonsHealth <= 0:
                print("Gordon cant resist to dragons attack and die.")

        elif self.Health <= 0:
            print(f"You killed the {self.Name}.")
    
    def FireBreath(self, gordon):
        if self.Health > 0:
            if gordon.GordonsHealth > 0:
                dragonFire = self.Damage * 2
                time.sleep(1)
                gordon.GordonsHealth -= dragonFire              
                print("-------------------------------------------------------------------------------------------------")
                print(f"The dragon breaths fire Gordon taking {dragonFire} damage Gordon's health:", gordon.GordonsHealth)
                
                dragonDOT = dragonFire // 3
                duration = 3
                for _ in range(duration):
                    if gordon.GordonsHealth <= 0:
                        print("Gordon cant resist to dragons firebreath and die.") 
                        break
                           
                    time.sleep(1)
                    gordon.GordonsHealth -= dragonDOT
                    print(f"Gordon is burning from Fire Breath. Gordon's health: {gordon.GordonsHealth}")

        elif gordon.GordonsHealth <= 0:
                        print("Gordon cant resist to dragons firebreath and die.") 
                                  

        elif self.Health <= 0:
            print(f"You killed the {self.Name}.")                   
                            

class Troll(Creatures):

    def TrollAttack(self, gordon):
        if self.Health > 0:
            if gordon.GordonsHealth > 0:
                time.sleep(1)
                gordon.GordonsHealth -= self.Damage
                print("-------------------------------------------------------------------------------------------------")
                print("Troll attacking to you Gordon's health:", gordon.GordonsHealth)
                
            elif gordon.GordonsHealth <= 0:
                print("Gordon cant resist to trolls attack and die.")

        elif self.Health <= 0:
            print(f"You killed the {self.Name}.")



    def TrollSlam(self, gordon):                          
        if self.Health > 0:
            if gordon.GordonsHealth > 0:  
                time.sleep(1)
                gordon.GordonsHealth -= self.Damage                   
                print("-------------------------------------------------------------------------------------------------")
                print("Troll attacking to you Gordon's health:", gordon.GordonsHealth)
                gordon.StunBar +=1
                print("Stunbar:", gordon.StunBar)
                if gordon.StunBar == 3:
                    gordon.GordonsHealth -= self.Damage
                    print("-------------------------------------------------------------------------------------------------")              
                    print("You stunned troll attacking you Gordon's health:", gordon.GordonsHealth)
                    time.sleep(2)
                    gordon.StunBar = 0

            elif gordon.GordonsHealth <= 0:
                print("Gordon cant resist to trolls slam and die.")

        elif self.Health <= 0:
            print(f"You killed the {self.Name}.")
 
                            

class Gordon:

    def __init__(self, gordonsHealth, damage, inventory):
        self.GordonsHealth = gordonsHealth
        self.Damage = damage
        self.Inventory = inventory
        self.StunBar = 0    
        self.Stamina = 10
        self.StaminaRegen = 1
        self.Level = 1
        self.Exp = 0
        self.ExpBar = 2

    def Show_Inventory(self):
        print("inventory: ", self.Inventory)

    def Use_Item(self, item_name):
        for item in self.Inventory:
            if item["name"].lower() == item_name.lower():
                if "heal" in item:
                    self.GordonsHealth += item["heal"]
                    self.Inventory.remove(item)
                    print("**************************************************************************")
                    print("You have found red potion and drink Gordon's health:", self.GordonsHealth)

                elif "damage" in item:
                    self.Damage = item["damage"]
                    print("**************************************************************************")
                    print(f"You equipped a {item['name']} with damage: {item['damage']}")
                return
        print("You don't have that item in your inventory.")


    def GainExp(self, xp):
        self.Exp += xp
        if self.Exp >= self.ExpBar:
            self.Level += 1
            self.Exp = 0
            self.ExpBar *= 2 
            print(f"You leveled up, Level: {self.Level}")
          
        else:
            print(f"You gained {xp} exp.")


    def Add_Inventory(self, item):    
        if item in self.Inventory:
            print("This item is already in.")

        else:
            self.Inventory.append(item)
            print(f"This {item} added in your inventory.")
        

    def Basic_Attack(self, creature):                     
        if creature:
            creature.Health -= self.Damage
            self.Regen_stamina()
            print("-------------------------------------------------------------------------------------------------")
            print(f"{creature.Name} has taking {self.Damage}, {creature.Name}s health: {creature.Health}.")


    def Double_Attack(self, creature):                      
        if self.Stamina > 0:
            doubled = 2 * self.Damage
            creature.Health -= doubled
            print("-------------------------------------------------------------------------------------------------")
            print(f"{creature.Name} has taking {doubled}, {creature.Name}s health: {creature.Health}.")

    
    def Use_stamina(self, amount):         
        if self.Stamina == 0:
            print("-------------------------------------------------------------------------------------------------")
            print("You havent yet enough stamina!")
            
        else:
            self.Stamina -= amount
            print("-------------------------------------------------------------------------------------------------")
            print("Current stamina:", self.Stamina)

    def Regen_stamina(self):
        if self.Stamina == 10:
            print("-------------------------------------------------------------------------------------------------")
            print("You have enough stamina current stamina:", self.Stamina)

        else:
            self.Stamina += self.StaminaRegen
            print("-------------------------------------------------------------------------------------------------")
            print("Your stamina reneweing:", self.Stamina)


    def DisplayStatus(self):
        print("-----------------GORDON'S STATS---------------------")
        print(f"Level:{self.Level} Health:{self.GordonsHealth}, Stamina:{self.Stamina}, Damage:{self.Damage}")
        print("----------------------------------------------------")

