# Final Project

## What we've learned
As a review and reference when building your final project, here are some of the major topics we discussed this semester:

### Object Oriented Programming
Object Oriented Programming (OOP) is a programming concept that involves modelling entities as objects, which contain specific properties and behaviors. OOP is useful for grouping data and functionality and avoiding repeated code. The main concepts of OOP are classes and objects. If we imagine building a house with OOP, a class would be the blueprint for the house and an object is the house itself. There are some scenarios where OOP is useful in your Python programs, but others you can get away with just using functions. An example of where OOP would be useful is when building a RPG game where there are players with different capabilities. For example, if you want all players to fight, but they all fight differently depending on what player type they are. In Python, you would design this like so:

```
class Player:
    def __init__(self, name):
        self.name = name
    
    def fight(self):
        print("Regular player cannot fight!")


class Knight(Player):
    def fight(self):
        print("You swing your mighty sword!")


class Wizard(Player):
    def fight(self):
        print("FIREBALL")
```

This example uses `Player` as the base class. Then we **inherit** from Player to get the fight method and the name attribute. In the **subclasses** `Knight` and `Wizard`, we **override** the `fight` method to customize the functionality for the different types of players. We can now create objects from these classes like this:

```
cool_knight = Knight("Sir Robbin")
cool_knight.fight() # You swing your mighty sword!

wiz = Wizard("Gandalf the Grey")
wiz.fight() # FIREBALL
```

### Packages
A package in Python is a way to organize and reuse code. It’s essentially a directory (folder) that contains multiple modules (Python files) and a special file called __init__.py.

Packages allow you to:

- Group related code together.
- Reuse code across projects.
- Avoid naming conflicts by using namespaces.

Python has a massive ecosystem of pre-built packages that you can install using `pip`, Python's package manager.

Example: Installing the requests package:
```
pip install requests
```

Once installed, you can import and use it in your code:
```
import requests
response = requests.get("https://api.example.com")
print(response.text)
```

### API Requests
An Application Programming Interface (API) is a set of rules or protocols that allows different software applications to communicate with each other, essentially acting as a bridge to exchange data and functionalities between them. APIs are very useful when you want to access some specific type of data in your application that is hosted by someone else. For example, if you wanted to make a Weather app you would use a Weather API to pull realtime weather data for a user's current location. You can use APIs in your Python programs either by installing a Python package (using `pip install`) or using the `requests` package to send requests your desired API's endpoints. Here's an example of using the `requests` package and the [dog facts API](https://kinduff.github.io/dog-api/):

```
import requests

response = requests.get("http://dog-api.kinduff.com/api/facts")
print(response.json()) # {'facts': ['There are only 350 Cisky Terriers in the world, possibly making it the rarest breed.'], 'success': True}
```

`json` is just a format of data, similar to a dictionary in Python. Many APIs use json as their data format because it is structured nicely and readable.

### Websites
A website is a collection of pages (like chapters in a book) that are connected and hosted on the internet. You can view these pages using a web browser (like Chrome or Safari) by typing a web address, such as www.google.com. The web address is similar to the API address in the previous example, but instead of returning a data in JSON format, it is returning HTML pages for you to view in your web browser. You can create your own website in Python using the package `flask`.

Install flask
```
pip install flask
```

Then you can use `flask` in your code in a file called `app.py`
```
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    welcome = "<h1>Welcome to my website</h1>"
    return welcome
```

Now run the command in your terminal
```
flask run
```

## Project Ideas
- Make a game using classes and objects, where you can add `Player` objects to a `Game` object and have them randomly fight. The last player standing (the one that still has non-zero `health`) wins. Make different types of players that can do varying levels of damage.
- Write a Python program that uses an API of your choice to fetch data and do something cool with it. Here is [a list](https://github.com/public-apis/public-apis) of APIs to choose from.
- Download a python package using `pip` and use it to do something creative (example: Use the `openai` package to make a chatbot). Here is [a list](https://github.com/jdnvn/python2/blob/main/m2/packages/python_packages.md) of cool python packages to try.
- Make a personal website with the `flask` package and use ChatGPT to write some HTML code for you.
- Finish one of the class projects that you didn't get to finish.
