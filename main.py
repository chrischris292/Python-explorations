from BeautifulSoup import BeautifulSoup
import urllib2


url= 'http://www.fftoday.com/stats/playerstats.php?Season=2014&GameWeek=1&PosID=10&LeagueID=1'
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

rank = soup.find("tr").td.contents
print rank
