"""
Flask App for Random Cat Images.

This Flask application generates a random cat image from a list of images when accessed via the root URL.
"""


from flask import Flask, render_template
import random

app = Flask(__name__, template_folder='templates')

# list of cat images
images = [
    'https://media.tenor.com/t0eFbcxLGgIAAAAC/fat-cat-laser-eyes.gif',
    'https://media.tenor.com/pOS38tUuVnQAAAAd/cat-meme.gif',
    'https://media.tenor.com/lQlIBQeeruwAAAAd/wanted-cat.gif'
]


@app.route('/')
def index():
    """
    Generate a random cat image URL.

    Returns:
        str: URL of a randomly selected cat image.
    """
    url = random.choice(images)
    return render_template('index.html', url=url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
