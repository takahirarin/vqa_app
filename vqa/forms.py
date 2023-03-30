from django import forms
from .models import VQA

class VQAForm(forms.ModelForm):
    class Meta:
        model = VQA
        fields = ['image', 'text']

# class TextForm(forms.ModelForm):
#     class Meta:
#         model = VQA
#         fields = ['text']

    def save(self):
        data = self.cleaned_data
        vqa = VQA(image=data['image'], text=data['text'])
        vqa.save()