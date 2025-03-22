from django.urls import path

from medical_appointments.views import home_page, booking_edit, booking_delete


urlpatterns = [
    path('', home_page, name='booking'),
    path('<int:id>', booking_edit),
    path('delete/<int:id>', booking_delete),
]
