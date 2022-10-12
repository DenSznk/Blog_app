from django.shortcuts import render


def home(request):
    name = 'Test task for the position of junior Python developer Made by Denis Sazonenko'
    return render(request, 'blog_application/default.html', {'name': name})
