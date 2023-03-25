from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('home.html')

@app.route('/pagina1', methods=['GET'])
def pag1():
  nome = request.args.get('nome')
  sesso = request.args.get('sesso')
  hobbies = request.args.getlist('hobbies')
  citta = request.args.get('citta')
  presentazione = request.args.get('presentazione')
  return render_template('pag1.html', nome=nome, sesso=sesso, hobbies=hobbies, citta=citta, presentazione = presentazione)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)