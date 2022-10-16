from django.urls import path

from blog_application.views import posts_list_view, post_detail_view, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', posts_list_view, name='posts_list'),
    path('<int:pk>', post_detail_view, name='posts_detail'),
    path('create/', PostCreateView.as_view(), name='posts_create'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='posts_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='posts_delete'),

]



