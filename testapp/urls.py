from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^tables/$', views.TableListView.as_view(), name='table_list'),
    url(r'^tables/create/$', views.create_table, name='table_create'),
    url(r'^tables/(?P<pk>\d+)/update/$', views.update_table, name='table_update'),
    url(r'^tables/(?P<pk>\d+)/delete/$', views.delete_table, name='table_delete'),

    url(r'^tables/(?P<table_pk>\d+)/fields/$', views.FieldListView.as_view(), name='field_list'),
    url(r'^tables/(?P<table_pk>\d+)/fields/create/$', views.create_field, name='field_create'),
    url(r'^tables/(?P<table_pk>\d+)/fields/(?P<field_pk>\d+)/update/$', views.update_field, name='field_update'),
    url(r'^tables/(?P<table_pk>\d+)/fields/(?P<pk>\d+)/delete/$', views.delete_field, name='field_delete'),
]
