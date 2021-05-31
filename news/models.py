from django.db import models

from django.db import models


class Articles(models.Model):
    title = models.CharField('Article name', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    full_text = models.TextField('Example of article')
    date = models.DateTimeField('Release date')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "New"
