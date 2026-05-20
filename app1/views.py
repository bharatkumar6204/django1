from django.shortcuts import render

# Create your views here.
def home(request):
    context ={
        'name':'bharat','age':23, 'course': 'python full stack' # pass data to template
    }
    return render(request, 'home.html',context)
