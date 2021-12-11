from django.http import HttpResponse
from django.http.response import Http404
from django.core import serializers
from Interactions.models import Interaction
from django.views.decorators.csrf import csrf_exempt


import json


@csrf_exempt
def add_interaction(request):
    body = request.body
    body = json.loads(body)
    response = body
    try:
        interaction = Interaction(            
            sender = body['sender'], 
            recipient = body['recipient'], 
            message = body['message']
        )
        interaction.save()
        server_data = {
        "message": f"Interaction between {body['sender']} and {body['recipient']} was saved successfully",
        "status": 200
         }
    except Exception as e:
        print(e)
        server_data = {
        "message": f"Interaction between {body['sender']} and {body['recipient']} was not saved successfully",
        "status": 500
         }

    response['server_data'] = server_data
    response = json.dumps(response)
    return HttpResponse(response)

def get_interaction(request):

    if request.method != 'GET':
        return Http404("Not a valid request")
    else:
        response = Interaction.objects.all()
        response = serializers.serialize('json', response)
        return HttpResponse(response)
