import math
import random

itembag = []

tokenList = ["white1","white2","white3","orange1","blue1","blue2","blue4","red1","red2","red4","yellow1","yellow2","yellow4","moth1","green1","green2","green4","pink1","pink2","pink4"]

tokenValues = {"white1":1,"white2":2,"white3":3,"orange1":1,"blue1":1,"blue2":2,"blue4":4,"red1":1,"red2":2,"red4":4,"yellow1":1,"yellow2":2,"yellow4":4,"moth1":1,"green1":1,"green2":2,"green4":4,"pink1":1,"pink2":2,"pink4":4}

set1TokenCosts = {"orange1":3,"blue1":5,"blue2":10,"blue4":19,"red1":6,"red2":10,"red4":16,"yellow1":8,"yellow2":12,"yellow4":18,"moth1":10,"green1":4,"green2":08,"green4":14,"pink1":09}
set2TokenCosts = {"orange1":3,"blue1":5,"blue2":10,"blue4":19,"red1":4,"red2":08,"red4":14,"yellow1":9,"yellow2":13,"yellow4":19,"moth1":10,"green1":6,"green2":11,"green4":18,"pink1":12}
set3TokenCosts = {"orange1":3,"blue1":4,"blue2":08,"blue4":14,"red1":5,"red2":09,"red4":15,"yellow1":8,"yellow2":12,"yellow4":18,"moth1":10,"green1":6,"green2":11,"green4":21,"pink1":10}
set4TokenCosts = {"orange1":3,"blue1":5,"blue2":10,"blue4":19,"red1":7,"red2":11,"red4":17,"yellow1":8,"yellow2":12,"yellow4":18,"moth1":10,"green1":4,"green2":08,"green4":14,"pink1":11}

tileMoney = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:11,12:12,13:13,14:14,15:15,16:15,17:16,18:16,19:17,20:17,21:18,22:18,23:19,24:19,25:20,26:20,27:21,28:21,29:22,30:22,31:23,32:23,33:24,34:24,35:25,36:25,37:26,38:2$

