from datetime import datetime
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from DB.db import add_all_to_db, request_to_db_multi
from Defs.Config import LINKTOPINBOT, LIST_ADMINS
from Defs.Deeplinks import process_deeplinks
from Defs.Defs_Admin import on_start_admin
from Defs.Defs_Demo import run_demo
from Defs.State_Machine import States


async def on_start(message: Message, state: FSMContext, bot: Bot):
    user_id_here = message.chat.id

    # Если вошёл админ, то показываем другой интерфейс
    if user_id_here in LIST_ADMINS:
        await state.set_state(States.admin)
        await on_start_admin(user_id_here)

    else:
    # Проверяем имеется ли юзер в базе
        try:
            list_of_request = "inviter_code"
            result = request_to_db_multi(list_of_request, 'user_id', user_id_here)[0]
            sss = list(result)
            inviter_code = sss[0]
            await state.update_data(user_id=user_id_here)
            await state.update_data(inviter_code=inviter_code)
            if inviter_code != 'None':
                link = f'{LINKTOPINBOT}?start=invitelink{inviter_code}'
                await state.update_data(link=link)
            else:
                link = f'{LINKTOPINBOT}?start=demo'
                await state.update_data(link=link)

    # Если нет, то вносим
        except Exception as ex:
            await state.update_data(user_id=user_id_here)
            username_here = message.from_user.username
            if username_here is None:
                username_here = 'None'
            await state.update_data(username=username_here)
            first_name_here = message.from_user.first_name
            if first_name_here is None:
                first_name_here = 'None'
            await state.update_data(first_name=first_name_here)
            last_name_here = message.from_user.last_name
            if last_name_here is None:
                last_name_here = 'None'
            await state.update_data(last_name=last_name_here)

            # Обработка DeepLinks
            deep = await process_deeplinks(message.text, state, bot)
            # -----
            if deep == 'invitelink':
                data = await state.get_data()
                inviter_code = data['inviter_code']
                link = f'{LINKTOPINBOT}?start=invitelink{inviter_code}'
                await state.update_data(link=link)
            else:
                link = f'{LINKTOPINBOT}?start=demo'
                await state.update_data(link=link)

            data = await state.get_data()
            date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            list_subjects_of_DB = "user_id, came_from, inviter_code, username, first_name, last_name, date_of_use"
            list_data_of_DB = f"{data['user_id']}, '{data['came_from']}', '{data['inviter_code']}', '{data['username']}', '{data['first_name']}', '{data['last_name']}', '{date_time}'"
            add_all_to_db(list_subjects_of_DB, list_data_of_DB)

        await state.set_state(States.demo)
        await run_demo(message, state, bot, user_id_here)

