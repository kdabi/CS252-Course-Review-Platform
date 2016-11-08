import datetime
import numpy as np

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

#from ratings.handlers import ratings
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length=10, null=True)
    course_name = models.CharField(max_length=1000, null=True)
    course_preReq = models.CharField(max_length=1000, default='None')
    course_details = models.TextField(default='Not yet decided')
    course_credit = models.CharField(max_length=100, null=True)
#    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    ratings = GenericRelation(Rating, related_query_name='course_name')

    def average_rating(self):
#        all_ratings = map(lambda x: float(x.rating), self.review_set.all())
        all_ratings = [float(x.rating) for x in self.review_set.all()]
        return np.mean(all_ratings)

    def __str__(self):
        return self.course_id + ' : ' +  self.course_name

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
    comment = models.TextField(default='No Comments')
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
