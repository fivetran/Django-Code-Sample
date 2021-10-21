import datetime

import environ
env = environ.Env()
# reading .env file
environ.Env.read_env()

KEY = env("64_ENCODE") # also set in the settings.py file

CLOSE_PATH = '/close'
GROUP_ID = 'wad_crewmate' # change this to complete setup
EXTERNAL_ID = GROUP_ID # for AWS S3 connector
GROUP_AUTH = "Basic " + KEY
DEMO_PAGE_TEMPLATE = "PbfCardDemo.html"
DEMO_PATH = "/pbf"
FIVETRAN_PATH = "https://fivetran.com"
PBF_CARD_PAGE_BASE = FIVETRAN_PATH + "/connect-card/setup"
API_BASE = "https://api.fivetran.com/v1"
CONNECTORS_API = API_BASE + "/connectors"
LIST_CONNECTORS_API = API_BASE + "/groups/" + GROUP_ID + "/connectors"
PBF_CARD_TOKEN_SEGMENT = "connect-card-token"
FACEBOOK = "facebook"
S3 = "s3"
SALESFORCE = "salesforce_sandbox"
MYSQL = "mysql"
SERVICES = [FACEBOOK, S3, SALESFORCE, MYSQL] #add your new connector in here
AUTH_COOKIE_EXPIRES_IN = datetime.timedelta(hours=3)
CONNECTORS_RESET = True