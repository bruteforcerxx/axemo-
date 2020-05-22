from coinbase.wallet.client import Client
from tkinter import *
from tkinter.ttk import *
from threading import Thread
import queue
import json
import requests
import time


api_key = "qllinMZsWKJxMbm1"
secret_key = "O8166FUvpXgZk5XowalRE8cP0tVXRWkT"
coinbase_id = "98d51393-b7bf-5381-b727-21200c515708"
client = Client(api_key, secret_key)
sent = False
file_1 = open('axemo_bal.json', 'r')
bt_bal = json.load(file_1)
file_1.close()
btc_bal = f"{bt_bal:.5f}"

root = Tk()
root.resizable(False, False)
root.geometry("750x550")

style = Style()
style.configure('W.TButton', font=('Calibri', 30))

logo = PhotoImage(file='photos/logo.png')
logo2 = PhotoImage(file='photos/logo2.png')
ex = PhotoImage(file='photos/exc.png')
sc = PhotoImage(file='photos/success.png')


x = ''

print(float(x))
