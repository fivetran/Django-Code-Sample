from vandaley_app import service_config
from vandaley_app import parameters
from vandaley_app import api_calls
import json

def checkPermissions():
    token =  getToken()
    if token not in ('1k56c2c4xlti6_acc','shipping_auditorium'):
        return False
    return True

def getToken():
    return '1k56c2c4xlti6_acc'

def get_existing_connectors():
    response = api_calls.get_url(parameters.LIST_CONNECTORS_API)
    if response.status_code == 200:
        json_data = json.loads(response.text)
        return json_data['data']['items']
    else:
        return []

def getConfig(service):
    config = None
    if service == parameters.FACEBOOK:
        config = service_config.facebook_config(parameters.FACEBOOK, parameters.GROUP_ID,"facebook","table")
    elif service == parameters.SALESFORCE:
        config = service_config.salesforce_config(parameters.SALESFORCE, parameters.GROUP_ID, "salesforce_sandbox")
    elif service == parameters.ADWORDS:
        config = service_config.adwords_config(parameters.ADWORDS, parameters.GROUP_ID, "adwords","table","",['Date'])
    elif service == parameters.MYSQL:
        config = service_config.mysql_config(parameters.MYSQL, parameters.GROUP_ID, "mysql", "", "", "", "", "")
    
    return config

def getConnectCardToken(connector_id):
    segments = [parameters.CONNECTORS_API, connector_id,parameters.PBF_CARD_TOKEN_SEGMENT]
    url = '/'.join(segments)
    response = api_calls.post_url(url=url)
    json_data = json.loads(response.text)
    if response.status_code not in(200,201):
        return '-no-token-'
    return json_data['token']

def getPage(existing_connectors):
    
    context = dict()
    for service in parameters.SERVICES:
        for connector in existingConnectors:
            if service == connector['service']:
                key = f"{service}Disabled"
                context[key] = "disabled"
    return context
            

def delete_connector(connector_id):
    url = parameters.CONNECTORS_API + "/" + str(connector_id)
    return api_calls.delete_url(url)