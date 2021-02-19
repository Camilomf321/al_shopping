from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/<int:id>', views.blog_detail, name='blog_detail'),
]
