from coinbase.wallet.client import Client
import json
import requests

address = "sirvictor17@gail.com"
sender = "olumichael2015@outlook.com"
string_amount = '0.00000138'
amount = float(string_amount)

api_key = "qllinMZsWKJxMbm1"
secret_key = "O8166FUvpXgZk5XowalRE8cP0tVXRWkT"
ID ="98d51393-b7bf-5381-b727-21200c515708"


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
    checklist = [btc['id'], btc['currency'], float(btc['balance']['amount']), btc['primary'], btc['allow_withdrawals'],
                 btc['native_balance']['amount'],  btc['native_balance']['currency']]
    return checklist


def validate_checklist(check_lst):
    if check_lst[1] == 'BTC':
        if check_lst[3]:
            if check_lst[2] >= amount:
                if check_lst[4]:

                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
val = True

def send(c_v, val):

    if val:
        try:
            tx = c_v.send_money(ID, to=address, amount=amount, currency='BTC')
            sent = f'SENT {str(string_amount)}btc to {address} successfully!'
            print(tx)
            return sent

        except Exception as e:
            print(e, '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
            x = str(e)
            message = x.split(' ', 1)[1]

            return message



c_valid = client_validation(api_key, secret_key)
send(c_valid, val)

payload = {'amount': '0.00000138' , 'currency': 'XBT', 'address': 'chineduolu73@gmail.com', 'description': 'hr'}
r = requests.get('https://api.mybitx.com/api/1/send', params=payload)
sec_key = 'DADw2gjYH_dl9Kg6mLIMck8dqTSdfugJs9PYqYOdTXU'
key_id = 'k3ane3gbrr2pb'
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
try:
    rs = requests.post(r.url, auth=(key_id, sec_key)).json()
    print(rs)

except Exception as e:
    print(e,'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@' )
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')


def run():
    c_valid = client_validation(api_key, secret_key)
    check_list = get_check_list(c_valid)

    valid = validate_checklist(check_list)
    initiate_tx = send(c_valid, valid)

    print(initiate_tx)

