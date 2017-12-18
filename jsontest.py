import json
from django.http import HttpResponse

def foo_view(request):
    data = {'name':'xlaoshi','web':'django'}
    return HttpResponse(json.dumps(data),content_type='application/json')
    
foo_view()