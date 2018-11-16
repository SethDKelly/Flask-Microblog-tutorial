import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object) :
	# Flask and some extensions use the value of the secret key as a cryptographic key
	# useful to generate signatures or tokens
	# used to help prevent Cross-Site Request Forgery (CSRF)
	# first term looks for the value of an environment variable also called SECRET_KEY
	# second term is a hardcoded string
	# Value sourced from an environment variable is preferred
	# if the environment does not define the variable, then the hardcoded string is used instead.
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
	
	# take the location of the applications's database from SQLALCHEMY_DATABASE_URI
	# if taking the database URL from DATABASE_URL environment variable is not defined
	# configure a database named app.df located in the main directory of the application stored in the basedir variable
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.path.join(basedir, 'app.db')
	
	# No need to send a signal to application every time a change is made to DB
	# Set configuration flag to False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
