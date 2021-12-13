import requests
from bs4 import BeautifulSoup
import json


auth_data = {'email': 'email', 'password': 'pass', 'app': 'ics',
             'device_id': 'please add function get balance in api!'}
session = requests.session()
response = session.post('https://mcs.mail.ru/api/v1/auth/signin', data=auth_data)
parse_data = session.get('https://mcs.mail.ru/api/v1/projects/your_id/billing')
soup = BeautifulSoup(parse_data.text, 'lxml').text
balance_json = json.loads(soup)
balance = (balance_json['balance']).split('.')[0]

print(balance)
