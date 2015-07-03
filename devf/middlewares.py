"""Django main middlewares."""

from django.conf import settings
from django.http import HttpResponseRedirect


class SSLMiddleware(object):

    """Class to force SSL on Production."""

    def process_request(self, request):
        """Method that process the request and transform it to SSL request."""
        if not any([settings.DEBUG,
                    request.is_secure(),
                    request.META.get("HTTP_X_FORWARDED_PROTO", "") == 'https'
                    ]):
            url = request.build_absolute_uri(request.get_full_path())
            secure_url = url.replace("http://", "https://")
            return HttpResponseRedirect(secure_url)
