# news/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$',views.news_generate,name = 'news_gen'),
    url(r'^(?P<news_type>[a-z]+)$',views.news_generate,name = 'news_gen'),
    # url(r'^test',views.test_func),
    # url(r'^$',views.test_func),
]
