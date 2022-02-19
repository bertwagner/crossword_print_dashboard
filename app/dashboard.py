from flask import Flask, render_template, redirect, flash, request
import subprocess
import os

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

    publisher = request.form['publisher']
    date = request.form['date']

    download_puzzle(publisher,date)

    send_to_printer(PRINTER_NAME,'crossword.pdf')

    return redirect('/')

def download_puzzle(publisher,date):
    # Check cache before downloading

    folder_path_pdf = f'../data/pdf/{publisher}/'
    folder_path_puz = f'../data/puz/{publisher}/'

    # TODO get this to save in the right spot
    cmd = f'cd ../data/puz/{publisher}/ && xword-dl {publisher} --output {date}.puz'
    process = subprocess.Popen(cmd.split())
    output, error = process.communicate()

def send_to_printer(printer_name,file_name):
    cmd = f'lp -n 1 -o fit-to-page -d {printer_name} {file_name}'
    
    try:
        process = subprocess.Popen(cmd.split())
        output, error = process.communicate()
        flash("Your file has been sent to the printer","success")
    except Exception as e:
        flash(f'Something went wrong with printing: {str(e)}',"error")


def __make_folder_if_not_exists(folder_path,delete_files):
    path_exists = os.path.exists(folder_path)

    if not path_exists:
        os.makedirs(folder_path)