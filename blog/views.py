from django.shortcuts import render
from .models import *

# posts = [
#     {
#         'author': 'Shriyash',
#         'title': 'Django Framework',
#         'content': 'My Django Project List ',
#         'datePosted': 'January 30, 2020'
#     },
#     {
#         'author': 'Ritika',
#         'title': 'php Framework',
#         'content': 'My Php Project List ',
#         'datePosted': 'March 30, 2020'
#     }
# ]


def home(request):
    context = {
        # ? Post is your model this data is directly gonna come from your database
        # 'posts' : posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):

    return render(request, 'blog/about.html', {'title': 'about'})
