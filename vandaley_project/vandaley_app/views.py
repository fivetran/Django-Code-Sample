from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from vandaley_app import parameters
from vandaley_app import app_funcs
from vandaley_app import api_calls
from http import HTTPStatus
import json
import datetime

def index(request):
    return render(request,'PbfCardDemo.html')

def redirect_to_index(request):
    return redirect('vandelay_demo/')

def close(request):
    auth = request.GET.get('auth')
    path = parameters.FIVETRAN_PATH + parameters.DEMO_PATH
    resp = f"<script>window.close();window.opener.location.href='{path}?auth={auth}';</script>"
    return HttpResponse(resp)

def reset(request):
    if not parameters.CONNECTORS_RESET:
        return render(request,'error.html',{'error' : 'CONNECTORS_RESET needs to be set True in order to reset connectors'})

    if request.method == 'POST':
        permissions = app_funcs.checkPermissions()
        if not permissions:
            return render(request,'error.html',{'error' : 'Permission failure - failed in checkPermissions()'})
        
        existing_connectors = app_funcs.get_existing_connectors()

        for connector in existing_connectors:
            if connector['service'] in parameters.SERVICE:
                response = app_funcs.delete_connector(connector['id'])
                if response.status_code in(200,201,202):
                    print("connector", connector['id'], " successfully deleted") 
    return redirect('vandelay_demo/')


def connect_card_process(request):
    service = request.GET.get('service')
    permissions = app_funcs.checkPermissions()
    if not permissions:
        return render(request,'error.html',{'error' : 'Permission failure - failed in checkPermissions()'})
    
    config = app_funcs.getConfig(service)
    response = api_calls.post_url(url=parameters.CONNECTORS_API, values=config)
    if response.status_code not in(200,201):
        return render(request,'error.html',{'error' : f'Failed while posting on {parameters.CONNECTORS_API}'})
    json_data = json.loads(response.text)
    connector_id = json_data['data']['id']
    token = app_funcs.getConnectCardToken(connector_id)
    if token == '-no-token-':
        return render(request,'error.html',{'error' : 'token could not be generated, failed in getConnectCardToken'})
    
    redirect_url = parameters.FIVETRAN_PATH + parameters.DEMO_PATH + parameters.CLOSE_PATH
    redirect_url = redirect_url + "?auth=" + token

    main_url = parameters.PBF_CARD_PAGE_BASE
    main_url = main_url + f"?redirect_uri={redirectUri}"
    main_url = main_url + f"&auth={token}"
    
    return redirect(main_url)