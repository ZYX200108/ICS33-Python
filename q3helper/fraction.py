from goody import irange
from goody import type_as_str

import math

class Fraction:
    # Call as Fraction._gcd(...); no self parameter
    # Helper method computes the Greatest Common Divisor of x and y
    @staticmethod
    def _gcd(x : int, y : int) -> int:
        assert x >= 0 and y >= 0, 'Fraction._gcd: x('+str(x)+') and y('+str(y)+') must be >= 0'
        while y != 0:
            x, y = y, x % y
        return x

    # Returns a string that is the decimal representation of a Fraction, with
    #   decimal_places digits appearing after the decimal points.
    # For example: if x = Fraction(23,8), then x(5) returns '2.87500'
    def __call__(self, decimal_places):
        answer = ''
        num = self.num
        denom = self.denom
    
        # handle negative values
        if num < 0:
            num, answer = -num, '-'
        # handle integer part
        if num >= denom:
            answer += str(num//denom)
            num     = num - num//denom*denom
        # handle decimal part: 
        answer += '.'+f'{num*10**decimal_places//denom:0>{decimal_places}}'
        return answer
    
    @staticmethod
    # Call as Fraction._validate_arithmetic(..); with no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), lt (left type) and rt (right type)
    # An example call (from my __add__ method), which checks whether the type of
    #   right is a Fraction or int is...
    # Fraction._validate_arithmetic(right, {Fraction,int},'+','Fraction',type_as_str(right))
    def _validate_arithmetic(v, t : set, op : str, lt : str, rt : str):
        if type(v) not in t:
            raise TypeError('unsupported operand type(s) for '+op+
                            ': \''+lt+'\' and \''+rt+'\'')        

    @staticmethod
    # Call as Fraction._validate_relational(..); with no self parameter
    # Helper method raises exception with appropriate message if type(v) is not
    #   in the set of types t; the message includes the values of the strings
    #   op (operator), and rt (right type)
    def _validate_relational(v, t : set, op : str, rt : str):
        if type(v) not in t:
            raise TypeError('unorderable types: '+
                            'Fraction() '+op+' '+rt+'()')        


    def __init__(self,num=0,denom=1):
        try:
            if (type(num) == float) or (type(denom) == float):
                raise TypeError
            #self.num = int(num)
            #self.denom = int(denom)
            if denom == 0:
                raise TypeError
            if denom < 0:
                denom = -denom
                num = -num
            if num == 0:
                self.denom = 1
                self.num = 0
            else:
                commonDivisor = Fraction._gcd(abs(num), abs(denom))
                self.num = int(num // commonDivisor)
                self.denom = int(denom // commonDivisor)
        except TypeError:
            raise AssertionError
        

    def __repr__(self):
        return 'Fraction({},{})'.format(self.num, self.denom)
    
    def __str__(self):
        self.__repr__()
        return '{}/{}'.format(self.num, self.denom)
   

    def __bool__(self):
        if self.num / self.denom == 0:
            return False
        else:
            return True
    

    def __getitem__(self,i):
        tempvalue = False
        if i == 1:
            return self.denom
        elif i == 0:
            return self.num
        if 'numerator'.find(i) != -1:
            return self.num
        elif 'denominator'.find(i) != -1:
            return self.denom
        raise TypeError
    
 
    def __pos__(self):
        return '{}/{}'.format(self.num , self.denom)
    
    def __neg__(self):
        return '{}/{}'.format(-self.num , self.denom)
    
    def __abs__(self):
        return '{}/{}'.format(abs(self.num), abs(self.denom))
    

    def __add__(self,right):
        #print(type(right))
        tempNum2 = self.num
        tempDenom2 = self.denom
        Fraction._validate_arithmetic(right, {Fraction,int},'+','Fraction',type_as_str(right))
        if type(right) is int:
            x = Fraction(right)
            tempNum, tempDenom = x.num, x.denom
            #print(tempNum, tempDenom)
        else:
            tempNum, tempDenom = right.num, right.denom
        tempNum *= tempDenom2
        tempDenom2 *= tempDenom
        tempNum2 *= tempDenom
        tempNum2 += tempNum
        # commonDivisor = self._gcd(abs(self.num), abs(self.denom))
        # self.num = int(self.num / commonDivisor)
        # self.denom = int(self.denom / commonDivisor)
        return Fraction(tempNum2, tempDenom2)
        

    def __radd__(self,left):
        tempNum2 = self.num
        tempDenom2 = self.denom
        Fraction._validate_arithmetic(left, {Fraction,int},'+',type_as_str(left),'Fraction')
        if type(left) is int:
            x = Fraction(left)
            tempNum, tempDenom = x.num, x.denom
        else:
            tempNum, tempDenom = left.num, left.denom
        tempNum *= tempDenom2
        tempDenom2 *= tempDenom
        tempNum2 *= tempDenom
        tempNum2 += tempNum
        return Fraction(tempNum2, tempDenom2)


    def __sub__(self,right):
        tempNum1 = self.num
        tempDenom1 = self.denom
        Fraction._validate_arithmetic(right, {Fraction,int},'-','Fraction',type_as_str(right))
        if type(right) is int:
            x = Fraction(right)
            tempNum2, tempDenom2 = x.num, x.denom
        else:
            tempNum2, tempDenom2 = right.num, right.denom
        tempNum1 *= tempDenom2
        tempDenom2 *= tempDenom1
        tempNum2 *= tempDenom1
        tempNum1 -= tempNum2
        return Fraction(tempNum1, tempDenom2)
     
    def __rsub__(self,left):
        tempNum1 = self.num
        tempDenom1 = self.denom
        Fraction._validate_arithmetic(left, {Fraction,int},'-',type_as_str(left), 'Fraction')
        if type(left) is int:
            x = Fraction(left)
            tempNum2, tempDenom2 = x.num, x.denom
        else:
            tempNum2, tempDenom2 = left.num, left.denom
        tempNum1 *= tempDenom2
        tempDenom1 *= tempDenom2
        tempNum2 *= tempDenom1
        tempNum2 -= tempNum1
        return Fraction(tempNum2, tempDenom1)

     
    def __mul__(self,right):
        Fraction._validate_arithmetic(right, {Fraction,int},'*','Fraction',type_as_str(right))
        if type(right) is int:
            return Fraction(self.num * right, self.denom)
        else:
            return Fraction(self.num * right.num, self.denom * right.denom)

    def __rmul__(self,left):
        Fraction._validate_arithmetic(left, {Fraction,int},'*',type_as_str(left), 'Fraction')
        if type(left) is int:
            return Fraction(self.num * left, self.denom)
        else:
            return Fraction(self.num * left.num, self.denom * left.denom)

    
    def __truediv__(self,right):
        Fraction._validate_arithmetic(right, {Fraction,int},'/','Fraction',type_as_str(right))
        if type(right) is int:
            return Fraction(self.num, self.denom * right)
        else:
            return Fraction(self.num * right.denom, self.denom * right.num)

    def __rtruediv__(self,left):
        Fraction._validate_arithmetic(left, {Fraction,int},'/',type_as_str(left), 'Fraction')
        if type(left) is int:
            return Fraction(left * self.denom, self.num)
        else:
            return Fraction(left.num * self.denom, left.denom * self.num)


    def __pow__(self,right):
        Fraction._validate_arithmetic(right, {int},'**','Fraction',type_as_str(right))
        if right < 0:
            return Fraction(self.denom ** -right, self.num ** -right)
        else:
            return Fraction(self.num ** right, self.denom ** right)


    def __eq__(self,right):
        Fraction._validate_arithmetic(right, {Fraction,int},'==','Fraction',type_as_str(right))
        tempNum1 = self.num
        tempDenom1 = self.denom
        if type(right) is int:
            x = Fraction(right)
            tempNum2, tempDenom2 = x.num, x.denom
        else:
            tempNum2, tempDenom2 = right.num, right.denom
        if tempNum1 * tempDenom2 == tempDenom1 * tempNum2:
            return True
        else:
            return False
    

    def __lt__(self,right):
        Fraction._validate_arithmetic(right, {Fraction,int},'<','Fraction',type_as_str(right))
        tempNum1 = self.num
        tempDenom1 = self.denom
        if type(right) is int:
            x = Fraction(right)
            tempNum2, tempDenom2 = x.num, x.denom
        else:
            tempNum2, tempDenom2 = right.num, right.denom
        if tempNum1 * tempDenom2 < tempDenom1 * tempNum2:
            return True
        else:
            return False

    
    def __gt__(self,right):
        Fraction._validate_arithmetic(right, {Fraction,int},'<','Fraction',type_as_str(right))
        tempNum1 = self.num
        tempDenom1 = self.denom
        if type(right) is int:
            x = Fraction(right)
            tempNum2, tempDenom2 = x.num, x.denom
        else:
            tempNum2, tempDenom2 = right.num, right.denom
        if tempNum1 * tempDenom2 > tempDenom1 * tempNum2:
            return True
        else:
            return False

    # Uncomment this method when you are ready to write/test it
    # If this is pass, then no attributes will be set!
    def __setattr__(self,name,value):
        if name not in self.__dict__:
            self.__dict__[name] = value
        else:
            raise NameError
 


##############################


# Newton: pi = 6*arcsin(1/2); see the arcsin series at http://mathforum.org/library/drmath/view/54137.html
# Check your results at http://www.geom.uiuc.edu/~huberty/math5337/groupe/digits.html
#   also see http://www.numberworld.org/misc_runs/pi-5t/details.html
def compute_pi(n):
    def prod(r):
        answer = 1
        for i in r:
            answer *= i
        return answer
    
    answer = Fraction(1,2)
    x      = Fraction(1,2)
    for i in irange(1,n):
        big    = 2*i+1
        answer += Fraction(prod(range(1,big,2)),prod(range(2,big,2)))*x**big/big       
    return 6*answer





if __name__ == '__main__':
    # Put in simple tests for Fraction before allowing driver to run
 
    print()
    import driver
    
    driver.default_file_name = 'bscq31F21.txt'
#     driver.default_show_traceback= True
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
    driver.driver()
