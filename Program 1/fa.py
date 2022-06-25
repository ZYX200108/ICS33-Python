# Submitter: haodoz4(Zhang, Haodong)
# Partner  : yuxuez2(Zhou, Yuxue)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody


def read_fa(file : open) -> {str:{str:str}}:
    content = list(file)
    finalDict = {}
    for c in content:
        c.strip()
        tempList = c.split(';')
        x = tempList[0]
        tempList.pop(0)
        tempDict = {}
        for m in range(0, len(tempList), 2):
            tempDict[tempList[m]] = tempList[m + 1].strip()
        finalDict[x] = tempDict
    return finalDict


def fa_as_str(fa : {str:{str:str}}) -> str:
    finalList = []
    finalStr = ''
    for start, move in fa.items():
        list1 = [(x, y) for x, y in move.items()]
        finalList.append('  {} transitions: {}\n'.format(start, sorted(list1, key=lambda x: x[0])))
    finalList.sort()
    for words in finalList:
        finalStr += words
    return finalStr

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    finalList = [state]
    for moves in inputs:
        try:
            state = fa[state][moves]
            finalList.append((moves, state))
        except KeyError:
            finalList.append((moves, None))
            break
    return finalList
    
    
def interpret(fa_result : [None]) -> str:
    finalStr = ''
    finalStr += 'Start state = {}\n'.format(fa_result[0])
    fa_result.pop(0)
    for tuples in fa_result:
        if not tuples[0].isdigit():
            finalStr += '  Input = {}; illegal input: simulation terminated\n'.format(tuples[0])
            finalStr += 'Stop state = None\n'
            return finalStr
        finalStr += '  Input = {}; new state = {}\n'.format(tuples[0], tuples[1])
    finalStr += 'Stop state = {}\n'.format(fa_result[-1][1])
    return finalStr


if __name__ == '__main__':
    # Write script here
    # userInput = input('Supply the file name describing the Finite Automaton: ')
    # print('\nFinite Automaton Display: state (str): list of transitions ([(str,str)])')
    # print(fa_as_str(read_fa(open(userInput))))
    # userInput2 = input('Supply the file name whose lines are a start-state and its inputs: ')
    # print('\nTrace of FA: from its start state')
    # for lines in list(open(userInput2)):
    #     # print(lines)
    #     startMove = lines.strip().split(';')[0]
    #     # print(startMove)
    #     moves = lines.strip().split(';')[1:]
    #     # print(moves)
    #     print(interpret(process(read_fa(open(userInput)), startMove, moves)))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
