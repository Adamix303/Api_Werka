from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    visited_exhibits = models.ManyToManyField('Exhibit', related_name='visitors', blank=True)
    points = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False) 
    
    def __str__(self):
        return self.username
    
    def calculate_points(self):
        total_points = sum(exhibit.points for exhibit in self.visited_exhibits.all())
        self.points = total_points
        self.save()



class Exhibit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    points = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name


