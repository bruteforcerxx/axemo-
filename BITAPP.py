
import json
import requests


secret_key = 'DADw2gjYH_dl9Kg6mLIMck8dqTSdfugJs9PYqYOdTXU'
key_id = 'k3ane3gbrr2pb'


def ask_user():
    destination = 'chineduolu73@gmail.com'
    amount = '0.00000133'
    order = [destination, amount, 'Tests']
    sim_add_to_pending(order)


def sim_add_to_pending(ordr):
    transit_list = []
    for x in range(7):
        file_a = open('pending_tx_list.json', 'r')
        pending_list = json.load(file_a)
        file_a.close()
        pending_list.append(ordr)
        transit_list.append(ordr)
        file_update = open('pending_tx_list.json', 'w')
        json.dump(pending_list, file_update)
        file_update.close()
    check_bal(transit_list)


def check_bal(tr_lst):
    payload = {'asset': 'XBT'}
    r = requests.get('https://api.mybitx.com/api/1/balance', params=payload)
    rs = requests.get(r.url, auth=(key_id, secret_key)).json()
    bal = rs['balance'][0]['balance']
    compare(tr_lst, bal)


def compare(tr, bal):
    total = 0
    for x in tr:
        total += float(x[1])
    check_if_sendable(tr, total, bal)


def check_if_sendable(tr, total, bal):
    print('INITIATING TRANSACTION...\n')
    if float(bal) > total:
        send(tr)
    else:
        print('INSUFFICIENT BALANCE!\n')
        request_funding(tr, total,bal)


def request_funding(tr, total, bal):
    print('SIMULATING CREATING ADDRESS AND WAITING FOR BTC...')
    balance = bal
    while bal == balance:
        print('checking balance...')
        payload = {'asset': 'XBT'}
        r = requests.get('https://api.mybitx.com/api/1/balance', params=payload)
        rs = requests.get(r.url, auth=(key_id, secret_key)).json()
        balance = rs['balance'][0]['balance']
        print(balance)
    print('ACCOUNT CREDITED!\n')
    print('RETRYING TRANSACTION...\n')
    check_if_sendable(tr, total, balance)


def send(tr):
    for x in tr:
        print(f'sending {x[1]}btc to {x[0]}...')
        payload = {'amount': x[1], 'currency': 'XBT', 'address': x[0], 'description': f'from {x[2]}'}
        r = requests.get('https://api.mybitx.com/api/1/send', params=payload)
        rs = requests.post(r.url, auth=(key_id, secret_key)).json()
        print(f'sent {x[1]}btc to {x[0]} successfully\n')


ask_user()


