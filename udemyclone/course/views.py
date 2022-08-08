from pickle import TRUE
from django.shortcuts import render,redirect
from django.contrib import messages 
from course.models import Course, CourseLesson, Video,Purchasecourse




# Create your views here.
def course(request):
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request, 'course/course.html',context)


def coursehome(request,slug):
    course = Course.objects.get(sno =slug)
    course_lessons = CourseLesson.objects.filter(lesson_model = course)
    
    videos = Video.objects.filter(video_course  = course)
    # get the purchase course 
    # uid=Course.objects.get(sno = slug)    
    # purchaged_course=Purchasecourse.objects.get(purchase_course = uid)
    # print(purchaged_course.purchase_id)
    try:
        uid=Course.objects.get(sno = slug)
        purchaged_course=Purchasecourse.objects.get(purchase_course = uid)
   
        
    except:
        purchaged_course=  purchaged_course=Purchasecourse.objects.none()
        pass
    print(purchaged_course)


    context  ={'course': course, 'course_lessons' : course_lessons , 'videos': videos, 'purchase_course': purchaged_course }
   
   
    return render(request, 'course/coursehome.html', context)

def buycourse(request):
    if request.method =="POST":

        course_id= request.POST['courseid'] 
        purchase_course = Course.objects.get(sno = course_id)
       
       
        price=request.POST['price']
        

        purchase = Purchasecourse( purchase_course = purchase_course, purchase_id=True, price=price, )
       
        messages.success(request,'thank you for buying this course ....!!!')
        purchase.save()
       

    return redirect('/')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allcourse=Course.objects.none()
        
    else:
        allcourseTitle=Course.objects.filter(title__icontains=query)
        allcourseAuthor=Course.objects.filter(author__icontains=query)
        allcourseContent =Course.objects.filter(content__icontains=query)
        allcourse=  allcourseTitle.union(allcourseContent, allcourseAuthor)
    if allcourse.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    context={'allcourse': allcourse, 'query': query}
    return render(request, 'course/search.html', context)