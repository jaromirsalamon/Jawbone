import urllib
import requests

# Jawbone configuration
JAWBONE_SERVER = 'https://jawbone.com/'
JAWBONE_AUTHORIZATION_URL = '%s/auth/oauth2/auth' % JAWBONE_SERVER
JAWBONE_ACCESS_TOKEN_URL = '%s/auth/oauth2/token' % JAWBONE_SERVER
JAWBONE_CHECK_AUTH = '%s/nudge/api/users/@me' % JAWBONE_SERVER


class Jawbone(object):
    
    def __init__(self, scope = 'basic_read'):
        self.client_id = 'wW72slJ0DRE'
        self.client_secret = 'b5094b76bb306afdcaddece57ffd2adeda90d30f'
        self.redirect_uri = 'https://www.google.cz'
        self.scope = 'basic_read extended_read move_read'
    
    def auth(self): 
   
        params = { 
            'client_id'     : self.client_id,
            'scope'         : self.scope,
            'redirect_uri'  : self.redirect_uri,
            'response_type' : 'code'  
        }

        context = {
            'auth_url': JAWBONE_AUTHORIZATION_URL,
            'params'  : urllib.urlencode(params)
        }
        
        url = '{auth_url}/?{params}'.format(**context)
        
        response = requests.get(url)
        
        #return response.content
        return url 