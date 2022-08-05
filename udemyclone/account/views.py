from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
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
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')

        user = User.objects.create_user(username, signupemail, pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, 'your account successfully ceated  !!!')
        

        return redirect('home')

    else:
        return HttpResponse(" 404 Page not found " )




def logIn(request):
    if request.method == 'POST':
        # post the user details 
        username = request.POST['username']
        password= request.POST['pass']
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        messages.success(request, " you are log in succesfully!!!")
        return redirect('home')

    else:
        # Return an 'invalid login' error message.
        messages.error(request, " your input credential are wrong . please try again!!!")
        return redirect('home')

def logOut(request):
    logout(request)
    messages.success(request, " you are log out succesfully!!!")
    return redirect('home')