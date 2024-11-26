from flask import Flask, render_template, request, redirect, url_for
from models import db, ListaSpesa  # Importa il database e il modello

app = Flask(__name__)

# Configurazione del database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inizializza SQLAlchemy con l'app Flask
db.init_app(app)

# Crea il database se non esiste
with app.app_context():
    db.create_all()

# Aggiungere un elemento alla lista
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        nuovo_elemento = ListaSpesa(elemento=elemento)
        db.session.add(nuovo_elemento)
        db.session.commit()
    return redirect(url_for('home'))

# Rimuovere un elemento dalla lista
@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    elemento = ListaSpesa.query.get_or_404(indice)
    db.session.delete(elemento)
    db.session.commit()
    return redirect(url_for('home'))

# Svuota tutti gli elementi dalla lista
@app.route('/svuota', methods=['POST'])
def svuota():
    ListaSpesa.query.delete()
    db.session.commit()
    return redirect(url_for('home'))

# Pagina principale
@app.route('/')
def home():
    lista_spesa = ListaSpesa.query.all()
    return render_template('index.html', lista=lista_spesa)

if __name__ == '__main__':
    app.run(debug=True)
