import requests
from bs4 import BeautifulSoup
import json


auth_data = {'email': 'email', 'password': 'pass', 'app': 'ics',
             'device_id': 'device'}

session = requests.session()
response = session.post('https://mcs.mail.ru/api/v1/auth/signin', data=auth_data)
session.headers.update({'x-csrf-token': 'csrf'})
parse_data = session.get('https://mcs.mail.ru/iam/api/v2/projects/pid/billing/')
soup = BeautifulSoup(parse_data.text, 'lxml').text
balance_json = json.loads(soup)
balance = (str(balance_json['balance'])).split('.')[0]
print(balance)
