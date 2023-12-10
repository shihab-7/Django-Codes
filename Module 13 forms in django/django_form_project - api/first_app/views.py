from django.shortcuts import render
from .forms import contactForm, StudentData , PassworsValidationProject

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

def DjangoForm(request):
    # print(request.POST)
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'djangoform.html', {'form': form})

# if diye validity check na korle django error dito cleaned_data use korte dito na . r cleaned_data use kore html code theke just datagulo filter out kore nite pari

# file input neowar best approach
# def DjangoForm(request):
#     if request.method == 'POST':
#         form = contactForm(request.POST, request.FILES)
#         if form.is_valid():
#             file = form.cleaned_data['file']
#             with open('./first_app/upload/' + file.name, 'wb+') as destination:
#                 for chunk in file.chunks():
#                     destination.write(chunk)
#             print(form.cleaned_data)
#             return render(request , 'djangoform.html', {'form':form})
#     else:
#         form = contactForm()
#     return render(request, 'djangoform.html', {'form':form})

def StudentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request, 'djangoform.html', {'form': form})


# password checker :
def Passwordvalidation(request):
    if request.method == 'POST':
        form = PassworsValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PassworsValidationProject()
    return render(request, 'djangoform.html', {'form': form})