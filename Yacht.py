import random
import os
import re
from time import sleep

isGameplay = True

#Iniciallize game
class Init:
    def Start():
        while isGameplay == True:
            os.system('clear')
            print("* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - *")
            print("|                                                                                                     |")
            print("|                                                                                                     |")
            print("|                                                                                                     |")
            print("|                                                                                                     |")
            print("""|                                                                                                     |
|                         _  _  __    ___  _  _  ____    ____  __  ___  ____                          |
|                        ( \/ )/ _\  / __)/ )( \(_  _)  (    \(  )/ __)(  __)                         |
|                         )  //    \( (__ ) __ (  )(     ) D ( )(( (__  ) _)                          |
|                        (__/ \_/\_/ \___)\_)(_/ (__)   (____/(__)\___)(____)                         |
|                                                                                                     |""")
            print("|                                                                                                     |")
            print("|                                                                                                     |")
            print("|                                                                                                     |")
            print("|                                                                                                     |")
            print("|                                                                                                     |")
            print("|                                         by Jiwon Kang                                               |")
            print("|                                                                                                     |")
            print("|                                                                                                     |")
            print("|                                                                                                     |")
            print("|                                                                                                     |")
            print("|                                                                                                     |")
            print("* - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - *")
            print("Press Enter to continue...")
            userInput = input(">> ")
            if userInput == "help":
                sleep(0.5)
                Main.Help()
            else:
                break
            

    
#Database
class Database : 
    isPlayer1 = True
    player1Score = {"Aces" : "-", "Deuces" : "-", "Threes" : "-", "Fours" : "-", "Fives" : "-", "Sixes" : "-", "Bonus" : "-", "Choice" : "-", "Fullhouse" : "-", "FourofaKind" : "-", "S.Straight" : "-", "L.Straight" : "-", "Yacht" : "-" }
    player2Score = {"Aces" : "-", "Deuces" : "-", "Threes" : "-", "Fours" : "-", "Fives" : "-", "Sixes" : "-", "Bonus" : "-", "Choice" : "-", "Fullhouse" : "-", "FourofaKind" : "-", "S.Straight" : "-", "L.Straight" : "-", "Yacht" : "-" }
    total1 = 0
    total2 = 0
    sumBonus1 = 0
    sumBonus2 = 0
    
    def Init():
        Database.isPlayer1 = True
        Database.player1Score = {"Aces" : "-", "Deuces" : "-", "Threes" : "-", "Fours" : "-", "Fives" : "-", "Sixes" : "-", "Bonus" : "-", "Choice" : "-", "Fullhouse" : "-", "FourofaKind" : "-", "S.Straight" : "-", "L.Straight" : "-", "Yacht" : "-" }
        Database.player2Score = {"Aces" : "-", "Deuces" : "-", "Threes" : "-", "Fours" : "-", "Fives" : "-", "Sixes" : "-", "Bonus" : "-", "Choice" : "-", "Fullhouse" : "-", "FourofaKind" : "-", "S.Straight" : "-", "L.Straight" : "-", "Yacht" : "-" }
        Database.total1 = 0
        Database.total2 = 0
        Database.sumBonus1 = 0
        Database.sumBonus2 = 0
    
    def Sum(playerDatabase, result):
        if playerDatabase == Database.player1Score:
            Database.total1 = Database.total1 + result
        elif playerDatabase == Database.player2Score:
            Database.total2 = Database.total2 + result
    
    def BonusSum(playerDatabase, result):
        if playerDatabase == Database.player1Score:
            Database.sumBonus1 = Database.sumBonus1 + result
        elif playerDatabase == Database.player2Score:
            Database.sumBonus2 = Database.sumBonus2 + result
            
        

