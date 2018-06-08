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
            # 'avatar',
        )

    # def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['avatar'].queryset = Avatar.objects.all()


# class ChangeAvatarForm(forms.ModelForm):
#     def __init__(self, user, *args, **kwargs):
#         super(ChangeAvatarForm, self).__init__(*args, **kwargs)
#         self.fields['avatars'] = forms.ModelChoiceField(
#             queryset=Avatar.objects.all()
#         )
#
#     class Meta:
#         model = Avatar


# class ChangeAvatarForm(forms.ModelChoiceField):
#     def __init__(self, *args, **kwargs):
#         super(ChangeAvatarForm, self).__init__(*args, **kwargs)
#         self.fields['avatars'] = forms.ChoiceField(
#             choices=[(o.id, o.image) for o in
#                      Avatar.objects.all()], widget=forms.RadioSelect()
#         )
