from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from profiles.forms import EditProfileForm


@login_required
def profile(request):
    return render(request, 'profiles/profile.html', {'user': request.user})


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    form = EditProfileForm(instance=request.user)
    return render(request, 'profiles/profile_edit.html', {'form': form})
