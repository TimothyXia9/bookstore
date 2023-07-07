import os
from django.contrib import admin
from django.urls import path, include
from django.views import static
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static as img_static
from apps.manages import views
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(url(r'^static/(?P<path>.*)$', static.serve,
        {'document_root': settings.STATIC_ROOT}, name='static'))

