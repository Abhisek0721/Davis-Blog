from django.shortcuts import render, redirect
from django.core.signing import Signer #for encrypting the password
import json
from .models import Account

signer = Signer(salt='extra') # for encription of password

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, "blog.html")

def login(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_user = Account.objects.filter(username=username).first()
        if (check_user):
            jsonPassword = json.dumps(signer.unsign_object(check_user.password)) #dumps() converts python dictionary into json
            dictPassword = json.loads(jsonPassword) #loads() converts json into python dictionary
            if(password==dictPassword['password']):
                # Login Successful
                return redirect('/')
            else:
                # Wrong Password
                return redirect('/login')
        else:
            # username doesn't exist
            return redirect('/login')
    return render(request, "login.html")

def signup(request):
    if (request.method == "POST"):
        firstName = request.POST.get('fname')
        lastName = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        check_user = Account.objects.filter(username=username).exists()
        if(check_user):
            return redirect('/signup')
        else:
            password = signer.sign_object({'password': password}) #encrypted password
            User = Account.objects.create(firstName=firstName, lastName=lastName, username=username, email=email, password=password)
            User.save()
            return redirect('/login')
    return render(request, "signup.html")

