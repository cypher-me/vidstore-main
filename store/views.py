from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import VideoItem

# Create your views here.

# temp data for testing

temp_data = [
    {
        "video_title" : "Video 1",
        "video_description" : "lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem ",
        "video_content" : "lorem lorem lorem lorem lorem lorem ",
        "date_posted" : "today",
    },{
        "video_title" : "Video 2",
        "video_description" : "lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem ",
        "video_content" : "lorem lorem lorem lorem lorem lorem ",
        "date_posted" : "today",
    },
    {
        "video_title" : "Video 3",
        "video_description" : "lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem lorem ",
        "video_content" : "lorem lorem lorem lorem lorem lorem ",
        "date_posted" : "today",
    },
]


def index(req):

    context = {
        'posts' : temp_data
    }

    # return HttpResponse('home pade')
    return render(req, 'store/index.html', context)

def about(req):

    return render(req, 'store/about.html', {"title" : "about page"})

@login_required
def store(req):
    videos = VideoItem.objects.all()


    return render(req, 'store/store.html', {"videos" : videos})