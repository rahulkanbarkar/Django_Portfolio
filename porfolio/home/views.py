from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("<html> head this is my homepage(/)")
      context={'name':'Rahul','course':'Django'}
      return render(request,'home.html', context)

def about(request):
        # return HttpResponse("this is my about page(/about)")
        return render(request,'about.html')


def project(request):
        # return HttpResponse("this is my project page(/project)")
        return render(request,'project.html')


def contact(request):
        if request.method=="POST":
                print ("this is post")
                name=request.POST['name']
                email=request.POST['email']
                phone=request.POST['phone']
                desc=request.POST['desc']
                print(name, email, phone,desc)
                ins=Contact(name=name, email=email, phone=phone, desc=desc)
                ins.save()
                print("the data has been written to the db")
        # return HttpResponse("this is my contact page(/contact)")
        return render(request,'contact.html')
