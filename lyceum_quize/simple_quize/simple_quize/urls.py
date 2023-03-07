from django.contrib import admin
from django.urls import path

from chance_to_surrender.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
]
