from etls.reddit_etl import connect_reddit
from utils.constants import SECRET, CLIENT_ID
from etls.reddit_etl import extract_posts   

def reddit_pipeline(file_name: str, subreddit: str,time_filter = 'day', limit=None):
    # Connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')

    #Extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)