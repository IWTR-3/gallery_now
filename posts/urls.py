from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [

    ## main features - post & theme ##
    path('', views.index, name='index'),  # 모든 theme 조회
    path('post-list/<int:theme_pk>', views.post_list,
         name='post_list'),  # theme 상세
    path('post/<int:post_pk>', views.detail, name='detail'),  # post detail 조회

    ## like, visited ##
    path('post/<int:post_pk>/like', views.like, name='like'),
    path('post/<int:post_pk>/visited', views.visited, name='visited'),

    ## review CRUD, like ##
    path('post/<int:post_pk>/review', views.review_create, name='review_create'),  # review 작성
    path('post/<int:post_pk>/review/<int:review_pk>/update',
         views.review_update, name='review_update'),  # review 수정
    path('post/<int:post_pk>/review/<int:review_pk>/delete',
         views.review_delete, name='review_delete'),  # review 삭제
     path('post/<int:post_pk>/review/<int:review_pk>/like/', views.review_likes, name='review_like'),




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
## review CRUD, like ##
## like, visited ##
## main features - post & theme ##
