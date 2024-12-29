import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #f06, #4a90e2);
                color: white;
                text-align: center;
            }
            h1 {
                font-size: 4em;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
            }
        </style>
    </head>
    <body>
        <h1>Hello</h1>
    </body>
    </html>
    """

if __name__ == '__main__':
    # Get the PORT from environment variables or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
