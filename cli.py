import feedparser
import os

from rename import main

#CLI Version
path = input("Which directory need to be scanned? ")
rss = feedparser.parse(input("Which feed do you want to parse? "))

main(path, rss)