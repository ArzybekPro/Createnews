from django.shortcuts import render
# Create your views here.


def index(request):
    context={
        'title':'news about world'
    }
    return render(request, 'main/index.html')

def about(request):
    return render(request,'main/about.html')