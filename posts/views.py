from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Theme, Exhibition, Review, Artist, Gallery
from posts import api
from .forms import ReviewForm


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

# 전시 detail 조회


def detail(request, exhibition_pk):

    return render(request, 'posts/detail.html')


# 임시 코드 
def theme2(request):
    return render(request, 'posts/theme2.html')

def detail2(request):

    return render(request, 'posts/detail.html')


# 리뷰 C

def review_create(request, exhibition_pk):
    exhibition = Exhibition.objects.get(pk=exhibition_pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.exhibition = exhibition
            review.user = request.user
            review.save()

            return redirect('posts:detail', exhibition_pk=exhibition_pk)
    else:
        review_form = ReviewForm()
    
    context = {
        'exhibition': exhibition,
        'review_form': review_form,
    }
    return render(request, 'posts/review_create.html', context)



# 리뷰 U

def review_update(request, exhibition_pk, review_pk):
    exhibition = Exhibition.objects.get(pk=exhibition_pk)
    review = Review.objects.get(exhibition_pk=exhibition_pk, pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review_form.save()
                return redirect('posts:detail', exhibition_pk=exhibition_pk)
    else:
        review_form = ReviewForm(instance=review)
    
    context = {
        'review_form': review_form,
        'exhibition': exhibition,
        'review_form': review_form,
    }
    return render(request, 'posts/review_update.html', context)



# 리뷰 D

def review_delete(request, exhibition_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('posts:detail', exhibition_pk)




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
