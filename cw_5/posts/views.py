from django.shortcuts import render
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def my_posts(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user)
    else:
        posts = []
    return render(request, 'posts/my_posts.html', {'posts': posts})

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'  # Укажи свой шаблон
    context_object_name = 'posts'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
