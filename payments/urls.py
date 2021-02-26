from django.urls import path
from . import views
app_name = 'payments'

urlpatterns = [
    path('create-payment/', views.create_payment, name='create_payment'),
    path('cancel/', views.cancel_payment, name='cancelled'),
    path('success/', views.success_payment, name='success')
]
