import datetime
import numpy as np

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length=20)
    course_name = models.CharField(max_length=200)
    course_preReq = models.CharField(max_length=100, null=True)
    course_details = models.TextField(null=True)
#    review = models.ForeignKey(Review, on_delete=models.CASCADE)

    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
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
    comment = models.TextField(null=True)
    rating = models.IntegerField(choices=RATING_CHOICES)
#    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.comment

#class Assignment:

#class Deadline(models.Model):
 #   course = models.ForeignKey(Course, on_delete=models.CASCADE)


