from functools import reduce

def singleCombine(element1,element2):
    return element1 +'\n' + element2 +'\n'


def allCombine(element1,element2):
    #return element1  + '\n' + '-.-.'*10 + '\n' + '-.-.'*10 + '\n\n' + element2
    return element1  + '\n' + r'=.=.'*8 + '\n\n' + element2

def mapCombine(element1):
    return reduce(singleCombine,element1)


def sendText(stor_list):
    single_str_list = list(map(mapCombine,stor_list))
    all_str_list    = reduce(allCombine,single_str_list)
    return all_str_list


