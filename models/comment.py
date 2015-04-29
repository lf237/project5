from google.appengine.ext import ndb
from models import ParkingLot

class Comment(ndb.Model):
    text = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
    atype = ndb.IntegerProperty()
    lot = ndb.KeyProperty(ParkingLot, repeated=True)