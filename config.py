# config.py

class Config(object):
#Enable Flask's debugging features. Should be False in production
class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_ECHO = True
class ProductionConfig(Config):
	DEBUG = False

app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig
}