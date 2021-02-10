from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('offer/<offer_id>', views.contact_offer, name='contact_offer'),

]
