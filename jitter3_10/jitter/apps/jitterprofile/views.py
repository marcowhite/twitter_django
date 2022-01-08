from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import JitterProfileForm

# Create your views here.

def jitterprofile(request, username):
    user = get_object_or_404(User, username=username)
    jitts = user.jitts.all()

    for jitt in jitts:
        likes = jitt.likes.filter(created_by_id=request.user.id)
        if likes.count()>0:
            jitt.liked = True
        else:
            jitt.liked = False
    context = {
        'user': user,
        'jitts': jitts
    }

    return render(request, 'jitterprofile/jitterprofile.html', context)
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = JitterProfileForm(request.POST, request.FILES, instance=request.user.jitterprofile)
        if form.is_valid():
            form.save()
            return redirect('jitterprofile', username = request.user.username)
    else:
        form = JitterProfileForm(instance=request.user.jitterprofile)
    context={
        'user': request.user,
        'form': form
    }
    return render(request, 'jitterprofile/edit_profile.html', context)

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

def followers(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'jitterprofile/followers.html', {'user': user})
def follows(request, username):
    user = get_object_or_404(User, username=username)

    return render(request, 'jitterprofile/follows.html', {'user': user})