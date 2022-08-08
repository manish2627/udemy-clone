from udemy.models import Contact
from django.shortcuts import render,HttpResponse
from course.models import Course
from django.contrib import messages 
from math import ceil 

# Create your views here.
def home(request):
    courses = Course.objects.all()
    n= len(courses)
    nSlides= n//4 + ceil((n/4) + (n//4))
    context = {"courses": courses, 'range':range(0,nSlides)}
    return render(request, 'home/home.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content= request.POST['content']
        if len(name)<2 or len(email)<5 or len(phone) <10 or len(content) <5:
             messages.error(request, 'Please enter the correct details !!!')
             messages.error(request, 'Please enter the correct details !!!')
        else:
            contact = Contact(name=name, email=email, phone= phone, content= content)
            contact.save()
            messages.success(request, 'your massage has been sent succesfully  !!!')
        
    return render(request, 'home/contact.html') 

def about(request):
    return render(request, 'home/aboutme.html')
    

