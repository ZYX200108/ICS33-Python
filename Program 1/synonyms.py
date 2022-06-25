import re                               # used in my sentence_at_a_time generator function
import math                             # use in cosine_meteric
import prompt                           # for use in script
import goody                            # for use in script
from collections import defaultdict     #  dicts and defaultdicts are == when they have the same keys/associations


# For use in build_semantic_dictionary: see problem specifications
def sentence_at_a_time(open_file : open, ignore_words : {str}) -> [str]:
    end_punct    = re.compile('[.?\!;:]')
    remove_punct = re.compile(r'(,|\'|"|\*|\(|\)|--)')

    prev   = []
    answer = []
    for l in open_file:
        l = remove_punct.sub(' ',l.lower())
        prev = prev + l.split()
        while prev:
            w = prev.pop(0)
            if end_punct.search(w):
                while end_punct.search(w):
                    w = w[0:-1]
                if w != '' and w not in ignore_words:
                    if end_punct.search(w):
                        print(w)
                    answer.append(w)
                    yield answer
                    answer = []
            else:
                if w != '' and w not in ignore_words:
                    answer.append(w)
                    
    # handle special case of last sentence missing final punctuation                
    if answer:
        yield answer


def build_semantic_dictionary(training_files: [open], ignore_file: open) -> {str: {str: int}}:
    ignore_set = {l.strip() for l in list(ignore_file)}
    lis_original = []
    lis = []
    dic = {}
    for i in training_files:
        answer = sentence_at_a_time(i, ignore_set)
        sub_lis = [i for i in answer]
        lis_original += sub_lis
    for i in lis_original:
        j = set(i)
        if len(j) > 1:
            lis.append(i)
    for i in lis:
        for j in i:
            if j not in dic:
                sub_lis = {}
                for x in lis:
                    if j in x:
                        num = x.count(j)
                        for y in x:
                            if y == j:
                                continue
                            else:
                                if y not in sub_lis:
                                    sub_lis[y] = 1*num
                                else:
                                    sub_lis[y] += 1*num
                    else:
                        continue
                dic[j] = sub_lis
    return dic
            
            
    


def dict_as_str(semantic: {str: {str: int}}) -> str:
    context = ''
    value = [len(semantic[i]) for i in semantic]
    for i in sorted(semantic):
        sub_context = ''
        count = 1
        for j in sorted(semantic[i]):
            if count != len(semantic[i]):
                sub_context += '{}@{}, '.format(j, semantic[i][j])
                count += 1
            else:
                sub_context += '{}@{}'.format(j, semantic[i][j])
        context += '  context for ' + i + ' = ' + sub_context + '\n'
    max_num = max(value)
    min_num = min(value)
    context += '  min/max context lengths = {}/{}\n'.format(min_num, max_num)
    return context

       
def cosine_metric(context1 : {str:int}, context2 : {str:int}) -> float:
    part_up = 0
    for i in context1:
        if i not in context2:
            part_up += 0
        else:
            part_up += context1[i] * context2[i]
    part_down_context1 = 0
    for j in context1:
        part_down_context1 += context1[j]**2
    part_down_context2 = 0
    for k in context2:
        part_down_context2 += context2[k]**2
    part_down = math.sqrt(part_down_context1)*math.sqrt(part_down_context2)
    answer = part_up / part_down
    return answer


def most_similar(word : str, choices : [str], semantic : {str:{str:int}}, metric : callable) -> str:
    winner = ''
    winner_score = 0
    for i in choices:
        if i not in semantic:
            raise ZeroDivisionError
        else:
            score = metric(semantic[word], semantic[i])
            if score > winner_score:
                winner = i
                winner_score = score
    return winner


def similarity_test(test_file : open, semantic : {str:{str:int}}, metric : callable) -> str:
    lis = [l.strip() for l in list(test_file)]
    problems = [i.split(' ') for i in lis]
    count_num = len(problems)
    count_correct = 0
    answer = ''
    for i in problems:
        choice = i[1:len(i)-1]
        question = i[0]
        answer_given = i[-1]
        try:
            answer_get = most_similar(question, choice, semantic, metric)
            if answer_get == answer_given:
                count_correct += 1
                answer += '  Correct: \'{}\' is most like \'{}\' from {}\n'.format(question, answer_get, choice)
            else:
                answer += '  Incorrect: \'{}\' is most like \'{}\', not \'{}\' from {}\n'.format(question, answer_given, answer_get, choice)
        except ZeroDivisionError:
            answer += '  Metric failure: could not choose synonym for \'{}\' from {}\n'.format(question, choice)
    answer += '{}% correct\n'.format((count_correct / count_num)*100)
    return answer
        
        





# Script

if __name__ == '__main__':
    # Write script here
    open_files = []
    while True:
        try:
            file = input('Supply the name of a text file for training (or type done)[done]: ') or 'no-more'
            if file == 'done':
                break
            elif file == 'no-more':
                continue
            else:
                open_files.append(open(file))
        except FileNotFoundError:
            print('  file named archie_comics.txt rejected: cannot be opened')
    print()
    dic = build_semantic_dictionary(open_files, open('ignore_words.txt'))
    answer = input('Display (True/False) Semantic Dictionary?[False]: ') or 'False'
    if answer == 'True':
        print(dict_as_str(dic))
    print()
    value = True
    while value:
        try:
            file_name = open(input('Supply the name of a problem file[synonym_problems.txt]: ') or 'synonym_problems.txt')
            value = False
        except FileNotFoundError:
            print('  file named archie_comics.txt rejected: cannot be opened')
    answer = similarity_test(file_name, dic, cosine_metric)
    print(answer)

    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
