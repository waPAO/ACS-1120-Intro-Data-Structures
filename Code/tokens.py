import re 

def tokenize(corpus):
    final_text = remove_punctuation(remove_actions(remove_names(corpus)))
    final_text = final_text.lower()
    final_text = text_to_list(final_text)
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

def text_to_list(corpus):
    split_text = re.split('\s+', corpus)
    if '' in split_text:
        split_text.remove('')
    return split_text

if __name__=='__main__':
    pass