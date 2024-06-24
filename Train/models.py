
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class Station(models.Model):
    name = models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True,null=True,blank=True)
    def __str__(self) :
        return f"{self.name}"

class Train(models.Model):
    name = models.CharField(max_length=100)
    schedule = models.TextField()
    image = models.ImageField(upload_to='Train/media/uploads/', blank = True, null = True)
    station=models.ManyToManyField(Station)
    quantity = models.IntegerField(default=0)
    borrowing_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    
    def __str__(self):
        return str(self.name)
    


from django.utils import timezone

class BorrowingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    borrowing_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} borrowed {self.train.title} on {self.borrowing_date}"


class Comment(models.Model):
    train= models.ForeignKey(Train, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # jkhn e ei class er object toiri hobe sei time ta rekhe dibe
    
    def __str__(self):
        return f"Comments by {self.name}"
    
class seat(models.Model):
    train=models.ForeignKey(Train, on_delete=models.CASCADE)
    


