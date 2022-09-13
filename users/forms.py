from datetime import datetime
from django import forms
from tempus_dominus.widgets import DatePicker
from webprofile.models import Post
from users.models import FormUser


class UserForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = FormUser
        fields = '__all__'
        labels = {
            'name': 'Nome',
            'email': 'Email',
            'password': 'Senha',
            'password_confirm': 'Senha novamente',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }


class PostForms(forms.ModelForm):
    publication_date = forms.DateTimeField(
        initial=datetime.now,
        label='Data de publicação',
        disabled=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = '__all__'
        labels = {
            'user': 'Usuário',
            'title': 'Título',
            'image': 'Imagem',
            'summary': 'Resumo',
            'content': 'Conteúdo',
            'category': 'Categoria',
            'post_is_published': 'Marcar como publicado',
        }

        widgets = {
            'publication_date': DatePicker(),
        }
