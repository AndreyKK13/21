from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.forms import PostForm, ComentForm
from blog.models import Post, Comment, Quiz


# Create your views here.

def main_veiw(request):
    posts = Post.objects.all()
    for i in posts:
        print(i.title)
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            print(data)
            form = PostForm(data)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                post_id = post.id
                return redirect(f'/post/{post_id}/')
        else:
            form = PostForm
        form = PostForm()
        return render(request, 'main_page.html', {'pst': posts, 'form':form, 'user': request.user})
    else:
        return render(request, 'main_page.html', {'pst': posts, 'user': request.user})


def commentForm(data):
    pass



def post_view(request, pk, comment=None):
    qs = Post.objects.filter(pk=pk)
    post = qs.first()
    coments = Comment.objects.filter(to_post=post)
    coments = coments.all()
    form = ComentForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            print(data)
            form = ComentForm(data)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.to_post = post
                comment.save()
        return render(request, 'main_page.html', {'post': post, 'form':form, 'user': request.user})
    return render(request, 'one_post.html', {'post': post, 'comments': coments})
def quiz_list(request,):
    quizes = Quiz.objects.all()
    return render(request, 'quizes_list.html', {'quizes':quizes})

def quiz_detail(request, pk):
    quiz = Quiz.objects.filter(id=pk).first()
    quiz.questions = quiz.question_set.all()
    for questions in quiz.questions:
        questions.answers = questions.answer_set.all()
    return render(request, 'quiz_detail.html', {'quiz':quiz})