from datetime import datetime
from django import forms
from tempus_dominus.widgets import DatePicker
from webprofile.models import Post


Choice_value = [('1', 'First'), ('2', 'Second'), ('3', 'Third')]


class PostForms(forms.ModelForm):
    publication_date = forms.DateTimeField(
        initial=datetime.now,
        label='Data de publicação',
        disabled=True)
    # post_is_published = forms.BooleanField(
    #     initial=False, label='Marcar como publicado')

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
            'post_is_published': forms.CheckboxInput(),
        }

    # def clean(self):
    #     fields = {
    #         'username': self.cleaned_data.get('username'),
    #         'password': self.cleaned_data.get('password')}
    #
    #     errors = {}
    #
    #     for key, value in fields.items():
    #         if not value.strip():
    #             errors[key] = 'Preencha este campo'
    #
    #     if not fields['username'].isalpha():
    #         errors['name'] = 'Só é permitido letras neste campo'
    #
    #     if errors:
    #         for erro in errors:
    #             error_message = errors[erro]
    #             self.add_error(erro, error_message)
    #     return self.cleaned_data
