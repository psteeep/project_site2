from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailNew(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


class NewsUpdateNew(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm


class NewsDeleteNew(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'


def create(request):
    error = ' '
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Incorrect form'

    form = ArticlesForm()
    data = {
        'form': form
    }
    return render(request, 'news/create.html', data)
