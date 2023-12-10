from django.shortcuts import render

# Create your views here.

def data(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        # method a post er jaygay jodi get use kori tobe link a sob data dekha jay ja sensitive data expose kore dey
        email = request.POST.get('email')
        select= request.POST.get('select')
        return render(request, 'data.html', {'name': name, 'email': email, 'select': select})
    else:
        return render(request, 'data.html')

def form(request):
    # print(request.POST)
    return render(request, 'form.html')