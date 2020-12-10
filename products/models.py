from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Pizza(models.Model):
#     name = models.CharField(max_length=30)
#     test_users = models.ManyToManyField(User,related_name='test_users')
#     def __str__(self):
#         return self.name


class Product(models.Model):
    title=models.CharField(max_length = 100)
    url=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)
    #votes_total=models.IntegerField(default=1)
    upvoted_by = models.ManyToManyField(User,related_name='upvoted')
    body=models.TextField()
    image=models.ImageField(default='images/default.png',blank=True)
    icon=models.ImageField(default='images/defaulticon.png',blank=True)
    hunter=models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def pub_date_pretty(self):return self.pub_date.strftime('%b %e %Y')
    def __str__(self): return self.title
    def summary(self): return self.body[:150]+'...'
    def votes_total(self): return self.upvoted_by.count()
