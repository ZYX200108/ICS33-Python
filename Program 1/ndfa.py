# Submitter: haodoz4(Zhang, Haodong)
# Partner  : yuxuez2(Zhou, Yuxue)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody


def read_ndfa(file : open) -> {str:{str:{str}}}:
    content = list(file)
    finalDict = {}
    for c in content:
        c.strip()
        tempList = c.split(';')
        x = tempList[0]
        tempList.pop(0)
        tempDict = {}
        for y in range(0, len(tempList), 2):
            if tempList[y] not in tempDict:
                tempDict[tempList[y]] = {tempList[y + 1].strip()}
            else:
                tempDict[tempList[y]].add(tempList[y + 1].strip())
        finalDict[x] = tempDict
    return finalDict


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    finalList = []
    finalStr = ''
    for start, moves in ndfa.items():
        tempList = []
        for move in moves.items():
            tempList.append((move[0], sorted(list(move[1]))))
            tempList.sort()
        finalList.append('  {} transitions: {}\n'.format(start, tempList))
    finalList.sort()
    for words in finalList:
        finalStr += words
    return finalStr


def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    finalList = [state]
    currentState = [state]
    for moves in inputs:
        tempSet = set() 
        for positions in currentState:
            if moves in ndfa[positions]:
                tempSet.update(ndfa[positions][moves])
                currentState = list(tempSet)
        if len(tempSet) == 0:
            finalList.append((moves, tempSet))
            break
        finalList.append((moves, tempSet))
    return finalList


def interpret(result : [None]) -> str:
    finalStr = ''
    finalStr += 'Start state = {}\n'.format(result[0])
    result.pop(0)
    for tuples in result:
        finalStr += '  Input = {}; new possible states = {}\n'.format(tuples[0], sorted(list(tuples[1])))
    finalStr += 'Stop state(s) = {}\n'.format(sorted(list(result[-1][1])))
    return finalStr


if __name__ == '__main__':
    # Write script here
    userInput = input('Supply the file name describing a Non-Deterministic Finite Automaton: ')
    print('\nNon-Deterministic Finite Automaton Display: state (str): list of transitions ([(str,[str])])')
    print(ndfa_as_str(read_ndfa(open(userInput))))
    userInput2 = input('Supply the file name whose lines are a start-state and its inputs: ')
    print()
    for lines in list(open(userInput2)):
        print('Trace of NDFA: from its start state')
        # print(lines)
        startMove = lines.strip().split(';')[0]
        # print(startMove)
        moves = lines.strip().split(';')[1:]
        # print(moves)
        print(interpret(process(read_ndfa(open(userInput)), startMove, moves)))
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
