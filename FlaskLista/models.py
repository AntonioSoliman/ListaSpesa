from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # Inizializziamo SQLAlchemy

class ListaSpesa(db.Model):  # Definizione della tabella
    id = db.Column(db.Integer, primary_key=True)  # ID elemento, unico
    elemento = db.Column(db.String(100), nullable=False)  # Elemento, non nullo
