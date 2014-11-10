__author__ = 'ChristopherChan'
import twitter
import re
import nltk
from textblob import TextBlob
api = twitter.Api(consumer_key='DdBFALjNxyXKUn1B5yhseE94g',
                      consumer_secret='bznrXQqjf5KRqfT3zTpsAoLYP2mWitQ2cMWUQYtKNighad5M9K',
                      access_token_key='1517073156-Kk9XfrKd2WPKio1fT7UNbKHFpHKRXkzlGaPLU5g',
                      access_token_secret='JcqQtZg9L0xVd5lsZwQbp0hpGyKrJWeLkWNEjHFD30o8C')

'''
This code gets user timeline from screen name
'''
class twitter:


    def __init__(self):
        self

def getTwitterTimeline(status):
    tweetString = ""
    status = api.GetUserTimeline(screen_name = status)
    for s in status:
        parsedString = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",s.text).split())
        s.text = parsedString
        '''tweetString = tweetString + " " + parsedString'''
    return status


def get_ngrams(status):
    status = getTwitterTimeline(screen_name=status)
    tokenized_content = nltk.word_tokenize(status)
    content_model = nltk.ngrams(tokenized_content,3)
    for i in content_model:
        print i

'''
    This library is pretty innacurate
    Accrued results like "do the Knicks have a clue this year" with a rating of 0.0
'''
def get_sentiment_analysis(status):
    status = getTwitterTimeline(status)
    for s in status:
        blob = TextBlob(s.text)
        print s.text
        for sentence in blob.sentences:
            print(sentence.sentiment.polarity)


get_sentiment_analysis("rsherman25")



