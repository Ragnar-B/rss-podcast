import feedparser

from rename import rename

#CLI Version
path = input("Which directory need to be scanned? ")
rss = feedparser.parse(input("Which feed do you want to parse? "))

rename(path, rss)