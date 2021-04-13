from django.shortcuts import render


# Create your views here.
def memberships(request):
    return render(request, 'memberships/memberships.html')
