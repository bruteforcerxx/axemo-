import requests
import json

secret_key = 'DADw2gjYH_dl9Kg6mLIMck8dqTSdfugJs9PYqYOdTXU'
key_id = 'k3ane3gbrr2pb'


def generate_address():
    payload = {'asset': 'XBT'}
    r = requests.get('https://api.mybitx.com/api/1/funding_address', params=payload)
    rs = requests.get(r.url, auth=(key_id, secret_key)).json()
    return rs


def save_address_info(i):
    file_b = open('save_address_info.json', 'r')
    record_list = json.load(file_b)
    file_b.close()
    if i not in record_list:
        record_list.append(i)
    file_update = open('save_address_info.json', 'w')
    json.dump(record_list, file_update)
    file_update.close()


def extract_address(i):
    btc_address = i['address']
    id = i['account_id']
    return [btc_address, id]


def save_pure_address(ad):
    file_b = open('luno_pure_addresses.json', 'r')
    record_list = json.load(file_b)
    file_b.close()
    new_record = {'address': ad[0], 'account_id': ad[1]}
    if new_record not in record_list:
        record_list.append(new_record)
    file_update = open('luno_pure_addresses.json', 'w')
    json.dump(record_list, file_update)
    file_update.close()


def run():
    info = generate_address()
    save_address_info(info)
    address = extract_address(info)
    save_pure_address(address)
    print(f'Address: {address[0]}')

