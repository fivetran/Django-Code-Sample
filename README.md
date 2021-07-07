# vandelay_lift
Uplift on the current vandelay demo page

## Templates
*error.html* - serves up the error message.

*pbfcarddemo.html* - serves up the landing page for the PBF demo.

*api_calls.py* - handles the GET request, POST request, DELETE request, and data dump.

*app_funcs.py* - handles getting the connectors, getting the configuration for each service, getting the token for the connect card, getting the page for the connectors.

*config.py* - handles holding the API credentials.

*parameters.py* - handles the different API parameters and route configurations.

*service_config.py* - handles building the config object for each service.

*views.py* - handles rendering the homepage, redirecting to reset demo, redirecting to the connector setup page, etc.