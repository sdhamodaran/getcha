#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
from imageWork import pickRandomImageName
app = Flask(__name__)
@app.route('/get_image')
def get_image():
    imageName = pickRandomImageName()
    return imageName

@app.route('/verify')
def verify():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


