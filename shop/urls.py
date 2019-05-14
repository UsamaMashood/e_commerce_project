from django.urls import path
from . import views
urlpatterns = [
    path('', views.shop_home, name = 'shop_home'),
    path('about/', views.shop_about, name = 'shop_about'),
    path('contect/', views.shop_contect, name = 'shop_contect'),
    path('tracker/', views.tracker, name = 'tracker'),
    path('search/', views.search, name = 'search'),
    path('productview/<int:pd_id>', views.productview, name = 'productview'),
    path('checkout/', views.checkout, name = 'checkout'),

]
