import os
from dotenv import load_dotenv

load_dotenv()

class DevelopmentConfig:
  SECRET_KEY = os.getenv('SECRET_KEY')
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 465
  MAIL_USERNAME = os.getenv('MAIL')
  MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
  MAIL_USE_TLS = False
  MAIL_USE_SSL = True
  
  
class ProductionConfig:
  pass