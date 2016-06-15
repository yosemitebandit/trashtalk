"""The trashtalk server."""

import random
import os

import flask


# Read in the phrases.
input_path = 'phrases/'
input_filenames = (
  'defeat.txt', 'greeting.txt', 'idle.txt', 'init.txt', 'laughter.txt',
  'ready.txt', 'sobbing.txt', 'victory.txt'
)
phrases = {}
for input_filename in input_filenames:
  key = input_filename.split('.')[0]
  input_file_path = os.path.join(input_path, input_filename)
  with open(input_file_path) as input_file:
    phrases[key] = [p.strip() for p in input_file.readlines()]


# Setup the flask app.
app = flask.Flask(__name__)


@app.route('/')
def root():
  return flask.render_template('index.html')


@app.route('/defeat')
def defeat():
  return random.choice(phrases['defeat'])


@app.route('/greeting')
def greeting():
  return random.choice(phrases['greeting'])


@app.route('/idle')
def idle():
  return random.choice(phrases['idle'])


@app.route('/init')
def init():
  return random.choice(phrases['init'])


@app.route('/laughter')
def laughter():
  return random.choice(phrases['laughter'])


@app.route('/ready')
def ready():
  return random.choice(phrases['ready'])


@app.route('/sobbing')
def sobbing():
  return random.choice(phrases['sobbing'])


@app.route('/victory')
def victory():
  return random.choice(phrases['victory'])


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8989)
