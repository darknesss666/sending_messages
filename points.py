import vk
import time
import traceback
from ast import literal_eval

TOKEN = input('Введи сюда токен: ')#тут нужно ввести обрезанный токен kate mobile.
session = vk.Session(access_token = TOKEN)
vk_api = vk.API(session, v='5.135')
users = literal_eval(input('Введи сюда айдишки участников: '))#тут нужно ввести айдишки людей через запятую.

for user_id in users:
    try:
        vk_api.messages.send(random_id = 0, peer_id = int(user_id), message = '''это точки, не обращай внимания.
скрипт написан @id534452871 (darknesss666).''')
        time.sleep(3)
    except vk.exceptions.VkAPIError as e:
        if e.code == 902:
            print(f'\033[33m@id{user_id} запретил писать себе в лс, пф, больно надо.')
        elif e.code == 14:
            print(f'\033[0m\033[33m@id{user_id} – ему отправить в лс сообщение не удалось из-за ебаной капчи((.')
print('''\033[0m\033[1;32mТочки были отправлены.
Это нужно для того, чтобы после создания бесед вы могли писать кому угодно и ошибка не выходила.''')