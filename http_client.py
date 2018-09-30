import requests

r = requests.get('http://127.0.0.1:8081/')
r = requests.post('http://127.0.0.1:8081/', data = {'name':'value', 'save':True, 'scan':'True'})

# 496965346e9315ac003bee54b97362f56f773b309c09a8597ff867a81ff5f77a