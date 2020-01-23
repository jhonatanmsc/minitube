"""minitube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.views import MyVideoView, HomeView, thumbs_up, thumbs_down, AddVideoView, ScoresView
from minitube import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name=HomeView.name),
    path('video/add/', AddVideoView.as_view(), name=AddVideoView.name),
    path('video/<int:id>', MyVideoView.as_view(), name=MyVideoView.name),
    path('scores/', ScoresView.as_view(), name=ScoresView.name),
    path('like/<int:id>', thumbs_up, name="like"),
    path('dislike/<int:id>', thumbs_down, name="dislike"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
