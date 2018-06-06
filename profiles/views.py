from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from profiles.forms import EditProfileForm


@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'profiles/profile.html', args)


@login_required
def profile_edit(request):
    if (request.method == 'POST'):
        form = EditProfileForm(request.POST)
        if (form.is_valid()):
            form.save()
            redirect('profiles')
    else:
        form = EditProfileForm()
        args = {'form': form}
        return render(request, 'profiles/profile_edit.html',
                      args)
