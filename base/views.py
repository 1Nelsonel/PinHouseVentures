from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Property, Agent, Location, Propertycategory, Blog, Comment, User,PropertyComment,MessageAgent
from .forms import CommentForm,PropertyCommentForm ,MessageAgentForm

# Create your views here.


def home(request):
    properties = Property.objects.all()
    blogs = Blog.objects.all()
    agents = User.objects.all()
    context = {'properties': properties, 'blogs': blogs, 'agents': agents}
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
    context = {'agents': agents, 'blogs': blogs}
    return render(request, 'base/agents.html', context)


def agent(request, pk):
    agent = User.objects.get(id=pk)
    properties = Property.objects.filter(agent=agent)
    agents = User.objects.all()
    blogs = Blog.objects.all()

    
    # message an agent
    form = MessageAgentForm()

    if request.method == 'POST':
        form = MessageAgentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.save()
            return redirect("agent", pk=agent.id)
    else:
        reviews = MessageAgentForm()

    context = {'agent': agent, 'properties': properties,'reviews': reviews,
               'agents': agents, 'blogs': blogs}
    return render(request, 'base/agent.html', context)

# def agent(request, pk):
#     agent = User.objects.get(id=pk)
#     properties = Property.objects.filter(agent=agent)
#     agents = User.objects.all()
#     blogs = Blog.objects.all()

#     form = MessageAgentForm()

#     if request.method == 'POST':
#         form = MessageAgentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.agent = agent
#             comment.save()
#             return redirect("agent", pk=agent.id)

#     context = {'agent': agent, 'properties': properties, 'reviews': form,
#                'agents': agents, 'blogs': blogs}
#     return render(request, 'base/agent.html', context)




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
    context = {'properties': properties, 'users': users,
               'categories': categories, 'blogs': blogs}
    return render(request, 'base/listings.html', context)


def listing(request, pk):
    property = Property.objects.get(id=pk)
    properties = Property.objects.all()
    categories = Propertycategory.objects.all()
    blogs = Blog.objects.all()


    reviews = MessageAgentForm()

    # comments
    propertycomments = PropertyComment.objects.all()

    # add comment
    if request.method == 'POST':
        form = PropertyCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.property = property
            comment.save()
            return redirect("listing", pk=property.id)
    else:
        commentform = PropertyCommentForm()

    context = {'property': property,'propertycomments':propertycomments,'commentform':commentform,'reviews': reviews,
               'properties': properties, 'categories': categories, 'blogs': blogs}
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

    # comments
    comments = Comment.objects.all()

    # add comment
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect("blog", pk=blog.id)
    else:
        form = CommentForm()

    context = {'blog': blog, 'blogs': blogs, 'form': form,
               'properties': properties, 'categories': categories, 'comments': comments}
    return render(request, 'base/blog.html', context)


def contact(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'base/contact.html', context)
