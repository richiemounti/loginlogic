import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'P@ssw0rd!'
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL') or 'admin@email.com'

    DEMO_PASSWORD = os.environ.get('DEMO_PASSWORD') or 'P@ssw0rd!'
    DEMO_EMAIL = 'demo@email.com'

    DEMO_ADMIN_PASSWORD = os.environ.get('DEMO_ADMIN_PASSWORD') or 'P@ssw0rd!'
    DEMO_ADMIN_EMAIL = 'demo_admin@mail.com'   

    DEBUG = False
    TESTING = False
    FLASK_DEBUG = 0
   

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    


class ProductionConfig(Config):
    DEBUG = False
    


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    CSRF_ENABLED = False
    LOGIN_DISABLED = True
    WTF_CSRF_ENABLED = False


config = {
    'development': 'app.config.DevelopmentConfig',
    'testing': 'app.config.TestingConfig',
    'default': 'app.config.ProductionConfig'
}