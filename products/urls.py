from django.conf.urls import url
from . import views as product_views

app_name = 'products'

urlpatterns = [
    url(r'^$', product_views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',product_views.product_list,name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',product_views.product_detail,name='product_detail'),
]