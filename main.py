#import dependencies
import random

#import local libraries
import gameLogic.cards as cards
import gameLogic.players as players
import gameLogic.gameEvents as gE

#Logic that adds all players to the game
def startGame():
    try:
        nPlayers = int(input("How many players: "))
    except:
        print("Enter a number")

    for i in range(nPlayers):
        print(f"Name of player {i+1}")
        playerName = input()
        players.addPlayer(playerName)

    print()
    print("The following players are playing:")
    for i in range(players.getPlayerCount()):
        print(players.getPlayer(i)[0])
#First rouund of round 1, red or black
def redBlack(player):
    choice = input(f"{players.getPlayer(player)[0]}, Rood (1) of Zwart (2): ")
    card = cards.getCard()
    if (card[0] == 1) or (card[0] == 2):
        if int(choice) == 2:
            return True, card
    if (card[0] == 0) or (card[0] == 3):
        if int(choice) == 1:
            return True, card
    return False, card

#Second round of round 1, higher or lower then the previous card
def highLow(player):
    currentcard = players.getCardArray(player)[0]
    card = cards.getCard()
    playerName = players.getPlayer(player)[0]
    print(f"{playerName} heeft op het moment de kaart: {cards.cardParser(currentcard[0], currentcard[1])}") 
    choice = int(input("Hoger (1) of lager (2): "))
    if choice == 1:
        if card[1] > currentcard[1]:
            return False, card
    elif choice == 2:
        if card[1] < currentcard[1]:
            return False, card
    return True, card

#Decides if card is inner or outer    
def innerOuter(player):
    currentcards = players.getCardArray(player)
    tempcurrent1 = currentcards[0][1]
    tempcurrent2 = currentcards[1][1]
    if tempcurrent1 > tempcurrent2:
        lowest = tempcurrent2
        highest = tempcurrent1
    else:
        lowest = tempcurrent1
        highest = tempcurrent2
    card = cards.getCard()
    playerName = players.getPlayer(player)[0]   
    players.printCurrendPlayerCards(player)
    choice = int(input("Binnen (1) of buiten (2)"))

    if choice == 1:
        if lowest < card[1] and highest > card[1]:
            return False, card
    if choice == 2:
        if lowest > card[1] and highest < card[1]:
            return False, card
    return True, card


#Add cards, add drinks, to player object, logic works for round 1
def adjustScoreRound1(player, card, drinkBool):
    if drinkBool == True:
        players.addDrink(1, player)
        print(f"-> Fout! Je kaart was: {cards.cardParser(card[0], card[1])}, drink 1 slok")
    else:
        print(f"-> Goed! Je kaart was: {cards.cardParser(card[0], card[1])}")             
    players.addCard(card, player)
    playerinfo = players.getPlayer(player)
    players.printCurrendPlayerCards(player)
    print('--------------------------------\n')

#Calls all the logic to play  out round 1 (colour, high/low, in/outer, has (not) suit)
def roundOne():
    for i in range(players.getPlayerCount()):
        hasToDrink, card = redBlack(i)
        adjustScoreRound1(i, card, hasToDrink)
    
    for i in range(players.getPlayerCount()):
        hasToDrink, card = highLow(i)
        adjustScoreRound1(i, card, hasToDrink)

    for i in range(players.getPlayerCount()):
        hasToDrink, card = innerOuter(i)
        adjustScoreRound1(i, card, hasToDrink)


players.addPlayer("Henk")
players.addPlayer("Klaas")
players.addPlayer("Jan")

roundOne()
