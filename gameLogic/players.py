players = []

#Add player object to array with name provided (rest of the entries are boilerplate for later code)
def addPlayer(name):
    players.append([name, 0, []])

#Returns number of players in player array
def getPlayerCount():
    return len(players)

#Return player at index
def getPlayer(index):
    return players[index]