import jinja2
import os
import webapp2
from google.appengine.ext.webapp import template
from models import blog

directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'views'))
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(directory))

HTML_TEMPLATE = jinja_environment.get_template('blog.html')

class Blog(webapp2.RequestHandler):
	def get(self):
		blogs = blog.Blog.all()
		data = {
			"message": self.request.get("message"),
			"blogs": blogs,
		}
		self.response.out.write(HTML_TEMPLATE.render(data))
	
