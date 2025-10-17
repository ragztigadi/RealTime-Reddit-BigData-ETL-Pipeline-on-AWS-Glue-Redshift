from utils.constants import SECRET, CLIENT_ID
from utils.constants import OUTPUT_PATH

from etls.reddit_etl import connect_reddit
from etls.reddit_etl import extract_posts
from etls.reddit_etl import load_data_to_csv
from etls.reddit_etl import transform_data

import pandas as pd

def reddit_pipeline(file_name: str, subreddit: str,time_filter = 'day', limit=None):
    # Connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')

    #Extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    print(f"Extracted posts: {len(posts)}")

    #Transformation
    post_df = transform_data(post_df)

    #Loading to CSV
    file_path = f"{OUTPUT_PATH}/{file_name}.csv"
    load_data_to_csv(post_df, file_path)

    return file_path
