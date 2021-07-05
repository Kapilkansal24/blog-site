from django.urls import path
from . import views 

urlpatterns = [
    path("addblog/", views.addblog),   # localhost/blog/addblog
    path("afterblog/", views.afterblog.as_view()),
    path("allblogs/", views.allblogs),
    path("myblog/", views.myblog),
    path("api/", views.Getapi.as_view()),  # localhost/blog/api/
    path("search/", views.search)
]