from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

r_kb_1 = ReplyKeyboardMarkup(resize_keyboard=True,
                             keyboard=[
                                 [
                                     KeyboardButton(text='Начать заново')
                                 ]
                             ]
                             )

r_kb_2 = ReplyKeyboardMarkup(resize_keyboard=True,
                             keyboard=[
                                 [
                                     KeyboardButton(text='Начать заново'),
                                     KeyboardButton(text='Тарифы')
                                 ]
                             ]
                             )

r_kb_admin = ReplyKeyboardMarkup(resize_keyboard=True,
                                 keyboard=[
                                 [
                                     KeyboardButton(text='PING'),
                                     KeyboardButton(text='База Полная'),
                                     KeyboardButton(text='ЛОГИ')
                                 ]
                                 ]
                                 )
