db_config ={
    'DEV':{
        'DRIVER':"postgresql",
        'USERNAME':"postgres",
        'PASSWORD':"d37@u!t90",
        'HOST':"localhost",
        'PORT':'5432',
        'DB_NAME':'postgres'
    },
'PROD':{
        'DRIVER':"postgresql",
        'USERNAME':"postgres",
        'PASSWORD':"123Welcome",
        'HOST':"192.168.1.6",
        'PORT':'5432',
        'DB_NAME':'postgres'
    },
'STG':{
        'DRIVER':"postgresql",
        'USERNAME':"postgres",
        'PASSWORD':"123Welcome",
        'HOST':"192.168.1.6",
        'PORT':'5432',
        'DB_NAME':'postgres'
    }
}

class Configuration:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    ENV = 'PROD'
    SQLALCHEMY_DATABASE_URI = db_config[ENV]['DRIVER']+"://"+db_config[ENV]['USERNAME']+":"+db_config[ENV]['PASSWORD']+"@"+db_config[ENV]['HOST']+":"+db_config[ENV]['PORT']+"/"+db_config[ENV]['DB_NAME']
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Configuration):
    DEBUG = True
    TESTING = True
    ENV = 'DEV'

class StagingConfig(Configuration):
    DEBUG = False
    TESTING = True
    ENV = 'STG'

class ProductionConfig(Configuration):
    DEBUG  = False

Config = dict(dev=DevelopmentConfig,stg=StagingConfig,prod=ProductionConfig)