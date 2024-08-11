import asyncio

from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from Defs.Config import CHANNEL
from Defs.Inline_KBD import i_kb_1, build_inline, i_kb_2
from Defs.Reply_KBD import r_kb_1, r_kb_2
from Defs.State_Machine import States


async def run_demo(message: Message, state: FSMContext, bot: Bot, user_id_here):
    # Динамическая ссылка на ПИНбота
    data = await state.get_data()
    link = data['link']
    kb_builded = build_inline(link)

    await message.answer('Как работает PINbot?', reply_markup=r_kb_1)
    await asyncio.sleep(2)

    await bot.copy_message(user_id_here, CHANNEL, 9)
    await asyncio.sleep(5)
    data = await bot.copy_message(user_id_here, CHANNEL, 50, disable_notification=True)  # Текстовый закреп
    mess_id = data.message_id
    await asyncio.sleep(2)
    await bot.copy_message(user_id_here, CHANNEL, 11, disable_notification=True)
    await asyncio.sleep(5)
    await bot.delete_message(user_id_here, mess_id)
    await asyncio.sleep(2)
    data = await bot.copy_message(user_id_here, CHANNEL, 50, disable_notification=True)  # Текстовый закреп
    mess_id = data.message_id
    await asyncio.sleep(2)

    await bot.copy_message(user_id_here, CHANNEL, 14, disable_notification=True)
    await asyncio.sleep(5)
    await bot.delete_message(user_id_here, mess_id)
    await asyncio.sleep(2)
    data = await bot.copy_message(user_id_here, CHANNEL, 50, disable_notification=True)  # Текстовый закреп
    mess_id = data.message_id
    await asyncio.sleep(2)

    await bot.copy_message(user_id_here, CHANNEL, 16, disable_notification=True)
    await asyncio.sleep(5)
    await bot.delete_message(user_id_here, mess_id)
    await asyncio.sleep(2)
    data = await bot.copy_message(user_id_here, CHANNEL, 37, disable_notification=True)
    mess_id = data.message_id
    await bot.edit_message_reply_markup(user_id_here, mess_id, reply_markup=i_kb_1)  # Котики
    await asyncio.sleep(2)

    await bot.copy_message(user_id_here, CHANNEL, 18, disable_notification=True)
    await asyncio.sleep(5)
    await bot.delete_message(user_id_here, mess_id)
    await asyncio.sleep(2)
    data = await bot.copy_message(user_id_here, CHANNEL, 37, disable_notification=True)
    mess_id = data.message_id
    await bot.edit_message_reply_markup(user_id_here, mess_id, reply_markup=i_kb_1)  # Котики
    await asyncio.sleep(2)

    await bot.copy_message(user_id_here, CHANNEL, 20, disable_notification=True)
    await asyncio.sleep(5)
    await bot.delete_message(user_id_here, mess_id)
    await asyncio.sleep(2)
    data = await bot.copy_message(user_id_here, CHANNEL, 38, disable_notification=True)
    mess_id = data.message_id
    await bot.edit_message_reply_markup(user_id_here, mess_id, reply_markup=kb_builded)  # ПИНбот
    await asyncio.sleep(2)

    await bot.copy_message(user_id_here, CHANNEL, 22, disable_notification=True)
    await asyncio.sleep(5)
    await bot.delete_message(user_id_here, mess_id)
    await asyncio.sleep(2)
    data = await bot.copy_message(user_id_here, CHANNEL, 38, disable_notification=True)
    mess_id = data.message_id
    await bot.edit_message_reply_markup(user_id_here, mess_id, reply_markup=kb_builded)  # ПИНбот
    await asyncio.sleep(2)

    await bot.copy_message(user_id_here, CHANNEL, 24, disable_notification=True)
    await asyncio.sleep(5)
    await bot.delete_message(user_id_here, mess_id)
    await asyncio.sleep(2)
    data = await bot.copy_message(user_id_here, CHANNEL, 25, disable_notification=True)
    mess_id = data.message_id
    await asyncio.sleep(2)

    await bot.copy_message(user_id_here, CHANNEL, 26, disable_notification=True)
    await asyncio.sleep(5)
    await bot.delete_message(user_id_here, mess_id)
    await asyncio.sleep(2)
    data = await bot.copy_message(user_id_here, CHANNEL, 25, disable_notification=True)
    mess_id = data.message_id
    await asyncio.sleep(2)

    await bot.copy_message(user_id_here, CHANNEL, 28, disable_notification=True)
    await asyncio.sleep(5)
    await bot.delete_message(user_id_here, mess_id)
    await asyncio.sleep(2)
    data = await bot.copy_message(user_id_here, CHANNEL, 25, disable_notification=True)
    mess_id = data.message_id
    await asyncio.sleep(2)

    await bot.copy_message(user_id_here, CHANNEL, 30, disable_notification=True)
    await asyncio.sleep(5)
    await bot.delete_message(user_id_here, mess_id)
    await asyncio.sleep(2)
    data = await bot.copy_message(user_id_here, CHANNEL, 38, disable_notification=True)
    mess_id = data.message_id
    await bot.edit_message_reply_markup(user_id_here, mess_id, reply_markup=kb_builded)  # ПИНбот
    await asyncio.sleep(2)

    await bot.copy_message(user_id_here, CHANNEL, 32, disable_notification=True)
    await asyncio.sleep(5)
    await bot.delete_message(user_id_here, mess_id)
    await asyncio.sleep(2)
    data = await bot.copy_message(user_id_here, CHANNEL, 38, disable_notification=True)
    mess_id = data.message_id
    await bot.edit_message_reply_markup(user_id_here, mess_id, reply_markup=kb_builded)  # ПИНбот
    await asyncio.sleep(2)

    await bot.copy_message(user_id_here, CHANNEL, 39)
    await asyncio.sleep(3)
    await bot.copy_message(user_id_here, CHANNEL, 43, disable_notification=True)
    await asyncio.sleep(5)
    # await bot.delete_message(user_id_here, mess_id)
    # await asyncio.sleep(2)
    # data = await bot.copy_message(user_id_here, CHANNEL, 38)
    # mess_id = data.message_id
    # await bot.edit_message_reply_markup(user_id_here, mess_id, reply_markup=kb_builded)  # ПИНбот
    # await asyncio.sleep(5)

    await bot.copy_message(user_id_here, CHANNEL, 44, disable_notification=True)
    await asyncio.sleep(3)
    await bot.copy_message(user_id_here, CHANNEL, 45, disable_notification=True)
    await asyncio.sleep(5)
    # await bot.delete_message(user_id_here, mess_id)
    # await asyncio.sleep(2)
    # data = await bot.copy_message(user_id_here, CHANNEL, 38)
    # mess_id = data.message_id
    # await bot.edit_message_reply_markup(user_id_here, mess_id, reply_markup=kb_builded)  # ПИНбот
    # await asyncio.sleep(5)

    await bot.copy_message(user_id_here, CHANNEL, 46, disable_notification=True)
    await asyncio.sleep(3)
    await bot.copy_message(user_id_here, CHANNEL, 47, disable_notification=True)
    await asyncio.sleep(5)
    # await bot.delete_message(user_id_here, mess_id)
    # await asyncio.sleep(2)
    data = await bot.copy_message(user_id_here, CHANNEL, 38, disable_notification=True)
    mess_id = data.message_id
    # await bot.edit_message_reply_markup(user_id_here, mess_id, reply_markup=kb_builded)  # ПИНбот
    await asyncio.sleep(2)

    await bot.copy_message(user_id_here, CHANNEL, 48, disable_notification=True)
    await asyncio.sleep(5)
    await bot.delete_message(user_id_here, mess_id)
    # await asyncio.sleep(2)
    # data = await bot.copy_message(user_id_here, CHANNEL, 38)
    # mess_id = data.message_id
    # await bot.edit_message_reply_markup(user_id_here, mess_id, reply_markup=kb_builded)  # ПИНбот
    await asyncio.sleep(2)

    await state.set_state(States.end)
    await end_of_demo(message, state, bot)


