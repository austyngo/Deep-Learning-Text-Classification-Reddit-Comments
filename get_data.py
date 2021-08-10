import praw
import pandas as pd
from datetime import datetime, date
from praw.models import MoreComments
import config

reddit = praw.Reddit(client_id= config.clientid,  
                    client_secret= config.secret,
                    user_agent = config.useragent,
                    username= config.username,
                    password= config.password)
 
def get_comments(subreddit): 
    sub = reddit.subreddit(subreddit)
    posts = set() 
    posts.update(sub.hot(limit=None))

    comment_ = []
    flair = []

    for sub in posts:
        print(sub.title)
        for com in sub.comments:
            if isinstance(com, MoreComments):
                continue 
            if com.author_flair_text is not None:
                print(com.body)
                comment_.append(com.body)
                print(com.author_flair_text) 
                flair.append(com.author_flair_text)
    
    d = {'comment': comment_, 'flair': flair}
    df = pd.DataFrame(data = d)

    return df

def userDate(tstamp):
    return datetime.utcfromtimestamp(tstamp).strftime('%Y-%m-%d %H:%M:%S')

def main():
    subreddit = 'PoliticalCompassMemes'
    data = get_comments(subreddit)
    data.to_csv('comments4.csv') 

if __name__ == '__main__':
    main() 