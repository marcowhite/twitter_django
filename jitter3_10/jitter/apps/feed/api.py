import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Jitt

@login_required
def api_add_jitt(request):
    data = json.loads(request.body)
    body = data['body']

    jitt = Jitt.objects.create(body=body, created_by=request.user)

    return JsonResponse({'succses': True})