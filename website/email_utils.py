
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_contact_emails(data):
    context = {
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "email": data["email"],
        "phone": data.get("phone", ""),
        "message": data["message"],
    }

    # Notify your business inbox first.
    admin_text = render_to_string(
        "emails/admin_notification.txt", context
    )
    admin_html = render_to_string(
        "emails/admin_notification.html", context
    )

    admin_email = EmailMultiAlternatives(
        subject=f"New website inquiry from {context['first_name']} "
                f"{context['last_name']}",
        body=admin_text,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.CONTACT_RECIPIENT_EMAIL],
        reply_to=[context["email"]],
    )
    admin_email.attach_alternative(admin_html, "text/html")
    admin_email.send(fail_silently=False)

    # Confirm receipt to the visitor.
    customer_text = render_to_string(
        "emails/customer_confirmation.txt", context
    )
    customer_html = render_to_string(
        "emails/customer_confirmation.html", context
    )

    customer_email = EmailMultiAlternatives(
        subject="We've received your message",
        body=customer_text,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[context["email"]],
    )
    customer_email.attach_alternative(customer_html, "text/html")
    customer_email.send(fail_silently=False)
