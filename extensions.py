import json
import requests

from config import keys, TOKEN


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_prise(quote:str, base:str, amount:str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработеть валюту {quote}.')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количство{amount}')
        r = requests.get(f'https://api.exchangerate.host/convert?from={keys[quote]}&to={keys[base]}&amount={amount}')
        total_base = json.loads(r.content)[keys[base]]

