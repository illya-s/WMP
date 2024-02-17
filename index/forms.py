from django.forms import forms, ModelForm
from .models import Song, Ministry, SongMinistry


class SongForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.help_text
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    class Meta:
        model = Song
        fields = ["name", "media", "key", "bpm", "tse", "text", "structure", "user"]

class MinistrysForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.help_text
    class Meta:
        model = Ministry
        fields = ["date", "time", "name", "type", "description", "bible_passage", "invited_user"]

class SongMinistryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.help_text
    class Meta:
        model = SongMinistry
        fields = ["songs", "model"]