import requests


class MlnnClient(object):
    base_url = 'http://185.195.24.98:5000'

    def request(self, text, **kwargs):
        params = {"text": text}
        params.update(kwargs)
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()

