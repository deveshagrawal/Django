from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
                       url(r'^$', views.article_list),
                       url(r'^article/(?P<pk>[0-9]+)/$', views.article_detail),
)