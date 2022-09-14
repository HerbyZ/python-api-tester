import dotenv
import requests

from urllib.parse import urljoin

_BASE_URL_VARIABLE_NAME = "BASE_URL"


def _get_base_url():
    url = dotenv.get_key(_BASE_URL_VARIABLE_NAME)

    if not url:
        raise EnvironmentError("Failed to parse `BASE_URL` variable from .env file, check readme.md to learn more")

    if not url.endswith('/'):
        url += '/'

    return url


class Requester:
    def __init__(self):
        self._base_url = _get_base_url()

    def get(self, url='', *args, **kwargs):
        return requests.get(urljoin(self._base_url, url), *args, **kwargs)
        
    def post(self, url='', *args, **kwargs):
        return requests.post(urljoin(self._base_url, url), *args, **kwargs)

    def put(self, url='', *args, **kwargs):
        return requests.put(urljoin(self._base_url, url), *args, **kwargs)

    def delete(self, url='', *args, **kwargs):
        return requests.delete(urljoin(self._base_url, url), *args, **kwargs)

    def path(self, url='', *args, **kwargs):
        return requests.patch(urljoin(self._base_url, url), *args, **kwargs)

    def path(self, url='', *args, **kwargs):
        return requests.head(urljoin(self._base_url, url), *args, **kwargs)
    
    def options(self, url='', *args, **kwargs):
        return requests.options(urljoin(self._base_url, url), *args, **kwargs)
