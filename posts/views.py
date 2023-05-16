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


def post_list(request, theme_pk):
    theme = Theme.objects.get(pk=theme_pk)
    context = {
        'theme': theme,
    }
    return render(request, 'posts/theme.html', context)

# 전시 detail 조회


def detail(request, post_pk):

    post = Exhibition.objects.get(pk=post_pk)

    context = {
        'post': post,
    }

    return render(request, 'posts/detail.html', context)


def like(request, post_pk):

    post = Exhibition.objects.get(pk=post_pk)

    return redirect('posts:detail', post_pk)


def visited(request, post_pk):

    post = Exhibition.objects.get(pk=post_pk)

    return redirect('posts:detail', post_pk)

# 리뷰 C


def review(request, post_pk):
    return redirect('posts:detail', post_pk)

# 리뷰 U


def review_update(request, post_pk, review_pk):
    return redirect('posts:detail', post_pk)

# 리뷰 D


def review_delete(request, post_pk, review_pk):
    return redirect('posts:detail', post_pk)


def review_like(request, post_pk, review_pk):
    return redirect('posts:detail', post_pk)


@login_required
def create_theme(request):

    context = {}

    return render(request, 'posts/test/create_theme.html', context)


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
