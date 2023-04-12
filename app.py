from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('homeunes.html')

@app.route("/home/")
def home():
    return render_template('homeunes.html')

@app.route("/quemsomos/")
def quemsomos():
    return render_template('quemsomosunes.html')

@app.route("/contato/")
def contato():
    return render_template('contatounes.html')


