from django.shortcuts import render
from requests import api
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .tasks import Zohosubs
import json

# Create your views here.
@api_view(['GET'])
def get_subs_list(request):

    obj = Zohosubs(request.session['config'])
    subs = obj.list_subs()
    subs = json.loads(subs.text)
    return Response(subs, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_subs_id(request):
    obj = Zohosubs(request.session['config'])
    subs = obj.subs_by_id()
    subs = json.loads(subs.text)
    return Response(subs, status=status.HTTP_200_OK)