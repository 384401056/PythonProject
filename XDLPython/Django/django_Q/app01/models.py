from django.db import models

# Create your models here.

class BookType(models.Model):
    caption = models.CharField(max_length=64)


class Book(models.Model):
    name = models.CharField(max_length=64)
    page = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pubdate = models.DateField()
    book_type = models.ForeignKey('BookType')

    def __str__(self):
        return '%s' % self.name