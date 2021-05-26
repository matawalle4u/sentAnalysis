import PreProcess
import Bagofwordsimproved as bow

from PreProcess import PreProcess as pp

tweet ="nodate3.csv"
lexicons = ['lexicon/mylexicon.csv']
content  = open(tweet, 'r').readlines()

for each_tweet in content:
    process = pp(each_tweet)
    #print(each_tweet)
    #preprocess each tweet
    
    print(each_tweet)
    #if len(process.processed_doc)>80:
    #bow.compare_performance(' '.join(process.processed_doc) , lexicons)
   