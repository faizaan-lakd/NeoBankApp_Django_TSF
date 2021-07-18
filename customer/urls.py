from django.urls import path
from customer import views

urlpatterns = [
    path('', views.customer, name='customer'),
    path('history/', views.history , name="history"),
    path('profile/<int:cust_id>', views.profile, name="profile"),
]