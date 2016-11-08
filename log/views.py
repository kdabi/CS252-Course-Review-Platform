#!python
#log/views.py
import sys
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from pexpect import pxssh
from django import forms

from .models import Review, Course, Faculty
from .forms import ReviewForm
from .forms import LoginForm

import datetime

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
def homepage(request):
    return render(request,"homepage.html")

def contact(request):
    return render(request,"contact.html")

def user_login(request):
    username = request.POST.get('username',None)
    psswd = request.POST.get('password',None)
    s = pxssh.pxssh()

    try:
        ## trying doing ssh 
        if s.login ('vyom.cc.iitk.ac.in', username, psswd):
            s.logout()
            print ("Logged Out")
            if username :
                user, created = User.objects.get_or_create(username=username)
                user.set_password('123')
                user.save()
                if created:
                    user.set_password('123')
                    user.save()
            user = authenticate(username=username, password='123')
            login(request, user)
            return render(request,"home.html")
    except:
        ## error if the user is not valid
        # return render( 'login.html')
        # return HttpResponseRedirect('/login/')
        return HttpResponseRedirect('/login_failed/')
        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="login/")
def home(request):
    course_list = Course.objects.order_by('course_id')
    context = {'course_list':course_list}	
    return render(request,"home.html",context)

@login_required(login_url="/login/")
def apphome(request):	
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request,"apphome.html",context)

@login_required(login_url="/login/")
def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)

@login_required(login_url="/login/")
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})

@login_required(login_url="/login/")
def course_list(request):
    course_list = Course.objects.order_by('course_id')
    context = {'course_list':course_list}
    return render(request, 'reviews/course_list.html', context)

@login_required(login_url="/login/")
def faculty_list(request):
    faculty_list = Faculty.objects.order_by('fac_name')
    context = {'faculty_list':faculty_list}
    return render(request, 'reviews/faculty_list.html', context)

@login_required(login_url="/login/")
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'reviews/course_detail.html', {'course': course})

@login_required(login_url="/login/")
def add_review(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.POST:
        form = ReviewForm(request.POST)
    else:
        form = ReviewForm()
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        summary = form.cleaned_data['summary']
#        user_name = form.cleaned_data['user_name']
        user_name = request.user.username
        review = Review()
        review.course = course
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.summary = summary
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:course_detail', args=(course.id,)))

    return render(request, 'reviews/course_detail.html', {'course': course, 'form': form})