async def end_of_demo(message: Message, state: FSMContext, bot: Bot):
    id_here = message.chat.id
    await bot.send_message(id_here, 'Условия подписки - нажми кнопку "Тарифы" внизу экрана', reply_markup=r_kb_2)
    await bot.copy_message(id_here, CHANNEL, 51, reply_markup=i_kb_2)  # Всё


async def tarifs(message: Message, state: FSMContext, bot: Bot):
    await message.answer('🟢 Как получить доступ к сервису PINbota?\n'
                                         'Доступ к сервису осуществляется через платную подписку по реферальным ссылкам партнерской программы\n\n'
                                         '🟠 Сколько стоит подписка?\n'
                                         'Стоимость подписки со скидкой в 40% по реферальной партнерской ссылке - 1020 рублей в месяц\n\n'
                                         '🟣 Как стать партнером?\n'
                                         'При оплате доступа на 3 месяца в сумме 3060 рублей пользователь Сервиса PINbot автоматически становится ПАРТНЕРОМ и будет получать вознаграждение в размере 15% от платежей новых подписчиков пришедших по его реферальной ссылке\n\n'
                                         '🔴 Бонусы для пользователей Сервиса PINbot\n'
                                         '- Ознакомительная бесплатная подписка на PINbot на 7 дней\n'
                                         '- При  оплате подписки на 6 мес дополнительная скидка 10% - 5508 рублей (918 руб/мес)\n'
                                         '- При оплате годовой подписки (12 мес) дополнительная скидка 20% - 9792 (816 руб/мес)\n\n'
                                         '🟢 Итого:\n'
                                         '1 месяц - 1020р.\n'
                                         '3 месяца - 3060р.\n'
                                         '6 месяцев - 5508р.\n'
                                         '12 месяцев - 9792р.\n\n')

