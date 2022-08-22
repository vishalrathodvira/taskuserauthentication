from django.urls import path
from . import views


urlpatterns = [
    path('', views.signup, name='signup'),
    path('signin',views.signin,name='signin'),
    path('profile',views.profile,name='profile'),
    path('show',views.show,name='show'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),




]