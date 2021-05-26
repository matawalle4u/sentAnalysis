# import tweepy
# class StreamListener(tweepy.StreamListener):
#     def on_status(self, status):
#         for tweet in tweepy.Cursor(api.search,q='#katsina', lang="en", geocode="9.077751, 8.6774567, 910770km", since="2019-02-03").items():
#             print(tweet.text)
#         #print(status.id_str, status.text)
#     def on_error(self, status_code):
#         print(status_code)
#         sys.exit()
#try:

           # starting_date = datetime.datetime(2020, 1, 1)

           # shekara =int(starting_date.strftime('%Y'))
           # wata = int(starting_date.strftime('%m'))
            #rana = int(starting_date.strftime('%d'))



# if __name__=="__main__":
#     auth = tweepy.OAuthHandler("DtqeMfk3QBZMDI14CU06Erqvo", "5zd0UzKEVs26rJUOfXEcnTkOtkHaY55hNCcIlskPxpyChoiiJG")
#     auth.set_access_token("1295250059584364544-WgX42OkmmuP0J1BagODoFSO8OTYpi9", "r1qd0dhI9dLCSyBOKF6fWfD4FGYHYE8dT1CY1HESIQT2X")
#     api=tweepy.API(auth)
#     streamListener = StreamListener()
#     stream = tweepy.Stream(auth=api.auth, listener=streamListener, tweet_mode='extend')
#     tags = ['kidnappings', 'kidnap', 'bandits', 'banditry', 'katsinagunmen', 'katsinaarmedmen' 'ransome']
#     stream.filter(track=tags)

import sys
import tweepy
import datetime
tags = [
        'kidnappings-NIGERIA',
        'kidnap',
        'bandits',
        'fulani',
        'katsinabanditry' 
        'ransome',
        'armedmen',
        '9jaKidnaps',
        'northBandits',]
        
class streamListener(tweepy.StreamListener):
   def on_status(self, status):
      try:
         starting_date = datetime.datetime(2020, 1, 1)
         shekara =int(starting_date.strftime('%Y'))
         wata = int(starting_date.strftime('%m'))
         rana = int(starting_date.strftime('%d'))

         print(status.id_str, status.text, status.created_at, status.coordinates, status.place)
         data_ = '{}, {}, {}\n'.format(status.id_str, status.text, status.created_at, status.coordinates, status.place)
         print(status.created_at)
         open('original_tweet_data.csv', 'a+').write(data_)

      except UnicodeEncodeError:
         pass

   def on_error(self, status_code):
      print(status_code)
      sys.exit()

   def on_timeout(self):
      print >> sys.stderr, 'Timeout...'
      return True # Don't kill the stream

if __name__=="__main__":
   key_words = "kidnappings-NIGERIA OR bandits OR katsina-killings OR herdsmen OR ransome"
   auth = tweepy.OAuthHandler("DtqeMfk3QBZMDI14CU06Erqvo", "5zd0UzKEVs26rJUOfXEcnTkOtkHaY55hNCcIlskPxpyChoiiJG")
   auth.set_access_token("1295250059584364544-WgX42OkmmuP0J1BagODoFSO8OTYpi9", "r1qd0dhI9dLCSyBOKF6fWfD4FGYHYE8dT1CY1HESIQT2X")
   api=tweepy.API(auth)
   for tweet in tweepy.Cursor(api.search, q=key_words, since='2020-01-01', untill='2020-08-01', locations=[12.00,-8.52,12.98,7.61], lang="en").items():
      date_tweet = str(tweet.created_at)
      kwanan_wata =  date_tweet[0:10]
      new_kw = kwanan_wata.replace('-', '')
      data_ = '{},{},{}\n'.format(tweet.text, tweet.id, new_kw)
      print(tweet.text, tweet.id, new_kw)
      #print(status.id_str, status.text, status.created_at, status.coordinates, status.place)
      try:

         open('new_extracted_tweet_data.csv', 'a+').write(data_)
      except UnicodeEncodeError:
         pass
