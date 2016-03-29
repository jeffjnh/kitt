import praw
from pprint import pprint




def getReddit(channel):
    subreddit = reddit.get_subreddit(channel)
    
    
def getRandSubmissionFromSub(channel):
    sub = getRndSubmission(channel)
    response = {}
    response['title'] = sub.title
    response['link'] = sub.url
    return response
    
def getRndSubmission(channel):
    global reddit
    return reddit.get_random_submission(channel)
    
    
################################################################
    
    
def getRandomSubmissionFromAll(unsafe=False):
    global reddit
    subreddit = reddit.get_random_subreddit(unsafe)
    return getRandSubmissionFromSub(subreddit.display_name)