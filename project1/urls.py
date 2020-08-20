"""
MAIN URLS
"""
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #adding fields urls
    re_path('', include('apps.fields.urls')),
    re_path('', include('apps.prueba.urls'))

]
