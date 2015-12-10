__author__ = 'shreyas'

import urllib2
import webapp2
import jinja2
from handlers.BaseHandler import BaseHandler
from google.appengine.api import users
from Stream import Personal
from Stream import Artist
import json

class RecomendArtistHandler(webapp2.RequestHandler, BaseHandler):
    def get(self):
        self.cache('rec_artists')

        user_id = users.get_current_user().user_id()
        me = Personal.query(Personal.user_id==user_id).get()

        if me.liked_artists:
            key = '&client_id=Mzk0Njg1OHwxNDQ5NTQ2NTUx'

            base_url = "http://api.seatgeek.com/2/recommendations/performers?" #performers.id=35&performers.id=2446&client_id="

            my_fav_artists = me.liked_artists
            base_url = base_url + "performers.id=" + str(my_fav_artists.pop(0).id)
            while(len(my_fav_artists)>0):
                base_url = base_url + "&performers.id=" + str(my_fav_artists.pop(0).id)

            url = base_url + key
            response = urllib2.urlopen(url)
            data = response.read()
            values = json.loads(data)

            if values['recommendations']:
                recommended_artists = list()
                output = values['recommendations']
                for artist in output:
                    new_artist = Artist(name=artist['performer']['name'], id=artist['performer']['id'], image_link=artist['performer']['image'])
                    recommended_artists.append(new_artist)

            for thing in recommended_artists:
                self.response.write(thing.name)

        else:
            self.response.write("In order to get recommendations, you must like least 1 song")