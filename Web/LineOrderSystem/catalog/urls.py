from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('customer/', views.customer, name='customer'),
    path('contact/',views.contact, name = 'contact'),
    path('reference/',views.reference, name = 'reference')

]
