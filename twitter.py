import json
import random

from requests_oauthlib import OAuth1Session


def get_twitter(config):
    """
    Get tweet that you are following
    :param config: configuration file
    :return: void
    """

    c = dict(config.items('twitter'))

    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    params = {
        'screen_name': c['screen_name'],
        'count': int(c['tweet_cnt']),
    }
    # url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
    # url = 'https://api.twitter.com/1.1/friends/ids.json'
    # url = 'https://api.twitter.com/1.1/friends/list.json'

    twitter = OAuth1Session(
        c['consumer_key'],
        c['consumer_secret'],
        c['access_token'],
        c['access_token_secret']
    )

    req = twitter.get(url, params=params)

    if req.status_code == 200:
        # Parse JSON style response
        timeline = json.loads(req.text)
        tl = random.choice(timeline)
        line = '-' * 100
        print('\n'.join([
            line,
            "Today's tweet: {}".format(tl['text']),
            line
        ]))

    else:
        # Error occured
        print('Failed to access Twitter API: {}'.format(req.status_code))
