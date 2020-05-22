import requests


secret_key = 'DADw2gjYH_dl9Kg6mLIMck8dqTSdfugJs9PYqYOdTXU'
key_id = 'k3ane3gbrr2pb'
string_amount = '0.00000027'
address = 'chineduolu73@gmail.com'
des = f'sent {string_amount} to {address}'


def send_bitcoin():
    payload = {'amount': string_amount, 'currency': 'XBT', 'address': address, 'description': des}
    r = requests.get('https://api.mybitx.com/api/1/send', params=payload)
    print(r.url)
    rs = requests.post(r.url, auth=(key_id, secret_key)).json()
    return rs


def run():
    response = send_bitcoin()
    print(response)



