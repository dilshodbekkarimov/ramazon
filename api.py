import requests
import json
import button.py

url = 'https://islomapi.uz/api'

def get_today(city):
    http = f'{url}/present/day?region={city}'
    r = requests.get(http)
    return r.json()




def get_weekday(city):
    http = f'{url}/present/week?region_week={city}'
    r = requests.get(http)
    return r.json()


 
def get_monthly(city):
    http = f'{url}/present/monthly?region={city}'
    r = requests.get(http)
    return r.json()


def user_create(username, telegram_id):
    http = f'{url}/user_create/'
    r = requests.post(http, data={
        "username": username,
        "telegram_id": telegram_id
        })
    # print(r.status_code)

    if r.status_code == 201:
        return True
    else:
        return False

    user_create('ssssaaaa', 878045048)