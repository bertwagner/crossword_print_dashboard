# Crossword Print Dashboard

A locally hosted website for easily downloadomg crossword files and sending them to a network printer

![Screenshot of Crossword Print Dashboard](app/static/images/demo-screenshot.jpg)

## Background

I like solving crosswords on paper. I want to be able to print puzzles from a variety of source easily.  This web app runs on a Raspberry Pi server on my local network and allows me to print puzzles on-demand via my phone.

## Instructions
1. Run `FLASK_APP=app/dashboard.py flask run --host=0.0.0.0 --port=80`. 
2. Open [http://localhost:5000](http://localhost:5000) in your browser.

NOTE: This application is intended to run on your secure home network. It is not secure.  Don't do stupid things with it.