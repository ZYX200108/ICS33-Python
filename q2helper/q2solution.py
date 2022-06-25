import re
from goody import irange
from collections import defaultdict

# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the files repattern1a.txt, repattern1b.txt, and
#   repattern2a.txt. The patterns must be all on the first line

def pages (page_spec : str, unique :  bool) -> [int]: #result in ascending order
    
    pageSpec = page_spec.strip().split(',')
    pattern = r'^([1-9][0-9]*)(?:(?:(-|:)([1-9][0-9]*))(?:(?:/)([1-9][0-9]*))?)?$'
    finalList =[]
    if unique:
        for specs in pageSpec:
            m = re.match(pattern, specs)
            assert m != None, 'No match'
            firstNum, Sign, secondNum, thirdNum = [i if i != None else None for i in m.group(1,2,3,4)]
            if firstNum != None:
                firstNum = int(firstNum)
            if secondNum != None:
                secondNum = int(secondNum)
            if thirdNum != None:
                thirdNum = int(thirdNum)
            tempSet = set()
            if thirdNum == None:
                if Sign == None:
                    tempSet.add(firstNum)
                elif Sign == '-':
                    if secondNum < firstNum:
                        raise AssertionError
                    while firstNum <= secondNum:
                        tempSet.add(firstNum)
                        firstNum += 1
                elif Sign == ':':
                    tempValue = 0
                    while tempValue <= secondNum:
                        tempSet.add(tempValue + firstNum)
                        tempValue += 1
            else:
                if Sign == None:
                    tempSet.add(firstNum)
                elif Sign == '-':
                    if secondNum < firstNum:
                        raise AssertionError
                    while firstNum <= secondNum:
                        tempSet.add(firstNum)
                        firstNum += thirdNum
                elif Sign == ':':
                    tempValue = 0
                    while tempValue <= secondNum:
                        tempSet.add(tempValue + firstNum)
                        tempValue += thirdNum
            finalList += list(tempSet)
        finalSet = set(finalList)
        return sorted(list(finalSet))
    else:
        for specs in pageSpec:
            m = re.match(pattern, specs)
            assert m != None, 'No match'
            firstNum, Sign, secondNum, thirdNum = [i if i != None else None for i in m.group(1,2,3,4)]
            if firstNum != None:
                firstNum = int(firstNum)
            if secondNum != None:
                secondNum = int(secondNum)
            if thirdNum != None:
                thirdNum = int(thirdNum)
            tempList = []
            if thirdNum == None:
                if Sign == None:
                    tempList.append(firstNum)
                elif Sign == '-':
                    while firstNum <= secondNum:
                        tempList.append(firstNum)
                        firstNum += 1
                elif Sign == ':':
                    tempValue = 0
                    while tempValue < secondNum:
                        tempList.append(tempValue + firstNum)
                        tempValue += 1
            else:
                if Sign == None:
                    tempList.append(firstNum)
                elif Sign == '-':
                    while firstNum <= secondNum:
                        tempList.append(firstNum)
                        firstNum += thirdNum
                elif Sign == ':':
                    tempValue = 0
                    while tempValue < secondNum:
                        tempList.append(tempValue + firstNum)
                        tempValue += thirdNum
            finalList += tempList
        return sorted(finalList)
            

def expand_re(pat_dict:{str:str}):
    for key in pat_dict:
        for pattern in pat_dict:
            if key in pat_dict[pattern] and key != pattern:
                pat_dict[pattern] = re.sub('#{}#'.format(key), '(?:{})'.format(pat_dict[key]), pat_dict[pattern])





if __name__ == '__main__':
    
    p1a = open('repattern1a.txt').read().rstrip() # Read pattern on first line
    print('Testing the pattern p1a: ',p1a)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1a,text)
        print(' ','Matched' if m != None else "Not matched")
        
    p1b = open('repattern1b.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p1b: ',p1b)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1b,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
        
    p2 = open('repattern2a.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p2: ',p2)
    for text in open('bm2a.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p2,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
    print('\nTesting pages function')
    for text in open('bm2b.txt'):
        text = text.rstrip().split(';')
        text,unique = text[0], text[1]=='True'
        try:
            p = pages(text,unique)
            print('  ','pages('+text+','+str(unique)+') = ',p)
        except:
            print('  ','pages('+text+','+str(unique)+') = raised exception')
        
    
    print('\nTesting expand_re')
    pd = dict(digit = r'[0-9]', integer = r'[+-]?#digit##digit#*')
    print('  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary
    # {'digit': '[0-9]', 'integer': '[+-]?(?:[0-9])(?:[0-9])*'}
    
    pd = dict(integer       = r'[+-]?[0-9]+',
              integer_range = r'#integer#(..#integer#)?',
              integer_list  = r'#integer_range#(,#integer_range#)*',
              integer_set   = r'{#integer_list#?}')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'integer': '[+-]?[0-9]+',
    #  'integer_range': '(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?',
    #  'integer_list': '(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?)(,(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?))*',
    #  'integer_set': '{(?:(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?)(?,(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?))*)?}'
    # }
    
    pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'a': 'correct',
    #  'b': '(?:correct)',
    #  'c': '(?:(?:correct))',
    #  'd': '(?:(?:(?:correct)))',
    #  'e': '(?:(?:(?:(?:correct))))',
    #  'f': '(?:(?:(?:(?:(?:correct)))))',
    #  'g': '(?:(?:(?:(?:(?:(?:correct))))))'
    # }
    
    print()
    print()
    import driver
    driver.default_file_name = "bscq2F21.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