class Dice :
    rollChances = 3
    diceDot = []
    rolledDice = []
    rerollList = [1, 1, 1, 1, 1]
    dicerow1 = []
    dicerow2 = []
    dicerow3 = []
    
    def Init():
        Dice.rollChances = 3
        Dice.diceDot.clear()
        Dice.rolledDice.clear()
        Dice.rerollList = [1, 1, 1, 1, 1]
    
    def FirstRoll():
        Dice.Init()
        for i in range(0, 5):
            tempDice = random.randrange(1, 6)
            Dice.rolledDice.append(tempDice)
        Dice.rollChances =  Dice.rollChances - 1
    
    def Reroll():
        for i in range(0, 5):
            if Dice.rerollList[i] == 0:
                pass
            elif Dice.rerollList[i] == 1:
                Dice.rolledDice[i] = random.randrange(1,6)
        Dice.rollChances = Dice.rollChances - 1
                
    def SetDot(dot):
        if dot == 1:
            Dice.dicerow1 = [' ',' ']
            Dice.dicerow2 = [' ', 'o', ' ']
            Dice.dicerow3 = [' ', ' ']
        elif dot == 2:
            Dice.dicerow1 = [' ',' ']
            Dice.dicerow2 = ['o', ' ', 'o']
            Dice.dicerow3 = [' ', ' ']
        elif dot == 3:
            Dice.dicerow1 = ['o',' ']
            Dice.dicerow2 = [' ', 'o', ' ']
            Dice.dicerow3 = [' ', 'o']
        elif dot == 4:
            Dice.dicerow1 = ['o','o']
            Dice.dicerow2 = [' ', ' ', ' ']
            Dice.dicerow3 = ['o', 'o']                
        elif dot == 5:
            Dice.dicerow1 = ['o','o']
            Dice.dicerow2 = [' ', 'o', ' ']
            Dice.dicerow3 = ['o', 'o']
        elif dot == 6:
            Dice.dicerow1 = ['o','o']
            Dice.dicerow2 = ['o', ' ', 'o']
            Dice.dicerow3 = ['o', 'o']
            
    def DotPrint():
        for i in range(0, 5):
            Dice.SetDot(Dice.rolledDice[i])
            globals()["diceGraphic{}".format(i)] = [Dice.dicerow1, Dice.dicerow2, Dice.dicerow3]
         
            
            
    def PrintDiceInterface():
        Dice.DotPrint()
        fixGraphic = ["", "", "", "", ""]
        for i in range(0,5):
            if Dice.rerollList[i] == 0:
                fixGraphic[i] = "X"
            else:
                fixGraphic[i] = " "
        
        print(f"""
                Dice 1        Dice 2        Dice 3        Dice 4        Dice 5     
             * - - - - *   * - - - - *   * - - - - *   * - - - - *   * - - - - *  
             |  {diceGraphic0[0][0]}   {diceGraphic0[0][1]}  |   |  {diceGraphic1[0][0]}   {diceGraphic1[0][1]}  |   |  {diceGraphic2[0][0]}   {diceGraphic2[0][1]}  |   |  {diceGraphic3[0][0]}   {diceGraphic3[0][1]}  |   |  {diceGraphic4[0][0]}   {diceGraphic4[0][1]}  |   
             |  {diceGraphic0[1][0]} {diceGraphic0[1][1]} {diceGraphic0[1][2]}  |   |  {diceGraphic1[1][0]} {diceGraphic1[1][1]} {diceGraphic1[1][2]}  |   |  {diceGraphic2[1][0]} {diceGraphic2[1][1]} {diceGraphic2[1][2]}  |   |  {diceGraphic3[1][0]} {diceGraphic3[1][1]} {diceGraphic3[1][2]}  |   |  {diceGraphic4[1][0]} {diceGraphic4[1][1]} {diceGraphic4[1][2]}  |   
             |  {diceGraphic0[2][0]}   {diceGraphic0[2][1]}  |   |  {diceGraphic1[2][0]}   {diceGraphic1[2][1]}  |   |  {diceGraphic2[2][0]}   {diceGraphic2[2][1]}  |   |  {diceGraphic3[2][0]}   {diceGraphic3[2][1]}  |   |  {diceGraphic4[2][0]}   {diceGraphic4[2][1]}  |   
             * - - - - *   * - - - - *   * - - - - *   * - - - - *   * - - - - *  
        Fix  :    {fixGraphic[0]}             {fixGraphic[1]}             {fixGraphic[2]}             {fixGraphic[3]}             {fixGraphic[4]}
    """)
        print("                                         Reroll : ", Dice.rollChances)
        print("")
            
        
