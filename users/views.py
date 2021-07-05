from random import randint
from django.http import HttpResponse
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from wsgiref.util import FileWrapper as fw
import csv
from .models import UserModel
from .forms import Login, Signup, GetEmail, Otp, ChangePassword


# Create your views here. 
def about(request):
    """ 
        This is about method for about page
    """
    return render(request, "about.html")

def login(request):
    """
        Method for return login page
    """
    if request.session.get("email"):
        return render(request, "index.html")
    form_ = Login()
    return render(request, "login.html", {'form' : form_}) # form = form_

def afterlogin(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                obj = UserModel.objects.get(email=email)
            except:
                msg = "User Does Not Exists"
                form = Login()
                return render(request, "login.html", {"msg" : msg, "form" : form})
            else:
                if password == obj.password:   
                    request.session['email'] = email   
                    return render(request, "index.html")
                else:
                    msg = "Invalid Password"
                    form = Login()
                    return render(request, "login.html", {"msg" : msg, "form" : form})
        else:
            msg = "INVALID FORM"
            form_ = Login()
            return render(request, "login.html", {"form" : form_, "msg" : msg})
    else:
        return redirect
def signup(request):
    form_ = Signup()
    return render(request, "signup.html", {"form" : form_})

class After_signup(View): # to make this a view class we have to inherit View class
    
    def get(self, request):  # this will call for get method
        return redirect("/users/signup/")
    
    def post(self, request): # this will call for post method
        form = Signup(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            fname = form.cleaned_data['firstname']
            lname = form.cleaned_data['lastname']
            password = form.cleaned_data['password']
            cpassword = form.cleaned_data['cpassword']
            pic = form.cleaned_data['picture']
            if password == cpassword:
                try:
                    UserModel.objects.get(email=email)
                except:
                    UserModel.objects.create(firstname=fname, lastname=lname, email=email, password=password, pic=pic)
                    msg = "Login to Continue...."
                    return render(request, "nav.html", {"msg" : msg})
                else:
                    msg = "User Already Exist...Login To Continue"
                    form = Signup()
                    return render(request, "signup.html", {"msg" : msg, "form" : form})
            else:
                msg = "Incorrect Password"
                form = Signup()
                return render(request, "signup.html", {"msg" : msg, "form" : form})
        else:
            msg = "Invalid Form"
            form = Signup()
            return render(request, "signup.html", {"msg" : msg, "form" : form})

def logout(request):
    del request.session['email']
    return redirect("/")

def profile(request):
    email = request.session['email']
    obj = UserModel.objects.get(email=email)
    username = email.split("@")[0]
    return render(request, "profile.html", {"object" : obj, "username" : username})

def forgot(request):
    form = GetEmail()
    return render(request, "getemail.html", {"form" : form})

def sendmail(request):
    form = GetEmail(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        try:
            UserModel.objects.get(email=email)
        except:
            msg = "EMAIL DOES NOT EXIST!!! TRY AGAIN"
            form = Login()
            return render(request, "login.html", {"form" : form, "msg" : msg})
        else:
            subject = "Mail for forgot password of myblogs.com"
            from_email = "simrangrover5@gmail.com"
            to_email = email
            otp = randint(1000, 9999)
            request.session['otp'] = str(otp)
            message = f"This is mail for forgot password and your otp is {otp}"
            send_mail(subject=subject, message=message, from_email=from_email, recipient_list=[to_email], auth_password=settings.EMAIL_HOST_PASSWORD)
            form = Otp()
            return render(request, "getotp.html", {"form" : form})
    
def checkotp(request):
    if request.method == "POST":
        form = Otp(request.POST)
        if form.is_valid():
            otp = form.cleaned_data['otp']
            actual = request.session.get("otp")
            if otp == actual:
                form = ChangePassword()
                del request.session['otp']
                return render(request, "getpass.html", {'form' : form})
            else:
                del request.session['otp']
                msg = "OTP DOES NOT MATCHED"
                form = Login()
                return render(request, "login.html", {"form" : form, "msg" : msg})
    else:
        return redirect("/users/login/")

def downloadcsv(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="file.csv"'

    writer = csv.writer(response)
    writer.writerow(['Simran', 'Grover', 'Python Developer', 'Data Sciencist'])
    writer.writerow(['Sachin', 'Yadav', 'Data Scientist', 'Hadoop Engineer'])
    return response

def downloadpdf(request):
    f = open("pdffile.pdf", 'rb')
    response = HttpResponse(fw(f), content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="pdffile.pdf"'
    return response

# how we will use our server to use asgi application
# structure for your blog application
# Blog Form --> blog details