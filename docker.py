import feedparser
import os
from rename import rename

#Environment Variables
path  = os.environ["path"]
rss = feedparser.parse("os.environ[rss]")

rename(path, rss)