# Submitter: haodoz4(Zhang, Haodong)
# Partner  : yuxuez2(Zhou, Yuxue)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    dictionary1 = {}
    for l in [l.strip() for l in list(file)]:
        dictionary1[l.split(';')[0]] = {l.split(';')[1]} if l.split(';')[0] not in dictionary1 else set.union({i for i in dictionary1[l.split(';')[0]]}, {l.split(';')[1]})
    return dictionary1


def graph_as_str(graph : {str:{str}}) -> str:
    str_return = ''
    for i in sorted(list(graph.items())):
        str_return += '  {} -> {}\n'.format(i[0], sorted(list(i[1])))
    return str_return


def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:
    #if start not in graph.keys():
        #return 'Entry Error: \'{}\';  Illegal: not a source node Please enter a legal String'.format(start)
    #else:
    reached_set = set()
    trace = False
    exploring_list = [start]
    while not trace:
        for i in exploring_list[:]:
            reached_set.add(i)
            exploring_list.pop(0)
            if i in graph.keys():
                get_value = graph.get(i)
                for j in get_value:
                    if j not in reached_set:
                        exploring_list.append(j)
            trace = True if len(exploring_list) == 0 else False        
    return reached_set
        
        


if __name__ == '__main__':
    # Write script here
    file = open(input('Supply the file name describing the graph: '))
    print('\nGraph Display: source node (str) -> destination nodes sorted ([str])')
    dic = read_graph(file)
    print(graph_as_str(dic))
    while True:
        start_node = input('Supply a starting node (or type done): ')
        if start_node == 'done':
            break
        else:
            if start_node not in dic.keys():
                print('  Entry Error: \'{}\';  Illegal: not a source node\n  Please enter a legal String\n'.format(start_node))
                continue
            else:
                trace = input('Supply algorithm tracing option[True]: ')
                print('From the supplied starting node a the set of reachable nodes: {}'.format(reachable(dic, start_node, trace)))
                print()
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
