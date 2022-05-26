from django.shortcuts import render
from . models import Course


def courses_list(request):
    courses = Course.objects.all().order_by('-date')

    context = {
        'courses': courses
    }

    return render(request, "courses.html", context)
