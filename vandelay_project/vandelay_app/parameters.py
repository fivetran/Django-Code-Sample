import datetime

CLOSE_PATH = '/close'
GROUP_ID = 'quenched_serotonin'
GROUP_AUTH = "Basic bUN5WnU3VjJJYXdtMXhCVDpyZnphNnVxeWFOdGZMQVdjOXJVMGM3WXRHbjlKU05vdQ=="
DEMO_PAGE_TEMPLATE = "PbfCardDemo.html"
DEMO_PATH = "/vandelay_demo"
FIVETRAN_PATH = "https://fivetran.com"
PBF_CARD_PAGE_BASE = FIVETRAN_PATH + "/connect-card/setup"
API_BASE = "https://api.fivetran.com/v1"
CONNECTORS_API = API_BASE + "/connectors"
LIST_CONNECTORS_API = API_BASE + "/groups/" + GROUP_ID + "/connectors"
PBF_CARD_TOKEN_SEGMENT = "connect-card-token"
FACEBOOK = "facebook"
ADWORDS = "adwords"
SALESFORCE = "salesforce_sandbox"
MYSQL = "mysql"
SERVICES = [FACEBOOK, ADWORDS, SALESFORCE, MYSQL]
AUTH_COOKIE_EXPIRES_IN = datetime.timedelta(hours=3)
CONNECTORS_RESET = True