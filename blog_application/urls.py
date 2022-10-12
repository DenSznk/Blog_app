from django.urls import path

from blog_application.views import posts_list_view, post_detail_view

urlpatterns = [
    path('', posts_list_view, name='posts_list'),
    path('<int:pk>', post_detail_view, name='posts_detail'),

]
