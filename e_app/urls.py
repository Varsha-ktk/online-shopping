from django.urls import path

from e_app import views, admin_views, seller_views, customer_views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.Login,name='login'),
    path('pluto',views.pluto,name='pluto'),
    path('corona',views.corona,name='corona'),

    path('adminbase',views.adminbase, name='adminbase'),
    path('customerbase', views.customerbase, name='customerbase'),
    path('sellerbase', views.sellerbase, name='sellerbase'),

    path('customer',views.customer, name='customer'),
    path('seller', views.seller, name='seller'),
    path('login_view',views.login_view, name='login_view'),



    # admin

    path('admin_customerview',admin_views.admin_customerview,name='admin_customerview'),
    path('admin_sellerview', admin_views.admin_sellerview, name='admin_sellerview'),

    path('seller_delete/<int:id>/',admin_views.seller_delete,name='seller_delete'),
    path('customer_delete/<int:id>/', admin_views.customer_delete, name='customer_delete'),

    path('seller_update/<int:id>/',admin_views.seller_update,name='seller_update'),


    # seller
    path('product', seller_views.product, name='product'),
    path('product_view', seller_views.product_view, name='product_view'),
    path('product_delete/<int:id>/', seller_views.product_delete, name='product_delete'),
    path('product_update/<int:id>/', seller_views.product_update, name='product_update'),

    #customer
    path('customer_productview',customer_views.customer_productview,name='customer_productview'),








]