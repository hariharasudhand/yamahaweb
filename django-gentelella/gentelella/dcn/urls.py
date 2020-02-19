from django.conf.urls import url
from django.urls import path
from . import views
from .views import DCNListView, DCNPartsView

urlpatterns = [
    path('create/', DCNListView.as_view(template_name='dcn/create_new.html'), name='dcn-create'),
    path('', DCNPartsView.as_view(template_name='dcn/dcn_parts.html'), name='dcn_parts'),
    path('', DCNPartsView.as_view(template_name='dcn/addrows.html'), name='add_rows'),
    url(r'^add_create/$', views.add_create, name='add_create'),
    #path('add_create', views.add_create, name='add_create'),
    #url(r'^add_cr/$', views.add_cr, name='add_cr'),
    url(r'^dcn_parts/$', views.dcn_parts, name='dcn_parts'),
]