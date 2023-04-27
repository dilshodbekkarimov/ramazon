"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types
from button import *
from api import *
from bot import admin
from aiogram.dispatcher.filters import Text
API_TOKEN = 'admin'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    markup = menu()
    
    await message.reply("Assalomu alaykum hurmatli foydalanuvchi sizga kerakli taqvim vaqtini tanlang ", reply_markup=markup)









@dp.message_handler(text='Bugungi kun uchun taqvimni olish')
async def echo(message: types.Message):
    markup = region()
    await message.answer("o'zingiz joylashgan shahar yoki o'zingizga yaqin bo'lgan shaharni tanlang!!!", reply_markup=markup)



@dp.message_handler(text='Shu haftalik taqvimni olish')
async def echo(message: types.Message):
    markup = region_week()
  
    await message.answer("o'zingiz joylashgan shahar yoki o'zingizga yaqin bo'lgan shaharni tanlang!!!", reply_markup=markup)


@dp.message_handler(text='Bir oylik taqvimni olish')
async def echo(message: types.Message):
    markup = region_monthly()
 
    await message.answer("o'zingiz joylashgan shahar yoki o'zingizga yaqin bo'lgan shaharni tanlang!!!", reply_markup=markup)


@dp.callback_query_handler(Text(startswith='region_'))
async def echo(c: types.CallbackQuery):
    inx = c.data.index('_')
    region =c.data[inx+1:]
    data = get_today(region)
    info = f"""
Shahar: {data['region']}
Sana: {data['date']}
Hafta kuni: {data['weekday']}b 
Bomdod: {data['times']['tong_saharlik']}
Quyosh: {data['times']['quyosh']}
Peshin: {data['times']['peshin']}
Asir: {data['times']['asr']}
Shom_iftor: {data['times']['shom_iftor']}
Hufton: {data['times']['hufton']}
    
    """
    await c.message.answer(info)


@dp.callback_query_handler(Text(startswith='region_week_'))
async def echo(c: types.CallbackQuery):
    inx = c.data.index('_')
    region_week =c.data[inx+1:]
    data = get_weekday(region_week)
    info = f"""
Shahar: {data['region']}
Sana: {data['date']}
Hafta kuni: {data['weekday']}
Bomdod: {data['times']['tong_saharlik']}
Quyosh: {data['times']['quyosh']}
Peshin: {data['times']['peshin']}
Asir: {data['times']['asr']}
Shom_iftor: {data['times']['shom_iftor']}
Hufton: {data['times']['hufton']}
    
    """
    await c.message.answer(info)

@dp.callback_query_handler(Text(startswith='region_monthly_'))
async def echo(c: types.CallbackQuery):
    inx = c.data.index('_')
    region_monthly =c.data[inx+1:]
    data = get_monthly(region_monthly)
    info = f"""
Shahar: {data['region']}
Sana: {data['date']}
Hafta kuni: {data['weekday']}
Bomdod: {data['times']['tong_saharlik']}
Quyosh: {data['times']['quyosh']}
Peshin: {data['times']['peshin']}
Asir: {data['times']['asr']}
Shom_iftor: {data['times']['shom_iftor']}
Hufton: {data['times']['hufton']}
    """
    return await  c.message.answer(info)
 
    # await message.answer(message.text)












if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)