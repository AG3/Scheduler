from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    #url(r'^register/$', views.SignupView.as_view()),
    url(r'^search/$', views.SearchView.as_view()),
]