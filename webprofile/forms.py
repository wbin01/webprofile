from django import forms
from webprofile.models import Post


class PostForms(forms.ModelForm):
    post_is_published = forms.ChoiceField(
        label='Marcar como publicado',
        choices=(('yes', 'Sim'), ('no', 'Não'),))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

            if 'name="publication_date"' in str(visible):
                # visible.field.widget = forms.HiddenInput()
                visible.field.widget.attrs['readonly'] = 'readonly'

    class Meta:
        model = Post
        exclude = ['user', 'publication_date']  # '__all__'
        labels = {
            'title': 'Título',
            'image': 'Imagem',
            'summary': 'Resumo',
            'content': 'Conteúdo',
            'category': 'Categoria',
        }

        widgets = {
            'summary': forms.Textarea(attrs={'rows': 2}),  # 'cols': 15
            'content': forms.Textarea(attrs={'rows': 10}),
        }

    def clean(self):
        # wayfinder_map_form.cleaned_data['media_file']
        img = self.cleaned_data.get('image')
        errors = {}

        if not img:
            errors['image'] = 'Cadê a imagem pô?!'

        if errors:
            for erro in errors:
                error_message = errors[erro]
                self.add_error(erro, error_message)
        return self.cleaned_data