tilePoints = {0:0,1:0,2:0,3:0,4:0,5:0,6:1,7:1,8:1,9:1,10:2,11:2,12:2,13:2,14:3,15:3,16:3,17:3,18:4,19:4,20:4,21:4,22:5,23:5,24:5,25:5,26:6,27:6,28:6,29:7,30:7,31:7,32:8,33:8,34:8,35:9,36:9,37:9,38:10,39:10,40:10,41:11,42:11,4$

tileRubies = {0:False,1:False,2:False,3:False,4:False,5:True,6:False,7:False,8:False,9:True,10:False,11:False,12:False,13:True,14:False,15:False,16:True,17:False,18:False,19:False,20:True,21:False,22:False,23:False,24:True,25$

cauldron = []

tokenCost = set1TokenCosts

turnCount = 1

pointTotal = 0

ratTails = 0

dropCount = 0

money = 0

points = 0

rubies = 1

finalSquare = 0

deathPoint = 8

whiteCount = 0

cauldronExploded = False

def resetItembag():
        itembag.append(tokenList[0])
        itembag.append(tokenList[0])
        itembag.append(tokenList[0])
        itembag.append(tokenList[0])
        itembag.append(tokenList[1])
        itembag.append(tokenList[1])
        itembag.append(tokenList[2])
        itembag.append(tokenList[3])
        itembag.append(tokenList[14])

def printItembag():
        print("Your bag contains the following tokens : ", itembag)

def buyToken():
        global money
        print ("Here are the prices of available tokens : ", tokenCost)
        tokensPurchased = 0
        while money > 0 and tokensPurchased < 2:
                newPurchase = input("Would you like to purchase a token? (Y/N) : ").lower()
                if newPurchase == "n":
                        break
                while newPurchase == "y":
                        print ("You have ", money, "money.")
                        tokenRequested = input("Please enter the name of the token you wish to purchase : ")
                        if tokenRequested not in tokenList:
                                print ("Token not found! Please try again")
                                continue
                        else:
                                if money >= tokenCost[tokenRequested]:
                                        itembag.append(tokenRequested)
                                        print ("Success! You have purchased one ", tokenRequested, " token.")
                                        newPurchase = "n"
                                        tokensPurchased += 1
                                        money -= tokenCost[tokenRequested]
                                else:
                                        print("The selected token is too expensive! Try something cheaper")
                                        continue
        print ("Token purchasing over!")

def endTurn():
        global cauldron
        global cauldronExploded
        global whiteCount
        global money
        global rubies
        global points
        for i in cauldron:
                itembag.append(i)
        cauldron = []
        cauldronExploded = False
        whiteCount = 0
        money = 0
        rubies = False
        points = 0
        finalSquare = 0

def printCauldron():
        print("Your Cauldron currently contains the following tokens : ", cauldron)

def explodeCauldron():
        global cauldronExploded
        print("Unlucky! Your Cauldron Exploded :( ")
        cauldronExploded = True

def drawToken():
        global whiteCount
        randint = random.randint(0,len(itembag)-1)
        tokenDrawn = itembag[randint]
        cauldron.append(tokenDrawn)
        itembag.remove(tokenDrawn)
        if tokenDrawn[0] == "w":
                whiteCount += tokenValues[tokenDrawn]

def playTurn():
        global whiteCount
        global deathPoint
        while whiteCount < deathPoint:
                response = input("Would you like to draw a token from your bag? (Y/N)").lower()
                if response[0] == "y":
                        drawToken()
                elif response[0] == "n":
                        break
                        buyToken()
                else:
                        print ("Please respond Y or N")
                        continue
                printCauldron()
        else:
                explodeCauldron()

def givePoints():
        global cauldronExploded
        global pointTotal
        global points
        global money
        global rubies
        determineTileBonuses()
        if cauldronExploded == False:
                if turnCount < 9:
                        pointTotal += points
                else:
                        pointTotal += points
                        pointTotal += math.floor(money/5)
                        pointTotal += math.floor(rubies/2)
        while cauldronExploded == True:
                response2 = input("Since your Cauldron has exploded you must choose between Money and Points! Type M or P.").lower()
                if response2[0] == "m":
                        buyToken()
                        cauldronExploded = False
                elif response2[0] == "p":
                        pointTotal += points
                        cauldronExploded = False
                else:
                        print ("Please respond M or P")
                        continue

def determineTileBonuses():
        global money
        global rubies
        global points
        global tileMoney
        global tilePoints
        global tileRubies
        global cauldron
        global finalSquare
        for i in cauldron:
                finalSquare += tokenValues[i]
        money = tileMoney[finalSquare]
        points = tilePoints[finalSquare]
        rubies = tileRubies[finalSquare]
        if rubies == True:
                print ("You finished on tile :", finalSquare, ". This means you have ", money, "money to spend and gained ", points, " points! You also get a Ruby!")
        elif rubies == False:
                print ("You finished on tile :", finalSquare, ". This means you have ", money, "money to spend and gained ", points, " points!")

def chooseSet():
        global tokenCost
        global numPlayers
        global setChosen
        numPlayers = input("Please enter how many players you are playing with : ")
        setChosen = input("Please enter which set you would like to play : set")
        if setChosen == "1":
                tokenCost = set1TokenCosts
        elif setChosen == "2":
                tokenCost = set2TokenCosts
        elif setChosen == "3":
                tokenCost = set3TokenCosts
        elif setChosen == "4":
                tokenCost = set4TokenCosts
        print ("You have chosen to play with set ", setChosen)

def blacksBonus():
        global numPlayers
        if numPlayers == "2":
                blacksBonus = input("To represent having more, less or an equal amount of black tokens as the other player, Enter >, = or < : ")
                if blacksBonus == ">":
                        dropletCount += 1
                        rubies += 1
                elif blacksBonus == "=":
                        dropletCount += 1
        elif numPlayers == "3" or numPlayers == "4":
                blacksBonus = input("Enter the number of players that you have more black tokens than : ")
                if response6 == "2":
                        rubies += 1
                        dropletCount += 1
                elif response6 == "1":
                        dropletCount += 1

def pinkBonus():
        global setChosen
        global pinkTotal
        pinkTotal = 0
        for i in cauldron:
                if i == "pink1":
                        pinkTotal += 1
        if setChosen == "1":
                if pinkTotal == 1:
                        pointTotal += 1
                elif pinkTotal == 2:
                        pointTotal += 1
                        rubies += 1
                elif pinkTotal > 2:
                        pointTotal += 2
                        dropletTotal += 1
        elif setChosen == "2":
                if pinkTotal == 1:
                        itembag += "black1"

def exeuteBonuse():
        blackBonus()
        pinkBonus()
        greenBonus()

def playGame():
        global turnCount
        resetItembag()
        chooseSet()
        while turnCount < 10:
                print ("This is turn ", turnCount)
                printItembag()
                playTurn()
                givePoints()
                endTurn()
                turnCount += 1
        else:
                print ("Game Over. Your final score was : ", pointTotal)

playGame()



