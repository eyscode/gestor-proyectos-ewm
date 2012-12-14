from django import forms
from models import Profile

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

class ReunionForm(forms.Form):
    resumen=forms.CharField(
        max_length=100,
        error_messages={'required':'el resumen es necesario'},
        widget=forms.TextInput(attrs={'class':'input-xlarge','style':'height:28px'})
    )
    descripcion=forms.CharField(
        widget=forms.Textarea(attrs={'rows':'8','class':'input-xxlarge'})
    )
    fecha_inicio = forms.DateTimeField(required=False)
    fecha_fin = forms.DateTimeField(required=False)