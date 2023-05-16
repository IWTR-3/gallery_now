from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [

    path('', views.index, name='index'),  # theme_list 조회
    path('<int:theme_pk>', views.theme, name='theme'),  # theme detail 조회

    path('exhibition/<int:exhibition_pk>/', views.detail,
         name='detail'),  # exhibition detail 조회
    path('exhibition/<int:exhibition_pk>/review',
         views.review, name='review'),  # review 작성
    path('exhibition/<int:exhibition_pk>/review/<int:review_pk>/update/',
         views.review_update, name='review_update'),  # review 수정
    path('exhibition/<int:exhibition_pk>/review/<int:review_pk>/delete/',
         views.review_delete, name='review_delete'),  # review 삭제

    # 이하 관리자만 접근 가능한 url 목록
    path('staff/', views.staff, name='staff'),
    path('staff/update_exhibition_list/',
         views.update_exhibition_list, name='update_exhibition_list'),

    # path('staff/create_theme/', views.create_theme, name='create_theme'),
    # path('<int:theme_pk>/update/', views.update_theme, name='update_theme'),
    # path('<int:theme_pk>/delete/', views.delete_theme, name='delete_theme'),


]

# <int:post_pk>/detail/<int:detail_pk>/likes/
# <int:post_pk>/detail/<int:detail_pk>/reviews/
# <int:post_pk>/detail/<int:detail_pk>/reviews/<int:review_pk>/
# <int:post_pk>/detail/<int:detail_pk>/reviews/<int:review_pk>/likes/
# <int:post_pk>/detail/<int:detail_pk>/reviews/<int:review_pk>/update/
