from django.urls import path
from . import views


urlpatterns = [
    path('<int:page>/', views.posts, name="posts"),
    path('post/<int:pk>', views.post, name="post"),
    path('blog/', views.blog, name="blog"),
]
