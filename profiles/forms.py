from django import forms
from django.contrib.auth.forms import UserChangeForm
from dixit.models import Player


class EditProfileForm(UserChangeForm):
    class Meta:
        model = Player
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'profile_picture',
            # 'avatar'
        )

    # def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['avatar'].queryset = Avatar.objects.all()

