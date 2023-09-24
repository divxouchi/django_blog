
from django.contrib import admin
from django.urls import path
from blog.views import flontpage, post_detail, post_new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', flontpage),
    path('new/', post_new, name='post_new'),
    path("<slug:slug>/",post_detail, name="post_detail")
]
