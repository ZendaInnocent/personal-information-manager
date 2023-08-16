from django.contrib.messages import get_messages
from django.template.loader import render_to_string
from django.utils.deprecation import MiddlewareMixin


class HtmxMessageMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if (
            'HX-Request' in request.headers
            and 300 <= response.status_code < 400
            and 'HX-Redirect' not in response.headers
        ):
            response.write(
                render_to_string(
                    template_name='toast.html',
                    context={
                        'messages': get_messages(request),
                    },
                    request=request,
                )
            )
        return response
