from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:theme_pk>/', views.theme, name='theme'),
    path('theme2', views.theme2, name='theme2'),
    path('detail', views.detail, name='detail'),
    # 이하 관리자만 접근 가능한 url 목록
    path('staff/', views.staff, name='staff'),
    path('staff/update_exhibition_list/', views.update_exhibition_list, name='update_exhibition_list'),
    path('staff/create_theme/', views.create_theme, name='create_theme'),
    path('<int:theme_pk>/update/', views.update_theme, name='update_theme'),
    path('<int:theme_pk>/delete/', views.delete_theme, name='delete_theme'),
]

# <int:post_pk>/detail/<int:detail_pk>/likes/
# <int:post_pk>/detail/<int:detail_pk>/reviews/
# <int:post_pk>/detail/<int:detail_pk>/reviews/<int:review_pk>/
# <int:post_pk>/detail/<int:detail_pk>/reviews/<int:review_pk>/likes/
# <int:post_pk>/detail/<int:detail_pk>/reviews/<int:review_pk>/update/

