import flask
import functools


def login_required(method):
	@functools.wraps(method)
	def wrapper(*args, **kwargs):
		if 'username' in flask.session:
			return method(*args, **kwargs)
		else:
			flask.flash("Badges? You don't need no stinking badges, but you do need a login.")
			return flask.redirect(flask.url_for('main'))
	return wrapper

