from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm, PostForm, commentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import post, comment
from django.contrib.auth.models import Group
# home
def home(request):
    posts = post.objects.all().order_by('-id')
    return render(request, 'blog/home.html', {'posts': posts})

#About
def about(request):
    return render(request, 'blog/about.html')

#Contact
def contact(request):
    return render(request, 'blog/contact.html')

#Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        user=request.user
        posts = post.objects.filter(user=user)
        user = request.user
        full_name = user.get_full_name()
        groups = user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts': posts, 'full_name': full_name, 'groups': groups})
    else:
        messages.success(request, 'Kindly Login first!')
        return HttpResponseRedirect('/login/')
        
    

#logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#Signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'You became an Author!')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group) 
            login(request, user)
            messages.success(request, 'Logged in Succesfully!!')
            return HttpResponseRedirect('/dashboard/')          
    else :
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

#login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
                form = LoginForm(request=request, data=request.POST)
                if form.is_valid():
                    uname = form.cleaned_data['username']
                    upass = form.cleaned_data['password']
                    user = authenticate(username=uname, password=upass)
                    if user is not None:
                        login(request, user)
                        messages.success(request, 'Logged in Succesfully!!')
                        return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')
    
#add post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            image = request.FILES['image']
            title = request.POST['title']
            description = request.POST['description']
            new = post(image=image, title=title, description=description, user=request.user)
            new.save()
            messages.success(request, 'Uploaded!')
            return HttpResponseRedirect('/')
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login')

#update post
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = post.objects.get(pk=id)
            form = PostForm(request.POST, request.FILES, instance=pi)
            if form.is_valid():
                form.save()
            messages.success(request, 'Updated Succesfully!')
            return HttpResponseRedirect('/')
            
        else:
            pi = post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')

#delete post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login')

#comment
def user_comment(request, id):
    pf = post.objects.get(pk=id)
    if request.method == 'POST':
        cf = commentForm(request.POST or None)
        if cf.is_valid():
            content = request.POST.get('content')
            comments = comment.objects.create(posts=pf, user=request.user, content=content)
            comments.save()
            messages.success(request, 'Thanks for commenting!')
            return HttpResponseRedirect('/')
    else:
        cf = commentForm()
        comm = comment.objects.all()
    return render(request, 'blog/comments.html', {'cf': cf, 'post': pf, 'comm': comm})