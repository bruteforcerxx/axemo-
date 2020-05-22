from coinbase.wallet.client import Client
import json
import requests


api_key = "qllinMZsWKJxMbm1"
secret_key = "O8166FUvpXgZk5XowalRE8cP0tVXRWkT"
notification_url = "https://ponzi.herokuapp.com/api/notifications_list"


def start_from():
    file_1 = open('pagination_id_list.json', 'r')
    ids = json.load(file_1)
    file_1.close()
    return ids[0]


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
    checklist = btc['id']
    return checklist


def get_tx_list(client, acc_id, s):
    txs = client.get_transactions(acc_id, limit=100, order='asc', starting_after=s)
    return txs


def save_tx_list(t_list):
    file_1 = open('pagination.json', 'r')
    tx_lst = json.load(file_1)
    file_1.close()
    tx_lst.append(t_list)

    file = open('pagination.json', 'w')
    json.dump(tx_lst, file)
    file.close()


def parse_tx_list(tx_list):

    file = open('Tx_list.json', 'w')
    json.dump(tx_list, file)
    file.close()
    file_1 = open('Tx_list.json', 'r')
    txs = json.load(file_1)
    file_1.close()

    for i in txs['data']:
        for k, v in i.items():
            if k == 'to' in i:
                file_1 = open('send_tx.json', 'r')
                txs = json.load(file_1)
                file_1.close()
                rs = i['to']
                for c, d in rs.items():
                    if c == 'email':
                        data_1 = [i['id'], i['status'], i['amount']['amount'], rs['email']]
                        txs.append(data_1)
                        file = open('send_tx.json', 'w')
                        json.dump(txs, file)
                        file.close()
                        final_tx_confirmation(data_1)
                    elif c == 'address':
                        data_1 = [i['id'], i['status'], i['amount']['amount'], rs['address']]
                        txs.append(data_1)
                        file = open('send_tx.json', 'w')
                        json.dump(txs, file)
                        file.close()

                        final_tx_confirmation(data_1)
            elif k == 'from' in i:
                file_2 = open('receive_tx.json', 'r')
                txs = json.load(file_2)
                file_1.close()
                rs = i['details']
                if rs['subtitle'] != 'From Bitcoin address':
                    data_1 = [i['id'], i['status'], i['amount']['amount'], rs['subtitle']]
                    txs.append(data_1)
                    file = open('receive_tx.json', 'w')
                    json.dump(txs, file)
                    file.close()
                    final_tx_confirmation(data_1)


def get_notification_list(url):
    r = requests.get(url).json()
    return r


def save_notification(n_list):

    file_1 = open('notif_tx_id.json', 'r')
    old_ids = json.load(file_1)
    file_1.close()

    for i in n_list['data']:
        if i['id'] not in old_ids:
            old_ids.append(i['id'])

            file = open('notif_tx_id.json', 'w')
            json.dump(old_ids, file)
            file.close()
            get_useful_data_url(i)


def get_useful_data_url(l):
    u_data = [l['id'], l['type'], l['additional_data']['amount']['amount'], l['data']['address']]
    final_tx_confirmation(u_data)


def final_tx_confirmation(data):
    bal = float(data[2])
    if bal > 0.00000000:
        print(f'CREDIT ALERT! OF {data[2]}btc FROM {data[3]}\n')
        final_receive_data_save(data)
    elif bal < 0.00000000:
        print(F'DEBIT ALERT!, SENT {data[2][1:]}btc TO {data[3]}\n')
        final_send_data_save(data)


def final_receive_data_save(f_list):
    file_1 = open('final_receive_data_save.json', 'r')
    saved_list = json.load(file_1)
    file_1.close()
    if f_list not in saved_list:
        saved_list.append(f_list)
        file = open('final_receive_data_save.json', 'w')
        json.dump(saved_list, file)
        file.close()


def final_send_data_save(f_list):
    file_1 = open('final_send_data_save.json', 'r')
    saved_list = json.load(file_1)
    file_1.close()
    if f_list not in saved_list:
        saved_list.append(f_list)
        file = open('final_send_data_save.json', 'w')
        json.dump(saved_list, file)
        file.close()


def save_pagination_id(tx_list):
    id = tx_list['data']
    file_1 = open('pagination_id_list.json', 'r')
    ids = json.load(file_1)
    file_1.close()
    for p in id:
        i = p['id']
        if i not in ids:
            ids.insert(0, i)
    file = open('pagination_id_list.json', 'w')
    json.dump(ids, file)
    file.close()


def print_balance():
    file = open('id.json', 'r')
    btc = json.load(file)
    file.close()
    b = btc['balance']['amount']
    print(f'BALANCE: {b}')


def run():
    sf = start_from()
    c_valid = client_validation(api_key, secret_key)
    btc_id = get_check_list(c_valid)
    txs_list = get_tx_list(c_valid, btc_id, sf)
    save_tx_list(txs_list)
    parse_tx_list(txs_list)
    new_lst = get_notification_list(notification_url)
    save_pagination_id(txs_list)
    save_notification(new_lst)
    get_check_list(c_valid)
    print_balance()

