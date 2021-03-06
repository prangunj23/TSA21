from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginuser, name='login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logoutuser, name='logout'),
    path('user', views.user, name="user"),
    path('event', views.event, name="event"),
    path('loginevent', views.loginevent, name="loginevent"),
    path('puzzles', views.puzzles, name="puzzles"),
    path('contact', views.contact, name="contact"),
    path('updatedifficulty', views.updatediff, name="update"),
    path('presentevent', views.present, name="present"),
    path('lichess', views.lichess, name="lichess")
]
