from django.db import models
import requests
from requests.exceptions import HTTPError

# Create your models here.
class Cartelera:
    api_url=""
    def __init__(self):
        self.api_url = "https://apiseriespersonajes.azurewebsites.net"

    def series(self):
        api_series = "/api/Series"
        self.api_url = self.api_url + api_series

        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            series = response.json()
        except HTTPError as http_err:
            print('HTTP_Error:', http_err)
        except Exception as err:
            print('Error:', err)

        return series