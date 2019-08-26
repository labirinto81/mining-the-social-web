import json
import matplotlib
import twitter

CONSUMER_KEY = 'nWtXkbv44HkOE5Wr1s9G209oG'
CONSUMER_SECRET = 'Fe7eQL7X0kdrZ1EABiMzo3o3iwCXzzkuVIJyZce5t9Nll0UMsF'
OAUTH_TOKEN = '1163695062158577664-IBTngVuitIOd5vAMkCN5tNPkHTSu15'
OAUTH_TOKEN_SECRET = 'NDz9y5DebNHoaCZTmGccgq2QNhuMJgLQuXXxucpuIga3A'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

q = '#MothersDay'
count = 100

for label, data in (('Word', words),
                    ('Screen Name', screen_names),
                    ('Hashtag', hashtags)):
    pt = PrettyTable(field_names=[label, 'Count'])
    c = Counter(data)
    [ pt.add_row(kv) for kv in c.most_common()[:10] ]
    pt.align[label], pt.align['Count'] = 'l', 'r' # Set column alignment
    print(pt)


word_counts = sorted(Counter(words).values(), reverse=True)

plt.loglog(word_counts)
plt.ylabel("Freq")
plt.xlabel("Word Rank")