from collections import defaultdict
from goody import type_as_str

# Iterators are covered in Week #4
# Implement all methods but iterators after Week #3

class Bag:
    def __init__(self, iterate1 = []):
        tempdict = {}
        for values in iterate1:
            if values not in tempdict:
                tempdict[values] = 1
            else:
                tempdict[values] += 1
        self.dict = tempdict
    
    
    def __repr__(self):
        tempList = []
        for key, values in self.dict.items():
            while values > 0:
                tempList.append(key)
                values -= 1
        if len(tempList) == 0:
            return 'Bag()'
        else:
            tempTuple = (tempList)
            return 'Bag{}'.format(tempTuple)
    
    
    def __str__(self):
        tempList = []
        for key, values in self.dict.items():
            tempList.append('{}[{}]'.format(key, values))
        return 'Bag{}'.format(tuple(tempList))
    
    
    def __len__(self):
        tempValue = 0
        for values in self.dict.values():
            tempValue += values
        return tempValue
    
    
    def unique(self):
        return len(self.dict)
    
    
    def __contains__(self, arg1):
        if arg1 in self.dict.keys():
            return True
        else:
            return False
        
    
    def count(self, arg1):
        if arg1 in self.dict.keys():
            return self.dict[arg1]
        else:
            return 0
    
    
    def add(self, arg1):
        if arg1 in self.dict.keys():
            self.dict[arg1] += 1
        else:
            self.dict[arg1] = 1
    
    
    def __add__(self, right):
        if type(right) != Bag:
            raise TypeError
        tempList = []
        for key, value in self.dict.items():
            while value > 0:
                tempList.append(key)
                value -= 1
        for key, value in right.dict.items():
            while value > 0:
                tempList.append(key)
                value -= 1
        return Bag(tempList)
    
    def remove(self, arg1):
        if arg1 in self.dict.keys():
            self.dict[arg1] -= 1
            if self.dict[arg1] == 0:
                self.dict.pop(arg1)
        else:
            raise ValueError
    
    
    def __eq__(self, right):
        if type(right) != Bag:
            return False
        boolValue = True
        for key, value in right.dict.items():
            if not ((key in self.dict) and (right.dict[key] == self.dict[key])):
                boolValue = False
        return boolValue
    
    
    def __ne__(self, right):
        if type(right) != Bag:
            return True
        boolValue = True
        for key, value in right.dict.items():
            if not ((key in self.dict) and (right.dict[key] == self.dict[key])):
                boolValue = False
        if boolValue:
            return False
        else:
            return True
    
    class iterableObject:
        def __init__(self, dict2):
            self.max = sum(dict2.values())
            self.min = 0
            tempList = []
            for key, value in dict2.items():
                while value > 0:
                    tempList.append(key)
                    value -= 1
            self.list = tempList
            
        def __iter__(self):
            return self
            
        
        def __next__(self):
            if self.min < self.max:
                x = self.list[self.min]
                self.min += 1
                return x
            else:
                raise StopIteration
    
    
    def __iter__(self):
        return Bag.iterableObject(self.dict)
                

if __name__ == '__main__':
    #Put your own test code here to test Bag before doing bsc tests

    print('Start simple testing')

    import driver
    driver.default_file_name = 'bscp21F21.txt'
#     driver.default_show_exception =True
#     driver.default_show_exception_message =True
#     driver.default_show_traceback =True
    driver.driver()
