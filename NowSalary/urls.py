
#from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('first.urls')),
    path('admin/', admin.site.urls),
    path('employee/', include('employee.urls')),
    path('manager/', include('manager.urls')),
    path('', include('django.contrib.auth.urls')),
    path('accountant/', include('accountant.urls')),
    #path('', include('employee.urls')),
   # path('', include('manager.urls')),
]


