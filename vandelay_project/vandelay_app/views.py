from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from vandelay_app import parameters
from vandelay_app import app_funcs
from vandelay_app import api_calls
from http import HTTPStatus
import json
import datetime
import sys

def index(request):
    return render(request,'PbfCardDemo.html')

def tailwind(request):
    return render(request,'tailwind.html')

def redirect_to_index(request):
    return redirect('pbf/')

def close(request):
    auth = request.GET.get('auth')
    path = parameters.FIVETRAN_PATH + '/dashboard/connectors'
    resp = f"<script>window.close();window.opener.location.href='{path}?auth={auth}';</script>"

    return HttpResponse(resp)

@csrf_exempt
def reset(request):
    if not parameters.CONNECTORS_RESET:
        return render(request,'error.html',{'error' : 'CONNECTORS_RESET needs to be set True in order to reset connectors'})

    if request.method == 'POST':
        permissions = app_funcs.checkPermissions()
        
        if not permissions:
            return render(request,'error.html',{'error' : 'Permission failure - failed in checkPermissions()'})
        
        existing_connectors = app_funcs.get_existing_connectors()
        print('existing_connectors ', existing_connectors)

        for connector in existing_connectors:
            print('connector ', connector)

            if connector['service'] in parameters.SERVICES:
                print('Deleting connector ', connector['id'])
                response = app_funcs.delete_connector(connector['id'])

                if response.status_code in(200,201,202):
                    print("connector", connector['id'], " successfully deleted")

    return redirect('/pbf')


def connect_card_process(request):
    service = request.GET.get('service').lower()
    permissions = app_funcs.checkPermissions()

    if not permissions:
        return render(request,'error.html',{'error' : 'Permission failure - failed in checkPermissions()'})
    
    config = app_funcs.getConfig(service)

    response = api_calls.post_url(url=parameters.CONNECTORS_API, values=config)
    print(response.text)

    if response.status_code not in(200,201):
        return render(request,'error.html',{'error' : f'Failed while posting on {parameters.CONNECTORS_API} {response.text}'})
    
    json_data = json.loads(response.text)
    connector_id = json_data['data']['id']
    token = app_funcs.getConnectCardToken(connector_id)
    
    if token == '-no-token-':
        return render(request,'error.html',{'error' : 'token could not be generated, failed in getConnectCardToken'})
    
    redirect_url = parameters.FIVETRAN_PATH + '/dashboard/connectors'
    redirect_url = redirect_url + "?auth=" + token

    main_url = parameters.PBF_CARD_PAGE_BASE
    main_url = main_url + f"?redirect_uri={redirect_url}"
    main_url = main_url + f"&auth={token}"
    
    return redirect(main_url)