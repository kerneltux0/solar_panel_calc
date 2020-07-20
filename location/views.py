from django.shortcuts import render, get_object_or_404, redirect
import http.client, urllib.parse
import json

# Create your views here.
def locateUser(request):
    location = {}
    if 'postal_code' in request.GET:
        postal_code = request.GET['postal_code']
        api = http.client.HTTPConnection('api.positionstack.com')
        params = urllib.parse.urlencode({
            'access_key': 'my key',
            'query': postal_code,
            'limit': 1
        })
        api.request('GET', '/v1/forward?{}'.format(params))
        res = api.getresponse()
        apiData = res.read()
        info = json.loads(apiData)
        ## create conditional for invalid zip/postal code
        location = info['data'][0]

    return render(request, 'location.html', {'location': location})