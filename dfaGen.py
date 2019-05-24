
coordinates = {"U": [ 0, 1],
               "D": [ 0,-1],
               "L": [-1, 0],
               "R": [ 1, 0]}

opposites = {"U": "D",
             "D": "U",
             "L": "R",
             "R": "L"}

rightTurn = {"U": "R",
             "D": "L",
             "L": "U",
             "R": "D"}

# Untreated states represented by their 1234 encoding
untreatedStates = {"": 0}
# TreatedStates also represented by 1234 encoding
treatedStates = {}
# Transfers (or transitions) represented as (startState, input) : newState
transfers = {}
# States that have been previously considered
seenStates = {}

dfa = [] # might be same as transfers, also might need to be 2d

currentUntreatedState = 0
newState = 0

def statesGen(k):
    if(k % 2 == 1):
        k -= 1
    # While untreatedStates is not empty
    while(untreatedStates):
        # Choose a state from untreatedStates
        stateTuple = untreatedStates.popitem()
        stateStr = stateTuple[0]
        stateNum = stateTuple[1]

        buildAugWalks(stateStr, k)

        if(stateStr not in treatedStates.values()):
            treatedStates[stateNum] = stateStr

        
def buildAugWalks(stateStr, k):
    global currentUntreatedState
    global newState

    while(True):
        augmentedWalks = [stateStr + "2", stateStr + "3"]
        # 4 can only come after a 3
        if(stateStr[-1:] == "3"):
            augmentedWalks.append(stateStr + "4")
        # Handle the empty walk state (only test starting with '1')
        if(stateStr == ""):
            augmentedWalks = ["1"]
        for augWalk in augmentedWalks:
            tempStateStr = stateStr
            while(len(augWalk) > 0):
                aWTransfer = augWalk
                tempSTransfer = tempStateStr
                # addCheck checks if a walk of length k - len(state) from state can cause a loop
                if(addCheck(augWalk, k - len(augWalk))):
                    if(augWalk not in untreatedStates and augWalk not in seenStates):
                        # "If t is a state we have not seen so far, put it in the set of untreated states"
                        currentUntreatedState += 1
                        untreatedStates[augWalk] = currentUntreatedState
                        seenStates[augWalk] = currentUntreatedState
                    # "In any case, keep track of the transfer from [state] to [augWalk] in the set of transfers" 
                    # [startState, input] : endState
                    # [state, input] : augWalk
                    # tempStateStr
                    if(tempSTransfer + "#" + aWTransfer[-1:] not in transfers):
                        # '#' acts as delimiter so that the state string and next move can be separate, but still 
                        # hashable for dict lookup (good ol' Python...)
                        transfers[tempSTransfer + "#" + aWTransfer[-1:]] = [newState, seenStates.get(aWTransfer)]
                        seenStates[aWTransfer] = newState
                        newState += 1
                    else:
                        break
                else:
                    augULDR = translateToUDLR(augWalk)
                    augULDR = augULDR[1:]
                    augWalk = translateTo1234(augULDR)

                    tempStateStrULDR = translateToUDLR(tempStateStr)
                    tempStateStrULDR = tempStateStrULDR[1:]
                    tempStateStr = translateTo1234(tempStateStrULDR)
        return

    
# Add moves to current walk to see if a loop can be created in length k or less
def addCheck(string, k):
    # First, translate to absolute steps (UDLR)
    stringUDLR = translateToUDLR(string)
    # Get a list of all grid positions that this walk has visited
    positions = getCoords(stringUDLR)
    # Initialize current position as the last position in the list
    currentPosition = positions[-1]
    # Initial addition is empty
    addition = ""
    return addCheckHelper(stringUDLR, positions, currentPosition, k, addition)


# WORKS
# Things it handles:
#   Does not allow backtracking of any kind. Will only consider next steps that are NOT 
#   opposite the last step
# Recursive helper for addCheck
def addCheckHelper(string, positions, currentPosition, k, addition):
    # We've run out of moves
    if(k < 0):
        return False
    if(addition):
        # Add next step to current position
        string += addition
        currentPosition[0] += coordinates[addition][0]
        currentPosition[1] += coordinates[addition][1]
        # Have we been to this position before (did this move create a loop)?
        if(currentPosition in positions):
            return True
        positions.append(currentPosition)
    # DFS
    # Need to disallow doubling back
    check1 = False
    check2 = False
    check3 = False
    check4 = False
    if(string[-1:] != "D"):
        check1 = addCheckHelper(string, positions.copy(), currentPosition.copy(), k - 1, "U")
    if(string[-1:] != "U"):
        check2 = addCheckHelper(string, positions.copy(), currentPosition.copy(), k - 1, "D")
    if(string[-1:] != "R"):
        check3 = addCheckHelper(string, positions.copy(), currentPosition.copy(), k - 1, "L")
    if(string[-1:] != "L"):
        check4 = addCheckHelper(string, positions.copy(), currentPosition.copy(), k - 1, "R")
    return check1 or check2 or check3 or check4

