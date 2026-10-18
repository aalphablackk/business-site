
import logging

from django.contrib import messages
from django.shortcuts import redirect, render

from .email_utils import send_contact_emails
from .forms import ContactForm

logger = logging.getLogger(__name__)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            try:
                send_contact_emails(form.cleaned_data)
            except Exception:
                logger.exception("Failed to process contact form emails")
                messages.error(
                    request,
                    "We couldn't send your message right now. "
                    "Please try again shortly.",
                )
            else:
                messages.success(
                    request,
                    "Thank you! Your message has been received.",
                )
                return redirect("website:contact")
    else:
        form = ContactForm()

    return render(
        request,
        "pages/contact.html",
        {"form": form},
    )
