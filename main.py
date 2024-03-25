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
    headers = {'User-Agent': 'Mozilla/5.0 by /u/BiharanInDelhi'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        app.logger.error('Failed to fetch meme: status code %s, response body: %s', response.status_code, response.text)
        return jsonify({'error': 'An error occurred while fetching the meme'}), 500
    data = response.json()
    memes = [post['data']['url'] for post in data['data']['children'] if 'jpg' in post['data']['url'] or 'png' in post['data']['url']]
    if memes:
        meme_url = random.choice(memes)
        return jsonify({'meme_url': meme_url})
    else:
        return jsonify({'error': 'No memes found'}), 404

if __name__ == '__main__':
    app.run(debug=True)