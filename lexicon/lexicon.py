"""
Reformat the MPQA lexicon into an easier-to-parse format.
"""


# For doing cool regular expressions
import re

#sunan lexicon file da mukayi creating
f = open('lexicon.csv', 'w')

# Read in the lexicon. Here's an example line:
#
# type=weaksubj len=1 word1=abandoned pos1=adj stemmed1=n priorpolarity=negative
#
# For now, just use a regular expression to grab the word and the priorpolarity parts.
with open('subjclueslen1-HLTEMNLP05.tff', 'rt') as file:
    for line in file.readlines():
        #print(line)
        #create regular exp da zai yi searching
        m = re.search('.*word1=(\S+).*priorpolarity=(\S+)', line)

        #assign score to 
        score = 0
        if m.group(2) == 'positive':
            score = 1
        elif m.group(2) == 'negative':
            score = -1
        f.write("%s,%d\n" % (m.group(1), score))

f.close()
        