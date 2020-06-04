#import dependencies
import random

#import local libraries
import gameLogic.cards as cards
import gameLogic.players as players

players.addPlayer("Tjalle")

print(f"playercount: {players.getPlayerCount()}")
print(f"player add index 0: {players.getPlayer(0)}")

#Get 52 cards, and parses them to human readable format en prints it to console
# for i in range(52):
#     card = cards.getCard()
#     parsed = cards.cardParser(card[0], card[1])
#     print(parsed)