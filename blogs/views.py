from django.shortcuts import render, redirect
from django.core.signing import Signer #for encrypting the password
import json
from .models import Account, Contact


signer = Signer(salt='extra') # for encription of password

# Create your views here.
def home(request):
    if ('auth' in request.session):
        data = {
                "auth" : request.session["auth"],
                "username": request.session["username"], 
                "name" : request.session["fname"]+" "+request.session["lname"],
                "email" : request.session["email"]
            }
        return render(request, 'index.html', data)
    else:
        return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if (request.method == 'POST'):
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        msg = request.POST.get("msg")
        contact = Contact.objects.create(firstName= fname, lastName= lname, email=email, message=msg)
        contact.save()
        return redirect('/')
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
                request.session['auth'] = True
                request.session['username'] = username
                request.session["fname"] = check_user.firstName
                request.session['lname'] = check_user.lastName
                request.session["email"] = check_user.email
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

def logout(request):
    request.session.pop('auth')
    request.session.pop('username')
    request.session.pop("fname")
    request.session.pop('lname')
    request.session.pop("email")
    return redirect('/login')



