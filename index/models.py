from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Song(models.Model):
    KEYS = [
        ('Ab', 'Ab'),
        ('A', 'A'),
        ('A#', 'A#'),
        ('Bb', 'Bb'),
        ('H', 'H'),
        ('C', 'C'),
        ('C#', 'C#'),
        ('Db', 'Db'),
        ('D', 'D'),
        ('D#', 'D#'),
        ('Eb', 'Eb'),
        ('E', 'E'),
        ('F', 'F'),
        ('F#', 'F#'),
        ('Gb', 'Gb'),
        ('G', 'G'),
        ('G#', 'G#'),
    ]

    name = models.CharField(help_text="Название песни", max_length=250, null=True)
    media = models.URLField(help_text="Ссылка на видео с YouTube", null=True, blank=True)
    key = models.CharField(help_text="Тональность", max_length=2, choices=KEYS, default="C", null=True, blank=True)
    bpm = models.PositiveIntegerField(help_text="Метроном", validators=[MaxValueValidator(400)], null=True, blank=True)
    tse = models.CharField(help_text="Размер Такта", max_length=5, null=True, blank=True)
    text = models.TextField(help_text="Текст песни", max_length=10000, null=True)
    structure = models.TextField(help_text="Структура", max_length=250, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        permissions = [("can_edit", "Can edit Song"),]
    def __str__(self):
        return self.name

class TypeMinistry(models.Model):
    name = models.CharField(help_text="Название", max_length=250, null=True)

    def __str__(self):
        return self.name

class Ministry(models.Model):
    date = models.DateField(help_text="Дата", null=True, blank=True)
    time = models.TimeField(help_text="Время", null=True, blank=True)
    name = models.CharField(help_text="Название", max_length=250, null=True, blank=True)

    type = models.ForeignKey(TypeMinistry, on_delete=models.CASCADE, help_text="Вид служения", null=True, blank=True)
    description = models.TextField(help_text="Описание", null=True, blank=True)
    bible_passage = models.TextField(help_text="Места из Библии", null=True, blank=True)
    invited_user = models.ManyToManyField(User, help_text="Пригласить пользователя", blank=True)

    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        permissions = [("can_edit", "Can edit Ministry"),]
    def __str__(self):
        return self.name

class SongMinistry(models.Model):
    songs = models.ForeignKey(Song, on_delete=models.CASCADE, help_text="Песни", null=True, blank=True)
    model = models.ForeignKey(Ministry, on_delete=models.CASCADE, help_text="Служение", null=True, blank=True)

    def __str__(self):
        return self.songs.name