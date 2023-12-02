# eita banay nite hobe inner directory te ei views.py banano thake na

# eitar vitor ei oisob function thakbe jeigula website a exicute hoy url a click korle

# akhon jodi akta contact url banay page ta show korte chai tahoile eikhane oi kajer jonno j function ta lagbe oita likhbo

from django.http import HttpResponse

def home(request):
    return HttpResponse("This is home page")

def contact(request):
    return HttpResponse("This is a contact page")

# eikhane httpresponse return korte hoy
# eita k akhon urls.py a jaya import kore nibo