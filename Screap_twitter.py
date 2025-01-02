import snscrape.modules.twitter as sntwitter
import pandas as pd

# Parameter Scraping
tweet_url = 'https://twitter.com/username/status/tweet_id'  # Ganti dengan URL Tweet yang diinginkan
max_comments = 50  # Jumlah komentar maksimum yang ingin diambil

# Mengumpulkan komentar di bawah Tweet
comments = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'url:"{tweet_url}"').get_items()):
    if i >= max_comments:
        break
    comments.append([tweet.date, tweet.user.username, tweet.content, tweet.likeCount, tweet.replyCount, tweet.retweetCount])

# Menyimpan data ke DataFrame
df = pd.DataFrame(comments, columns=['Date', 'Username', 'Comment', 'Likes', 'Replies', 'Retweets'])

# Menyimpan ke file CSV
df.to_csv('twitter_comments.csv', index=False)
print("Scraping selesai! Data disimpan dalam 'twitter_comments.csv'")
