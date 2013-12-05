import flask, flask.views
import os
import utils


class Remote(flask.views.MethodView):
	# decorator replaces get or post with the wrapper
	# but the wrapper also knows what the get or post
	# methods are
	# the decorator executes, then it invokes the 
	# method via *args (the method) and **kwargs (what's
	# passed through the methods)

	@utils.login_required
	def get(self):
		return flask.render_template('remote.html')
		
	@utils.login_required
	def post(self):
		result = eval(flask.request.form['expression'])
		flask.flash(result)
		return flask.redirect(flask.url_for('remote'))

		#alternate method?
		#return self.get()
