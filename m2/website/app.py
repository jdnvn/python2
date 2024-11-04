from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    welcome = f"<h1>Welcome to Joe's website</h1>"
    ip_html = f"<p>Your IP address is {request.access_route[0]}</p>"
    return welcome + ip_html

@app.route('/<name>')
def hello(name):
    personal = f'<h1>Hello, {name}!</h1>'
    instruc = '<p>Thanks for visiting my site</p>'
    return personal + instruc

@app.route('/spooky')
def spooky():
    html = """
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Haunted House</title>
                <style>
                    /* Body style */
                    body {
                        background-color: #000;
                        color: #fff;
                        font-family: 'Courier New', Courier, monospace;
                        overflow: hidden;
                        text-align: center;
                        height: 100vh;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                    }

                    /* Flickering title */
                    h1 {
                        font-size: 4em;
                        text-shadow: 0 0 5px red, 0 0 10px darkred, 0 0 20px darkred;
                        animation: flicker 1.5s infinite alternate;
                    }

                    /* Ghostly paragraph */
                    p {
                        font-size: 1.2em;
                        opacity: 0.8;
                        max-width: 600px;
                        margin: 20px auto;
                        animation: float 3s ease-in-out infinite;
                    }

                    /* Flickering keyframes */
                    @keyframes flicker {
                        0% { opacity: 1; text-shadow: 0 0 5px red, 0 0 10px darkred, 0 0 20px darkred; }
                        50% { opacity: 0.6; text-shadow: none; }
                        100% { opacity: 1; text-shadow: 0 0 5px red, 0 0 10px darkred, 0 0 30px darkred; }
                    }

                    /* Floating keyframes */
                    @keyframes float {
                        0%, 100% { transform: translateY(0); }
                        50% { transform: translateY(-10px); }
                    }

                    /* Blood-drip effect */
                    .blood-drip {
                        color: red;
                        text-shadow: 0 0 5px darkred;
                        position: absolute;
                        top: 0;
                        left: 50%;
                        transform: translateX(-50%);
                        font-size: 1.5em;
                        animation: drip 2s infinite;
                    }

                    /* Blood drip animation */
                    @keyframes drip {
                        0% { opacity: 0; transform: translate(-50%, -10px); }
                        50% { opacity: 1; transform: translate(-50%, 10px); }
                        100% { opacity: 0; transform: translate(-50%, 30px); }
                    }
                </style>
            </head>
            <body>
                <h1>Welcome to the Haunted House</h1>
                <p>If you dare to enter, beware of the restless spirits that wander within. They are always watching...</p>
                <div class="blood-drip">BLOOD DRIPS...</div>
            </body>
        </html>
    """
    return html
