import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable = False,  defaults =  {}):
    def show_listing(s):
        for ln_number, text_of_ln in enumerate(s.split('\n'),1):       
            print(f' {ln_number: >3} {text_of_ln.rstrip()}')

    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    def Unique(lis):
        lis_return = []
        for i in lis:
            if i not in lis_return:
                lis_return.append(i)
        return lis_return
    
    pattern_use = '^[a-zA-Z]([1-9]|[a-zA-Z]|_)*$'
    if re.match(pattern_use, str(type_name)):
        if type_name in keyword.kwlist:
            raise SyntaxError
    else:
        raise SyntaxError
    if type(field_names) == list:
        for i in field_names:
            if re.match(pattern_use, i):
                if i in keyword.kwlist:
                    raise SyntaxError
            else:
                raise SyntaxError
    elif type(field_names) == str:
        lis = field_names.split(' ')
        field_names = []
        for i in lis[:]:
            if i != '':
                if ',' in i:
                    field_names.append(i.strip(','))
                else:
                    field_names.append(i)
        lis_temp = []
        for i in field_names:
            lis_temp += i.split(',')
        field_names = lis_temp
        for i in field_names:
            if re.match(pattern_use, i):
                if i in keyword.kwlist:
                    raise SyntaxError
            else:
                raise SyntaxError
    else:
        raise SyntaxError
    
    field_names = Unique(field_names)
    
    if len(defaults) != 0:
        for i in defaults:
            if i not in field_names:
                raise SyntaxError
    
    class_temp = '''\
class {type_name}:
    _fields = {field_names}
    _mutable = {mutable}
        
    def __init__(self, {value}):
        {item}    
    def __repr__(self):
        return f'{type_name}({context})'
        
    {get_functions}    
    def __getitem__(self, index):
        if type(index) == int:
            if index == 0:
                {index_is_0}
                
            {int_need}
            else:
                raise IndexError
        elif type(index) == str:
            if index in self.__dict__:
                return self.__dict__[index]
            else:
                raise IndexError
        else:
            raise IndexError
    
    def __eq__(self, right):
        if type(self) != type(right):
            return False
        else:
            for i in {field_names}:
                if self[i] != right[i]:
                    return False
            else:
                return True
    
    def _asdict(self):
        return self.__dict__.copy()
     
    def _make(iter):
        return {type_name}(*iter)
    
    def _replace(self,**kargs):
        for k, v in kargs.items():
            if k not in self.__dict__:
                raise TypeError
        if self._mutable:
            for k, v in kargs.items():
                self.__dict__[k] = v
        else:
            newDict = self.__dict__.copy()
            for k, v in kargs.items():
                newDict[k] = v
            list1 = [v for v in newDict.values()]
            return {type_name}._make(list1)
    '''
    class_definition = class_temp.format(type_name=type_name, field_names=field_names, mutable=mutable, value = ', '.join(str(i) + '=' + str(defaults[i]) if i in defaults else str(i) for i in field_names), 
                                         item = '        '.join(['self.' + str(i) + ' = '  + str(i) + '\n' for i in field_names]),
                                         context=','.join(str(i) + '=' + '{self.' + i + '}' for i in field_names),
                                         get_functions = '\n    '.join('def get_' + i + '(self):\n        return self.' + i + '\n' for i in field_names),
                                         index_is_0 = 'return self.get_' + field_names[0] + '()',
                                         int_need = '\n            '.join('elif index == ' + str(i) + ':\n                return self.get_' + field_names[i] + '()\n' for i in range(1, len(field_names)))
                                         ).strip()

    # Debugging aid: uncomment show_listing below so it always displays source code
    # show_listing(class_definition)
    
    # Execute class_definition's str from name_space; followed by binding the
    #   attribute source_code to the class_definition; after the try/except bloc
    #   return this created class object; if any syntax errors occur, show the
    #   listing of the class and trace the error, in the except clause
    name_space = dict( __name__ = f'pnamedtuple_{type_name}' )                
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except (TypeError,SyntaxError):                    
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    # Test simple pnamedtuple below in script: Point=pnamedtuple('Point','x,y')
    Triple1    = pnamedtuple('Triple1', 'a b c')
    #driver tests
    import driver  
    driver.default_file_name = 'bscp3F21.txt'
#     driver.default_show_exception_message = True
#     driver.default_show_traceback = True
    driver.driver()
