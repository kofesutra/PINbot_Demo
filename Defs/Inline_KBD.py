from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

i_kb_1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='КОТИКИ!',
            callback_data='done'
        )
    ]
])

i_kb_2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Перейти в PINbot',
            url='http://t.me/pinanybot'
        )
    ]
])


# def build_inline(link):
#
#     inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#         [
#             InlineKeyboardButton(
#                 text='Перейти в PINbot',
#                 url=link
#             )
#         ]
#     ])
#     return inline_keyboard


def build_inline(link):

    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Перейти в PINbot',
                callback_data='done'
            )
        ]
    ])
    return inline_keyboard
