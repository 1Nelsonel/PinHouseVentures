from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)

def faqs(request):
    context = {}
    return render(request, 'base/faqs.html', context)

def agents(request):
    context = {}
    return render(request, 'base/agents.html', context)

def agent(request):
    context = {}
    return render(request, 'base/agent.html', context)

def listings(request):
    context = {}
    return render(request, 'base/listings.html', context)

def listing(request):
    context = {}
    return render(request, 'base/listing.html', context)
 
def blogs(request):
    context = {}
    return render(request, 'base/blogs.html', context)

def blog(request):
    context = {}
    return render(request, 'base/blog.html', context)

def contact(request):
    context = {}
    return render(request, 'base/contact.html', context)