from django.urls import path

from medical_appointments.views import booking, booking_edit, booking_delete


urlpatterns = [
    path('', booking, name='booking'),
    path('<int:id>', booking_edit, name='edit'),
    path('delete/<int:id>', booking_delete, name='delete'),
]
