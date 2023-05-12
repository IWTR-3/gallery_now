from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:theme_pk>/', views.theme, name='theme'),
    path('create/', views.create_theme, name='create_theme'),
    path('<int:theme_pk>/update/', views.update_theme, name='update_theme'),
    path('<int:theme_pk>/delete/', views.delete_theme, name='delete_theme'),
]

# <int:post_pk>/detail/<int:detail_pk>/likes/
# <int:post_pk>/detail/<int:detail_pk>/reviews/
# <int:post_pk>/detail/<int:detail_pk>/reviews/<int:review_pk>/
# <int:post_pk>/detail/<int:detail_pk>/reviews/<int:review_pk>/likes/
# <int:post_pk>/detail/<int:detail_pk>/reviews/<int:review_pk>/update/

