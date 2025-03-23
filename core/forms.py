from django import forms
from users.models import User


class LoginForms(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterUserForms(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()


class PasswordResetForms(forms.Form):
    email = forms.EmailField(label='Correo')
    new_password = forms.CharField(widget=forms.PasswordInput, label='Nueva contraseña')
    repeat_password = forms.CharField(widget=forms.PasswordInput, label='Repetir nueva contraseña')

    def clean(self):
        super(PasswordResetForms, self).clean()
        email = self.cleaned_data.get('email')
        new_password = self.cleaned_data.get('new_password')
        old_password = self.cleaned_data.get('repeat_password')

        user = User.objects.filter(email=email)
        if new_password != old_password:
            self._errors['new_password'] = self.error_class([
                'Las contraseñas no coinciden'])
        if len(user) == 0:
            self._errors['email'] = self.error_class([
                'No existe el correo en el sistema'])

        return self.cleaned_data
