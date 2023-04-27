from .models import Articles
from django.forms import ModelForm,Textarea,TextInput,DateInput

class ArticlesForm(ModelForm):
    class Meta:
        model=Articles
        fields=['title','anons','full_text','date']
        
        widgets={
            'title':Textarea(attrs={
                'placeholder':'name of title'
            }),
            'anons':TextInput(attrs={
                'placeholder':'name of anons'
            }),
            'date':DateInput(attrs={
                'placeholder':'name of date'
            }),
            'full_text':Textarea(attrs={
                'placeholder':'name of text'
            })
        }