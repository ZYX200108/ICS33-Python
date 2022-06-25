from goody import type_as_str
from math import sqrt

class Interval:
    pass

   


    
if __name__ == '__main__':
    g = Interval.mid_err(9.8,.05)
    print(repr(g))
    g = Interval.min_max(9.75,9.85)
    print(repr(g))
    d = Interval.mid_err(100,1)
    t = (d/(2*g)).sqrt()
    print(t,repr(t),t.relative_error())    

    import driver    
    driver.default_file_name = 'bscp22F21.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
