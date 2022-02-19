from flask import Flask, render_template, redirect, flash
import subprocess

#MOVE TO CONFIG
PRINTER_NAME='BrotherHL2170W'
APP_SECRET='not-so-secret'

app = Flask(__name__)
app.secret_key=APP_SECRET

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/print', methods=['POST'])
def print():

    # Download the puzzle (check if already in cache)

    send_to_printer(PRINTER_NAME,'crossword.pdf')

    flash("Your file has been sent to the printer","success")
    return redirect('/')


def send_to_printer(printer_name,file_name):
    cmd = f'lp -n 1 -o fit-to-page -d {printer_name} {file_name}'
    process = subprocess.Popen(cmd.split())
    output, error = process.communicate()

    # TODO: TEST THIS, FLASH ERROR MESSAGES ON HOME PAGE
    if error != None:
        flash('Something went wrong with printing: {error}',"error")
