from django.shortcuts import render

# Create your views here.
def index(request):
    """
    generates index page template
    """
    return render(request, 'home/index.html')