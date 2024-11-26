from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#configurazione db

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# inizializza SQLAlchemy
db.init_app(app)

#crea il database se non esiste
with app.app_context():
    db.create_all()

# Lista della spesa
lista_spesa = []

# Aggiungere un elemento alla lista
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista_spesa.append(elemento)
    return redirect(url_for('home'))

# Rimuovere un elemento dalla lista
@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista_spesa):
        lista_spesa.pop(indice)
    return redirect(url_for('home'))

# Pagina principale
@app.route('/')
def home():
    return render_template('index.html', lista=lista_spesa)

if __name__ == '__main__':
    app.run(debug=True)
