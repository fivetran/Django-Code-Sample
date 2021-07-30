import environ
env = environ.Env()
# reading .env file
environ.Env.read_env()

# Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
API_KEY = env("API_KEY")
API_SECRET = env("API_SECRET")