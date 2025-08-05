import os

DATAFILE = os.path.join("wordhuntwords.txt")
with open(DATAFILE, "r") as f:
    STORAGE = f.read().split("\n")

ORDER = " abcdefghijklmnopqrstuvwxyz"
LETTER_VALUES = {}
for i in range(len(ORDER)):
    LETTER_VALUES[ORDER[i]] = i+1

def convert(text, length):
    val = 0
    for i in range(length): val += LETTER_VALUES[text[i] if i < len(text) else " "] * 27**(length-1-i)
    return val

def clamp(minV, val, maxV):
    return max(minV, min(val, maxV))


def getRange(prefix):
    val = convert(prefix, len(prefix))
    
    startRange, endRange = 0, len(STORAGE) - 1
    left, right = startRange, endRange
    res = -1
    while left <= right:
        mid = left + (right - left)//2
        temp = convert(STORAGE[mid][:len(prefix)], len(prefix))
        if temp < val:
            left = mid + 1
        else:
            if temp == val:
                res = mid
            right = mid - 1
    startRange = res
    
    left, right = startRange, endRange
    res = -1
    while left <= right:
        mid = left + (right - left)//2
        temp = convert(STORAGE[mid][:len(prefix)], len(prefix))
        if temp > val:
            right = mid - 1
        else:
            if temp == val:
                res = mid
            left = mid + 1
    endRange = res

    return [startRange, endRange]

def getValidSteps(prefix, start, end):
    valid = set()
    for word in STORAGE[start:end]:
        if len(prefix) + 1 <= len(word):
            valid.add(word[len(prefix)])
    return valid


# # benchmark

# import time
# import random

# total = 0
# tests = 0
# while True:
#     test = [ORDER[random.randint(0, 26)] for x in range(random.randint(1, 3))]
#     start = time.time()
#     bounds = getRange(test)
#     getValidSteps(test, bounds[0], bounds[1])
#     end = time.time()
#     tests += 1
#     total += (end-start)
#     print("avg tests {:10}s out of {:07} tests".format(total/tests, tests))