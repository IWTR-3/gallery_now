from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Theme, Exhibition, Review, Artist, Gallery
from posts import api


# Create your views here.

# 첫 페이지 모든 theme의 list를 보여준다.
def index(request):

    theme_list = Theme.objects.all()

    context = {
        'theme_list': theme_list,
    }
    # return render(request, 'posts/test/now.html', context)
    return render(request, 'posts/index.html', context)

# 선택된 테마의 포함된 전시 리스트를 보여준다.


def theme(request, theme_pk):
    theme = Theme.objects.get(pk=theme_pk)
    context = {
        'theme': theme,
    }
    return render(request, 'posts/theme.html', context)

# 임시 theme


def theme2(request):

    return render(request, 'posts/theme2.html')

# 임시 detail


def detail(request):
    return render(request, 'posts/detail.html')

# 테마를 생성한다.


@login_required
def create_theme(request):

    context = {}

    return render(request, 'posts/test/create_theme.html', context)


@login_required
def update_theme(request, post_pk):
    context = {}
    return render(request, 'posts/test/update_theme.html', context)


@login_required
def delete_theme(request, post_pk):

    context = {}

    return redirect('posts:index')


@login_required
def staff(request):
    if request.user.is_admin:
        context = {
            'items': Exhibition.objects.all()
        }
        return render(request, 'posts/test/staff.html', context)


@login_required
def update_exhibition_list(request):
    if request.method == "POST":
        # admin user 일 때만 동작
        if request.user.is_admin:
            print(api.update())
    return redirect('posts:staff')


# 관리자의 테마 생성 플로우
"""
0. 태그 관리자 페이지 에서 태그 통계 확인
1. 테마 생성하기 버튼 입력
"""
