import random

import gameLogic.cards as cards
import gameLogic.players as players

players.addPlayer("Tjalle")

for i in range(52):
    card = cards.getCard()
    parsed = cards.cardParser(card[0], card[1])
    print(parsed)