import json
import requests
import datetime

info = (f"Введите название валюты и дату в формате (USD yyyy-mm-dd).\n" \
       f"Либо только дату чтобы посмотреть курс к гривне на текущую дату.\n")
print(info)

def func(n = input() .split()):
    if len(n) > 1:
        base, date = n
        url = f"https://api.apilayer.com/exchangerates_data/{date}&base={base}"
        payload = {}
        headers = {"apikey": "hJaF3GAvU5V4PCM7h5kQarz3l4x7NIBE"}
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.text
        JSON = json.loads(result)
        base_responce = JSON["base"]
        rate = JSON["rates"]["UAH"]
        print(f"{base_responce}\n{rate}")
    else:
        base = n[0]
        date = datetime.date.today()
        url = f"https://api.apilayer.com/exchangerates_data/{date}&base={base}"
        payload = {}
        headers = {"apikey": "hJaF3GAvU5V4PCM7h5kQarz3l4x7NIBE"}
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        result = response.text
        JSON = json.loads(result)
        base_responce = JSON["base"]
        rate = JSON["rates"]["UAH"]
        print(f"{base_responce}\n{rate}")
func()












