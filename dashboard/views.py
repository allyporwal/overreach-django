from django.shortcuts import render


# Create your views here.
def dashboard(request):
    '''Render the user's dashboard'''

    return render(request, 'home/index.html')
