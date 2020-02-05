import json
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
import seaborn as sns

tweets_file = 'data.txt'

data_array = []
opn_tweets_file = open(tweets_file, "r") #open data.text file
for line in opn_tweets_file: # read data.text file and load it into array
    try:
        tweet = json.loads(line)
        data_array.append(tweet)
    except:
        continue

print(len(data_array))

tweets = pd.DataFrame() #empty data frame

tweets['text'] = list(map(lambda tweet: tweet['text'], data_array)) #return key'text' value and store it in text column
tweets['country'] =list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, data_array))


ax=sns.countplot(tweets['country'], data=tweets,order=tweets['country'].value_counts()[:5].index,palette='Blues_d')
ax.set_ylabel('Number of Tweets')
ax.set_xlabel('Countries')
ax.set_title('Top 5 Countries')
ax.tick_params(axis='x', labelsize=10)
plt.show()

def search_for_word(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets['python'] = list(map( lambda tweet: search_for_word('python', tweet),tweets['text']))
tweets['javascript'] = list(map(lambda tweet: search_for_word('javascript', tweet),tweets['text']))
tweets['ruby'] = list(map(lambda tweet: search_for_word('ruby', tweet),tweets['text']))

print (tweets['python'].value_counts()[True])
print (tweets['javascript'].value_counts()[True])
print (tweets['ruby'].value_counts()[True])


prg_leng=['python','javascript','ruby']
tweets['relevant'] = list(map(lambda tweet: search_for_word('programming', tweet) or search_for_word('tutorial', tweet),tweets['text']))

num_prg_leng=[tweets[tweets['relevant']==True]['python'].value_counts()[True],
              tweets[tweets['relevant']==True]['javascript'].value_counts()[True],
              tweets[tweets['relevant']==True]['ruby'].value_counts()[True]]

print(tweets[(tweets['relevant']==True) & (tweets['python']==True)]['python'].value_counts())
print(tweets[(tweets['relevant']==True) & (tweets['javascript']==True)]['javascript'].value_counts())
print(tweets[(tweets['relevant']==True) & ( tweets['ruby']==True)]['ruby'].value_counts())

ax= sns.barplot(x=prg_leng,y=num_prg_leng,palette='Blues_d')
ax.set_ylabel('Number of Tweets')
ax.set_title('Python vs. JavaScript vs. Ruby')
plt.show()

def search_for_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

tweets['link'] = list(map(lambda tweet: search_for_link(tweet),tweets['text']))

print ('{} links for python'.format(len(tweets[(tweets['python'] == True) & (tweets['relevant']==True) & (tweets['link']!='')]['link'].index)))
print ('{} links for javascript'.format(len(tweets[(tweets['javascript']==True) & (tweets['relevant']==True) & (tweets['link']!='')]['link'])))
print ('{} links for ruby'.format(len(tweets[(tweets['ruby']==True)& (tweets['relevant']==True)& (tweets['link']!='')]['link'])))

print (tweets[(tweets['python'] == True) & (tweets['relevant']==True) & (tweets['link']!='')]['link'])
print (tweets[(tweets['javascript']==True) & (tweets['relevant']==True) & (tweets['link']!='')]['link'])
print (tweets[(tweets['ruby']==True)& (tweets['relevant']==True)& (tweets['link']!='')]['link'])

