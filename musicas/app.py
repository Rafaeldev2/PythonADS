from flask import Flask, render_template, request, redirect
from pymongo import MongoClient


app = Flask(__name__, template_folder='public') 

# Conexão ao MongoDB
def conectar_bd():
    client = MongoClient('localhost', 27017)  # Conexão padrão ao MongoDB
    db = client['Musicas_DB']  # Nome do banco de dados
    return db

# Rota inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para adicionar música
@app.route('/adicionar')
def adicionar():
    return render_template('adicionar.html')

@app.route('/adicionar_musica', methods=['POST'])
def adicionar_musica():
    db = conectar_bd()
    nome = request.form['nome']
    artista = request.form['artista']
    ano = request.form['ano']
    genero = request.form['genero']
    link_youtube = request.form['link_youtube']

    db.musicas.insert_one({
        'nome': nome,
        'artista': artista,
        'ano': ano,
        'genero': genero,
        'link_youtube': link_youtube
    })

    return redirect('/?adicionado=sucesso')


# Rota para buscar música
@app.route('/buscar')
def buscar():
    return render_template('buscar.html')

@app.route('/buscar_musica', methods=['GET'])
def buscar_musica():
    db = conectar_bd()
    nome = request.args.get('nome')
    artista = request.args.get('artista')

    query = {}

    if nome:
        query['nome'] = nome
    if artista:
        query['artista'] = artista
    resultados = list(db.musicas.find(query))

    return render_template('buscar.html', resultados = resultados)


# Rota para atualizar música
@app.route('/atualizar')
def atualizar():
    return render_template('atualizar.html')

@app.route('/atualizar_musica', methods=['POST'])
def atualizar_musica():
    db = conectar_bd()
#  COMPLETAR

# Rota para deletar música
@app.route('/deletar')
def deletar():
    return render_template('deletar.html')

@app.route('/deletar_musica', methods=['POST'])
def deletar_musica():
    db = conectar_bd()
#     COMPLETAR


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,debug=True)