#PrintScoreboard
class Scoreboard :
    def PrintScore() :
        os.system('clear')
        print(f"""
* SCORE BOARD
|| Player 1 ||
||  Aces : {Database.player1Score['Aces']}  | Deuces : {Database.player1Score["Deuces"]} | Threes : {Database.player1Score['Threes']} | Fours : {Database.player1Score["Fours"]} | Fives : {Database.player1Score["Fives"]} | Sixes : {Database.player1Score['Sixes']} | {Database.sumBonus1} / 63 Bonus : {Database.player1Score['Bonus']} ||
|| Choice : {Database.player1Score['Choice']} | Fullhouse : {Database.player1Score['Fullhouse']} | Four of a Kind : {Database.player1Score['FourofaKind']} | S.Staright : {Database.player1Score['S.Straight']} | L.Straight : {Database.player1Score['L.Straight']} | Yacht : {Database.player1Score['Yacht']} ||
|| Total : {Database.total1} ||

|| Player 2 ||
||  Aces :  {Database.player2Score['Aces']} | Deuces : {Database.player2Score["Deuces"]} | Threes : {Database.player2Score['Threes']} | Fours : {Database.player2Score["Fours"]} | Fives : {Database.player2Score["Fives"]} | Sixes : {Database.player2Score['Sixes']} | {Database.sumBonus2}/ 63 Bonus : {Database.player2Score['Bonus']} ||
|| Choice : {Database.player2Score['Choice']} | Fullhouse : {Database.player2Score['Fullhouse']} | Four of a Kind : {Database.player2Score['FourofaKind']} | S.Staright : {Database.player2Score['S.Straight']} | L.Straight : {Database.player2Score['L.Straight']} | Yacht : {Database.player2Score['Yacht']} ||
|| Total : {Database.total2} ||
""")
        if Database.isPlayer1 == True:
            print("                                     ** Player 1 Turn **")
        elif Database.isPlayer1 == False:
            print("                                     ** Player 2 Turn **")

            
class PlayerAction:
    scored = False
    def Fix():
        print("Select Dice to Fix or Unfix | Cancel : Anything")
        while True:
            userInput = input(">> ")
            if userInput in ["1", "2", "3", "4", "5"]:
                if Dice.rerollList[int(userInput) - 1] == 0:
                  Dice.rerollList[int(userInput) - 1] = 1
                  break
                elif Dice.rerollList[int(userInput) - 1] == 1:
                   Dice.rerollList[int(userInput) - 1] = 0
                   break
            else:
                break
    
    def Score():
        if Database.isPlayer1 == True:
            playerDB = Database.player1Score
        elif Database.isPlayer1 == False:
            playerDB = Database.player2Score
            
        while True:
            Scoreboard.PrintScore()
            Dice.PrintDiceInterface()
            print("Select the Score")
            print("Aces : 1 | Deuces : 2 | Threes : 3 | Fours : 4 | Fives : 5 | Sixes : 6 || Back : Anything")
            print("Choices : q | Fullhouse : w |  Four of a Kind : e | S.Straight : r | L.Straight : t | Yacht : y")
            userInput = input(">> ")
            if userInput == "1":
                if playerDB["Aces"] != "-":
                    print("You aleady selected that score.")
                    continue
                else:
                    pass
                Score.Aces(playerDB)
                break
           
            elif userInput == "2":
                if playerDB["Deuces"] != "-":
                    print("You aleady selected that score.")
                    continue
                else:
                    pass
                Score.Deuces(playerDB)
                break
           
            elif userInput == "3":
                if playerDB["Threes"] != "-":
                    print("You aleady selected that score.")
                    continue
                else:
                    pass
                Score.Threes(playerDB)
                break
            
            elif userInput == "4":
                if playerDB["Fours"] != "-":
                    print("You aleady selected that score.")
                    continue
                else:
                    pass
                Score.Fours(playerDB)
                break            
            
            elif userInput == "5":
                if playerDB["Fives"] != "-":
                    print("You aleady selected that score.")
                    continue
                else:
                    pass
                Score.Fives(playerDB)
                break            
            
            elif userInput == "6":
                if playerDB["Sixes"] != "-":
                    print("You aleady selected that score.")
                    continue
                else:
                    pass
                Score.Sixes(playerDB)
                break
            
            elif userInput == "q":
                if playerDB["Choice"] != "-":
                    print("You aleady selected that score.")
                    continue
                else:
                    pass
                Score.Choice(playerDB)
                break
            
            elif userInput == "w":
                if playerDB["Fullhouse"] != "-":
                    print("You aleady selected that score.")
                    continue
                else:
                    pass
                Score.Fullhouse(playerDB)
                break
                
            elif userInput == "e":
                if playerDB["FourofaKind"] != "-":
                    print("You aleady selected that score.")
                    continue
                else:
                    pass
                Score.FourofaKind(playerDB)
                break
                
            elif userInput == "r":
                if playerDB["S.Straight"] != "-":
                    print("You aleady selected that score.")
                    continue
                else:
                    pass
                Score.SStraight(playerDB)
                break
                
            elif userInput == "t":
                if playerDB["L.Straight"] != "-":
                    print("You aleady selected that score.")
                    continue
                else:
                    pass
                Score.LStraight(playerDB)
                break

            elif userInput == "y":
                if playerDB["Yacht"] != "-":
                    print("You aleady selected that score.")
                    continue
                Score.Yacht(playerDB)
                break
            else:
                break
                        
    def UserInput():
        while True:
            Scoreboard.PrintScore()
            Dice.PrintDiceInterface()
            if Checker.CanFullhouse == True:
                print("You Can Score Fullhouse!")
            if Checker.CanFourofaKind == True:
                print("You Can Score Four of a Kind!")
            if Checker.CanSStraight == True:
                print("You Can Score S.Straight!")
            if Checker.CanLStraight == True:
                print("You Can Score L.Straight!")
            if Checker.CanYacht == True:
                print("You Can Score Yacht!")
                
            print("Choose Your Action...")
            print("fix : 1 | reroll : 2 | score : 3 | or help")
            userInput = input(">> ")
            if userInput == "1" :
                PlayerAction.Fix()
                Scoreboard.PrintScore()
                Dice.PrintDiceInterface()
            elif userInput == "2":
                if Dice.rollChances == 0:
                    print("You spended all of Reroll chances!")
                    sleep(0.5)
                    continue
                else:
                    break
            elif userInput == "3":
                Scoreboard.PrintScore()
                Dice.PrintDiceInterface()
                PlayerAction.Score()
                if PlayerAction.scored == True:
                    break
                else:
                    continue
            elif userInput == "help":
                Main.Help()
                continue
                
            else:
                print("ERROR!")
                
                sleep(1)
                continue
                
    def EndTurn():
        if Database.isPlayer1 == True:
            Database.isPlayer1 = False
        elif Database.isPlayer1 == False:
            Database.isPlayer1 = True
        Checker.End()
        Dice.rollChances = 3


