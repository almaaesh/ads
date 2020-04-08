from django.conf.urls import url
from django.contrib.auth import views
from django.urls import path, re_path

from post.views import ProductListView, ProductDetailView, UserPostListView, ProuctByCategoryListView, \
    ProductByCountryListView, ProuctByCountryCategoryListView

app_name = 'post'

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    # Todo: count category items by country and remove c from url
    path('c/<slug:country_slug>/', ProductByCountryListView.as_view(), name='product-by-country'),
    path('category/<slug:category_slug>/', ProuctByCategoryListView.as_view(), name='product-by-category'),
    path('<slug:country_slug>/<slug:category_slug>/', ProuctByCountryCategoryListView.as_view(),
         name='product-by-country-category'),

    path('detail/<slug:country_slug>/<slug:category_slug>/<int:product_id>/<slug:slug>/', ProductDetailView.as_view(), name='detail'),

    # for Users
    path('user-post/', UserPostListView.as_view(), name='user-post'),
]
