
from django.shortcuts import render,redirect,HttpResponse
# from django.contrib.auth.models import User
from account.models import User
from django.contrib import messages 
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.
def signUp(request):
    if request.method == 'POST':
        # post the user details 
        username = request.POST['username']
        fname = request.POST['fname']
        lname= request.POST['lname']
        signupemail = request.POST['signupemail']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        print(username, fname, lname,signupemail,pass1,pass2)
        # check user length 
        # if len(username)<10:
        #     messages.error(request, " Your user name must be under 10 characters")
        #     return redirect('home')
        # check for user name 
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        # check for password match 
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        # creating user
        try:
            myuser=User.objects.get(user=username)
            myuser2=User.objects.get(email=signupemail)
            messages.error(request,'The username/email you entered has already been taken. Please try another username/email')
            return redirect('/') 
        except:
            myuser = User(user=username,email=signupemail,password=pass1)
            myuser.save()
            messages.success(request,'Account created successfully  Please check your mail to conform your email')
            return redirect('/') 


def logIn(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        try:
            user=User.objects.get(email=email,password=password)
            if user.mail_validate==0:
                # token=send_verification_link(user)
                messages.warning(request,'Please check your mail to conform your email')
                return redirect('/')
            else:
                request.session['user']=user.user
                request.session['uid']=user.id
                messages.success(request,'Login Successfullly')
                return redirect('/')
        except:
            messages.error(request,'invalid credencials')
            return redirect('/')


def logOut(request):
    request.session.flush()
    messages.success(request,'you are loged out!!!')
    return redirect('/')