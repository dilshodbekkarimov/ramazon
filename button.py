from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from api import *


def menu():
    button = ['Bugungi kun uchun taqvimni olish','Shu haftalik taqvimni olish','Bir oylik taqvimni olish']
    button_key = ReplyKeyboardMarkup(row_width=2)
    for i in button:
        button_key.insert(
            InlineKeyboardButton(text=i)
            )
    return button_key

def region():
    city = {
        "Toshkent": 'toshkent',
        "Qarshi": 'qarshi',
        "Denov": 'denov',
        "Samarqand": 'samarqand',
        "Jizzax": 'jizzax',
        "Guliston": 'guliston',
        "Farg'ona": "farg'ona",
        "Nmanagan": 'namangan',
        "Andijon": 'andijon',
        "Buxoro": 'buxoro',
        "Navoiy": 'navoiy',
        "Xorazim": 'xiva',
        "Nukis": 'nukus',
        
    }
    city_key = InlineKeyboardMarkup(row_width=2)
    for i, value in city.items():
        city_key.insert(
            InlineKeyboardButton(text=i, callback_data=f"region_{value}")
            )
    return city_key


def region_week():
    city = {
        "Toshkent": 'toshkent',
        "Qarshi": 'qarshi',
        "Denov": 'denov',
        "Samarqand": 'samarqand',
        "Jizzax": 'jizzax',
        "Guliston": 'guliston',
        "Farg'ona": "farg'ona",
        "Nmanagan": 'namangan',
        "Andijon": 'andijon',
        "Buxoro": 'buxoro',
        "Navoiy": 'navoiy',
        "Xorazim": 'xiva',
        "Nukis": 'nukus',
        
    }
    city_key = InlineKeyboardMarkup(row_width=2)
    for i, value in city.items():
        city_key.insert(
            InlineKeyboardButton(text=i, callback_data=f"region_week_{value}")
            )
    return city_key


def region_monthly():
    city = {
        "Toshkent": 'toshkent',
        "Qarshi": 'qarshi',
        "Denov": 'denov',
        "Samarqand": 'samarqand',
        "Jizzax": 'jizzax',
        "Guliston": 'guliston',
        "Farg'ona": "farg'ona",
        "Nmanagan": 'namangan',
        "Andijon": 'andijon',
        "Buxoro": 'buxoro',
        "Navoiy": 'navoiy',
        "Xorazim": 'xiva',
        "Nukis": 'nukus',
        
    }
    city_key = InlineKeyboardMarkup(row_width=2)
    for i, value in city.items():
        city_key.insert(
            InlineKeyboardButton(text=i, callback_data=f"region_monthly_{value}")
            )
    return city_key