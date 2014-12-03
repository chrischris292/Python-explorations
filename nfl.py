from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
import re
import urllib2
import feedparser
import nltk
from textblob import TextBlob

data = {}

def getPassingData():
    url= 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2014-season-regular-category-passing'
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    table = soup.find(id="sortableContent")
    tableBody = table.find("table")
    for row in tableBody.findAll("tr",{"valign" : "top"}):
        i = 0
        name = ""
        attempts = 0
        attemptsG = 0
        compl = 0
        percentage = 0
        yards = 0
        yardsG = 0
        long = 0
        td = 0
        int = 0
        sack = 0
        sackYl = 0
        rating = 0
        for stats in row.findAll("td"):
            print stats.text
            if(i == 0):
                print stats.text
                name = stats.text
            if(i == 4):
                attempts = stats.text
            if(i==5):
                attemptsG = stats.text
            if(i==6):
                compl = stats.text
            if(i==7):
                percentage = stats.text
            if(i==8):
                yards = stats.text
            if(i==9):
                yardsG = stats.text
            if(i==10):
                long = stats.text
            if(i==11):
                td = stats.text
            if(i==12):
                int = stats.text
            if(i==13):
                sack = stats.text
            if(i==14):
                sackYl = stats.text
            if(i==15):
                rating = stats.text
            i= i+1

        nameTuple = getFirstLastName(name)
        statsTemp = {"first": nameTuple["first"],"last":nameTuple["last"], "attempts": attempts,"attemptsG" : attemptsG, "compl" : compl, "percentage": percentage,"yards":yards, "yardsG":yardsG,"long":long,"td":td,"int":int,"sack":sack,"sackYl":sackYl,"rating":rating}

        data[name] = statsTemp
    print data
    return data

def getNewsArticles(name):
    name = parseName(name)
    url= "https://news.google.com/news/feeds?q="+name+"&output=rss&num=100"
    print url
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page.read())
    for article in soup.findAll("item"):
        print article.find("title").text
        testimonial = TextBlob(article.find("title").text)
        print testimonial.sentiment




'''
Parse Name
Helper Function
Description: Remove Spaces for reading url properly
'''
def parseName(name):
    string = ""
    for char in name:
        if(char!=" "):
            string = string+char
    return string

'''
getFirstLastName
Description: This is very hacky but gets first and last name
'''
def getFirstLastName(name):
    firstName = ""
    lastName = ""
    flag = False
    for char in name:
        if(char==" "):
            flag = True
        else:
            if(flag == False):
                firstName = firstName + char
            else:
                lastName = lastName + char

    nameTuple = {"first" : firstName, "last":lastName}
    return nameTuple


data = getPassingData()
print data["Russell Wilson"]