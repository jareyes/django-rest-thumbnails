from django import http

def sendfile(request, thumbnail, **kwargs):
    response = http.HttpResponse()
    response['X-Sendfile'] = thumbnail.url
    del response['Content-Type'] # Let the proxy figure this out
    return response
