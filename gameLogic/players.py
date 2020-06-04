players = []

def addPlayer(name):
    players.append([name, 0, []])

def getPlayerCount():
    return len(players)

def getPlayer(index):
    return players[index]