async def process_deeplinks(link, state, bot):
    result = '_'
    if 'Начать заново' in link:  # Нужно для обработки нажатия кнопки Начать заново
        result = 'заново'
        await state.update_data(came_from=result)
        await state.update_data(inviter_code='None')
        return result
    elif 'start' in link:  # Если в диплинке есть команда start
        srez = link[7:]  # Обрезаем в нём первые символы '/start '
        if not srez:  # Если строка пустая
            result = 'обычный_запуск'
            await state.update_data(came_from=result)
            await state.update_data(inviter_code='None')
            return result
        else:
            if 'altenter' in link:
                result = 'альтернативный'
                await state.update_data(came_from=result)
                await state.update_data(inviter_code='None')
                return result

            elif 'invitelink' in link:
                inviter_code = link[17:]  # Обрезаем в нём ещё символы 'invitelink' и получаем id юзера из ссылки
                result = 'invitelink'
                await state.update_data(came_from=result)
                await state.update_data(inviter_code=inviter_code)
                return result

            else:
                result = srez
                print(result)
                await state.update_data(came_from=result)
                await state.update_data(inviter_code='None')
                return result

