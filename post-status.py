import pandas as pd
import sys
import markovify
import configparser
import tweepy

def get_tweets_dataframe(output_path):
    return pd.read_csv(output_path)

def remove_tweets_with_mentions(df):
    df = df[~df.tweet.str.contains("@")]
    df = df[~df.tweet.str.contains("http")]
    df = df[~df.tweet.str.contains(".com")]
    df = df[~df.tweet.str.contains("inara")]
    df = df[~df.tweet.str.contains("Inara")]
    df = df[~df.tweet.str.contains("INARA")]

    return df

def tweets_column_to_list(df):
    return df['tweet'].tolist()

def generate_message(tweets_list):
    while True:
        text_model = markovify.Text(tweets_list).make_sentence()
        if text_model != None:
            return text_model

    
def create_config():
    config = configparser.ConfigParser()
    config.read(sys.argv[2])
    return config['twitter']['consumer_key'], config['twitter']['consumer_secret'], config['twitter']['access_token'], config['twitter']['access_token_secret']


def post_tweet(message):

    consumer_key, consumer_secret, access_token, access_token_secret = create_config()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    api.update_status(message)

if __name__ == "__main__":
    output_path = sys.argv[1]

    df = get_tweets_dataframe(output_path)
    
    df = remove_tweets_with_mentions(df)

    tweets_list = tweets_column_to_list(df)

    message = generate_message(tweets_list)

    post_tweet(message)
    
    