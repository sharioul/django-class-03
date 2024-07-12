from django.contrib import admin
from django.urls import path
from myproject.views import home,contract,about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home),
    path('contract',contract),
    path('about',about),
]
