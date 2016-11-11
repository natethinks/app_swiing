from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils.text import slugify

# Create your models here.
#for easier templating I need to create a model field for each section.
#Also need to make links to the event pages in the templating
class Adventure(models.Model):
    title = models.CharField(max_length=200)
    a_slug = models.SlugField(unique=True, help_text="Just type asdf or whatever. This will auto generate upon save")
    header_image = models.ImageField(upload_to='adventure_images/')
    short_description = models.CharField(max_length=500)
    what_you_get = models.TextField(default = 'you get a super awesome trip')
    day_layout = models.TextField(default = 'randominput')
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    inventory = models.IntegerField(default = 0)
    price = models.DecimalField(default = 0000, max_digits=29, decimal_places=2, help_text="Price with decimals. EX 10.00 is $10.00")
    stripe_price = models.IntegerField(default = 0000, help_text="Price without decimals. EX 1059 is $10.59")
    single_payment = models.DecimalField(default = 0000, max_digits=29, decimal_places=2, help_text="One number including cents. EX 1000 is $10.00")
    def __str__(self):
        return self.title
    def is_upcoming(self):
        return timezone.now < self.start_date
    def is_current(self):
        return self.start_date < timezone.now() < self.end_date
    def is_past(self):
        return self.end_date < timezone.now
    def save(self, *args, **kwargs):
        self.a_slug = slugify(self.title) + slugify(self.start_date)
        super(Adventure, self).save(*args, **kwargs)
