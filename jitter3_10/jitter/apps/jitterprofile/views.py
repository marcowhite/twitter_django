from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def jitterprofile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user
    }

    return render(request, 'jitterprofile/jitterprofile.html', context)

@login_required
def follow_jitter(request, username):
    user = get_object_or_404(User, username=username)

    request.user.jitterprofile.follow.add(user.jitterprofile)

    return redirect('jitterprofile', username = username)

@login_required
def unfollow_jitter(request, username):
    user = get_object_or_404(User, username=username)

    request.user.jitterprofile.follow.remove(user.jitterprofile)

    return redirect('jitterprofile', username = username)