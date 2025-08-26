import requests

'''
response=requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input':{'topic':"my girlfriend"}})
'''

response=requests.post(
    "http://localhost:8000/essay/invoke",
    json={'input':{'topic':"my best city"}})

print(response.json()['output']['content'])
