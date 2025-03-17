from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


import matplotlib as plt

first_button_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Меню")]
], resize_keyboard=True, one_time_keyboard=True)

#МЕНЮ..............................................................................
main_inlines_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Чем заняться❓", callback_data="Zanatie")],
    [InlineKeyboardButton(text="Вопрос онлайн-гиду 👨‍💻", callback_data="QuestionsAI")],
    [InlineKeyboardButton(text="Погода 🌤", callback_data="weather",)],
    [InlineKeyboardButton(text="Карта Екатеринбурга 🌍", callback_data="Map", url="https://yandex.ru/maps/org/yeltsin_tsentr/1676805608/?ll=60.591528%2C56.844913&z=14")],
])


#Чем заняться////////////////////////////////////////////////////////////////////////////////////////
second_inlines_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Прогуляться 🚶", callback_data="progulka")],
    [InlineKeyboardButton(text="Отдохнуть 💆", callback_data="otdyx")],
    [InlineKeyboardButton(text="Поесть 🍽", callback_data="eda")]
])

#Прогуляться
progulka_inlines_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Туристические маршруты по городу 🥾", callback_data="tyr")],
    [InlineKeyboardButton(text="Ознакомительная прогулка 🔎", callback_data="ozn_progulka")],
])

#Туристические маршруты (линии)
tyr_inlines_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Достопримечательности (красная линия)🔴", callback_data="red_line")],
    [InlineKeyboardButton(text="Стрит арт (фиолетовая линия)🟣", callback_data="purple_line")],
    [InlineKeyboardButton(text="Храмы (синяя линия)🔵", callback_data="blue_line")]
])

#Ознакомительная прогулка
ozn_progulka_inlines_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Прогулка по живописным местам 🌇", callback_data="ziv_mest")],
    [InlineKeyboardButton(text="Фото-прогулка 📸", callback_data="foto_prog")],
])


#Отдохнуть////////////////////////////////////////////////////////////////////////////////////////
otdyx_inlines_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Культурно-досуговые заведения 🙋", callback_data="kut_zaved")],
    [InlineKeyboardButton(text="Развлечения 🎡", callback_data="razvet")],
])

#Культурно-досуговые заведения
kut_zaved_inlines_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Музеи 🏛", callback_data="Musem")],
    [InlineKeyboardButton(text="Театры 🎭", callback_data="Theat")],
    [InlineKeyboardButton(text="Галереи 🎨", callback_data="Galery")]
])

#Поесть////////////////////////////////////////////////////////////////////////////////////////
eda_inlines_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Рестораны и кафе 🍛", callback_data="rest")],
    [InlineKeyboardButton(text="Фаст-фуд рестораны 🍟", callback_data="fast_fud")],
])




ai_button_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Начать новый диалог")],
    [KeyboardButton(text="Вернуться в меню")]
], resize_keyboard=True, one_time_keyboard=True)

lol_button_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Начать новый диалог")],
    [KeyboardButton(text="Вернуться в меню")]
], resize_keyboard=True, one_time_keyboard=True)