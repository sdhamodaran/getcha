#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
from databaseActions import imageCount
@app.route('/get_image')
def get_image():
    imageIdArray = imageCount()
    imageName = pickRandomImageName(imageIdArray)
    return imageName

@app.route('/verify')
def verify():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)


