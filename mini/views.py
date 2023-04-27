from django.shortcuts import render,redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


# Create your views here.
def mini_home(request):
    news = Articles.objects.order_by('-date')
    return render(request,'mini/mini_home.html',{'news': news})


def NewsDetail(DetailView):
    model = Articles
    template_name='mini/detail_view.html'
    context_object_name= 'article'
    



def create(request):
    error= ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error='blank is not true'
    form=ArticlesForm()
    data={
        'form':form,
        'error':error
    }
    return render(request , 'mini/create.html',data)