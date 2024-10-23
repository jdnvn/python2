import requests

response = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random')
response_json = response.json()

print(response_json['text'])


response = requests.get('https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg')
with open('dogs.jpeg', 'wb') as f:
    f.write(response.content)
