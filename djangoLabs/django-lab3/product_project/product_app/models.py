from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=20)
    # category = models.CharField(max_length=20)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} "
