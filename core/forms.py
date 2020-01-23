from django import forms

from core.models import Video, Theme


# get options for django object list
def to_options(array):
    options = [('', 'selecione...'), ]

    for element in array:
        if hasattr(element, 'id'):
            el = (element.id, element)
        elif hasattr(element, 'name'):
            el = (element.name, element)
        options.append(el)
    return options


class VideoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    media = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control", "id": "media"}))
    themes = forms.MultipleChoiceField(widget=forms.SelectMultiple(attrs={"class": "form-control select2"}, choices=to_options(Theme.objects.all())))
    descr = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    thumbnail = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Video
        fields = ['title', 'media', 'themes', 'thumbnail',]