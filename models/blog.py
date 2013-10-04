from google.appengine.ext import db

class Blog(db.Model):
	title = db.StringProperty()
	text = db.TextProperty()	

