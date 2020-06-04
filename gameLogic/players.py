#Initsialise Empty array to carry playerdatas
players = []

#Add player object to array with name provided (rest of the entries are boilerplate for later code) [name, drinks, cards]
def addPlayer(name):
    players.append([name, 0, []])

#Returns number of players in player array
def getPlayerCount():
    return len(players)

#Return player at index
def getPlayer(index):
    return players[index]

#Adds one drink to playerindex, returns new count
def addDrink(n, playerIndex):
    players[playerIndex] += n
    return players[playerIndex]
