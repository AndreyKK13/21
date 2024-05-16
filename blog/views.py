from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


# Create your views here.

def main_veiw(request):
    posts = Post.objects.all()
    for i in posts:
        print(i.title)
    return render(request, 'main_page.html', {'pst': posts})

def post_view(request, pk):
    qs = Post.objects.filter(pk=pk)
    post = qs.first()
    coments = Comment.objects.filter(to_post=post)
    coments = coments.all()
    return render (request, 'one_post.html', {'post': post, 'comments': coments})