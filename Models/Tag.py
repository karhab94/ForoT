from google.appengine.ext import db

class Tag(db.Model):
    tag = db.StringProperty()
