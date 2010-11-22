import time
import urllib
import urllib2

'''
DELICIOUS API SAMPLER

So far this just shows an example of how to make auth work.


'''

y_app_id = 'FT6seU5e'
y_app_domain = 'wiggleback.com'
y_key = 'dj0yJmk9UXJ5czhPZUY2NEhPJmQ9WVdrOVJsUTJjMlZWTldVbWNHbzlNakEyTlRZME1UYzJNZy0tJnM9Y29uc3VtZXJzZWNyZXQmeD0zOA--'
y_secret = '4ec6b9c1ae778a18f50be42d3848107ec12bda23'
y_app_url = 'http://www.wiggleback.com/bkn'
params = ''
params += 'oauth_signature='+y_secret +'%26'
params += '&oauth_consumer_key='+y_key
params += '&oauth_signature_method=PLAINTEXT' # could also be hmac-sha1
params += '&oauth_version='+'1.0'
params += '&oauth_callback=oob' # I don't need a callback
params += '&oauth_nonce='+'whatthe' # random string
params += '&oauth_timestamp='+str(time.time()) # must be +-600 seconds current time.
#params += '&oauth_timestamp='+str(int(time.time())) # must be +-600 seconds current time.
req = 'https://api.login.yahoo.com/oauth/v2/get_request_token?'
print req+params
x = urllib2.urlopen(req+params)
print 'x: ',x.read()
