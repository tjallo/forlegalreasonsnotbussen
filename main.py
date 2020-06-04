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


startGame()