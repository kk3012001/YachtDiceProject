import random
diceNow = []
numberofDice = 5
rolleddice = {}

for i in range(0, numberofDice):
    tempDice = random.randrange(1, 6)
    diceNow.append(tempDice)
print(diceNow)
        
for i in range(0, len(diceNow)):
    rolleddice["dice{}".format(i)] = diceNow[i]

print(rolleddice)

class Dice:
    
    
    def setdot(dot):
            if dot == 1:
                dicerow1 = [' ',' ']
                dicerow2 = [' ', 'o', ' ']
                dicerow3 = [' ', ' ']
                print(dicerow1)
            elif dot == 2:
                dicerow1 = [' ',' ']
                dicerow2 = ['o', '', 'o']
                dicerow3 = [' ', ' ']
            elif dot == 3:
                dicerow1 = ['o',' ']
                dicerow2 = [' ', 'o', ' ']
                dicerow3 = [' ', 'o']
            elif dot == 4:
                dicerow1 = ['o','o']
                dicerow2 = [' ', ' ', ' ']
                dicerow3 = ['o', 'o']                
            elif dot == 5:
                dicerow1 = ['o','o']
                dicerow2 = [' ', 'o', ' ']
                dicerow3 = ['o', 'o']
            elif dot == 6:
                dicerow1 = ['o','o']
                dicerow2 = ['o', ' ', 'o']
                dicerow3 = ['o', 'o']
                
    def dotprint():
        for i in range(0, len(diceNow)):
         rolleddice["dice{}".format(i)] = diceNow[i]
         Dice.setdot(rolleddice["dice1"])
