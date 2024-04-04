
from django.contrib import admin
from django.urls import path
from session import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.setsession),
    path('get/', views.getsession),
    path('delete/', views.deletesession)
]
