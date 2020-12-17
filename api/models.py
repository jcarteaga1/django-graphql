from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, blank=False)

class Booking(models.Model):
    people = models.ManyToManyField(Person, related_name="bookings", blank=False)
