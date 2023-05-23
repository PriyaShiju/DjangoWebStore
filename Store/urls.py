from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

#import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    
]  