import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6029706415:AAEbxd9xooHfYUW4Op3OrX4cnxk4of6HrMw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(372512859, 'Бот активирован новым человеком')
    kb = types.InlineKeyboardMarkup(3)
    kb.add(types.InlineKeyboardButton('НАЧАТЬ ОБУЧЕНИЕ ✅', callback_data='next_1'))
    kb.add(types.InlineKeyboardButton('ЗАДАТЬ ВОПРОС ТРЕЙДЕРУ🤔', url='t.me/yar_pro_trading'))
    kb.add(types.InlineKeyboardButton('КАНАЛ ТРЕЙДЕРА🌐', url='https://t.me/+uRdHytS46iw3NjRi'))
    await message.answer_photo(types.InputFile('1.jpg'), """
<b>ДОБРО ПОЖАЛОВАТЬ В МОЙ БЕСПЛАТНЫЙ АВТОРСКИЙ КУРС ПО ТОРГОВЛЕ БИНАРНЫМИ ОПЦИОНАМИ🥳</b>

Меня зовут Ярослав Миров👋🏻

<b>📌В ДАННОМ КУРСЕ ВЫ:</b>

- Познакомитесь с основами торговли.
- Узнаете как перестать сливать депозит и системно его увеличивать.
- Как не ловить тильт (азарт).
- Изучите по шагам проверенную торговую стратегию.

<b>Проходимость сделок по стратегии более 75%🔝💰</b>

Стратегия работает на любом брокере, но рекомендую <a href="https://quotex.com/sign-up/?lid=242171">Quotex</a> или <a href="https://pocketoption-official.com">Pocket Option</a>, потому что они проверены временем.

🔗Если еще нет аккаунта на этих платформах, то можете зарегистрироваться сейчас👇🏻

<a href="https://quotex.com/sign-up/?lid=242171">Quotex.com</a>
<a href="https://pocketoption-official.com">PocketOption.com</a>

*Если какая-то из ссылок не откроется, сообщите мне.

*При возникновении вопросов по ходу изучения курса тоже можете писать. Проконсультирую👌

<b>✍🏻Писать сюда</b> - @yar_pro_trading 

Предлагаю приступить к обучению😎

Жмите на кнопку <b>НАЧАТЬ ОБУЧЕНИЕ👇🏻</b>""", reply_markup=kb)


@dp.callback_query_handler(text='next_1')
async def next_1(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(3)
    kb.add(types.InlineKeyboardButton('СЛЕДУЮЩИЙ УРОК➡️', callback_data='next_2'))
    kb.add(types.InlineKeyboardButton('ЗАДАТЬ ВОПРОС ТРЕЙДЕРУ🤔', url='t.me/yar_pro_trading'))
    kb.add(types.InlineKeyboardButton('TradingView📈', url='https://tradingview.com/'))
    kb.add(types.InlineKeyboardButton('Investing📰', url='https://investing.com'))
    await callback.answer()
    await callback.message.answer_video('BAACAgIAAxkBAAMJZJKGSRYei4DVbp3IPz94NElIQOEAAnIzAAKLr4hIt34sW3m4lIIvBA', caption='''
<b>📌1 УРОК.

ИЗ ДАННОГО УРОКА ВЫ УЗНАЕТЕ</b>:

- Что такое график в трейдинге в принципе.

- Какие бывают типы графика и зачем они нужны.

- Что такое Фундаментальный анализ.

- Инструменты для Фундаментального анализа.

- Что такое Технический анализ.

- Инструменты Технического анализа.

<b>✍️Если будут вопросы, пишите в лс -</b> @yar_pro_trading''', reply_markup=kb)

@dp.callback_query_handler(text='next_2')
async def next_1(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(3)
    kb.add(types.InlineKeyboardButton('СЛЕДУЮЩИЙ УРОК➡️', callback_data='next_3'))
    kb.add(types.InlineKeyboardButton('ЗАДАТЬ ВОПРОС ТРЕЙДЕРУ🤔', url='t.me/yar_pro_trading'))
    await callback.answer()
    await callback.message.answer_video('BAACAgIAAxkBAAMKZJKGklsl6p1EDQwblyEhXvX5wzkAAnszAAKLr4hI8819SVPAWtcvBA', caption='''
<b>📌2 УРОК.

ИЗ ДАННОГО УРОКА ВЫ УЗНАЕТЕ:</b>

- Что такое таймфрейм.

- Как работает таймфрейм.

- Какие бывают таймфреймы.

- Зачем нужны разные таймфреймы.

- Как переключать таймфреймы на платформе.

<b>✍️Если будут вопросы, пишите в лс -</b> @yar_pro_trading''', reply_markup=kb)

@dp.callback_query_handler(text='next_3')
async def next_1(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(3)
    kb.add(types.InlineKeyboardButton('СЛЕДУЮЩИЙ УРОК➡️', callback_data='next_4'))
    kb.add(types.InlineKeyboardButton('ЗАДАТЬ ВОПРОС ТРЕЙДЕРУ🤔', url='t.me/yar_pro_trading'))
    await callback.answer()
    await callback.message.answer_video('BAACAgIAAxkBAAMLZJKGw3JfjC_z7Kaa-LNg61w37VUAAn0zAAKLr4hI-6fq0CkS8vIvBA', caption='''
<b>📌3 УРОК.

ИЗ ДАННОГО УРОКА ВЫ УЗНАЕТЕ:</b>

- Что такое время экспирации.

- Как работает время экспирации.

- Как переключать время экспирации на платформе.

<b>✍️Если будут вопросы, пишите в лс -</b> @yar_pro_trading''', reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)