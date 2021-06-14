from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.conf import settings
from .models import  Join, Contact, Post
from django.contrib import messages
from django.views.generic import ListView


from django.db.models import Q # new
from django.views import generic

from django.utils import timezone
now = timezone.now()

# from project.forms import CommentForm


class  ResultsView(generic.ListView):
    model = Post
    context_object_name ='posts'
    template_name = 'blog.html'

    
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(subject__icontains = query) 
        )
        return object_list
 


def index (request):
    return render(request, 'index.html')


def contact (request):
    submitted = False

    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        submitted = True
        messages.success(request, "Thanks for contacting us")
    return render(request, 'contact_us.html')



def blog (request):
   
    if request.method  == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
       
        print(name, email, subject, message)
        ins = Post(name=name, email=email, subject=subject, message=message)
        ins.save()
        print("the data has been written to db")

        data = Post.objects.all()

        context = {
            "object_list": data
                    }


        # return render_to_response("blog.html", context)
        return render(request,'blog.html', context)

    return render(request, 'blog.html')

def about (request):
    return render(request, 'about.html')

def form (request):

    if request.method  == "POST":
        uname = request.POST['uname']
        pnumber = request.POST['pnumber']
        uemail = request.POST['uemail']
        pword = request.POST['pword']
       
        print(uname, pnumber, uemail, pword)
        ins = Join(uname=uname, pnumber=pnumber, uemail=uemail, pword=pword)
        ins.save()
        print("the data has been written to db")
        return render(request,'index.html',)

    return render(request, 'form.html')


def projects (request):
    return render(request, 'projects.html')