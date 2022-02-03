import math
import random

itembag = []
tokenList = ["white1", "white2", "white3", "orange1", "blue1", "blue2", "blue4", "red1", "red2", "red4", "yellow1",
             "yellow2", "yellow4", "moth1", "green1", "green2", "green4", "pink1"]
tokenValues = {"white1": 1, "white2": 2, "white3": 3, "orange1": 1, "blue1": 1, "blue2": 2, "blue4": 4, "red1": 1,
               "red2": 2, "red4": 4, "yellow1": 1, "yellow2": 2, "yellow4": 4, "moth1": 1, "green1": 1, "green2": 2,
               "green4": 4, "pink1": 1}
set1TokenCosts = {"orange1": 3, "blue1": 5, "blue2": 10, "blue4": 19, "red1": 6, "red2": 10, "red4": 16, "yellow1": 8,
                  "yellow2": 12, "yellow4": 18, "moth1": 10, "green1": 4, "green2": 8, "green4": 14, "pink1": 9}
set2TokenCosts = {"orange1": 3, "blue1": 5, "blue2": 10, "blue4": 19, "red1": 4, "red2": 8, "red4": 14, "yellow1": 9,
                  "yellow2": 13, "yellow4": 19, "moth1": 10, "green1": 6, "green2": 11, "green4": 18, "pink1": 12}
set3TokenCosts = {"orange1": 3, "blue1": 4, "blue2": 8, "blue4": 14, "red1": 5, "red2": 9, "red4": 15, "yellow1": 8,
                  "yellow2": 12, "yellow4": 18, "moth1": 10, "green1": 6, "green2": 11, "green4": 21, "pink1": 10}
set4TokenCosts = {"orange1": 3, "blue1": 5, "blue2": 10, "blue4": 19, "red1": 7, "red2": 11, "red4": 17, "yellow1": 8,
                  "yellow2": 12, "yellow4": 18, "moth1": 10, "green1": 4, "green2": 8, "green4": 14, "pink1": 11}
tileMoney = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13, 14: 14, 15: 15,
             16: 15, 17: 16, 18: 16, 19: 17, 20: 17, 21: 18, 22: 18, 23: 19, 24: 19, 25: 20, 26: 20, 27: 21, 28: 21,
             29: 22, 30: 22, 31: 23, 32: 23, 33: 24, 34: 24, 35: 25, 36: 25, 37: 26, 38: 26, 39: 27, 40: 27, 41: 28,
             42: 28, 43: 29, 44: 29, 45: 30, 46: 30, 47: 31, 48: 31, 49: 32, 50: 32, 51: 33, 52: 33, 53: 35}
tilePoints = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 1, 8: 1, 9: 1, 10: 2, 11: 2, 12: 2, 13: 2, 14: 3, 15: 3,
              16: 3, 17: 3, 18: 4, 19: 4, 20: 4, 21: 4, 22: 5, 23: 5, 24: 5, 25: 5, 26: 6, 27: 6, 28: 6, 29: 7, 30: 7,
              31: 7, 32: 8, 33: 8, 34: 8, 35: 9, 36: 9, 37: 9, 38: 10, 39: 10, 40: 10, 41: 11, 42: 11, 43: 11, 44: 12,
              45: 12, 46: 12, 47: 12, 48: 13, 49: 13, 50: 13, 51: 14, 52: 14, 53: 15}
tileRubies = {0: False, 1: False, 2: False, 3: False, 4: False, 5: True, 6: False, 7: False, 8: False, 9: True,
              10: False, 11: False, 12: False, 13: True, 14: False, 15: False, 16: True, 17: False, 18: False,
              19: False, 20: True, 21: False, 22: False, 23: False, 24: True, 25: False, 26: False, 27: False, 28: True,
              29: False, 30: True, 31: False, 32: False, 33: False, 34: True, 35: False, 36: True, 37: False, 38: False,
              39: False, 40: True, 41: False, 42: True, 43: False, 44: False, 45: False, 46: True, 47: False, 48: False,
              49: False, 50: True, 51: False, 52: True, 53: False}
cauldron = []
tokenCost = set1TokenCosts
turnCount = 1
pointTotal = 0
ratTails = 0
dropletCount = 0
money = 0
points = 0
rubies = 1
finalSquare = 0
deathPoint = 8
whiteCount = 0
cauldronExploded = False
numPlayers = 0
setChosen = 0


def reset_itembag():
    itembag.append(tokenList[0])
    itembag.append(tokenList[0])
    itembag.append(tokenList[0])
    itembag.append(tokenList[0])
    itembag.append(tokenList[1])
    itembag.append(tokenList[1])
    itembag.append(tokenList[2])
    itembag.append(tokenList[3])
    itembag.append(tokenList[14])


def print_itembag():
    print("Your bag contains the following tokens : ", itembag)


def buy_token():
    global money
    print("Here are the prices of available tokens : ", tokenCost)
    tokens_purchased = 0
    while money > 0 and tokens_purchased < 2:
        new_purchase = input("Would you like to purchase a token? (Y/N) : ").lower()
        if new_purchase == "n":
            break
        while new_purchase == "y":
            print("You have ", money, "money.")
            token_requested = input("Please enter the name of the token you wish to purchase : ")
            if token_requested not in tokenList:
                print("Token not found! Please try again")
                continue
            else:
                if money >= tokenCost[token_requested]:
                    itembag.append(token_requested)
                    print("Success! You have purchased one ", token_requested, " token.")
                    new_purchase = "n"
                    tokens_purchased += 1
                    money -= tokenCost[token_requested]
                else:
                    print("The selected token is too expensive! Try something cheaper")
                    continue
    print("Token purchasing over!")


