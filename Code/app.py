"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, request, redirect
from tokens import tokenize
from markov_chain_second import build_chain, walk_chain
from read import read
import twitter


app = Flask(__name__)

text = read('regular_show.txt')
parsed_text = tokenize(text)
markov_chain = build_chain(parsed_text)

@app.route("/")
def home():
    sentence = walk_chain(markov_chain)
    return render_template('index.html', sentence=sentence)

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
