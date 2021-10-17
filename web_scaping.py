import tweepy
import pandas

auth= tweepy.OAuthHandler(apikey,apikeysecret )
auth.set_access_token(token, tokensecret)
api = tweepy.API(auth,wait_on_rate_limit=True)

search_word= ['vaccination'] 
date_since= '2021-10-16'

places = api.search_geo(query="USA", granularity="country")
place_id = places[0].id

tweet_details=dict()

for i in range(len(search_word)):
    tweets= tweepy.Cursor(api.search_tweets, q=search_word[i] +'-filter:retweets place:%s' % place_id, lang='en', until= date_since).items(3000)
    tweet_details[i]= [[tweet.text,tweet.user.screen_name,tweet.user.location]for tweet in tweets]

dp=pandas.DataFrame(tweet_details[0])
dp.to_csv('tweetdata.csv')   


# geocode="30.627977,-96.334404,100km"
