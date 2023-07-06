from django.db import models

# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=100, verbose_name="Жанылык")
    text = models.TextField(verbose_name="Жанылык жонундо")
    image = models.ImageField(upload_to='images')
    create_date = models.DateTimeField(verbose_name="Тузулган убакыты")
    news_view = models.IntegerField(default=0, verbose_name="Коруучулар")

    class Meta:
        verbose_name = "Жанылык"
        verbose_name_plural = "Жанылыктар"
        ordering = ('-create_date',)

    def __str__(self):
        return f'{self.title} - {self.create_date}'


