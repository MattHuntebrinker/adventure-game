# You are welcome to write and include any other Python files you want or need
# however your game must be started by calling the main function in this file.

from random import randint
import random
import sys

class pm:
    def __init__(self):
        self.hp = 100
        
    def losehp(self,amount):
        self.hp = self.hp - amount
        return self.hp
    
    def gainhp(self,amount):
        self.hp = self.hp + amount
        return self.hp

class adventurer:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.gold = 100
        self.sword = 1
    
    def losehp(self,amount):
        self.hp = self.hp - amount
        return self.hp
    
    def gainhp(self,amount):
        self.hp = self.hp + amount
        return self.hp
    
    def gaingold(self,amount):
        self.gold = self.gold + amount
        return self.gold
    
    def losegold(self,amount):
        self.gold = self.gold - amount
        return self.gold
    
    def returnhealth(self):
        health = self.hp
        return health
    def returngold(self):
        return self.gold
    
    def swordupgrade(self):
        self.sword += .5
    
    def gethp(self):
        return self.hp
        
        

def start():
    print("Welcome adventurer, to the adventure game!")
    name = input("We just need a name to get started on your quest, what is your name?")
    print("Wonderful! Are you ready {0} for a quest of a lifetime?".format(name))
    print("You have a certain number of steps to get out of the dungeon, if you can't, the game is over")
    print("You start with 100 gold and 100 life points")
    return name

def game(name):
    p1 = adventurer(name)
    python = pm()
    turns = 10
    poisoned = False
    go = input('you have {0} steps left, would you like to proceed? (y/n)'.format(turns))
    if go == 'y':
        pass
    else:
        sys.exit()
    goodlist = ['You uncover a chest','You help a dying peasant','You sell your sword, buy another one','You find a health potion']
    badlist = ['The python monster appears!','Oh know, you were poisoned']
    while turns > 0:
        goodorbad = randint(0,1)
        if goodorbad == 0:
            scenario = random.choice(goodlist)
            print(scenario)
            if scenario == 'You uncover a chest':
                newgold = randint(100,300)
                print('You gained {0} gold'.format(newgold))
                totalgold = p1.gaingold(newgold)
                print('Your total amount of gold is {0}'.format(totalgold))
                
            elif scenario == 'You help a dying peasant':
                newgold = randint(75,200)
                print('The peasant gives you {0} gold'.format(newgold))
                totalgold = p1.gaingold(newgold)
                print('Your total amount of gold is {0}'.format(totalgold))
            
            elif scenario == 'You sell your sword, buy another one':
                swordcost = 100
                print('Your sword as been upgraded, but that comes at a cost')
                totalgold = p1.losegold(swordcost)
                print('That is going to cost you {0} gold'.format(swordcost))
                print('Your new gold total is {0}'.format(totalgold))
                
            elif scenario == 'You find a health potion':
                healthpot = randint(0,20)
                print('As you drink it, you feel your life points increasing')
                totallp = p1.gainhp(healthpot)
                print('Your health pottion raises your life points by {0}'.format(healthpot))
                print('Your new lifepoints total is {0}'.format(totallp))
                if poisoned == True:
                    badlist.append('Oh know, you were poisoned')
                poisoned = False
                
        
        if goodorbad == 1:
            scenario = random.choice(badlist)
            print(scenario)
            if scenario == 'The python monster appears!':
                print("You have found the python monster, now it's time for battle!")
                whowinsfight = randint(0,2)
                if whowinsfight == 0:
                    pmhealth = randint(20,30)
                    print('You win this round, you took {0} life points from the python monster'.format(pmhealth))
                    totallp = python.losehp(pmhealth)
                    print('His total health is {0}'.format(totallp))
                elif whowinsfight == 1:
                    healthloss = randint(20,30)
                    print('The python monster got the better of you that round')
                    totallp = p1.losehp(healthloss)
                    print('You lose {0} life points, your new total is {1}'.format(healthloss,totallp))
                elif whowinsfight == 2:
                    healthloss = randint(20,30)
                    pythonloss = randint(20,30)
                    totallp = p1.losehp(healthloss)
                    totalpython = python.losehp(pythonloss)
                    print('You both survive, but both come out damaged')
                    print('You lose {0} life points, your new total is {1} life points'.format(healthloss,totallp))
                    print('Python loses {0} life points, his new total is {1} life points'.format(pythonloss,totalpython))
            elif scenario == 'Oh know, you were poisoned':
                print('At the end of every turn, you will lose 10 life points unless you find a health potion')
                poisoned = True
                badlist.remove('Oh know, you were poisoned')
               
        turns -= 1
        if poisoned == True:
            totallp = p1.losehp(10)
            print('You are hurt from the poison, your new life points is {0}'.format(totallp))
        myhealth = p1.returnhealth()
        if myhealth <= 0:
            print('Oh know, you died! Game over, please play again')
            sys.exit()
        if turns > 0:
            go = input('you have {0} steps left, would you like to proceed? (y/n)'.format(turns))
            print('\n')
            if go == 'y':
                continue
            else:
                sys.exit()
                
    print('\n')
    print('Congrats! You made it out of the dungeon alive! You win!')
    gold = p1.returngold()
    endinghealth = p1.returnhealth()
    print('You ended with {0} gold and {1} health, well done!'.format(gold,endinghealth))

def main():
    name = start()
    game(name)
    
    
    
main()