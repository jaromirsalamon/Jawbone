from requests_oauth2 import OAuth2

# Jawbone configuration
JAWBONE_SERVER = 'https://jawbone.com'
JAWBONE_AUTHORIZATION_URL = '/auth/oauth2/auth'
JAWBONE_ACCESS_TOKEN_URL = '%s/auth/oauth2/token' % JAWBONE_SERVER
JAWBONE_CHECK_AUTH = '%s/nudge/api/users/@me' % JAWBONE_SERVER

client_id = r'wW72slJ0DRE'
client_secret = r'b5094b76bb306afdcaddece57ffd2adeda90d30f'
redirect_uri = 'https://www.google.cz'

# Note that these are Jawbone specific scopes
scope = 'basic_read extended_read move_read'
oauth = OAuth2(client_id, client_secret, JAWBONE_SERVER, redirect_uri, JAWBONE_AUTHORIZATION_URL)
authorization_url = oauth.authorize_url(scope)

print 'Please go to %s and authorize access.' % authorization_url
authorization_response = raw_input('Enter the full callback URL')