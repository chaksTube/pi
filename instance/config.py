# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True # Turns on debugging features in Flask
# BCRYPT_LEVEL = 12 # Configuration for the Flask-Bcrypt extension
MAIL_FROM_EMAIL = "chaks.gautam@gmail.com" # For use in application emails
SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'
STRIPE_API_KEY = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv'