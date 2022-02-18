from flask import Flask, render_template, redirect, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/print', methods=['POST'])
def print():

    # Download the puzzle (check if already in cache)

    # Send to printer

    flash("Your file has been sent to the printer")
    return redirect('/')