from django.contrib import admin
from django.urls import path
from blogs import views

admin.site.site_header = "Davis Blog"
admin.site.site_title =  "Davis Blog"
admin.site.index_title = "Davis Blog"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("blog", views.blog, name="blog"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
]

