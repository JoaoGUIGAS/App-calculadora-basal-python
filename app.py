from flask import Flask, render_template, request, jsonify
from projeto import calcular_tmb, calcular_gasto_energetico, calcular_macronutrientes

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    dados = request.json
    
    try:
        peso = float(dados['peso'])
        altura = float(dados['altura'])
        idade = int(dados['idade'])
        genero = dados['genero']
        nivel_atividade = dados['nivel_atividade']
        objetivo = dados['objetivo']
        
        tmb = calcular_tmb(peso, altura, idade, genero)
        calorias = calcular_gasto_energetico(tmb, nivel_atividade, objetivo)
        macros = calcular_macronutrientes(calorias, objetivo)
        
        return jsonify({
            'sucesso': True,
            'tmb': round(tmb),
            'calorias': round(calorias),
            'macros': macros
        })
    except Exception as e:
        return jsonify({
            'sucesso': False,
            'erro': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True) 