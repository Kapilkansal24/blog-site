from django.urls import path
from . import views 

urlpatterns = [
    path("about/", views.about), # localhost/users/about
    path("login/", views.login),
    path("afterlogin/", views.afterlogin),
    path("signup/", views.signup),
    path("aftersignup/", views.After_signup.as_view()),
    path("logout/", views.logout),
    path("profile/", views.profile),
    path("forgot/", views.forgot),
    path("sendmail/", views.sendmail),
    path("checkotp/", views.checkotp),
    path("downloadcsv/", views.downloadcsv),
    path("downloadpdf/", views.downloadpdf),
]