# Importação dos módulos e pacotes necessários.
from flask import Flask, render_template, redirect, request, flash

# Configuração do Flask.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SENAI791'

# Cria a rota para o INDEX do website.
@app.route('/')
def inicio():

    # Abre a página inicial.
    return render_template('index.html')

# Cria a rota que verifica qual combustível é mais viável.
@app.route('/verificar_combustivel', methods=['POST'])
def verificar_combustivel():
    
    # Recupera os valores digitados no formulário.
    gasolina = float(request.form['gasolina'])
    etanol = float(request.form['etanol'])
    
    # Grava o resultado da operação.
    resultado = "Etanol" if (etanol / gasolina < 0.7) else "Gasolina"
    
    # Gera o retorno da operação, apresentando o formulário com o resultado.
    return render_template('index.html', retorno=f'Baseando-se nos preços, é recomendavel abastecer com: {resultado}')

# Executa o website.
if __name__ == "__main__":
    app.run(debug=True)