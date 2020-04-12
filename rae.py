import praw
import config

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     password=config.password,
                     user_agent=config.user_agent,
                     username=config.username)

subreddit = reddit.subreddit('all')

words = {}

for submission in subreddit.hot(limit=100):
    print(submission.title)  # Output: the title of the submission
    for word in submission.title.split():
        if len(word) >= 6:
            if words.__contains__(word):
                words[word] = words[word] + 1
            else:
                words[word] = 1

for i in sorted (words, key=words.get):
    print (i)