def end_turn():
    global cauldron
    global cauldronExploded
    global whiteCount
    global money
    global rubies
    global points
    global finalSquare
    for i in cauldron:
        itembag.append(i)
    cauldron = []
    cauldronExploded = False
    whiteCount = 0
    money = 0
    rubies = False
    points = 0
    finalSquare = 0


def print_cauldron():
    print("Your Cauldron currently contains the following tokens : ", cauldron)


def explode_cauldron():
    global cauldronExploded
    print("Unlucky! Your Cauldron Exploded :( ")
    cauldronExploded = True


def draw_token():
    global whiteCount
    randint = random.randint(0, len(itembag) - 1)
    token_drawn = itembag[randint]
    cauldron.append(token_drawn)
    itembag.remove(token_drawn)
    if token_drawn[0] == "w":
        whiteCount += tokenValues[token_drawn]


def play_turn():
    global whiteCount
    global deathPoint
    while whiteCount < deathPoint:
        response = input("Would you like to draw a token from your bag? (Y/N)").lower()
        if response[0] == "y":
            draw_token()
        elif response[0] == "n":
            break
        else:
            print("Please respond Y or N")
            continue
        print_cauldron()
    else:
        explode_cauldron()


def give_points():
    global cauldronExploded
    global pointTotal
    global points
    global money
    global rubies
    determine_tile_bonuses()
    if not cauldronExploded:
        if turnCount < 9:
            pointTotal += points
        else:
            pointTotal += points
            pointTotal += math.floor(money / 5)
            pointTotal += math.floor(rubies / 2)
    else:
        while True:
            response2 = input("Your Cauldron has exploded. You must choose between Money and Points! (M/P)").lower()
            if response2[0] == "m":
                buy_token()
                break
            elif response2[0] == "p":
                pointTotal += points
                break
            else:
                print("Please respond M or P")
                continue


def determine_tile_bonuses():
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
    if rubies:
        print("You finished on tile :", finalSquare, ". This means you have ", money, "money to spend and gained ",
              points, " points! You also get a Ruby!")
    elif not rubies:
        print("You finished on tile :", finalSquare, ". This means you have ", money, "money to spend and gained ",
              points, " points!")


def choose_set():
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
    print("You have chosen to play with set ", setChosen)


def black_bonus():
    global numPlayers
    global rubies
    global dropletCount
    if numPlayers == "2":
        num_blacks = input(
            "To represent having more, less or an equal amount of black tokens as the other player, Enter >, = or < : ")
        if num_blacks == ">":
            dropletCount += 1
            rubies += 1
        elif num_blacks == "=":
            dropletCount += 1
    elif numPlayers == "3" or numPlayers == "4":
        num_blacks = input("Enter the number of players that you have more black tokens than : ")
        if num_blacks == "2":
            rubies += 1
            dropletCount += 1
        elif num_blacks == "1":
            dropletCount += 1


def pink_bonus():
    global setChosen
    global dropletCount
    global pointTotal
    global rubies
    num_pinks = 0
    for i in cauldron:
        if i == "pink1":
            num_pinks += 1
    print("You have ", num_pinks, " pink tokens in your cauldron")
    if num_pinks > 0:
        if setChosen == "1":
            if num_pinks == 1:
                pointTotal += 1
            elif num_pinks == 2:
                pointTotal += 1
                rubies += 1
            elif num_pinks > 2:
                pointTotal += 2
                dropletCount += 1
        elif setChosen == "2":
            print(
                "You may swap the pink tokens in your cauldron according to the following rules : \n "
                "[1 pink token : 1 black token, 1 point and 1 ruby] \n "
                "[2 pink tokens : 1 green1 token, 1 blue2 token, 3 points and a droplet increase] \n "
                "[3 pink tokens : 1 yellow4 token, 6 points, a ruby and a double droplet increase]")
            while True:
                swap_pinks = input("If you would like to swap any pink tokens, enter the quantity here : ")
                if swap_pinks == "0":
                    break
                elif swap_pinks == "1":
                    cauldron.remove("pink1")
                    itembag.append("moth1")
                    pointTotal += 1
                    rubies += 1
                    break
                elif swap_pinks == "2":
                    cauldron.remove("pink1")
                    cauldron.remove("pink1")
                    itembag.append("green1")
                    itembag.append("blue2")
                    pointTotal += 3
                    dropletCount += 1
                    break
                elif swap_pinks == "3":
                    cauldron.remove("pink1")
                    cauldron.remove("pink1")
                    cauldron.remove("pink1")
                    itembag.append("yellow4")
                    pointTotal += 6
                    rubies += 1
                    dropletCount += 2
                    break
                else:
                    print("Your request was not valid, please enter a number between 0 and 3")
                    continue
        elif setChosen == "3":
            for i in cauldron:
                if i == "pink1":
                    index = cauldron["pink1"]
        elif setChosen == "4":
            panic()


def green_bonus():
    if setChosen == "1":
        dostuff = 0


def execute_bonuses():
    black_bonus()
    green_bonus()
    pink_bonus()


def play_game():
    global turnCount
    reset_itembag()
    choose_set()
    while turnCount < 10:
        print("This is turn ", turnCount)
        print_itembag()
        play_turn()
        give_points()
        end_turn()
        turnCount += 1
    else:
        print("Game Over. Your final score was : ", pointTotal)


play_game()
