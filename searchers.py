from search import *

def addCoords(coordA, coordB):
    return [coordA[0] + coordB[0], coordA[1] + coordB[1]]

def checkCoord(coord):
    return 0 <= coord[0] and coord[0] <= 3 and 0 <= coord[1] and coord[1] <= 3 


class Solutions:
    board = []
    activeSearchers = 0
    solutions = []

class Searcher:
    DIRECTIONS = [
        (-1,  0),
        (-1,  1),
        ( 0,  1),
        ( 1,  1),
        ( 1,  0),
        ( 1, -1),
        ( 0, -1),
        (-1, -1)
    ]
    def __init__(self, summonedCoords, pathCoords, pathText):
        self.alive = True
        Solutions.activeSearchers += 1
        self.id = Solutions.activeSearchers

        self.path = pathCoords.copy()
        self.path.append(summonedCoords)
        self.pathText = pathText + Solutions.board[summonedCoords[0]][summonedCoords[1]]
        self.prefix = "".join([Solutions.board[pos[0]][pos[1]] for pos in pathCoords])

        if self.pathText in STORAGE:
            Solutions.solutions.append(self.path.copy())
        
        validSteps = []
        for direction in Searcher.DIRECTIONS:
            temp = addCoords(summonedCoords, direction)
            if checkCoord(temp) and not(temp in self.path):
                validSteps.append(temp)
        
        
        # print("Searcher ID: {:07} creating...".format(self.id))
        
        self.children = []
        temp = getRange(pathText)
        validChars = getValidSteps(pathText, temp[0], temp[1])

        if len(validChars) > 0:
            for step in validSteps:
                if Solutions.board[step[0]][step[1]] in validChars:
                    self.children.append(Searcher(step, self.path, self.pathText))
        if len(self.children) == 0:
            # print("Searcher ID: {:07} DEAD END".format(self.id))
            pass
    def destory(self):
        hasChildren = False
        for child in self.children:
            hasChildren = hasChildren or child.alive
            if child.alive:
                child.destory()
        if not(hasChildren):
            self.children = None
            self.alive = False
            Solutions.activeSearchers -= 1



