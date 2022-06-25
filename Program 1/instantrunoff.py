# Submitter: haodoz4(Zhang, Haodong)
# Partner  : yuxuez2(Zhou, Yuxue)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody


def read_voter_preferences(file : open):
    contents = [l.strip() for l in list(file)]
    lis = [i.split(';') for i in contents]
    dic = {j[0]: [j[k] for k in range(1, len(j))] for j in lis}
    return dic


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    dic_items = sorted(d, key=key, reverse=reverse)
    string_return = ''
    for i in dic_items:
        string_return += '  {} -> {}\n'.format(i, d[i])
    return string_return


def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    dic = {}
    for i in cie:
        num = 0
        for j in vp:
            for k in vp[j]:
                if k not in cie:
                    continue
                else:
                    if k == i:
                        num +=1
                    break
        dic[i] = num
    return dic


def remaining_candidates(vd : {str:int}) -> {str}:
    vd_min = min(vd.items(), key=(lambda x: (x[1])))
    return {i[0] for i in vd.items() if vd_min[1] not in i}


def run_election(vp_file : open) -> {str}:
    dic = read_voter_preferences(vp_file)
    cie = set(list(dic.values())[0])
    print('Preferences Display: voter (str) -> candidate choices decreasing ([str])')
    print(dict_as_str(dic))
    print()
    truthvalue = True
    num = 1
    while truthvalue:
        print('Vote count sorted by candidate on ballot #{}: shows only candidates still in election'.format(num))
        dic_num = evaluate_ballot(dic, cie)
        print(dict_as_str(dic_num))
        print('Vote count sorted by candidate on ballot #{}: shows only candidates still in election'.format(num))
        print(dict_as_str(dic_num, lambda x: dic_num[x], reverse=True))
        winner = remaining_candidates(dic_num)
        if len(winner) == 0 or len(winner) == 1:
            truthvalue = False
        else:
            num += 1
            cie = winner
    print('Winner singleton set: {}'.format(winner))
    return winner
        

        
       
if __name__ == '__main__':
    # Write script here
    file = open(input('Supply the file name describing all voter preferences: '))
    print()
    run_election(file)
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
