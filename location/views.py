from django.shortcuts import render, get_object_or_404, redirect
import http.client, urllib.parse
import json
import os

# Create your views here.
def locateUser(request):
    context = {}
    location = {}
    if 'postal_code' in request.GET:
        postal_code = request.GET['postal_code']
        api_url = http.client.HTTPConnection('api.positionstack.com')
        params = urllib.parse.urlencode({
            'access_key': os.environ['LOCATION_KEY'],
            'query': postal_code,
            'limit': 1
        })
        api_url.request('GET', '/v1/forward?{}'.format(params))
        api_response = api_url.getresponse()
        api_raw_data = api_response.read()
        api_json_data = json.loads(api_raw_data)
        if(len(api_json_data['data'])>0):
            location = api_json_data['data'][0]
            request.session['latitude'] = location['latitude']
            request.session['longitude'] = location['longitude']
            return render(request, 'location.html', {'location': location})
        else:
            return render(request, 'location.html', {'location': None})
        # if location['data'][0]:
        #     request.session['latitude'] = location['data'][0]['latitude']
        #     request.session['longitude'] = location['data'][0]['longitude']
            # save location['data'][0]['latitude'] & location['data'][0]['longitude'] to the session

    return render(request, 'location.html', {'context': context})