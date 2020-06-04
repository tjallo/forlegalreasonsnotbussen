import random

cards = [[0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13], [0, 14], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13], [1, 14], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [2, 12], [2, 13], [2, 14], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13], [3, 14]]

playedCards = []

def getCard():
    card = random.choice(cards)
    index = cards.index(card)
    cards.pop(index)
    playedCards.append(card)
    return card

def getLeftCards():
    return cards

def getPlayedCards():
    return playedCards

def cardParser(suitValue, cardValue):
    suit = ""
    card = ""
    if cardValue == 11:
        suit = "Jack"
    elif cardValue == 12:
        suit = "Queen"
    elif cardValue == 13:
        suit = "King"
    elif cardValue == 14:
        suit = "Ace"
    else:
        suit = str(cardValue)  
    

    if suitValue == 0:
        card = "Spades"
    elif suitValue == 1:  
        card = "Hearts"  
    elif suitValue == 2:
        card = "Diamonds"
    elif suitValue == 3:     
        card = "Clubs"   
    
    cardname = f"{suit} of {card}"

    return cardname