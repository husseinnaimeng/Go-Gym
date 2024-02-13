
from django.contrib import admin
from django.urls import path
from . import tasks
from django.http import HttpResponse

def index(request):
    pass

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",index)
]
