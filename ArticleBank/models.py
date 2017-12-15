from django.db import models

# Create your models here.

# Each model extends models.Model
class ArticlesCategory(models.Model):
    # Simple definition of string field
    CategoryName = models.CharField(max_length=30)
    CreateDate = models.DateField()

class Articles(models.Model):
    Title = models.CharField(max_length=100)
    Description= models.CharField(max_length=250)
    Text = models.CharField(max_length=500)
     # Defines a foreign key to Article Category
    ArticleCategory = models.ForeignKey(ArticlesCategory,on_delete=models.CASCADE)