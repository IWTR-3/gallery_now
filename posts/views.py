# posts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Theme, Exhibition, Review, Artist, Gallery
from posts import api
from .forms import ReviewForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

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
    return render(request, 'posts/post_list.html', context)


# 전시 detail 조회
def detail(request, post_pk):
    post = Exhibition.objects.get(pk=post_pk)
    reviews = post.review_set.all()
    review_form = ReviewForm()
    context = {
        'post': post,
        'review_form': review_form,
        'reviews': reviews
    }
    return render(request, 'posts/detail.html', context)


def like(request, post_pk):
    post = Exhibition.objects.get(pk=post_pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
        is_liked = False
    else:
        post.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return JsonResponse(context)


def visited(request, post_pk):
    post = Exhibition.objects.get(pk=post_pk)
    if request.user in post.like_users.all():
        post.visited_users.remove(request.user)
        is_visited = False
    else:
        post.visited_users.add(request.user)
        is_visited = True
    context = {
        'is_visited': is_visited,
    }
    return JsonResponse(context)


# 리뷰 C
def review_create(request, post_pk):
    exhibition = Exhibition.objects.get(pk=post_pk)
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.exhibition = exhibition
        review.user = request.user
        review.save()
        return redirect('posts:detail', post_pk=post_pk)
    else:
        review_form = ReviewForm()
    return redirect('posts:detail', post_pk=post_pk)


# 리뷰 U
# def review_update(request, post_pk, review_pk):
#     exhibition = Exhibition.objects.get(pk=post_pk)
#     review = Review.objects.get(pk=review_pk)
#     if request.user == review.user:
#         if request.method == 'POST':
#             review_form = ReviewForm(request.POST, instance=review)
#             if review_form.is_valid():
#                 review_form.save()
#                 return redirect('posts:detail', post_pk=post_pk)
#     else:
#         review_form = ReviewForm(instance=review)
#     return redirect('posts:detail', post_pk=post_pk)

def review_update(request, post_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    review_form = ReviewForm(instance=review)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('posts:detail', post_pk=post_pk)
    context = {
        'review_form': review_form,
        'review': review,
    }
    return render(request, 'posts/review_update.html', context)


# 리뷰 D
def review_delete(request, post_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('posts:detail', post_pk)


@login_required
def review_like(request, post_pk, review_pk):
    review = Review.objects.get(pk=review_pk)

    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
        is_liked = False
    else:
        review.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return JsonResponse(context)


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
