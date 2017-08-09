from django.shortcuts import render
def post_list(request):
    return render(request, 'blog/index.html', {})

def map(request):
    return render(request, 'blog/map.html', {})

def index(request):
    return render(request, 'blog/index.html', {})

def exp(request):
    return render(request, 'blog/exp.html', {})
