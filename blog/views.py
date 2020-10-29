from django.shortcuts import render

posts = [
    {
        'author': 'Shriyash',
        'title': 'Django Framework',
        'content': 'My Django Project List ',
        'date': 'October 30 2020'
    },
    {
        'author': 'Ritika',
        'title': 'php Framework',
        'content': 'My Php Project List ',
        'date': 'March 30 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):

    return render(request, 'blog/about.html', {'title': 'about'})
