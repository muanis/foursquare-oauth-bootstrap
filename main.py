#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from oauth2client.appengine import OAuth2Decorator
from oauth2client.appengine import OAuth2Handler


decorator = OAuth2Decorator(client_id='your_client_id',
    client_secret='your_client_secret',
    auth_uri='https://foursquare.com/oauth2/authenticate',
    token_uri='https://foursquare.com/oauth2/access_token',
    scope=['https://api.foursquare.com/v2/users/self/checkins'])
    
class MainHandler(webapp.RequestHandler):

    @decorator.oauth_required
    def get(self):
        places_url = "https://api.foursquare.com/v2/users/self/checkins?v=20111227"
        resp, content = decorator.http().request(places_url, 'GET')
        
        self.response.out.write(content)


def main():
    application = webapp.WSGIApplication([
    ('/', MainHandler),
    ('/oauth2callback', OAuth2Handler),
    ], debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
