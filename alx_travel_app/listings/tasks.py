from celery import shared_task

from django.core.mail import send_mail

@shared_task

def send_booking_email(customer_email, booking_details):

    subject = 'Booking Confirmation'

    message = f'Confirmation for your booking: {booking_details}'

    from_email = 'noreply@alxtravel.com'

    return send_mail(subject, message, from_email, [customer_email])