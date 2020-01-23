import pdb

import datetime

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView

from core.forms import VideoForm
from core.models import Video, Theme


class MyVideoView(View):
    name = 'my-video'
    template_name = 'my-video.html'

    def get(self, request, *args, **kwargs):
        video = Video.objects.get(id=kwargs['id'])
        context = {
            'video_id': video.id,
            'video': video.media.url,
            'thumbnail': video.thumbnail.url,
            'title': video.title,
            'thumbs_up': video.thumbs_up,
            'thumbs_down': video.thumbs_down,
            'themes': video.themes,
            'created_at': video.formated_created_at,
            'descr': video.descr

        }
        return render(request, self.template_name, context)


class HomeView(View):
    name = 'home'
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        videos = Video.objects.all()
        context = {
            'videos': videos,
        }
        return render(request, self.template_name, context)


class ScoresView(View):
    name = 'scores'
    template_name = 'scores.html'

    def get(self, request, *args, **kwargs):
        themes = Theme.objects.all()
        context = {
            'themes': themes,
        }
        return render(request, self.template_name, context)


class AddVideoView(CreateView):
    model = Video
    name = 'add-video'
    form_class = VideoForm
    template_name = 'add-video.html'

    def post(self, request, *args, **kwargs):
        form = request.POST
        video = Video.objects.create(
            title=form['title'],
            media='/videos/'+form['media'],
            descr=form['descr'],
            thumbnail=form['thumbnail'],
        )
        for theme in form['themes']:
            if video.themes.filter(descr=theme) and not Theme.object.filter(descr=theme):
                new_theme = Theme.objects.create(descr=theme)
                video.themes.add(new_theme)
        video.save()
        return redirect('/')


def thumbs_up(request, *args, **kwargs):
    video = Video.objects.get(id=kwargs['id'])
    video.like()
    video.save()
    return JsonResponse({'thumbs': video.thumbs_up})


def thumbs_down(request, *args, **kwargs):
    video = Video.objects.get(id=kwargs['id'])
    video.dislike()
    video.save()
    return JsonResponse({'thumbs': video.thumbs_down})