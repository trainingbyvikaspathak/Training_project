from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import os
from django.conf import settings

def index(request):
    return render(request,'index.html')
    file = open(os.path.join(settings.BASE_DIR, 'persons.json'))
    person_details = json.load(file) 
    return JsonResponse(person_details)

def search(request):
    id = request.GET.get('id',0)
    if id:
        file = open(os.path.join(settings.BASE_DIR, 'persons.json'))
        person_details = json.load(file) 
        for person in person_details:
            if id in person_details[person]:
                return JsonResponse(person)
                break
        else:
            return HttpResponse('Sorry ! Given ID not exist in our Record')

    else:
        return HttpResponse("Please Provide ID of person")

