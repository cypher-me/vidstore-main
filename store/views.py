from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.utils.decorators import method_decorator


from .models import VideoItem

# Create your views here.

# temp data for testing

def index(req):

    # return HttpResponse('home pade')
    return render(req, 'store/index.html')

def about(req):

    return render(req, 'store/about.html', {"title" : "about page"})

def checkout(req):
    return render(req, 'store/checkout.html')

# @login_required
# def store(req):
#     videos = VideoItem.objects.all()


#     return render(req, 'store/store.html', {"videos" : videos})
# @method_decorator(login_required)
class StoreListView(ListView):
    model = VideoItem
    template_name = 'store/store.html'
    context_object_name = 'videos'
    ordering = ['-upload_date']
    paginate_by = 2


class StoreDetailView(DetailView):
    model = VideoItem
    template_name = 'store/video_detail.html'

# class StoreCreateView(CreateView):
#     model = VideoItem
    


