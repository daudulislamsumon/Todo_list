from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('<list_id>', views.delete, name='delete'),
    path('<list_id>', views.cross, name='cross'),
]
