from coinbase.wallet.client import Client
import json
import time
api_key = "qllinMZsWKJxMbm1"
secret_key = "O8166FUvpXgZk5XowalRE8cP0tVXRWkT"


def client_validation(key, secret):
    client = Client(key, secret)
    return client


def get_check_list(client):
    account = client.get_account('BTC')
    file = open('id.json', 'w')
    json.dump(account, file)
    file.close()
    file_1 = open('id.json', 'r')
    btc = json.load(file_1)
    file.close()
    checklist = [btc['id'], btc['currency'], btc['balance']['amount'], btc['primary'], btc['allow_withdrawals'],
                 btc['native_balance']]

    return checklist


def create_address(btc_id, client):
    address = client.create_address(btc_id)
    return address


def address_record(add):
    file_a = open('addresses_record2.json', 'r')

    record_list = json.load(file_a)
    file_a.close()
    record_list.append(add)
    file_update = open('addresses_record2.json', 'w')
    json.dump(record_list, file_update)
    file_update.close()


def address_record_2(add):
    file_b = open('addresses.json', 'r')
    record_list = json.load(file_b)
    file_b.close()
    new_record = {'address': add[0], 'date_created': add[1]}
    record_list.append(new_record)
    file_update = open('addresses.json', 'w')
    json.dump(record_list, file_update)
    file_update.close()


def address_read(add):
    file_c = open('address_parser.json', 'w')
    json.dump(add, file_c)
    file_c.close()
    file_p = open('address_parser.json', 'r')
    adrss = json.load(file_p)
    file_p.close()
    address = adrss['address']
    date= adrss['created_at']
    return [address, date]


def run():
    time.sleep(1)
    c_valid = client_validation(api_key, secret_key)
    check_list = get_check_list(c_valid)
    btc_address = create_address(check_list[0], c_valid)
    main_address = address_read(btc_address)
    address_record_2(main_address)
    address_record(btc_address)
    print('address')
    return main_address[0]



