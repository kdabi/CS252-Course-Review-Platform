import datetime
import numpy as np

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

#from ratings.handlers import ratings

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length=10, null=True)
    course_name = models.CharField(max_length=1000, null=True)
    course_preReq = models.CharField(max_length=1000, default='None')
    course_details = models.TextField(default='Not yet decided')
    course_credit = models.CharField(max_length=100, null=True)
#    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def average_rating(self):
#        all_ratings = map(lambda x: float(x.rating), self.review_set.all())
        all_ratings = [float(x.rating) for x in self.review_set.all()]
        return np.mean(all_ratings)

    def __str__(self):
        return self.course_id + ' : ' +  self.course_name

class Faculty(models.Model):
    fac_id = models.CharField(max_length=100, null=True)
    fac_name = models.CharField(max_length=1000, null=True)
    fac_webpage = models.CharField(max_length=1000, default='None')
    fac_data = models.TextField(default='Not yet decided')

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.TextField(null=True)
    summary = models.CharField(max_length=100, default='Summary')
    rating = models.IntegerField(choices=RATING_CHOICES)
#    rating = models.ForeignKey('star_ratings.Rating')
#    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.comment

#class Assignment:

#class Deadline(models.Model):
 #   course = models.ForeignKey(Course, on_delete=models.CASCADE)

#ratings.register(Course)
