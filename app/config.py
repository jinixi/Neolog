class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = 'secret'
    DEBUG = True