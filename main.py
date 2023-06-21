import logging
import pyrogram
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6029706415:AAEbxd9xooHfYUW4Op3OrX4cnxk4of6HrMw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    try:
        await bot.send_message('lvp_soon', 'Бот активирован новым человеком')
    except: pass
    kb = types.InlineKeyboardMarkup(3)
    kb.add(types.InlineKeyboardButton('Начать обучение', callback_data='next_1'))
    kb.add(types.InlineKeyboardButton('Задать вопрос трейдеру', url='t.me/yar_pro_trading'))
    kb.add(types.InlineKeyboardButton('Канал трейдера', url='https://t.me/+uRdHytS46iw3NjRi'))
    await message.answer_photo(types.InputFile('1.jpg'), """
ДОБРО ПОЖАЛОВАТЬ В МОЙ БЕСПЛАТНЫЙ АВТОРСКИЙ КУРС ПО ТОРГОВЛЕ БИНАРНЫМИ ОПЦИОНАМИ🥳

Меня зовут Ярослав Миров👋🏻

📌В ДАННОМ КУРСЕ ВЫ:

- Познакомитесь с основами торговли.
- Узнаете как перестать сливать депозит и системно его увеличивать.
- Как не ловить тильт (азарт).
- Изучите по шагам проверенную торговую стратегию.

Проходимость сделок по стратегии более 75%🔝💰

Стратегия работает на любом брокере, но рекомендую Quotex или Pocket Option, потому что они проверены временем.

🔗Если еще нет аккаунта на этих платформах, то можете зарегистрироваться сейчас👇🏻

Quotex.com
PocketOption.com

*Если какая-то из ссылок не откроется, сообщите мне.

*При возникновении вопросов по ходу изучения курса тоже можете писать. Проконсультирую👌

✍🏻Писать сюда - @yar_pro_trading 

Предлагаю приступить к обучению😎

Жмите на кнопку НАЧАТЬ ОБУЧЕНИЕ👇🏻""", reply_markup=kb)


@dp.callback_query_handler(text='next_1')
async def next_1(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(3)
    kb.add(types.InlineKeyboardButton('Следующий урок', callback_data='next_2'))
    kb.add(types.InlineKeyboardButton('Задать вопрос трейдеру', url='t.me/yar_pro_trading'))
    kb.add(types.InlineKeyboardButton('Trading View', url='https://tradingview.com/'))
    kb.add(types.InlineKeyboardButton('Investing', url='https://investing.com'))
    await callback.answer()
    await callback.message.answer_video('BAACAgIAAxkBAAMJZJKGSRYei4DVbp3IPz94NElIQOEAAnIzAAKLr4hIt34sW3m4lIIvBA', caption='''
📌1 УРОК.

ИЗ ДАННОГО УРОКА ВЫ УЗНАЕТЕ:

- Что такое график в трейдинге в принципе.

- Какие бывают типы графика и зачем они нужны.

- Что такое Фундаментальный анализ.

- Инструменты для Фундаментального анализа.

- Что такое Технический анализ.

- Инструменты Технического анализа.

✍️Если будут вопросы, пишите в лс - @yar_pro_trading''', reply_markup=kb)

@dp.callback_query_handler(text='next_2')
async def next_1(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(3)
    kb.add(types.InlineKeyboardButton('Следующий урок', callback_data='next_3'))
    kb.add(types.InlineKeyboardButton('Задать вопрос трейдеру', url='t.me/yar_pro_trading'))
    await callback.answer()
    await callback.message.answer_video('BAACAgIAAxkBAAMKZJKGklsl6p1EDQwblyEhXvX5wzkAAnszAAKLr4hI8819SVPAWtcvBA', caption='''
📌2 УРОК.

ИЗ ДАННОГО УРОКА ВЫ УЗНАЕТЕ:

- Что такое таймфрейм.

- Как работает таймфрейм.

- Какие бывают таймфреймы.

- Зачем нужны разные таймфреймы.

- Как переключать таймфреймы на платформе.

✍️Если будут вопросы, пишите в лс - @yar_pro_trading''', reply_markup=kb)

@dp.callback_query_handler(text='next_3')
async def next_1(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(3)
    kb.add(types.InlineKeyboardButton('Следующий урок', callback_data='next_4'))
    kb.add(types.InlineKeyboardButton('Задать вопрос трейдеру', url='t.me/yar_pro_trading'))
    await callback.answer()
    await callback.message.answer_video('BAACAgIAAxkBAAMLZJKGw3JfjC_z7Kaa-LNg61w37VUAAn0zAAKLr4hI-6fq0CkS8vIvBA', caption='''
📌3 УРОК.

ИЗ ДАННОГО УРОКА ВЫ УЗНАЕТЕ:

- Что такое время экспирации.

- Как работает время экспирации.

- Как переключать время экспирации на платформе.

✍️Если будут вопросы, пишите в лс - @yar_pro_trading''', reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)