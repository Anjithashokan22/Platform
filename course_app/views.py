from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from credentials.models import User_detail
from course_app.models import Location,Course
from django.conf import settings
from urllib.parse import urljoin
from datetime import datetime

name='course_app'
# Create your views here.
def index(request):
    return HttpResponse("hello")

def my_view(request):
    locations = Location.objects.all()
    user_detail = User_detail.objects.get(user=request.user) 
    interests = user_detail.interests.all()
    user_interests = [] 
    for interest in interests:
        user_interests.append(interest) 
    unique_courses = set(Course.objects.filter(course_interest__in=user_interests))
    return render(request, 'test.html', {'unique_courses': unique_courses,'locations':locations})

def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    skills=course.course_skills.split(",")
    current_date = datetime.now().date()
    difference=course.course_date-current_date
    var=course.course_date.strftime('%A, %B %d, %Y')  
    return render(request, 'detail.html', {'course': course, 'var':var,'difference':difference, 'skills':skills})

