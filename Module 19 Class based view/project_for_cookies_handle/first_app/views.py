from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse

# Create your views here.

# django cookies setup

def home(request):
    response = render(request, 'home.html')
   # response.set_cookie('name', 'rahim') # eita dictionary hishebe thake pore context hishebe pass kore render kora jay
    # akhon cookie kono particuler time er jonno store korte chaile
    # response.set_cookie('name', 'rahim', max_age= 60*3) eita 180 second por auto remove hoye jabe browser theke
    # akhon jodi kew koyekdin er jonno store korte ba akta fixed deadline er jonno store korte chay tobe

    response.set_cookie('name', 'rahim', expires= datetime.utcnow()+timedelta(days = 7))
    # ei cookie ta 7 din por auto remove hoye jabe browser theke

    return response


# akhon set kora cookie er data dekhte chaile akata alada html template diye render korte hobe
def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request, 'get_cookie.html', {'name': name})


# jodi chai j kono specefic url visit korle cookie delete hoye jabe tobe oitar joono o alada akta html template render kore oitar url setup kore nite hobe
def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response


# django session setup

# user ei url visit korle akta session create hoye jabe jetate amra backend theke akta dictionary pass kore dissi
def set_session(request):
    data = {
        'name': 'rahim',
        'age': 20,
        'language': 'en'
    }
    # akhon jodi terminal a dekhte chai j session ta kotodiner jonno set hoilo by default tahole .get_session_cookie_age() ei function ta use korte hoy
    print(request.session.get_session_cookie_age()) 
    # ei function ta seconds format a value return kore.
    print(request.session.get_expiry_date())
    # ei function ta data return kore direct
    request.session.update(data)
    return render(request, 'home.html')

# akhon set kora session ta dekhte chaile
# def get_session(request):
#     name = request.session.get('name', 'this text replaced for delation')
#     age = request.session.get('age')
#     language = request.session.get('language')
#     return render(request, 'get_cookie.html', {'name': name, 'age': age, 'language':language})
# new template na banay direct get_cooki template ei session er data render kora hoise

def delete_session(request):
    # j kono akta specefic session data jodi delete korte chai
    # del request.session['name']

    # akhon full session tai database theke delete kore dite chaile flush() use korte hoy
    request.session.flush()
    return render(request, 'delete_cookie.html')

# ei function ta diye user website a akta fixed time porjonto kono activity show na korle auto session remove hoye jabe
def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name', 'this text replaced for delation')
        age = request.session.get('age')
        language = request.session.get('language')
        request.session.modified = True
        return render(request, 'get_cookie.html', {'name': name, 'age': age, 'language':language})
    else:
        return HttpResponse("Session Expired")