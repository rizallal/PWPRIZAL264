class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/project_pwp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False