from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from profiles.forms import EditProfileForm


@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'profiles/profile.html', args)


@login_required
def profile_edit(request):
    if (request.method == 'POST'):
        form = EditProfileForm(request.POST, instance=request.user)
        if (form.is_valid()):
            form.save()
            redirect('profiles')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'profiles/profile_edit.html',
                      args)

