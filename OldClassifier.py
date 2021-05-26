"""

Perform sentiment analysis using the MPQA lexicon.
Note, in this  approach, haven't  handle negations
or any of the other hard problems.
"""



import csv, re, operator
tweets = []

# this needs to be in Pre Processing class
def strip_non_ascii(string):
    #TODO remove while handling emoticons
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)




# Create tweet structure as below:
#
# id:       The ID of the tweet
# pubdate:  The publication date of the tweet
# orig:     The original, unpreprocessed string of characters
# clean:    The preprocessed string of characters

with open('nodate3.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #'\n'
    
    next(reader)
    for row in reader:

        tweet= dict()
        
        try:

            tweet['orig'] = row[0]
            tweet['id'] = int(row[1])
            
            
                # Ignore retweets
            if re.match(r'^RT.*', tweet['orig']):
                continue

            # we can apply all pre processing that we implemented here on the tweet['clean']
            tweet['clean'] = tweet['orig']
            # Remove all non-ascii characters
            tweet['clean'] = strip_non_ascii(tweet['clean'])
            # Normalize case
            tweet['clean'] = tweet['clean'].lower()
            # Remove the hashtag symbol
            tweet['clean'] = tweet['clean'].replace(r'#', '')

            #saving the cleaned data to the tweets
            tweets.append(tweet)

        except IndexError:
            pass



        

# Create a data structure to hold the lexicon.
# We will use a Python diction. The key of the dictionary will be the word
# and the value will be the word's score.
lexicon = dict()

# Read in the lexicon. 
with open('lexicon/mylexicon.csv', 'rt') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
# Use lexicon to score tweets
for tweet in tweets:
    score = 0
    for word in tweet['clean'].split():
        if word in lexicon:
            score = score + lexicon[word]

    tweet['score'] = score
    if (score > 0):
        tweet['sentiment'] = 'positive'
    elif (score < 0):
        tweet['sentiment'] = 'negative'
    else:
        tweet['sentiment'] = 'neutral'


# Print out summary stats
total = float(len(tweets))

# num_pos =0
# num_neg=0
# num_neu =0
# for t in tweets:
#     if t['sentiment']=='positive':
#         num_pos +=1
#     elif t['sentiment'] == 'negative':
#         num_neg+=1
#     else:
#         num_neu+=1

# tweets =[
#     ["Hey I saw arich girl with an iphone x"],
#     ["I think we should get that bastard out of his comfort zone"],
#     ["What time do we start the kidnap opeartion"],
#     ["the lexus has new features"]
# ]
# for t in tweets:
#     t['sentiment']=='Pos'

num_pos = sum([1 for t in tweets if t['sentiment'] == 'positive'])
num_neg = sum([1 for t in tweets if t['sentiment'] == 'negative'])
num_neu = sum([1 for t in tweets if t['sentiment'] == 'neutral'])

#Zamu iya dumping din result din as text file not just print it
print("Positive: %5d (%.1f%%)" % (num_pos, 100.0 * (num_pos/total)))
print("Negative: %5d (%.1f%%)" % (num_neg, 100.0 * (num_neg/total)))
print("Neutral:  %5d (%.1f%%)" % (num_neu, 100.0 * (num_neu/total)))


# Print out some of the tweets
tweets_sorted = sorted(tweets, key=lambda k: k['score'])

print("\n\nTOP NEGATIVE TWEETS")
negative_tweets = [d for d in tweets_sorted if d['sentiment'] == 'negative']
for tweet in negative_tweets[0:10]:
    print("id=%d, score=%.2f, clean=%s" % (tweet['id'], tweet['score'], tweet['clean']))

print("\n\nTOP POSITIVE TWEETS")
positive_tweets = [d for d in tweets_sorted if d['sentiment'] == 'positive']
for tweet in positive_tweets[-10:]:
    print("id=%d, score=%.2f, clean=%s" % (tweet['id'], tweet['score'], tweet['clean']))

print("\n\nTOP NEUTRAL TWEETS")
neutral_tweets = [d for d in tweets_sorted if d['sentiment'] == 'neutral']
for tweet in neutral_tweets[0:10]:
    print("id=%d, score=%.2f, clean=%s" % (tweet['id'], tweet['score'], tweet['clean']))
