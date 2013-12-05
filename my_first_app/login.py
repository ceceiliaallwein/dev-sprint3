
import flask, flask.views

# this is your database; ceceilia is the key, pw is bacon
users = {'ceceilia':'boom'}


class Login(flask.views.MethodView): 
	def get(self):
		return flask.render_template('login.html')

	def post(self):
		if 'logout' in flask.request.form:
			# pops the username off the session
			# what's the second arguement? password? built-in?  
			flask.session.pop('username', None)
			return flask.redirect(flask.url_for('login'))
		required = ['username','password']
		for r in required:
			if r not in flask.request.form:
				# what is the {0}?
				flask.flash("Error: {0} is required.".format(r))
				# preferred method for sending user to a different path
				return flask.redirect(flask.url_for('login'))
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
		return flask.redirect(flask.url_for('login'))

