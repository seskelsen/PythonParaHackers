import requests

session = requests.Session()
response = session.get('https://stackoverflow.com')
print(session.cookies.get_dict())
