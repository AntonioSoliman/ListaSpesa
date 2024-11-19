from flask import Flask, render_template
#render_template: collegare file HTML.
lista_spesa = []
#creazione di una funzione che aggiunge elementi alla lista spesa
@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista_spesa.append(elemento)
    return redirect(url_for('home'))

#creazione di una funzione che rimuove elementi dalla lista
@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
        if 0 <= indice < len(lista_spesa):
            lista_spesa.pop(indice)
        return redirect(url_for('home'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)