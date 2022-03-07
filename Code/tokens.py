import re 

def tokenize(corpus):
    final_text = remove_punctuation(remove_actions(remove_names(corpus)))
    return final_text

def remove_names(corpus):
    no_names = re.sub('.*?\:', '', corpus)
    return no_names

def remove_actions(corpus):
    no_actions = re.sub('\(.*?\)', '', corpus)
    no_actions = re.sub('\*.*?\*', '', no_actions)
    return no_actions

def remove_punctuation(corpus):
    no_punc = re.sub('[^\w\s*\']', '', corpus)
    return no_punc


if __name__=='__main__':
    text = open('tester.txt').read()
    final = tokenize(text)
    print(final)