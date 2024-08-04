from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
#username :- nani22
# pass :- nani8985 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('master/', views.Master, name='master'),
    path('', views.Index, name='index'),
    path('signup', views.signup, name='signup'),  # Ensure this is correct
    path('accounts/logout/', views.CustomLogoutView.as_view(), name='logout'), 
    path('accounts/', include('django.contrib.auth.urls')),

    #included the cart items
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_detail/', views.cart_detail, name='cart_detail'),

    #contact
    path('contact_us', views.Contact_Page, name='contact_page'),

    #checkout page
    path('checkout/', views.CheckOut, name='checkout'),

    # order page
    path('order/', views.Your_Order, name='order'),
    
    #product page
    path('product/', views.Product_page, name='product'),

    #product detail page
    path('product/<str:id>', views.Product_Detail, name='product_detail'),

    #search function
    path('search/', views.Search, name='search'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
