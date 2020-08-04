import client
from pprint import pprint
import nltk.data

if __name__ == '__main__':
    mlnnClient = client.MlnnClient()
    text = '''Ульяновская «Волга», чьими партнерами являются администрации Ульяновска и Ульяновской области, а титульным спонсором выступает Ульяновский станкостроительный завод (DMG MORI), занимает 8-е место в зоне «Урал-Поволжье» ПФЛ в текущем сезоне.'''

    print('NER SMI:')
    response = mlnnClient.ner_smi(text=text)
    pprint(response)

    print('NER ARB:')
    response = mlnnClient.ner_arb(text=text)
    pprint(response)

    print('LangDet:')
    response = mlnnClient.langdet(text=text)
    pprint(response)
