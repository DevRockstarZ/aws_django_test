from django.http import HttpResponse
import os
import django


TEST_ENV = os.environ.get('TEST_ENV') 

message = "TEST_ENV IS " + str(TEST_ENV) + " Django Version IS " + django.get_version()

def index(request):
    return HttpResponse("PJC is BYUNG-SIN.\n"+message)