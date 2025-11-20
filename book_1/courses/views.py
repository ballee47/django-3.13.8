from django.shortcuts import render

# Create your views here.
def app1_fnc(request):
    return render(request, 'courses/courses_main.html')