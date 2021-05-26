import json, re,collections, requests
import nltk
from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer

from nltk.sentiment.util import mark_negation
from collections import Counter
#from backport_collections import counter

#from sklearn.feature_extraction.text import CountVectorizer


def downl_file(url, saving_file):
    cont = requests.get(url, allow_redirects=True)
    open(saving_file, 'wb').write(cont.content)


class PreProcess:
    # this handles Preproccng
    processed_doc = []
    def __init__(self, document):

        stop_words = json.load(open('stp_words.json', 'r'))
        #document  = open(document, 'r').readlines()
        

        #for sentence in document:
        sentence = document.lower()
        tokenized_sentence  = sentence.split()
        stop_w_removed = [token for token in tokenized_sentence if token not in stop_words]
        for clean in stop_w_removed:
            if clean[0] !='@':

                stripped = (c for c in clean if 0 < ord(c) < 127)
                self.processed_doc.append(''.join(stripped))
            


class FileProcessing:
    
    content = []
    def __init__(self, document):
        pass
        

class LanguageProcessing:
    
    #www.wewsdsds.
    #re =r'www.\[Aa-Zz-0-9].\[Aa-Zz-0-9]'


    def tokens(text):
        return re.findall('[a-z]+', text.lower())

    file = open('dictionary.txt')
    kalmomi  = tokens(file.read())
    adadin_kalma = Counter(kalmomi)

    def nisa0(self, kalma):
        return {kalma}

    def nisa1(self, kalma):

        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        def splits(kalma):
            return [(kalma[:i], kalma[i:]) for i in range(len(kalma)+1)]

        # TODO need to check this indentation
        pairs = splits(kalma)
        deletes = [a+b[1:] for (a, b) in pairs if b]
        transposes = [a+b[1]+b[0]+b[2:] for (a,b) in pairs if len(b)>1]
        replaces = [a+c+b[1:] for (a, b) in pairs for c in alphabets if b]
        insertion = [a+c+b for (a,b) in pairs for c in alphabets]
        return set(deletes+transposes+replaces+insertion)

    def nisa2(self, kalma):
        return {e2 for e1 in self.nisa1(kalma) for e2 in self.nisa1(e1)}

    def known(self, words):
        return {w for w in words if w in self.adadin_kalma}

    
    def correct_spelling(self, word):
        # 1. Priority meaning
        print(self.known(self.nisa2(word)))

    def pos_tagging(self, word):
        sets_of_words = wn.synsets(word) 
        #wor=sets_of_words[0]
        for wor in sets_of_words:
            print('{}: {}'.format(word, wor.pos()))
            
    def stemming(self, word):
        st = PorterStemmer()
        return st.stem(word)
    def remove_repeated(self, word):
        #re to identify repeated first
        # check if a valid english if not remove
        repeat_pattern = re.compile(r'(\w*)(\w)\2(\w*)') # it has aa, bb, addaa e.g baaaaad
        match_sub = r'\1\2\3' 
        
        while True:
            if wn.synsets(word): #good sleep
                return word
            new_word =  repeat_pattern.sub(match_sub, word)
            if new_word !=word:
                word = new_word
                continue
            else:
                return new_word

