from django.db import models


# Create your models here.

class News(models.Model):
    head = models.CharField(null=False, blank=True, default=None, max_length=50)
    text = models.TextField(null=False, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.head}"

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class Image(models.Model):
    news = models.ForeignKey(News, null=False, blank=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(null=False, blank=True, default=None, upload_to="static/images")
    is_main = models.BooleanField(null=True, blank=True, default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return f"Image from '{self.news.head}'"

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
