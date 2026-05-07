from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
class Publisher(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250, blank=True)     #null=false so no subtitle would be stored in the db as "" to have only 1 state representing an empty subtitle instead of both "" and None
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    published_date = models.DateField()
    distribution_cost = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        if not self.subtitle:   #empty string is falsy
            return self.title
        
        return f"{self.title}: {self.subtitle}"