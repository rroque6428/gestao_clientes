from django.urls import path
from .views import home, my_logout, MyView


urlpatterns = [
    path('', home, name="home"),
    path('view/', MyView.as_view()),
    path('logout/', my_logout, name="logout"),
]