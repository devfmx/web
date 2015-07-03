"""Module to se tup custom storages systems."""

from django.conf import settings
from storages.backends.s3boto import S3BotoStorage


class MediaStorage(S3BotoStorage):

    """Change the Media Storage."""

    location = settings.MEDIAFILES_LOCATION
