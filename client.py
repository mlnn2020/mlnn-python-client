import requests


class MlnnClient(object):
    base_url = 'http://mlnn.net/api'

    def request(self, text, **kwargs):
        params = {"text": text}
        params.update(kwargs)
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        return response.json()

