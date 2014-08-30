import urllib
import requests
import json
import simplejson


class Jawbone(object):

    def __init__(self):

        self.config_json = open('config.json', 'r')
        self.config = json.load(self.config_json)
        
        self.client_id = self.config["client_id"]
        self.client_secret = self.config["client_secret"]
        self.redirect_uri = self.config["redirect_uri"]
        self.scope = self.config["scope"] or 'basic_read'
        self.base_url = "https://jawbone.com/"


    def doAuth(self, scope=None): 
 
        params = { 
            'scope'         : scope or self.scope,
            'client_id'     : self.client_id,
            'redirect_uri'  : self.redirect_uri,
            'response_type' : 'code'  
        }

        context = {
            'base_url': self.base_url,
            'params'  : urllib.urlencode(params)
        }

        # A hard redirect to the authorize page. 
        # User would see either the login to jawbone page, 
        # or authorize page if already logged in.
        
        url = '{base_url}auth/oauth2/auth/?{params}'.format(**context)
        
        #webbrowser.open(url) # Remove this for production, only for debugging
        
        return url 

    def getAccessToken(self, code, grant_type='authorization_code'):
     
        params = {
            'code'          : code,
            'client_id'     : self.client_id,
            'client_secret' : self.client_secret,
            'grant_type'    : grant_type
        }

        context = {
            'base_url': self.base_url,
            'params'  : urllib.urlencode(params)
        }
 
        token_url = '{base_url}auth/oauth2/token/?{params}'.format(**context)

        response = requests.get(token_url)
        
        if response.status_code == 200:
            json_encoded = json.dumps(response.json())
            json_data = json.loads(json_encoded)
            if 'access_token' in json_data.keys():
                return json_data['access_token']
            else:
                return json_data['error']
        else:
            return {
                'error': response.reason, 
                'status_code': response.status_code  
            }
            
    def doApiCall(self, access_token, endpoint, **kwargs):
 
        context = {
            'base_url': self.base_url,
            'endpoint': endpoint
        }

        api_call = '{base_url}{endpoint}'.format(**context)

        headers = {
           'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',   
            'Host'  : 'api.example.com',
            'Authorization': 'Bearer {0}'.format(access_token)
        }

        response = requests.get(api_call, headers=headers)

        if response.status_code == 200:
            if response.headers['content-type'] == 'image/png':
                return response.content
                '''
                with open('C:/workspace/Jawbone/output.png', 'wb') as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                '''
            else: 
                if response.headers['content-type'] == 'application/json':
                    #json_encoded = json.dumps(response.json())
                    #json_data = json.loads(json_encoded)
                    return simplejson.loads(response.content)
        else:
            return {
                'error': response.reason, 
                'status_code': response.status_code  
            }


    def doRefreshToken(self, refresh_code):
        '''
        Get the new access code for a refresh token

        Parse the response, and update your database entries
        with the new auth credentials.
        '''

        return self.getAccessToken(self, refresh_code, 'refresh_token')

    def getUserId(self, access_token):
        response = self.doApiCall(access_token, '/nudge/api/users/@me')
        
        """Return user details from Jawbone account"""
        xid = response['data'].get('xid', '')
        
        return xid
    
    
