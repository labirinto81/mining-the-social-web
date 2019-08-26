import twitter

CONSUMER_KEY = 'nWtXkbv44HkOE5Wr1s9G209oG'
CONSUMER_SECRET = 'Fe7eQL7X0kdrZ1EABiMzo3o3iwCXzzkuVIJyZce5t9Nll0UMsF'
OAUTH_TOKEN = '1163695062158577664-IBTngVuitIOd5vAMkCN5tNPkHTSu15'
OAUTH_TOKEN_SECRET = 'NDz9y5DebNHoaCZTmGccgq2QNhuMJgLQuXXxucpuIga3A'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable

print(twitter_api)

# The Yahoo! Where On Earth ID for the entire world is 1.
# See https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

# Prefix ID with the underscore for query string parameterization.
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument.

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

print("World trends")
print(world_trends)
print()
print(us_trends)

for trend in world_trends[0]['trends']:
    print(trend['name'])

#%%

for trend in us_trends[0]['trends']:
    print(trend['name'])

#%%

world_trends_set = set([trend['name']
                        for trend in world_trends[0]['trends']])

us_trends_set = set([trend['name']
                     for trend in us_trends[0]['trends']])

common_trends = world_trends_set.intersection(us_trends_set)

print(common_trends)