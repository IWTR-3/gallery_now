from django.shortcuts import render
from posts.models import Theme, Exhibition, Review, Artist, Gallery

# Create your views here.

# 첫 페이지 모든 theme의 list를 보여준다.
def index(request):
    
    theme_list = Theme.objects.all()

    context = {
        'theme_list':theme_list,
    }
    return render(request, 'posts/index.html', context)

# 선택된 테마의 포함된 전시 리스트를 보여준다.
def theme(request, theme_pk):
    theme = Theme.objects.get(pk=theme_pk)
    context = {
        'theme':theme,
    }
    return render(request, 'posts/theme.html', context)

# 테마를 생성한다.
def create_theme(request):

    context = {}

    return render(request, 'posts/index.html', context)

def update_theme(request, post_pk):
    context = {}
    return render(request, 'posts/index.html', context)

def delete_theme(request, post_pk):

    context = {}

    return render(request, 'posts/index.html', context)