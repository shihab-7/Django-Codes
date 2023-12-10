from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label="user name :", help_text="name should be within 70 characters", required = True, widget= forms.Textarea(attrs= {'id':'text_area', 'class':'class1 class2', 'placeholder':'enter your name'}))
    # file = forms.FileField()

    # email = forms.EmailField(label="user email")
    # age = forms.IntegerField() 
    # jodi emon hoy j decide na thake j ki input nibo tobe 
    age = forms.CharField(widget = forms.NumberInput)
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birthdate = forms.DateField()
    # birthdate a calander add kore date chose korar option dite chaaile
    birthdate = forms.CharField(widget= forms.DateInput(attrs= {'type':'date'}))
    # apointment = forms.DateTimeField()
    apointment = forms.CharField(widget= forms.DateTimeInput(attrs= {'type':'datetime-local'}) )
    CHOICES = [('S', 'small'),('M', 'medium'),('L', 'large')]
    # size = forms.ChoiceField(choices= CHOISES)
    size = forms.ChoiceField(choices = CHOICES, widget = forms.RadioSelect)

    MEALS = [("P","pepperoni"),("M","mashrooms"),("B","beef")]
    # pizza = forms.MultipleChoiceField(choices=MEALS)
    pizza = forms.MultipleChoiceField(choices= MEALS, widget= forms.CheckboxSelectMultiple)

    # label= diye essamoto nam deowa jay

# user theke jodi kono rule arop kore input nite chai tahole :

# class StudentData(forms.Form):
#     name = forms.CharField(widget= forms.TextInput)
#     email = forms.CharField(widget= forms.EmailInput)

# # # nam er validity check
# #     def clean_name(self):
# #         valname = self.cleaned_data['name']
# #         if len(valname) < 10:
# #             raise forms.ValidationError("Please enter atleast 10 characters")
# #         return valname

# # # mail er validity check
# #     def clean_email(self):
# #         valemail = self.cleaned_data['email']
# #         if '.com' not in valemail:
# #             raise forms.ValidationError("Please submit valid mail")
# #         return valemail

# # bar bar alada function na banay just akta function diyei sob kaj korte chaile:
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) < 10:
#             raise forms.ValidationError("Please enter atleast 10 characters")
#         if '.com' not in valemail:
#            raise forms.ValidationError("Please submit valid mail")
        
# # super() function diye sob data function a niye ashay r return korte hobe na auto hoye jabe

""" django er default built in data validation checker function use korte
django.core theke import korte hobe validators k tarpor : """

def check(value):
    if len(value) < 20:
        raise forms.ValidationError("Text must be at least 20 characters")

class StudentData(forms.Form):
    # name = forms.CharField(validators= [validators.MaxLengthValidator(10, message="Please enter name below 10 characters")])
    name = forms.CharField(validators= [validators.MinLengthValidator(10, message="Please enter name atleast 10 characters")])
    email = forms.CharField(widget= forms.EmailInput, validators= [validators.EmailValidator(message="Please enter a valid email address")])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(30, message="Age must be under 30"), validators.MinValueValidator(20, message="Age must be above 20")])
    # akhon jodi kono specific type er file input nite chai tobe :
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['png'], message='only can upload pdf files')])

# akhon jodi validation er moddhe nijer banano kono custom function use korte chai
    text = forms.CharField(widget= forms.TextInput,validators=[check])

# password validation checker project:

class PassworsValidationProject(forms.Form):
    name = forms.CharField(widget= forms.TextInput)
    password = forms.CharField(widget= forms.PasswordInput)
    Confirm_password = forms.CharField(widget= forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass= self.cleaned_data['password']
        val_confpass= self.cleaned_data['Confirm_password']
        val_name= self.cleaned_data['name']

        if val_confpass != val_pass:
            raise forms.ValidationError('Passwords doesn\'t match')
        if len(val_name) < 10:
            raise forms.ValidationError('name must be greater than 10 characters')
