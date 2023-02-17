import feedparser
NewsFeed = feedparser.parse("https://feeds.fireside.fm/selfhosted/rss")
entry = NewsFeed.entries[1]

print(entry.id)
