from django import forms

from core.models import Video


class VideoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    media = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control", "id": "media"}))
    themes = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={"class": "form-control select2"}))
    descr = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    thumbnail = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Video
        fields = ['title', 'media', 'themes', 'thumbnail',]