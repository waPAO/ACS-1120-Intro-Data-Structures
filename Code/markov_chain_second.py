from dictogram import Dictogram
from random import randint, choice
from read import read
from tokens import tokenize

def build_chain(words: list):
    markov_chain = {}
    for i in range(len(words)-2):
        current_word = words[i]
        next_word = words[i + 1]
        third_word = words[i + 2]
        k = (current_word, next_word)
        if k in markov_chain:
            markov_chain[k].add_count(third_word)
        else:
            markov_chain[k] = Dictogram([third_word])
    return markov_chain

def walk_chain(mk_chain):
    max_words = randint(8, 20)
    rand_words = []
    mk_keys = [key for key in mk]
    rand_key = choice(mk_keys)
    while len(rand_words) < max_words:
        word = mk_chain[rand_key].sample()
        rand_words.append(word)
        rand_key = (rand_key[1], word)

    for i in range(len(rand_words)):
        if rand_words[i] == 'i':
            rand_words[i] = 'I'
        elif rand_words[i] == "i'd":
            rand_words[i] = "I'd"
        elif rand_words[i] == "i'm":
            rand_words[i] = "I'm"
        elif rand_words[i] == "i've":
            rand_words[i] = "I've"

    sentence = ' '.join(rand_words)
    return sentence

if __name__=='__main__':
    text = read('regular_show.txt')
    parsed_text = tokenize(text)
    mk = build_chain(parsed_text)
    sentence = walk_chain(mk)
    print(sentence)
    







