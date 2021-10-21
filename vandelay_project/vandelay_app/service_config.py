
from vandelay_app import config


def facebook_config(service ,group_id ,schema ,table):
    config_values = {
        "service": f"{service}",
        "group_id": f"{group_id}",
        "trust_certificates": "true",
        "config": {
            "schema": f"{schema}",
            "table": f"{table}",
            "fields": ['account_id']
        }
    }

    return config_values

def salesforce_config(service ,group_id ,schema):
    config_values = {
    "service": f"{service}",
    "group_id": f"{group_id}",
    "trust_certificates": "true",
    "config": {
        "schema": f"{schema}"
        }
    }
    return config_values

def s3_config(service ,group_id ,schema, table, external_id, role_arn):
    config_values = {
    "service": f"{service}",
    "group_id": f"{group_id}",
    "trust_certificates": "true",
    "config": {
        "schema": f"{schema}",
        "table": f"{table}",
        "external_id": f"{external_id}",
        "role_arn": f"{role_arn}"
        }
    }

    return config_values

def mysql_config(service ,group_id ,schema_prefix, host, port, user, password, database):

    config_values = {
    "service": f"{service}",
    "group_id": f"{group_id}",
    "trust_certificates": "true",
    "config": {
        "schema_prefix": f"{schema_prefix}",
        "host": f"{host}",
        "port": f"{port}",
        "user": f"{user}",
        "password": f"{password}",
        "database": f"{database}",
            }
    } 
    return config_values