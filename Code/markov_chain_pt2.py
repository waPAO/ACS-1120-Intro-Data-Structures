from dictogram import Dictogram

def build(word_list):
    markovchain = {}
    for index in range(len(word_list)-1):
        firstword = word_list[index]
        secondword = word_list[index+1]
        if firstword not in markovchain:
            markovchain[firstword] = Dictogram()
            markovchain[firstword].add_count(secondword)
    print(markovchain)
    return markovchain


