from django.forms import ModelForm
from core.models.contato2 import Contato,Anuncie
#itens para a recaptcha
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget



class ContatoForm(ModelForm):
    #captcha
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    class Meta:
        model = Contato
        fields = ["nome", "sobrenome", "email", "telefone", "mensagem"]
        

class AnuncieForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    class Meta:
        model = Anuncie
        fields = '__all__'


    