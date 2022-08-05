from django.shortcuts import render


# Create your views here.
def coursehome(request):
   

    return render(request, 'course/coursehome.html', )