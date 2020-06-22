import twint
import sys
import datetime

def get_yesterday_date():
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d %H:%M:%S")

def get_tweets(output_path, user_name):
    c = twint.Config()
    c.Username = user_name
    c.Store_csv = True
    c.Output = output_path
    c.Since = get_yesterday_date()

    twint.run.Search(c)

if __name__ == "__main__":
    output_path = sys.argv[1]
    user_name = sys.argv[2]

    get_tweets(output_path, user_name)