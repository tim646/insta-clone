from django.db import models

class Post(models.Model):


    class Meta:
        db_table = "posts"