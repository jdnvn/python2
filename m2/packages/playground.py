import requests

response = requests.get('http://api.open-notify.org/astros.json')

print(response.json())


response = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Dwayne_%22The_Rock%22_Johnson_Visits_the_Pentagon_%2841%29_%28cropped%29.jpg/440px-Dwayne_%22The_Rock%22_Johnson_Visits_the_Pentagon_%2841%29_%28cropped%29.jpg')


with open('test.jpg', 'wb') as f:
    f.write(response.content)