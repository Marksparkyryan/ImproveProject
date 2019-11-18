from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.menu_list, name='home'),
    url(r'^menu/(?P<query>\w+)$', views.menu_list, name='menu_list'),
    url(r'^menu/(?P<pk>\d+)/edit/$', views.edit_menu, name='menu_edit'),
    url(r'^menu/(?P<pk>\d+)/$', views.menu_detail, name='menu_detail'),
    url(r'^menu/(?P<menu_pk>\d+)/item/(?P<item_pk>\d+)/$', views.item_detail, name='item_detail'),
    url(r'^menu/new/$', views.create_new_menu, name='menu_new'),
    url(r'^menu/search/', views.menu_search, name='menu_search'),
]
