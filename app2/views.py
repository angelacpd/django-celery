from django.http import HttpResponse
from django.views.generic.edit import FormView

from app2.forms import ReviewForm


class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg = "Thanks for the review!"
        return HttpResponse(msg)
