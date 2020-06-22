import pandas as pd
import sys
import markovify

def get_tweets_dataframe(output_path):
    return pd.read_csv(output_path)

def remove_tweets_with_mentions(df):
    df = df[~df.tweet.str.contains("@")]
    df = df[~df.tweet.str.contains("http")]
    df = df[~df.tweet.str.contains(".com")]


    return df

def tweets_column_to_list(df):
    return df['tweet'].tolist()

if __name__ == "__main__":
    output_path = sys.argv[1]

    df = get_tweets_dataframe(output_path)
    
    df = remove_tweets_with_mentions(df)

    tweets_list = tweets_column_to_list(df)

    text_model = markovify.Text(tweets_list)

    print(text_model.make_sentence())