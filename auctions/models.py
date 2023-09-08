import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import timedelta, date

class User(AbstractUser):
    def __str__(self):
        return self.username



# Объявление
class Auction(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    wanted = models.DecimalField(max_digits=7, decimal_places=2)

    date_start = models.DateField(auto_now_add=True)
    date_end = models.DateField(default= (datetime.date.today()+timedelta(days=7)), verbose_name='Auction ends at')

    category = models.ForeignKey('Category', null=True, verbose_name='category', on_delete=models.PROTECT)
    owner = models.ForeignKey('User', null=True, on_delete=models.PROTECT)
    active = models.BooleanField(default=True)
    image_url = models.CharField(max_length=500, blank=True)
    watchlist = models.ManyToManyField(User, blank=True, related_name="listingWatchlist")
    high_bid = models.ForeignKey('Bid', null=True, blank=True, on_delete=models.PROTECT)

    winner = models.ManyToManyField(User, blank=True, related_name="winner")

    class Meta:
        verbose_name_plural = "Auction"
        verbose_name = "listing"
        ordering = ["-date_end"]

    def __str__(self):
        return f"{self.title} : {self.wanted}$"


# Категория (Рубрика, прим: книга, дом, личные вещи)
class Category(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
        return self.title



# Ставка
class Bid(models.Model):

    bid = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    user = models.ForeignKey('User', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user}- bid: {self.bid}"



class Comment(models.Model):
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey('User', null=True, on_delete=models.PROTECT)
    auction = models.ForeignKey('Auction', blank=True,on_delete=models.CASCADE, related_name='comments')
    def __str__(self):
        return f"{self.user}: {self.text}. ({self.date})"

    class Meta():
        verbose_name_plural = "Comments"
        verbose_name = "comment"
        ordering = ["auction","date"]



