# SKIA
# STFE
# RIAL
# TOHO

from search import *
from searchers import *
import os



BOARD = ["skia",
         "stfe",
         "rial",
         "toho"]

Solutions.board = BOARD.copy()

# print(BOARD[1][2])

import time
start = time.time()

for i in range(4):
    for ie in range(4):
        tile = Searcher([i,ie], [], "")
        tile.destory()

OUT = os.path.join("solutions.txt")

with open(OUT, "w") as f:
    f.write("")

decoded = {}
values = []
for solution in Solutions.solutions:
    temp = ""
    for coord in solution:
        temp += BOARD[coord[0]][coord[1]]
    decoded[convert(temp, len(temp))] = temp
    values.append(convert(temp, len(temp)))

values.sort()

entered = []
with open(OUT, "a") as f:
    for value in values:
        if not(decoded[value] in entered):
            f.write(decoded[value] + "\n")
            entered.append(decoded[value])

end = time.time()
print(end-start)