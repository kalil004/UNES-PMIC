from flask import Flask, render_template, request, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_Host'] = 'localhost' # 127.0.0.1
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'unes'

mysql = MySQL(app)

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


@app.route("/contato/", methods=['GET', 'POST'])
def contatos():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))
       
        mysql.connection.commit()
        
        cur.close()

        return 'sucesso'
    return render_template('contatos.html')


# rota usuários para listar todos os usuário no banco de dados.
@app.route('/users/')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contatos")

    if users > 0:
        userDetails = cur.fetchall()

        return render_template("users.html", userDetails=userDetails)

app.run(debug=True)
