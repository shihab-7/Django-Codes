from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d ={'author' : 'rahim', 'age' : 20, 'lst' :[1 , 2 , 3] ,'birthday' : datetime.datetime.now(), 'courses':[
        {
            'id' : 1,
            'name' : 'python',
            'fees' : 3000
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fees' : 5000
        }, 
        {
            'id' : 3,
            'name' : 'cpp',
            'fees' : 1000
        }]}
    
    return render(request, 'first_app/home.html' , d) 
# d dictionary ta k akhon html file a jaya {{}} er maddhome access korle webpage a dekha jabe eivabei backend theke data pathano jay etai context in django