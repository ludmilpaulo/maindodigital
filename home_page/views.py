from django.shortcuts import render , redirect
from django.core.mail import send_mail , BadHeaderError
from django.http import HttpResponse  , HttpResponseRedirect
from .forms import *
from .models import *

from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage,\
                                  PageNotAnInteger
from django.core.mail import send_mail
from django.views.generic import ListView
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity



from django.template import RequestContext
from django.urls import reverse

from taggit.models import Tag



def home(request):
   obj = Carousel.objects.all()
   context = {
        "obj":obj,

   }

   return render(request, "home.html", context)


# Create your views here.

def aboutus_list(request, tag_slug=None):
    about = AboutUs.objects.all()
    why_choose_us = Why_Choose_Us.objects.all()
    chef = Chef.objects.all()
    posts = Post.objects.all()

    context = {
        'about' : about ,
        'why_choose_us' : why_choose_us ,
        'chef' : chef,
        'posts': posts
    }

    return render(request , 'about_us.html' , context)


######################################################################################################
def hire_detail_view(request, id, slug):
    instance = get_object_or_404(Post, id=id,
                                slug=slug,
                                available=True)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            #newdoc = Document(cv = request.FILES['cv'])
            form.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('home:about_us'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()


    context = {
        'object': instance,
        'documents': documents,
        'form': form
    }
    return render(request, "detail.html", context)




######################################################################################################


def send_email(request):
    bg = Contact.objects.all()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']

            # try :
            #     send_mail(subject,message,from_email,['ludmilpaulo@gmail.com'])

            # except BadHeaderError:
            #     return HttpResponse('ivalid header')

            return redirect('home:home_page')


    else:
        form = ContactForm()

    context = {
        'form' : form,
        'bg' : bg

    }

    return render(request , 'about_us.html' , context)



def send_success(request):
    return redirect('contact:send_email')

    #return HttpResponse('thanks you for you email ^_^')


