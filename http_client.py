import requests

r = requests.get('http://127.0.0.1:8081/')
r = requests('http://127.0.0.1:8081/', data = {'name':'value', 'save':True, 'scan':'True'})