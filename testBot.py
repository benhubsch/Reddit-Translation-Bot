import praw

reddit_user = "BotTranslator"
reddit_password = "8MC2EwvGGY4M"

# reddit = praw.Reddit(client_id = "Y0o7ag6bKGmyJg", \
#              client_secret = "6sxWB6W-QhdMVgGVdDiQTeWi7C4", \
#              user_agent = "BotTranslator 0.1", \
#              username = reddit_user, \
#              password = reddit_password)

reddit = praw.Reddit(user_agent="BotTranslator 0.1",
                  client_id='Y0o7ag6bKGmyJg',
                  client_secret='6sxWB6W-QhdMVgGVdDiQTeWi7C4')

reddit.login(reddit_user, reddit_password)

subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
