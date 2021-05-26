"""
Negations handled here, The result is stored
In an array with negated_ preceded for further
Usage, to use we retrieve all the words with 
negated__ before them and find their polarity
"""
import csv
def negate_sequence(text):
    negation = False
    delims = "?.,!:;"
    result = []
    words = text.split()
    prev = None
    pprev = None
    for word in words:
        stripped = word.strip(delims).lower()
        negated = "negated_" + stripped if negation else stripped
        result.append(negated)
        if prev:
            bigram = prev + " " + negated
            result.append(bigram)
            if pprev:
                trigram = pprev + " " + bigram
                result.append(bigram)
            pprev = prev
        prev = negated

        if any(neg in word for neg in ["not", "n't", "no"]):
            negation = not negation

        if any(c in word for c in delims):
            negation = False

    return result

def new_nega(text):

    negation = False
    delims = "?.,!:;"
    result = []
    words = text.split()
    prev = None
    negatives = ["not", "n't", "no"]

    for word in words:
        stripped = word.strip(delims).lower()
        negated = "negated_" + stripped if negation else stripped
        result.append(negated)

        if prev:
            bigram = prev + " " + negated
            result.append(bigram)
        #print(negated)
            prev = negated

        if any(neg in word for neg in negatives):
            negation = not negation

        if any(c in word for c in delims):
            negation = False

    return result
   

sen = "I like the new interface, it is not friendly and irritating"
#print(new_nega(sen))
#sen = "He seems not rich and happy, He iscompletely not alive, this is awfully arward"
#print('Sentence: {}\n'.format(sen))
print(negate_sequence(sen))
