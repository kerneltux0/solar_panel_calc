from django.shortcuts import render, get_object_or_404, redirect
import http.client, urllib.parse
import json

# Create your views here.
def locateUser(request):
    location = {}
    if 'postal_code' in request.GET:
        postal_code = request.GET['postal_code']
        api_url = http.client.HTTPConnection('api.positionstack.com')
        params = urllib.parse.urlencode({
            'access_key': 'my key',
            'query': postal_code,
            'limit': 1
        })
        api_url.request('GET', '/v1/forward?{}'.format(params))
        api_response = api_url.getresponse()
        api_data = api_response.read()
        info = json.loads(api_data)
        ## create conditional for invalid zip/postal code
        location = info['data'][0]

    return render(request, 'location.html', {'location': location})