# WORKING
# Translate walk (string) into a set of coordinates
def getCoords(string):
    currentCoord = [0,0]
    coords = [[0,0]]
    for c in string:
        currentCoord[0] += coordinates[c][0]
        currentCoord[1] += coordinates[c][1]
        coords.append(currentCoord.copy())
    return coords

# WORKING
def translateTo1234(string):
    if(string == "" or string == "0"):
        return ""
    newString = ""
    newString += "1"
    i = 1
    while i < len(string):
        if(string[i] == string[i-1]):
            newString += "2"
        elif(string[i] == opposites[string[i-1]]):
            newString += "1"
        else:
            if(i >= 2):
                if(string[i-2] == string[i] or (string[i - 2] != opposites[string[i]])):
                    newString += "3"
                else:
                    newString += "4"
            else:
                newString += "3"
        i += 1
    return newString

# WORKING
def translateToUDLR(string):
    if(string == ""):
        return ""
    if(string == "2"):
        return "R"
    newString = ""
    i = 0
    while i < len(string):
        if(string[i] == "1"):
            if(i == 0):
                newString += "R"
            else:
                newString += opposites[newString[i-1]]
        elif(string[i] == "2"):
            newString += newString[i-1]
        elif(string[i] == "3"):
            if(i >= 2):
                if(string[i-1] == "2"):
                    newString += rightTurn[newString[i-1]]
                else:
                    newString += newString[i-2]
            else:
                # if(i == 0):
                #     newString[0] = 2
                newString += rightTurn[newString[i-1]]
        elif(string[i] == "4"):
            newString += opposites[newString[i-2]]
        i += 1
    return newString

def dfaGen():
    transferKeys = [*transfers.keys()]
    transferValues = [*transfers.values()]

    dfa = [['-1' for x in range(0, 4)] for x in range(0, len(treatedStates))]

    for state in treatedStates:
        if(transferKeys):
            key = transferKeys.pop(0)
            value = transferValues.pop(0)
            statePlusStep = key.split("#")
            # stateStr = statePlusStep[0]
            transSymbol = statePlusStep[1]
            nextState = value[1]
            # Start in state 'state,' go to state 'nextState' on input symbol 'transSymbol'
            # for i in range(1, 4):
            # THE MINUS 1 IS IMPORTANT
            dfa[state][int(transSymbol) - 1] = nextState
    return dfa

def outputResults(k):
    transferKeys = [*transfers.keys()]
    treatedValues = [*treatedStates.values()]
    print("")
    print("Number of walks that can be extended into a loop with " + str(k) + " total moves or less: ", len(treatedStates))
    choice = input("Press [Enter] to save the list of walks to file, or enter a 1 to output the list to the console:")
    if(choice == '1'):
        print("")
        print("Walks that can be extended into a loop with " + str(k) + " total moves or less:")
        for walk in treatedValues:
            print(walk)
    else:
        outputFile = open("k" + str(k) + "_walks.txt", 'w')
        outputFile.write("Number of walks that can be extended into a loop with " + str(k) + " total moves or less: " + str(len(treatedStates)) + "\n")
        outputFile.write("\n")
        outputFile.write("Walks that can be extended into a loop with " + str(k) + " total moves or less:\n")
        for walk in treatedValues:
            outputFile.write(walk)
            outputFile.write("\n")
        outputFile.close()

        print("Data successfully written to k" + str(k) + "_walks.txt")

gettingInput = True
n = 0
while gettingInput:
    try:
        n = int(input("Enter a value for k (1 - 16): "))
    except:
        print("Invalid input")
    else:
        if n <= 0 or n > 20:
            print("Invalid input")
        else:
            if(n % 2 == 1):
                n -= 1
            statesGen(n)
            # dfa = dfaGen()
            outputResults(n)
            gettingInput = False