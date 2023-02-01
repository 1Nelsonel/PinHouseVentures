from django.shortcuts import render
from django.db.models import Q
from .models import Property, Agent, Location, Propertycategory, Blog, Comment, User

# Create your views here.


def home(request):
    properties = Property.objects.all()
    blogs = Blog.objects.all()
    agents = User.objects.all()
    context = {'properties': properties, 'blogs': blogs,'agents':agents}
    return render(request, 'base/home.html', context)


def about(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'base/about.html', context)


def faqs(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'base/faqs.html', context)


def agents(request):
    agents = User.objects.all()
    blogs = Blog.objects.all()
    context = {'agents': agents,'blogs': blogs}
    return render(request, 'base/agents.html', context)


def agent(request, pk):
    agent = User.objects.get(id=pk)
    properties = Property.objects.filter(agent=agent)
    agents = User.objects.all()
    blogs = Blog.objects.all()
    context = {'agent': agent, 'properties': properties, 'agents': agents,'blogs': blogs}
    return render(request, 'base/agent.html', context)


def listings(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    properties = Property.objects.filter(
        Q(title__icontains=q) |
        Q(location__name__icontains=q) |
        Q(category__name__icontains=q) |
        Q(agent__username__icontains=q)
    )
    users = User.objects.all()
    blogs = Blog.objects.all()
    categories = Propertycategory.objects.all()
    context = {'properties': properties,'users': users,'categories': categories,'blogs':blogs}
    return render(request, 'base/listings.html', context)


def listing(request, pk):
    property = Property.objects.get(id=pk)
    properties = Property.objects.all()
    categories = Propertycategory.objects.all()
    blogs = Blog.objects.all()
    context = {'property': property,
               'properties': properties, 'categories': categories,'blogs':blogs}
    return render(request, 'base/listing.html', context)


def blogs(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    blogs = Blog.objects.filter(
        Q(title__icontains=q) |
        Q(host__username__icontains=q)
    )

    properties = Property.objects.all()
    categories = Propertycategory.objects.all()
    context = {'blogs': blogs, 'properties': properties,
               'categories': categories}
    return render(request, 'base/blogs.html', context)


def blog(request, pk):
    blog = Blog.objects.get(id=pk)
    blogs = Blog.objects.all()
    properties = Property.objects.all()
    categories = Propertycategory.objects.all()
    context = {'blog': blog, 'blogs': blogs,
               'properties': properties, 'categories': categories}
    return render(request, 'base/blog.html', context)


def contact(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'base/contact.html', context)
