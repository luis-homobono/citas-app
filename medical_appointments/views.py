from django.shortcuts import render, get_object_or_404, redirect

from medical_appointments.models import MedicalAppointment


def booking(request):
    if request.method == 'POST':
        data = request.POST
        booking = MedicalAppointment.objects.create(
            patient=data['paciente'],
            appointment_type=data['tipo'][0],
            doctor_name=data['medico'],
            appointment_date=data['fecha_hora']
            )
        return redirect('booking')

    booking_active = MedicalAppointment.objects.filter(is_active=True)
    booking_no_active = MedicalAppointment.objects.filter(is_active=False)
    options = MedicalAppointment.AppointmentTypes.choices
    try:
        booking = MedicalAppointment.objects.last().id
    except:
        booking = 0

    context = {
        'appointment_type': [option[1] for option in options],
        'booking_active': booking_active,
        'booking_no_active': booking_no_active,
        'booking_id': booking + 1
    }

    return render(request, 'booking/booking.html', context=context)

def booking_edit(request, id):
    if request.method == 'POST':
        data = request.POST
        booking = get_object_or_404(MedicalAppointment, id=id)
        booking.appointment_date = data['fecha_hora']
        booking.appointment_type = data['tipo'][0]
        booking.doctor_name = data['medico']
        booking.save()
        return redirect('booking')

    booking = get_object_or_404(MedicalAppointment, id=id)
    options = MedicalAppointment.AppointmentTypes.choices
    datetime = booking.appointment_date.strftime("%Y-%m-%dT%H:%M")
    context = {
        'appointment_type': [option[1] for option in options],
        'booking': booking,
        'datetime': datetime
    }
    return render(request, 'booking/booking_edit.html', context=context)

def booking_delete(request, id):
    booking = get_object_or_404(MedicalAppointment, id=id)
    if request.method == 'POST':
        booking.is_active = False
        booking.save()

        return redirect('booking')

    options = MedicalAppointment.AppointmentTypes.choices

    context = {
        'appointment_type': [option[1] for option in options],
        'booking': booking
    }
    return render(request, 'booking/booking_delete.html', context=context)