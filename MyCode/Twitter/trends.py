import twitter

CONSUMER_KEY = 'nWtXkbv44HkOE5Wr1s9G209oG'
CONSUMER_SECRET = 'Fe7eQL7X0kdrZ1EABiMzo3o3iwCXzzkuVIJyZce5t9Nll0UMsF'
OAUTH_TOKEN = '1163695062158577664-IBTngVuitIOd5vAMkCN5tNPkHTSu15'
OAUTH_TOKEN_SECRET = 'NDz9y5DebNHoaCZTmGccgq2QNhuMJgLQuXXxucpuIga3A'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

ZUERICH_WOE_ID = 784794

zuerich_trends = twitter_api.trends.place(_id=ZUERICH_WOE_ID)

print("Zuerich Trends")
print(zuerich_trends)

for trend in zuerich_trends[0]['trends']:
    print(trend['name'])
