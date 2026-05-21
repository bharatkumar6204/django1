from django.shortcuts import render

# Create your views here.
def home(request):
    my_dict = {
        'compnay': 'Toyota',
        'owener': 'bharat',
        'cars':['toyota avalon','toyota camry','toyota corolla','toyota fortuner']
    }
    return render(request, 'home.html',my_dict)

def contact(request):
    context = {
        # 'compnay': 'Toyota',
        'owener': 'bharat',
        'cars':['toyota avalon','toyota camry','toyota corolla','toyota fortuner']
    }
    return render(request, 'contact.html',context)