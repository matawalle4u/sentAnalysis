#Take each w
import csv
import negations


def improved_bow(tweet, lexicon_file):

    done =[]
    result ={}

    words = negations.new_nega(tweet)
    for word in words:
        
        if word[0:8]=='negated_':
            new_word = word[8:]
            with open(lexicon_file, 'rt') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')

                next(reader)
                for row in reader:
                    if row[0] ==new_word and new_word not in done: 
                        #swap polarity here
                        if row[1] =='-1':
                            row[1] =1
                        else:
                            row[1] =-1
                        result[new_word] = {'count': words.count(word), 'Polarity':row[1]}
                        done.append(new_word)
                        break
        else:
            with open(lexicon_file, 'rt') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                next(reader)
                for row in reader:
                    try:
                        if word==row[0] and row !=''  and word not in done:
                            result[word] = {'count': words.count(word), 'Polarity':int(row[1])}
                            done.append(word)
                            break
                                
                    except IndexError:
                        pass
    return result


def classify_tweet(tweet, lexicon_file):
    bow = improved_bow(tweet, lexicon_file)
    result =0
    count =0
    for item in bow:
        if item[0:7]=='__Score':
            result +=bow[item]
            count+=1
    try:

        print(result/count)
    except ZeroDivisionError:
        pass
def compare_performance(tweet, lexicons):
    for lexicon in lexicons:
        classify_tweet(tweet, lexicon)

tweet = "I am warning you, I will take up arms kidnap you, You are not to be treated lightly"
tweet ="I am in love love and love with new interface, it is awesome awesome and awesome I no hate you"
lexicons = 'lexicon/lexicon.csv'
print(improved_bow(tweet, lexicons))
