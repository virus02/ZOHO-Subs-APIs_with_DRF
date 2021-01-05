from rest_framework import status
from rest_framework.response import Response
from .constants import ZOHO_GENERATE_TOKEN, ZOHO_REFRESH_TOKEN, ZOHO_CLIENT_ID, ZOHO_CLIENT_SECRET, ZOHO_REDIRECT_URI, ZOHO_ORG_ID
import requests, json
from rest_framework.decorators import api_view

@api_view(['POST'])
def get_auth_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        request.session['config'] = {}
        request.session['config']['code'] = code 
        request.session['config']['orgid'] = ZOHO_ORG_ID
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    return Response({'status': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 

@api_view(['POST'])
def storeauth(request):
    if request.method == 'POST':
        data = {
            'code': request.session['config']['code'],
            'client_id': ZOHO_CLIENT_ID,
            'client_secret': ZOHO_CLIENT_SECRET,
            'redirect_uri': ZOHO_REDIRECT_URI,
            'grant_type': 'authorization_code'
        }

        token = requests.post(ZOHO_GENERATE_TOKEN, data=data)
        token = json.loads(token.text)
        request.session['config']['access_token'] = token['access_token']
        request.session['config']['refresh_token'] = token['refresh_token']
        request.session.modified = True
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    return Response({'status': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def refreshauth(request):
    if request.method == 'POST':
        data = {
            'refresh_token': request.session['config']['refresh_token'],
            'client_id': ZOHO_CLIENT_ID,
            'client_secret': ZOHO_CLIENT_SECRET,
            'redirect_uri': ZOHO_REDIRECT_URI,
            'grant_type': 'refresh_token'
        }
        token = requests.post(ZOHO_REFRESH_TOKEN, data=data)
        token = json.loads(token.text)
        request.session['config']['access_token'] = token['access_token']
        request.session.modified = True
        return Response({'status': 'success'}, status=status.HTTP_200_OK)
    return Response({'status': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)