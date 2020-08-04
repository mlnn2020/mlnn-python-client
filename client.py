import requests

class MlnnClient(object):

    base_url = 'http://185.195.24.98:'

    def langdet(self, text):
        port = '8891'
        return self.request(text, port)

    def ner_smi(self, text):
        port = '8888'
        return self.request(text, port)

    def ner_arb(self, text):
        port = '8889'
        return self.request(text, port)

    def request(self, text, port, **kwargs):
        url = self.base_url + port
        response = requests.post(url, json={"text": text})
        response.raise_for_status()
        return response.json()

