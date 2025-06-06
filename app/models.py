from django.db import models



class LibraryBook(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    isbn = models.CharField(max_length=256, unique=True)

    availble = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
    

    class Meta:
        # verbose_name = "author"
        # verbose_name_plural = "libraryBooks"
        ordering = ["author"] #сортування
