from django.contrib import messages


class ErrorMessageMixin(object):
    """
    Adds a message with the ``ERROR`` level.
    """
    error_message = ''

    def form_invalid(self, form, form1):
        error_message = self.get_error_message()
        if error_message:
            messages.error(self.request, error_message)
        return super(ErrorMessageMixin, self).form_invalid(form, form1)

    def get_error_message(self):
        return self.error_message
