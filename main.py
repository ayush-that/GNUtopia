# app.py
from flask import Flask, render_template, jsonify
import requests
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meme')
def get_meme():
    subreddit = 'ProgrammerHumor'
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    data = response.json()
    memes = [post['data']['url'] for post in data['data']['children'] if 'jpg' in post['data']['url'] or 'png' in post['data']['url']]
    if memes:
        meme_url = random.choice(memes)
        return jsonify({'meme_url': meme_url})
    else:
        return jsonify({'error': 'No memes found'}), 404

if __name__ == '__main__':
    app.run(debug=True)