class Checker:
    CanFullhouse = False
    CanFourofaKind = False
    CanSStraight = False
    CanLStraight = False
    CanYacht = False
    triple = False
    
    
    def Fullhouse():
        for i in range(1,7):            
            if Dice.rolledDice.count(i) == 3:
                Checker.triple = True
            else:
                Checker.triple = False
        if Checker.triple == True:
            for i in (1, 7):
                if Dice.rolledDice.count(i) == 2:
                    Checker.CanFullhouse = True
                    Checker.triple = False
        else:
            Checker.CanFullhouse = False
            
    
    def FourofaKind():
        for i in range(1,7):
            if Dice.rolledDice.count(i) >= 4:
                Checker.CanFourofaKind = True
                
    def SStraight():
        for i in range(1,4):
            if (i in Dice.rolledDice) and (i+1 in Dice.rolledDice) and (i+2 in Dice.rolledDice) and (i+3 in Dice.rolledDice):
                Checker.CanSStraight = True
    
    def LStraight():
        for i in range(1,3):
            if (i in Dice.rolledDice) and (i+1 in Dice.rolledDice) and (i+2 in Dice.rolledDice) and (i+3 in Dice.rolledDice) and (i+4 in Dice.rolledDice):
                Checker.CanLStraight = True

    def Yacht():
        for i in range(1, 7):
            if Dice.rolledDice.count(i) == 5:
                Checker.CanYacht = True
    def End():
        Checker.CanFullhouse = False
        Checker.CanFourofaKind = False
        Checker.CanSStraight = False
        Checker.CanLStraight = False
        Checker.CanYacht = False
                
    def All():
        Checker.Fullhouse()
        Checker.FourofaKind()
        Checker.SStraight()
        Checker.LStraight()
        Checker.Yacht()

