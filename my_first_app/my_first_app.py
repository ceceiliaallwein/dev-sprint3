
from flask import Flask
import flask.views
import os
import functools

app = flask.Flask(__name__)

# Don't do this! 
app.secret_key = "bacon"

# this is your database; ceceilia is the key, pw is bacon
users = {'ceceilia':'boom'}

class Main(flask.views.MethodView): 
	def get(self):
		return flask.render_template('index.html')

	def post(self):
		if 'logout' in flask.request.form:
			# pops the username off the session
			# what's the second arguement? password? built-in?  
			flask.session.pop('username', None)
			return flask.redirect(flask.url_for('main'))
		required = ['username','password']
		for r in required:
			if r not in flask.request.form:
				# what is the {0}?
				flask.flash("Error: {0} is required.".format(r))
				# preferred method for sending user to a different path
				return flask.redirect(flask.url_for('main'))
		
		username = flask.request.form['username']
		password = flask.request.form['password']
		# if username is in users (database) and 
		# user at that username has the given (passed through) password 
		if username in users and users[username] == password:
			# if they're logged on then we can store their 
			# username in the session 
			flask.session['username'] = username
		else:
			flask.flash("Username doesn't exist or incorrect password")
		return flask.redirect(flask.url_for('main'))

 

def login_required(method):
	# decorator
	@functools.wraps(method)
	# takes args and keyword args
	def wrapper(*args, **kwargs):
		if 'username' in flask.session:
			return method(*args, **kwargs)
		else:
			flask.flash("A login is required to see the page!")
			return flask.redirect(flask.url_for('main'))
	return wrapper


class Remote(flask.views.MethodView):
	# decorator replaces get or post with the wrapper
	# but the wrapper also knows what the get or post
	# methods are
	# the decorator executes, then it invokes the 
	# method via *args (the method) and **kwargs (what's
	# passed through the methods)

	@login_required
	def get(self):
		return flask.render_template('remote.html')
		
	@login_required
	def post(self):
		result = eval(flask.request.form['expression'])
		flask.flash(result)
		return flask.redirect(flask.url_for('remote'))

		#alternate method?
		#return self.get()

class Music(flask.views.MethodView):
	@login_required
	def get(self):
		songs = os.listdir('static/music')
		return flask.render_template('music.html', songs=songs)



# had View.as_view instead of Main.as_view for a while
# must specify the class as a view 
# clarify what this is actually doing? 
app.add_url_rule('/',view_func=Main.as_view('main'),methods=['GET', 'POST'])
app.add_url_rule('/Remote/',view_func=Remote.as_view('remote'),methods=['GET', 'POST'])
app.add_url_rule('/Music/',view_func=Music.as_view('music'),methods=['GET'])


app.debug = True
app.run()