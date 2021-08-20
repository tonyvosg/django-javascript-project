from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {'author':'CoreyMS', 'title':'Blog Post 1', 'content':'first post content', 'date_posted':'Aug 27m 2018'}, 
    {'author':'CoreyMS', 'title':'Blog Post 1', 'content':'first post content', 'date_posted':'Aug 27m 2018'},
    {'author':'CoreyMS', 'title':'Blog Post 1', 'content':'first post content', 'date_posted':'Aug 27m 2018'},
    {'author':'CoreyMS', 'title':'Blog Post 1', 'content':'first post content', 'date_posted':'Aug 27m 2018'}, 
]
# Create your views here.
def home(request):
    return render(request, 'blog/home.html')
def about(request):
    return render(request, 'blog/about.html')