class Score:

    def Aces(PlayerDatabase):
        result = 0
        for i in range(0, 5):
            if Dice.rolledDice[i] == 1:
                result = result + 1
        PlayerDatabase["Aces"] = result
        Database.Sum(PlayerDatabase,result)
        Database.BonusSum(PlayerDatabase,result)
        Score.BonusCheck(PlayerDatabase)
        Dice.rollChances = 0
        PlayerAction.scored = True
        
    def Deuces(PlayerDatabase):
        result = 0
        for i in range(0, 5):
            if Dice.rolledDice[i] == 2:
                result = result + 2
        PlayerDatabase["Deuces"] = result
        Database.Sum(PlayerDatabase,result)
        Database.BonusSum(PlayerDatabase,result)
        Score.BonusCheck(PlayerDatabase)
        Dice.rollChances = 0
        PlayerAction.scored = True
        
    def Threes(PlayerDatabase):
        result = 0
        for i in range(0, 5):
            if Dice.rolledDice[i] == 3:
                result = result + 3
        PlayerDatabase["Threes"] = result
        Database.Sum(PlayerDatabase,result)
        Database.BonusSum(PlayerDatabase,result)
        Score.BonusCheck(PlayerDatabase)
        Dice.rollChances = 0
        PlayerAction.scored = True

    def Fours(PlayerDatabase):
        result = 0
        for i in range(0, 5):
            if Dice.rolledDice[i] == 4:
                result = result + 4
        PlayerDatabase["Fours"] = result
        Database.Sum(PlayerDatabase,result)
        Database.BonusSum(PlayerDatabase,result)
        Score.BonusCheck(PlayerDatabase)
        Dice.rollChances = 0
        PlayerAction.scored = True
        
    def Fives(PlayerDatabase):
        result = 0
        for i in range(0, 5):
            if Dice.rolledDice[i] == 5:
                result = result + 5
        PlayerDatabase["Fives"] = result
        Database.Sum(PlayerDatabase,result)
        Database.BonusSum(PlayerDatabase,result)
        Score.BonusCheck(PlayerDatabase)
        Dice.rollChances = 0
        PlayerAction.scored = True
    
    def Sixes(PlayerDatabase):
        result = 0
        for i in range(0, 5):
            if Dice.rolledDice[i] == 6:
                result = result + 6
        PlayerDatabase["Sixes"] = result
        Database.Sum(PlayerDatabase,result)
        Database.BonusSum(PlayerDatabase,result)
        Score.BonusCheck(PlayerDatabase)
        Dice.rollChances = 0
        PlayerAction.scored = True
        
    def BonusCheck(playerDatabase):
        if playerDatabase == Database.player1Score:
            if Database.sumBonus1 >= 63:
                playerDatabase["Bonus"] = 35
        elif playerDatabase == Database.player2Score:
            if Database.sumBonus2 >= 63:
                playerDatabase["Bonus"] = 35


    def Choice(PlayerDatabase):
        result = 0
        for i in range(0, 5):
            result = result + Dice.rolledDice[i]
        PlayerDatabase["Choice"] = result
        Database.Sum(PlayerDatabase,result)
        Dice.rollChances = 0
        PlayerAction.scored = True

    def Fullhouse(PlayerDatabase):
        result = 0
        if Checker.CanFullhouse == True:
            for i in range(0, 5):
                result = result + Dice.rolledDice[i]
            PlayerDatabase["Fullhouse"] = result
            Database.Sum(PlayerDatabase,result)
        else:
            PlayerDatabase["Fullhouse"] = 0
        Dice.rollChances = 0
        PlayerAction.scored = True
            
    def FourofaKind(PlayerDatabase):
        result = 0
        if Checker.CanFullhouse == True:
            for i in range(0, 5):
                result = result + Dice.rolledDice[i]
            PlayerDatabase["FourofaKind"] = result
            Database.Sum(PlayerDatabase,result)
        else:
            PlayerDatabase["FourofaKind"] = 0
        Dice.rollChances = 0
        PlayerAction.scored = True

    def SStraight(PlayerDatabase):
        if Checker.CanSStraight == True:
            PlayerDatabase["S.Straight"] = 15
            Database.Sum(PlayerDatabase, 15)
        else:
            PlayerDatabase["S.Straight"] = 0
        Dice.rollChances = 0
        PlayerAction.scored = True

    def LStraight(PlayerDatabase):
        if Checker.CanLStraight == True:
            PlayerDatabase["L.Straight"] = 30
            Database.Sum(PlayerDatabase, 30)
        else:
            PlayerDatabase["L.Straight"] = 0
        Dice.rollChances = 0
        PlayerAction.scored = True

    def Yacht(PlayerDatabase):
        if Checker.CanYacht == True:
            PlayerDatabase["Yacht"] = 50
            Database.Sum(PlayerDatabase, 50)
        else:
            PlayerDatabase["Yacht"] = 0
        Dice.rollChances = 0
        PlayerAction.scored = True
            
        
        
