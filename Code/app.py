"""Main script, uses other modules to generate sentences."""
from flask import Flask
from histogram import histogram_dictionary
from dictogram import Dictogram


app = Flask(__name__)


@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    return histogram_dictionary('oneFish.txt')


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    histogram = before_first_request()
    #word = random_word(histogram)
    return 'hello world'


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
