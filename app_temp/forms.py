from django import forms
from app_temp import Profile

class RegisterForm(forms.Form):
	nombre = forms.CharField()
	apellidos = forms.CharField()
	email = forms.EmailField()
	perfil = forms.ModelChoiceField(queryset=Profile.objects.all(), )
	passw = forms.CharField()
	repassw = forms.CharField()

	def cleaned_repassw(self):
		passw = self.cleaned_data["passw"]
		repassw = self.cleaned_data["repassw"]
		if passw != repassw:
			raise Exception("Los password no coinciden")
		return repassw