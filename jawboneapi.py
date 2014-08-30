import requests
import simplejson as json
import webbrowser

class JawboneAPI():
	"""

	The JawboneAPI class can be used for authentication at the Jawbone UP API. 
	This library also lets you execute API calls and returns all responses in 
	json format. In the future the API calls might be 

	"""

	def __init__(self):
		config_json = open('config.json', 'r')
		config = json.load(config_json)
		
		self.client_id = config["client_id"]
		self.client_secret = config["client_secret"]
		self.redirect_uri = config["redirect_uri"]
		self.scope = config["scope"] or 'basic_read'
		self.base_url = "https://jawbone.com/"

	# Method for getting the first authentication code
	def getAuth(self, scope): 
		u =  'https://jawbone.com/auth/oauth2/auth?response_type=code'
		u += '&client_id=' + self.client_id
		u += '&redirect_uri=' + self.redirect_uri
		u += '&scope=' + self.scope
		
		webbrowser.open(u) # Remove this for production, only for debugging
		return u

	# Methode for getting the access code for a user with a auth code.
	def getAccessToken(self, code):
		u =  'https://jawbone.com/auth/oauth2/auth/?'
		u += 'client_id=' + self.client_id
		u += '&client_secret=' + self.client_secret
		u += '&grant_type=authorization_code'
		u += '&code=' + code

		res = requests.get(u)
		if res.status_code == 200:
			# Should be in the format of: {"access_token": "token_here", "token_type": "Bearer", "expires_in": 31536000, "refresh_token": "refresh_token_here"}
			return json.loads(res)
		else:
			return res

	def apiCall(self, access_token, endpoint='/nudge/api/users/@me/moves', **kwargs):
		# for other parameters, look at: https://jawbone.com/up/developer/endpoints/
		u = 'https://jawbone.com'
		u += endpoint #endpoint # Change this to the endpoint you want 
		headers = {'content-type': 'application/json', 'host': 'api.example.com' ,'Authorization:': 'Bearer ' + access_token}
		res = requests.get(u, headers=headers)
		if res.status_code == 200:
			return json.loads(res)
		else:
			return {
            'error': res.reason, 
            'status_code': res.status_code  
        	}
		
	

