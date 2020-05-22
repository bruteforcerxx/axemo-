import requests


secret_key = 'DADw2gjYH_dl9Kg6mLIMck8dqTSdfugJs9PYqYOdTXU'
key_id = 'k3ane3gbrr2pb'
acc_id = 8130065625073981777


def get_tx_list():
    payload = {'min_row': -5, 'max_row': 0}
    r = requests.get(f'https://api.mybitx.com/api/1/accounts/{acc_id}/transactions', params=payload)
    print(r.url)
    rs = requests.get(r.url, auth=(key_id, secret_key)).json()
    return rs


def run():
    response = get_tx_list()
    for i in tx:
        print(i)
        print(
            '###################################################################################################################')

run()