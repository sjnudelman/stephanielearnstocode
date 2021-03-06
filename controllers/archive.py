import jinja2
import os
import webapp2
from google.appengine.ext.webapp import template

directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'views'))
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(directory))

HTML_TEMPLATE = jinja_environment.get_template('archive.html')

class Archive(webapp2.RequestHandler):
	def get(self):
		data = {
			"message": self.request.get("message"),
		}
		self.response.out.write(HTML_TEMPLATE.render(data))
