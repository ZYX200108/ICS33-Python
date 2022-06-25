# Generators must be able to iterate through any kind of iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v


# The combination of return and yield None make each of the following
#   a generator (yield None) that immediately raises the StopIteration
#   exception (return)

def sequence(*iterables):
    for x in iterables:
        for y in x:
            yield y

            
def group_when(iterable,p):
    tempList = []
    for x in iterable:
        if p(x):
            tempList.append(x)
            y = tempList
            tempList = []            
            yield y
        else:
            tempList.append(x)
    else:
        if len(tempList) != 0:
            yield tempList

                
def drop_last(iterable,n):
    templist= []
    for x in iterable:
        if len(templist) != n:
            templist.append(x)
        else:
            y = templist.pop(0)
            templist.append(x)
            yield y

        
def yield_and_skip(iterable,skip):
    try:
        i = iter(iterable)
        for x in i:
            yield(x)
            num = skip(x)
            while num > 0:
                next(i)
                num -= 1
    except StopIteration:
        pass
 
        
def alternate_all(*args):
    iterList = []
    for x in args:
        iterList.append(iter(x))
    while True:
        b = False
        for x in iterList:
            for y in x:
                b = True
                yield y
                break
        if b == False:
            break



def min_key_order(adict):
    # smallest = None
    # x = 0
    # while True:
    #     secondSmallest = None
    #     for keys, values in adict.items():
    #         if x == 0:
    #             smallest = keys
    #             x += 1
    #         elif secondSmallest == None:
    #             if mallest > keys:
    #                 smallest = keys
    smallestKey = None
    x = 0
    while True:
        b = False
        for k,v in sorted(adict.items()):
            if x == 0:
                smallestKey = k
                x += 1
                b = True
                yield (k,v)
                break
            else:
                if k > smallestKey:
                    smallestKey = k
                    b = True
                    yield (k,v)
                    break
        if b == False:
            break
         
           
         
if __name__ == '__main__':
    from goody import irange
    
    # Test sequence; you can add any of your own test cases
    print('Testing sequence')
    for i in sequence('abc', 'd', 'ef', 'ghi'):
        print(i,end='')
    print('\n')

    print('Testing sequence on hidden')
    for i in sequence(hide('abc'), hide('d'), hide('ef'), hide('ghi')):
        print(i,end='')
    print('\n')


    # Test group_when; you can add any of your own test cases
    print('Testing group_when')
    for i in group_when('combustibles', lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')

    print('Testing group_when on hidden')
    for i in group_when(hide('combustibles'), lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')


    # Test drop_last; you can add any of your own test cases
    print('Testing drop_last')
    for i in drop_last('combustible', 5):
        print(i,end='')
    print('\n')

    print('Testing drop_last on hidden')
    for i in drop_last(hide('combustible'), 5):
        print(i,end='')
    print('\n')


    # Test sequence; you can add any of your own test cases
    print('Testing yield_and_skip')
    for i in yield_and_skip('abbabxcabbcaccabb',lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')

    print('Testing yield_and_skip on hidden')
    for i in yield_and_skip(hide('abbabxcabbcaccabb'),lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')


    # Test alternate_all; you can add any of your own test cases
    print('Testing alternate_all')
    for i in alternate_all('abcde','fg','hijk'):
        print(i,end='')
    print('\n')
    
    print('Testing alternate_all on hidden')
    for i in alternate_all(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print('\n\n')
       
         
    # Test min_key_order; add your own test cases
    print('\nTesting Ordered')
    d = {1:'a', 2:'x', 4:'m', 8:'d', 16:'f'}
    i = min_key_order(d)
    print(next(i))
    print(next(i))
    del d[8]
    print(next(i))
    d[32] = 'z'
    print(next(i))
    print(next(i))
    


         
         
    import driver
    driver.default_file_name = "bscq4F21.txt"
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
