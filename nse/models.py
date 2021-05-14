from django.db import models
from django.db.models.base import Model
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date, datetime
from django.utils import timezone
import pytz

utc=pytz.UTC


# now both the datetime objects are aware, and you can compare them


class nifty(models.Model):
    MY_CHOICES = (
        ('BUY', 'BUY'),
        ('SELL', 'SELL'),
    )

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    signal = models.CharField(max_length=20, choices=MY_CHOICES,default="BUY")
    entry = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    advisory = models.TextField(max_length=500)

    # def __str__(self):
    #     return self

class banknifty(models.Model):
    MY_CHOICES = (
        ('BUY', 'BUY'),
        ('SELL', 'SELL'),
    )

    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    signal = models.CharField(max_length=20, choices=MY_CHOICES,default="BUY")
    entry = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    advisory = models.TextField(max_length=500)

    # def __str__(self):
    #     return self


class Customer(models.Model):
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    mobile = PhoneNumberField()
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.name

class members(models.Model):
    MY_CHOICES = (
        ('Trial', 'Trial'),
        ('Premium', 'Premium'),
    )

    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    membership = models.CharField(max_length=20, choices=MY_CHOICES,default="Trial")
    joinedon = models.DateTimeField(default=datetime.now)
    subscriptionenddate = models.DateTimeField(default=timezone.now,null=True)
    status = models.CharField(max_length=15,default="Active")

    def save(self, *args, **kwargs):
        datetime_start = utc.localize(datetime.now()) 
        if(datetime_start > self.subscriptionenddate):
            self.status = "Deactive"
        super(members, self).save(*args, **kwargs)


    # def save(self):
    #     datetime_start = utc.localize(datetime.now()) 
    #     # datetime_end = utc.localize(self.subscriptionenddate) 
    #     if(datetime_start > self.subscriptionenddate):
    #         print(datetime_start)
    #         print(self.subscriptionenddate)
    #         self.status = "Deactive"
    #     # print(datetime_start)
    #     # print(self.subscriptionenddate)

    #     super(members, self).save()