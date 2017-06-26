from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^refresh/$', views.UpdateDatabase),
    #url(r'^register/$', views.SignupView.as_view()),
]