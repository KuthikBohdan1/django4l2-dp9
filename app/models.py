from django.db import models



class LibraryBook(models.Model):
    title = models.CharField()
    author = models.CharField()
    isbn = models.CharField()

    availble = models.BooleanField()


    class Meta:
        