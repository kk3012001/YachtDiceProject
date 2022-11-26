import random
import os
from time import sleep

#Dice Output System
class Dice : 
    
    def roll(self, a):
        s="+ - - - - +"
        m1="|  o   o  |"
        m2="|  o      |"
        m3="|    o    |"
        m4="|      o  |"
        m5="|         |"
        if a == 1:
            str1=m5
            str2=m3
            str3=m5
        elif a == 2:
            str1=m2
            str2=m5
            str3=m4
        elif a == 3:
            str1=m2
            str2=m3
            str3=m4
        elif a == 4:
            str1=m1
            str2=m5
            str3=m1
        elif a == 5:
            str1=m1
            str2=m3
            str3=m1
        elif a == 6:
            str1=m1
            str2=m1
            str3=m1
        print(s)
        print(str1)
        print(str2)
        print(str3)
        print(s)
    
    
#Score System
player1 = "PLAYER 1"
player2 = "PLAYER 2"
player1score = dict()
player2score = dict()
isPlayer1 = True

#Player Turn
class PlayerTurn:
    def start(self, isPlayer1):
        if isPlayer1 == True:
            print(player1 + "'s TURN START")
            player = player1score
        else:
            print(player2 + "'s TURN START")
            player = player2score
        sleep(1)
        print("Rolling Dice...")
        sleep(1)
    
    
    
    


#Scoreboard
class Scoreboard :
    def display(self):
        os.system('clear')


#Iniciallize game
class Init:
    def start():
        print("""
         _  _  __    ___  _  _  ____    ____  __  ___  ____ 
        ( \/ )/ _\  / __)/ )( \(_  _)  (    \(  )/ __)(  __)
         )  //    \( (__ ) __ (  )(     ) D ( )(( (__  ) _) 
        (__/ \_/\_/ \___)\_)(_/ (__)   (____/(__)\___)(____)
        """)
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        input("Press Enter to continue...")

Init.start()
isGamestart = True
while isGamestart == True:
    break