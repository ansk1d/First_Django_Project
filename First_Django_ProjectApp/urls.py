from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),
    path('blogs', views.index )	 ,
    path('blogs/new', views.new)  ,
    path ('blogs/create', views.create),
    path ('blogs/<num>', views.number),
        path ('blogs/<num>/edit', views.edtnum),
        path ('blogs/<num>/delete', views.destroy),
]