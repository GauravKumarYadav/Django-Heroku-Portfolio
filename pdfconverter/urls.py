from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('postlist/',views.doclist,name="postlist"),
    path('contact/',views.sendcontactmail,name="sendcontactform"),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
