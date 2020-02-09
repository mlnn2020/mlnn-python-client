import client
from pprint import pprint


if __name__ == '__main__':
    print('Calling language detection API endpoint on the url:')
    mlnnClient = client.MlnnClient()
    response = mlnnClient.request(text='Русский язык')
    print('Printing response:')
    pprint(response)

