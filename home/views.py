from django.shortcuts import render


def index(request):
    '''Render the landing page'''
    return render(request, 'home/index.html')


def error_404(request, exception):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')
