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
            'password_confirm': forms.PasswordInput(),
        }

    def clean(self):
        fields = {
            'name': self.cleaned_data.get('name'),
            'email': self.cleaned_data.get('email'),
            'password': self.cleaned_data.get('password'),
            'password_confirm': self.cleaned_data.get('password_confirm')}

        errors = {}

        for key, value in fields.items():
            if not value.strip():
                errors[key] = 'Preencha este campo'

        if any(char.isdigit() for char in fields['name']):
            errors['name'] = 'Não inclua números neste campo'

        if errors:
            for erro in errors:
                error_message = errors[erro]
                self.add_error(erro, error_message)
        return self.cleaned_data


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
