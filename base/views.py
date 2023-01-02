from django.shortcuts import render

from .models import Property,Agent,Location,Propertycategory,Blog,Comment

# Create your views here.
def home(request):
    properties = Property.objects.all()
    context = {'properties': properties}
    return render(request, 'base/home.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)

def faqs(request):
    context = {}
    return render(request, 'base/faqs.html', context)

def agents(request):
    agents = Agent.objects.all()
    context = {'agents': agents}
    return render(request, 'base/agents.html', context)

def agent(request, pk):
    agent = Agent.objects.get(id=pk)
    properties = Property.objects.filter(agent=agent)
    agents = Agent.objects.all()
    context = {'agent': agent,'properties':properties,'agents': agents}
    return render(request, 'base/agent.html', context)

def listings(request):
    properties = Property.objects.all()
    agents = Agent.objects.all()
    # property = Property.objects.get(id=pk)
    categories = Propertycategory.objects.all()
    context = {'properties': properties, 'agents': agents,'categories':categories}
    return render(request, 'base/listings.html', context)

def listing(request, pk):
    property = Property.objects.get(id=pk)
    properties = Property.objects.all()
    categories = Propertycategory.objects.all()
    context = {'property': property,'properties': properties,'categories':categories}
    return render(request, 'base/listing.html', context)
 
def blogs(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'base/blogs.html', context)

def blog(request):
    context = {}
    return render(request, 'base/blog.html', context)

def contact(request):
    context = {}
    return render(request, 'base/contact.html', context)