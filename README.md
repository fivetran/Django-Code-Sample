# Vandelay Lift
Uplift on the current vandelay demo page. Where do I [recognize this name from](https://seinfeld.fandom.com/wiki/Vandelay_Industries)?

## Templates

*error.html* - serves up the error message.

*pbfcarddemo.html* - serves up the landing page for the PBF demo.

*api_calls.py* - handles the GET request, POST request, DELETE request, and data dump.

*app_funcs.py* - handles getting the connectors, getting the configuration for each service, getting the token for the connect card, getting the page for the connectors.

*config.py* - handles holding the API credentials.

*parameters.py* - handles the different API parameters and route configurations.

*service_config.py* - handles building the config object for each service.

*views.py* - handles rendering the homepage, redirecting to reset demo, redirecting to the connector setup page, etc.

## Getting Started

### Environment
* Make sure you have [brew](https://brew.sh/) installed
* Make sure you have pip installed (comes with [Python 3 installation via Brew](https://docs.python-guide.org/starting/install3/osx/))
* Make sure you have virtualenv installed (`pip install virtualenv`)
* Make sure you have [node](https://nodejs.org/en/) installed

### Python Stuff
* Make sure you're using Python 3 `python --version` or `python3 --version`
* Install a virtual env in the project directory: `python3 -m venv .venv`
* Activate the virtual env: `source .venv/bin/activate`
* Install requirements: `pip install -r requirements.txt`
* Install tailwind dependencies: `python3 manage.py tailwind install`

### Start the Engines
* Open up two terminals and run the following commands in each of them. Make sure you have your virtualenv sourced first!
* Run Django `python3 manage.py runserver`
* Run Tailwind `python3 manage.py tailwind start`

Then, navigate to the server in your browser at localhost:8000 😊

All files will automatically reload when they're changed via browsersync. If you want to adjust the base styling, it's in `vandelay_project/theme/templates`.

Available URLs:
- Vandaley Demo: http://127.0.0.1:8000/vandelay_demo
- Tailwind Demo: http://127.0.0.1:8000/tailwind/