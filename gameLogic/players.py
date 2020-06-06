#Initsialise Empty array to carry playerdatas
players = []

#Add player object to array with name provided (rest of the entries are boilerplate for later code) [name, drinks, cards]
def addPlayer(name):
    players.append([name, 0, []])

#Returns number of players in player array
def getPlayerCount():
    return len(players)

#Return player at index
def getPlayer(playerIndex):
    return players[playerIndex]

#Adds one drink to playerindex, returns new count
def addDrink(n, playerIndex):
    players[playerIndex][1] += n
    return players[playerIndex][1]

def addCard(card, playerIndex):
    players[2].append(card)