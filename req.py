import json
import requests
import datetime

print(f"Введите название валюты и дату в формате (USD yyyy-mm-dd).\n" \
       f"Либо только валюту чтобы посмотреть курс к гривне на текущую дату.\n")

def func(n = input() .split()):
    if len(n) > 1:
        base, date = n
        url = f"https://api.apilayer.com/exchangerates_data/{date}&base={base}"
        payload = {}
        headers = {"apikey": "hJaF3GAvU5V4PCM7h5kQarz3l4x7NIBE"}
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code
        if status_code != 200:
            if len(base) == 3:
                for i in base:
                    if i.isdigit():
                        print("Wrong currency name.")
                        exit()
            else:
                print("Wrong currency name.")
                exit()
            print("The date is not supported.")
            exit()
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
        if status_code != 200:
            if len(base) == 3:
                for i in base:
                    if i.isdigit():
                        print("Wrong currency name.")
                        exit()
            else:
                print("Wrong currency name.")
                exit()
            print("The date is not supported.")
            exit()
        result = response.text
        JSON = json.loads(result)
        base_responce = JSON["base"]
        rate = JSON["rates"]["UAH"]
        print(f"{base_responce}\n{rate}")
func()












