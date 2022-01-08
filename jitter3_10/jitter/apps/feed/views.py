from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
from .models import Jitt


@login_required
def feed(request):
    userids = [request.user.id]

    for jitter in request.user.jitterprofile.follow.all():
        userids.append(jitter.user.id)

    jitts = Jitt.objects.filter(created_by_id__in=userids)

    for jitt in jitts:
        likes = jitt.likes.filter(created_by_id=request.user.id)
        if likes.count()>0:
            jitt.liked = True
        else:
            jitt.liked = False

    return render(request, 'feed/feed.html', {'jitts':jitts})

@login_required
def search(request):
    query = request.GET.get('query','')

    if len(query)>0:
        jitters = User.objects.filter(username__icontains=query)
    else:
        jitters = []

    context = {
        'query':query,
        'jitters': jitters
    }
    return render(request, 'feed/search.html', context)