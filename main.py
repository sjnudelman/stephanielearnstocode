import webapp2
import controllers.index as index
import controllers.about as about
import controllers.blog as blog
import controllers.write_blog as write_blog
import controllers.archive as archive



app = webapp2.WSGIApplication([
	('/', index.Index),
	('/about', about.About),
	('/blog', blog.Blog),
	('/write_blog', write_blog.WriteBlog),
	('/archive', archive.Archive),
], debug=True)

