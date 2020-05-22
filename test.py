from coinbase.wallet.client import Client
from tkinter import *
from tkinter.ttk import *
from threading import Thread
import queue
import json
import requests
import time


root = Tk()
root.resizable(False, False)
root.geometry("750x550")

style = Style()
style.configure('W.TButton', font=('Calibri', 30))

logo = PhotoImage(file='photos/logo.png')
logo2 = PhotoImage(file='photos/logo2.png')
ex = PhotoImage(file='photos/exc.png')
sc = PhotoImage(file='photos/success.png')
sn = PhotoImage(file='photos/send.png')
rc = PhotoImage(file='photos/recive.png')

api_key = "qllinMZsWKJxMbm1"
secret_key = "O8166FUvpXgZk5XowalRE8cP0tVXRWkT"
coinbase_id = "98d51393-b7bf-5381-b727-21200c515708"
client = Client(api_key, secret_key)
sent = False
file_1 = open('axemo_bal.json', 'r')
bt_bal = json.load(file_1)
file_1.close()
btc_bal = f"{bt_bal:.5f}"
am_btc = input('btc: ')
am_btc = float(am_btc)
am_ngn = input('ngn: ')
am_ngn = float(am_ngn)
price = client.get_buy_price(currency_pair='BTC-NGN')
if am_btc:
    ng = float(am_btc) * float(price['amount'])
    ngn = f"{ng:.2f}"
    name = Label(root, text=f'NGN{ngn}    /    {am_btc}btc')
    name.config(background='white', foreground='purple', font=('Calibri', 15))
    name.place(x=150, y=314)
    print(f'NGN{ngn}    /    {am_btc}btc')
elif am_ngn:
    btc = float(am_ngn) / float(price['amount'])
    print(btc)
    print(price['amount'])
    btc = f"{btc:.8f}"
    name = Label(root, text=f'NGN{am_ngn}    /    {btc}btc')
    name.config(background='white', foreground='purple', font=('Calibri', 15))
    name.place(x=150, y=314)
    print(f'NGN{am_ngn}    /    {btc}btc')
else:
    name = Label(root, text=f'NGN{0.00}    /    {0.00000000}btc')
    name.config(background='white', foreground='purple', font=('Calibri', 15))
    name.place(x=150, y=314)





am_btc = 0.00
am_ngn = 3

price = client.get_buy_price(currency_pair='BTC-NGN')
if am_btc:
    ng = float(am_btc) * float(price['amount'])
    ngn = f"{ng:.2f}"
elif am_ngn:
    btc = float(am_ngn) / float(price['amount'])
    ngn = f"{ng:.2f}"


