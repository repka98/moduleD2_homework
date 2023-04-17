from django.urls import path
from .views import PostDetailView, PostList, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно почему
    path('', PostList.as_view()),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('update/', PostUpdateView.as_view(), name='post_update'),
    path('delete/', PostDeleteView.as_view(), name='post_delete'),

    # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
]