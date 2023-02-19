import feedparser
import os

# #Environment Variables
# path  = os.environ[path]
# rss = feedparser.parse("os.environ[rss]")

# #CLI Version
# path = input("Which directory need to be scanned? ")
# rss = feedparser.parse(input("Which feed do you want to parse? "))

def main(path, rss):
    for episode in range(0, len(rss.entries) -1):
        id = rss.entries[episode]
        for file in os.listdir(path):
            episode_mp3 = id.id + ".mp3"
            title_mp3 = id.title + ".mp3"
            if file == episode_mp3:
                os.rename(episode_mp3, title_mp3)
                print(f"Renamed {episode_mp3} to {title_mp3}.")

# if __name__ == "__main__":
#     main()