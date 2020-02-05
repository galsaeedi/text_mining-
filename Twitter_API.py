#tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#4 keys to access Twitter API
access_token = "752352954133450752-zSBvyn5MBfU3d7X7r58TZlnvsy6LhhE"
access_token_secret = "GnZuPNFCuwWoVuexGfJEng6N5ALpA1oAtBokoyzr9Hau0"
consumer_key = "YeMTgXYpjwjnmDhWCFslKO7Qy"
consumer_secret = "T3otl9uOe40vvhUpsbNyehOKRMbKOHtztgOkHTu5U1cbTIpC3O"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
