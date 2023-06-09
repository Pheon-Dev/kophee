from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('menu_item/<int:pk>', views.menu_item, name='menu_item'),
    path('delete_item/<int:pk>', views.delete_item, name='delete_item'),
    path('update_item/<int:pk>', views.update_item, name='update_item'),
    path('order_item/<int:pk>', views.order_item, name='order_item'),
    path('add_item/', views.add_item, name='add_item')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
