from django.contrib import admin
from django.urls import path, include
from home import views

#Django adimin header customization

admin.site.site_header="Login to Developer Rahul"
admin.site.site_title="Welcome to Rahuls's Dashboard"
admin.site.index_title="welcome to this portal"

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('project',views.project, name='project'),
    path('contact',views.contact, name='contact'), 
]
 