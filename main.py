from generate_string import generate_tweet
from generate_string import next_generation
from generate_string import random_population
from generate_string import print_population
from generate_string import selection
from generate_string import get_5_tweets
from generate_string import get_avg_fit
from generate_string import get_best
import tweepy
import copy
import time
__author__ = 'eric'


class TwitterAPI:
    def __init__(self):
        consumer_key = "SoipbvmeU7b2TryZ9iaKivHoC"
        consumer_secret = "qB1mp6zhtXCXjGSUmlebNCU3Pix3dDfKpfyH8mARG9ABdVAsh4"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "4131656833-U9dvsryUFXgq6FpxENQI2ZIzRWrer5pt1nUx1TF"
        access_token_secret = "BJFrbosEanXBOusomfPdlzLntfy3cDp673KNII9Krk7sE"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

#
# Main driver
# Generate a population and simulate generatons
#




# Create random starting population
current_pop = random_population()
print"==Original Population=="
print_population(current_pop)

best1 = copy.copy(selection(current_pop))
best2 = copy.copy(selection(current_pop))

for x in xrange(0, 100):
    print "Round " + str(x) + "*************************"
    # fast forward 200 generations
    best1 = copy.copy(selection(current_pop))
    best2 = copy.copy(selection(current_pop))

    #print "Generation " + str(i)
    current_pop = next_generation(current_pop, best1, best2)
    print_population(current_pop)

    # get 5 good sentences, and tweet them
    for c in get_5_tweets(current_pop):
        print c
        #twitter = TwitterAPI()
        #twitter.tweet(c)
    #print "Elite1: " + best1.return_tweet()
    #print "Elite2: " + best2.return_tweet()
    with open("avg_fit", "a") as avgfile:
        avgfile.write(str(get_avg_fit(current_pop)))
        avgfile.write("\n")
    with open("best_fit", "a") as bestfile:
        bestfile.write(str(get_best(current_pop).return_fitness()))
        bestfile.write("\n")
    #time.sleep(3)

with open("best_fit", "a") as bestfile:
    bestfile.write(get_best(current_pop).return_tweet())
