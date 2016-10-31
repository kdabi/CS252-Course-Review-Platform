#!python
#log/views.py
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from pexpect import pxssh

from .models import Review, Course
from .forms import ReviewForm

import datetime

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    s = pxssh.pxssh()
    try:
        if s.login ('vyom.cc.iitk.ac.in', username, psswd):
            user = User.objects.create_user(username, password='password')
            # auth.login(request, user)
            return HttpResponseRedirect('home.html')
    except:
        return HttpResponseRedirect('home.html')


@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")

@login_required(login_url="/login/")
def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)

@login_required(login_url="/login/")
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})

@login_required(login_url="/login/")
def course_list(request):
    course_list = Course.objects.order_by('-course_id')
    context = {'course_list':course_list}
    return render(request, 'reviews/course_list.html', context)

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
        user_name = form.cleaned_data['user_name']
        user_name = request.user.user_name
        review = Review()
        review.course = course
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:course_detail', args=(course.id,)))

    return render(request, 'reviews/course_detail.html', {'course': course, 'form': form})
