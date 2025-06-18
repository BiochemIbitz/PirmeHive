from django.urls import path, include
from . import views
from . import auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('service/<str:service_id>/', views.service_detail, name='service_detail'),
    path('book-service/<str:service_id>/', views.book_service, name='book_service'),
    
    # Authentication URLs
    path('signup/', auth_views.sign_up, name='signup'),
    path('signin/', auth_views.sign_in, name='signin'),
    path('signout/', auth_views.sign_out, name='signout'),
    path('auth/firebase/', auth_views.handle_firebase_auth, name='handle_firebase_auth'),
]
