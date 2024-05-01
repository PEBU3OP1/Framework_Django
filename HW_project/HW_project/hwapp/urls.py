from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('clients/', views.get_clients, name='clients'),
    path('client/', views.get_client, name='client'),
    path('order/', views.get_order_info, name='order'),
    path('orders/<int:client_id>/<str:period>', views.get_orders, name='orders'),
    path('add_product/', views.add_product, name='add_product'),
    path('upload_img/<int:product_id>', views.upload_image, name='upload_image'),
    path('update_product/<int:product_id>', views.update_product, name='update_product'),
]