class Main:
    def Help():
        print("""
                  
1. 주사위 5개를 던진다.
2. 이 중 원하는 주사위들은 남겨두고, 나머지 주사위들을 다시 던진다. 다시 던지기는 한 라운드에 2번까지(즉, 한 라운드에 최대 3번까지 던질 수 있다.) 가능하며, 앞에서 던지지 않았던 주사위도 원한다면 다시 던질 수 있다.
3. 주사위 던지기가 끝난 후 나온 최종 조합으로, 아래 제시된 족보 중 아직까지 기록되지 않은 하나를 반드시 선택하여, 점수판에 해당 족보의 점수를 규칙에 맞게 기록해야 한다.
4. 기록되지 않은 족보 중에서 만족하는 족보가 없거나, 있더라도 점수 기대값이 마음에 들지 않는 등의 사유로, 만족하지 않는 족보를 선택하는 경우, 선택한 족보의 점수칸에 0점으로 기록해야 한다.
5. 모든 플레이어가 점수판을 모두 채우면 게임이 끝난다. 점수판에 기록한 점수 총합이 가장 높은 사람이 승리하며, 순위를 가릴 경우 점수 총합이 높은 순서대로 순위를 결정한다.

Aces : 1이 나온 주사위 눈의 총합. 최대 5점.
Deuces : 2가 나온 주사위 눈의 총합. 최대 10점.
Threes : 3이 나온 주사위 눈의 총합. 최대 15점.
Fours : 4가 나온 주사위 눈의 총합. 최대 20점.
Fives : 5가 나온 주사위 눈의 총합. 최대 25점.
Sixes : 6이 나온 주사위 눈의 총합. 최대 30점.
보너스 : 상단 항목의 점수 합계가 63점 이상일 때, 35점을 추가로 얻는다.

Choice : 주사위 눈 5개의 총합. 최대 30점.
4 of a Kind : 동일한 주사위 눈이 4개 이상일 때, 주사위 눈 5개의 총합. 최대 30점.
Full House : 주사위를 3개, 2개로 묶었을 때 각각의 묶음 안에서 주사위 눈이 서로 동일할 때, 주사위 눈 5개의 총합. 최대 30점.
Small Straight : 이어지는 주사위 눈이 4개 이상일 때. 고정 15점.
Large Straight : 이어지는 주사위 눈이 5개일 때. 고정 30점.
Yacht : 동일한 주사위 눈이 5개일 때. 고정 50점.

                 """)
        print("Enter to Continue..")
        input(">> ")
            
    
    def Cycle():
        for i in range(0,2):
            while PlayerAction.scored == False:
                Scoreboard.PrintScore()
                if Dice.rollChances == 3:
                    Dice.FirstRoll()
                    Checker.End()
                    Checker.All()
                else:
                    Dice.Reroll()
                    Checker.End()
                    Checker.All()
                    
                Dice.PrintDiceInterface()
                PlayerAction.UserInput()
            Scoreboard.PrintScore()
            Dice.PrintDiceInterface()
            PlayerAction.EndTurn()
            print("Press Enter to continue...")
            input(">> ")
            PlayerAction.scored = False
            
    def CompareScore():
        Scoreboard.PrintScore()
        if Database.total1 > Database.total2:
            print("")
            print("")
            print("""
  ____  _                         _  __        ___       
 |  _ \| | __ _ _   _  ___ _ __  / | \ \      / (_)_ __  
 | |_) | |/ _` | | | |/ _ \ '__| | |  \ \ /\ / /| | '_ \ 
 |  __/| | (_| | |_| |  __/ |    | |   \ V  V / | | | | |
 |_|   |_|\__,_|\__, |\___|_|    |_|    \_/\_/  |_|_| |_|
                |___/                                         
                  """)
        elif Database.total1< Database.total2:
            print("""
  ____  _                         ____   __        ___       
 |  _ \| | __ _ _   _  ___ _ __  |___ \  \ \      / (_)_ __  
 | |_) | |/ _` | | | |/ _ \ '__|   __) |  \ \ /\ / /| | '_ \ 
 |  __/| | (_| | |_| |  __/ |     / __/    \ V  V / | | | | |
 |_|   |_|\__,_|\__, |\___|_|    |_____|    \_/\_/  |_|_| |_|
                |___/                                                       
                  """)
        else:
            print("""
  ____                           
 |  _ \ _ __ __ ___      __      
 | | | | '__/ _` \ \ /\ / /      
 | |_| | | | (_| |\ V  V / _ _ _ 
 |____/|_|  \__,_| \_/\_(_|_|_|_)
                                                   
                  """)


        
        

while isGameplay == True:
    Init.Start()
    Database.Init()
    for i in range(0, 12):
        Main.Cycle()
    Main.CompareScore()
    print("| Replay : r | | Exit : Anithing |")
    rePlay = input(">> ")
    if rePlay == "R":
        continue
    else:
        break