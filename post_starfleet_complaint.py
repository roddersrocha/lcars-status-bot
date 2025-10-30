# post_starfleet_complaint.py

import tweepy
import random
from datetime import datetime, timedelta, timezone

# Your Twitter API credentials (stored as GitHub secrets)
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# Authenticate with Twitter API
auth = tweepy.OAuth1UserHandler(
    CONSUMER_KEY, CONSUMER_SECRET,
    ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

# List of humorous Starfleet HR complaints
complaints = [
    "Anonymous: The replicator gave me decaf AGAIN.",
    "Anonymous: My phaser is set to 'stun' but it feels more like 'mild annoyance'.",
    "Anonymous: The holodeck keeps glitching and turning my vacation into a Klingon opera.",
    "Anonymous: Why does the turbolift always stop at every deck when I'm in a hurry?",
    "Anonymous: The ship's counselor is too empathetic; now I feel bad for complaining.",
    "Anonymous: Engineering won't fix the squeaky door in my quarters—claims it's 'ambient noise'.",
    "Anonymous: The food synthesizer only produces bland rations; where's the flavor variety?",
    "Anonymous: My communicator badge fell off during a red alert—embarrassing!",
    "Anonymous: The captain's logs are too dramatic; can we tone down the narration?",
    "Anonymous: Sickbay's hyposprays sting more than a Tribble bite.",
    "Anonymous: The viewscreen resolution is fuzzy; can't see enemy ships clearly.",
    "Anonymous: Shuttlecraft parking is a nightmare; always full during shift changes.",
    "Anonymous: The universal translator mangled my pickup line at the bar.",
    "Anonymous: Gravity plating failed in the gym; now I'm 'floating' through workouts.",
    "Anonymous: The ship's AI keeps suggesting I 'relax'—as if!",
    "Anonymous: Replicated uniforms shrink in the sonic shower.",
    "Anonymous: Borg assimilation threats in spam emails—IT, please filter better.",
    "Anonymous: The jefferies tubes are too cramped for routine maintenance.",
    "Anonymous: Ten Forward's happy hour doesn't have enough synthehol options.",
    "Anonymous: My PADD autocorrects 'phaser' to 'fazer'—unprofessional!"
]

def should_post():
    # Get the user's latest tweet
    try:
        tweets = api.user_timeline(count=1)
        if not tweets:
            return True  # No tweets yet, so post
        latest_tweet = tweets[0]
        created_at = latest_tweet.created_at
        now = datetime.now(timezone.utc)
        delta = now - created_at
        return delta > timedelta(hours=17)
    except tweepy.TweepyException as e:
        print(f"Error checking timeline: {e}")
        return False

if should_post():
    # Pick a random complaint
    complaint = random.choice(complaints)
    try:
        api.update_status(complaint)
        print(f"Posted: {complaint}")
    except tweepy.TweepyException as e:
        print(f"Error posting tweet: {e}")
else:
    print("Less than 17 hours since last post; skipping.")
