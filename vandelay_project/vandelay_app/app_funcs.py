from vandelay_app import service_config
from vandelay_app import parameters
from vandelay_app import api_calls
import json
import sys

def checkPermissions():
    token =  getToken()
    if token not in ('1k56c2c4xlti6_acc', 'wad_crewmate'):
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
    elif service == parameters.S3:
        config = service_config.s3_config(parameters.S3, parameters.GROUP_ID, "s3", "table_name", parameters.EXTERNAL_ID, "")
    elif service == parameters.MYSQL:
        config = service_config.mysql_config(parameters.MYSQL, parameters.GROUP_ID, "mysql", "", "", "", "", "")
    elif service == parameters.ORACLE:
        config = service_config.oracle_config(parameters.ORACLE, parameters.GROUP_ID, "test_oracle", "", "", "", "", "")
    elif service == parameters.GCF:
        config = service_config.gcf_config(parameters.GCF, parameters.GROUP_ID, "schema_name", "", "")
    return config

def getConnectCardToken(connector_id):
    segments = [parameters.CONNECTORS_API, connector_id,parameters.PBF_CARD_TOKEN_SEGMENT]
    url = '/'.join(segments)
    print(f"calling url {url}")
    response = api_calls.post_url(url=url,values=None)
    json_data = json.loads(response.text)
    if response.status_code not in(200,201):
        return '-no-token-'
    return json_data['token']

def getPage(existing_connectors):
    
    context = dict()
    for service in parameters.SERVICES:
        for connector in existing_connectors:
            if service == connector['service']:
                key = f"{service}Disabled"
                context[key] = "disabled"
    return context
            

def delete_connector(connector_id):
    url = parameters.CONNECTORS_API + "/" + str(connector_id)
    return api_calls.delete_url(url=url,values=None)