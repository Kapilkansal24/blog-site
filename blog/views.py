from django.shortcuts import render
from .forms import Addblog
from django.views import View 
from .models import Blogs
from users.models import UserModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BlogSerializer
# Create your views here.
def addblog(request):
    form = Addblog()
    return render(request, "blog.html", {"form" : form})

class afterblog(View):
    def get(self, request):
        form = Addblog()
        return render(request, "blog.html", {'form' : form})

    def post(self, request):
        form = Addblog(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            blog = form.cleaned_data['blog']
            category = form.cleaned_data['category']
            email = request.session.get("email")
            author = UserModel.objects.get(email=email)
            Blogs.objects.create(author=author, title=title, blog=blog, category=category)
            msg = "Successfully Added The Blog"
            return render(request, "index.html", {"msg" : msg})
        else:
            msg = "Invalid Form"
            form = Addblog()
            return render(request, "blog.html", {"msg" : msg, "form" : form}) 

def allblogs(request):
    blog = Blogs.objects.all()
    return render(request, "showblog.html", {"blog" : blog})

def myblog(request):
    email = request.session['email']
    obj = UserModel.objects.get(email=email)
    blog = Blogs.objects.filter(author=obj)
    return render(request, "showblog.html", {"blog" : blog})

class Getapi(APIView):

    def get(self, request):
        print(request.query_params['category'])  
        all_blogs = Blogs.objects.all()
        blogs = BlogSerializer(all_blogs, many=True)
        return Response(blogs.data)

    def post(self, request):
        print(request.data)

def search(request):
    category = request.POST.get("category")
    blog = Blogs.objects.filter(category=category)
    if not blog:
        msg = "No Blog Available For Your Category"
        return render(request, "index.html", {"msg" : msg})
    else:
        return render(request, "showblog.html", {"blog" : blog})

# ?<category> --> category="edu" --> 
