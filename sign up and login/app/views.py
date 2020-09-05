from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.crypto import get_random_string
import string
import string, base64, rsa
import random, uuid, hashlib
from cryptography.fernet import Fernet


# Create your views here.
def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method == 'POST':
        
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        uid = request.POST['uid']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        def generate(size):
            #code = ''.join(random.choice(string.letters[26:] + string.digits) for in range(size))               
            code = get_random_string(6, allowed_chars=string.ascii_uppercase + string.digits)
            

        uid = generate(size=6)

        def hash_password(password):
            salt = uuid.uuid4().hex
            return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

        def check_password(pass1, user_password):
            password, salt = hashed_password.split(':')
            return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
 
        pass1 = input('Please enter a password: ')
        hashed_password = hash_password(pass1)
        print('The string to store in the db is: ' + hashed_password)
        old_pass = input('Now please enter the password again to check: ')

        if check_password(hashed_password, pass2):
            print('You entered the right password')
        else:
            print('Passwords do not match')



        if len(pass1) <= 8:
            messages.error(request,"password must contain minimum 8 digits/letters")
            return redirect('/')
    
        

        if not uid.isalnum():
            return HttpResponse("unique id must be alphabets and digits")

        if pass1 != pass2:
            messages.error(request,'password not matched')
            

        myuser = User.objects.create_user(fname,lname,age,uid,email,pass1)
        
        myuser.save()
        return redirect('/')


def handleLogin(request):
    if request.method == 'POST':
        loginemail = request.POST['loginemail']
        loginpassword = request.POST['loginpassword']

        if user is not None:
            
            login(request,user)
            messages.success(requet,'Sucessfully logged-in')
        else:
            messages.error(request,'Invlid Username')
            return redirect('/')


        

