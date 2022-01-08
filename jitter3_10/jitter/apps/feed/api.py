import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Jitt, Like

@login_required
def api_add_jitt(request):
    data = json.loads(request.body)
    body = data['body']

    jitt = Jitt.objects.create(body=body, created_by=request.user)

    return JsonResponse({'succses': True})
@login_required
def api_add_like(request):
    data = json.loads(request.body)
    jitt_id = data['jitt_id']

    if not Like.objects.filter(jitt_id=jitt_id).filter(created_by=request.user).exists():
        like = Like.objects.create(jitt_id=jitt_id,created_by=request.user)

    return JsonResponse({'succses': True})