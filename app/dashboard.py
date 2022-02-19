from flask import Flask, render_template, redirect, flash, request
import subprocess
import os
from pathlib import Path

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

    project_dir = Path(__file__).resolve().parents[1]

    paths = {
        'pdf': os.path.join(project_dir,f'data/pdf/{publisher}/'),
        'puz': os.path.join(project_dir,f'data/puz/{publisher}/')
        }

    for path in paths.items():
        file_ext=path[0]
        folder_path=path[1]
        make_folder_if_not_exists(folder_path)
        file_path = os.path.join(folder_path,f'{date}.{file_ext}')
    
        if not os.path.exists(file_path):   
            # TODO: update xword-dl to download pdfs  
            cmd = f'xword-dl {publisher} --output {date}.{file_ext}'
            process = subprocess.Popen(cmd.split(), cwd=folder_path)
            output, error = process.communicate()

def send_to_printer(printer_name,file_name):
    cmd = f'lp -n 1 -o fit-to-page -d {printer_name} {file_name}'
    
    try:
        process = subprocess.Popen(cmd.split())
        output, error = process.communicate()
        flash("Your file has been sent to the printer","success")
    except Exception as e:
        flash(f'Something went wrong with printing: {str(e)}',"error")


def make_folder_if_not_exists(folder_path):
    path_exists = os.path.exists(folder_path)

    if not path_exists:
        os.makedirs(folder_path)