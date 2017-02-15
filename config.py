# config.py

class Config(object):
	'''
	Common configuration
	'''

class DevelopmentConfig(Config):
	'''
	Development configuration
	'''

	DEBUG = True
	SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
	'''
	Production configuration
	'''
	
	DEBUG = False

app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig
}