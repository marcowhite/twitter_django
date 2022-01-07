from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Jitt


@login_required
def feed(request):
    userids = [request.user.id]

    for jitter in request.user.jitterprofile.follow.all():
        userids.append(jitter.user.id)

    jitts = Jitt.objects.filter(created_by_id__in=userids)

    return render(request, 'feed/feed.html', {'jitts':jitts})
