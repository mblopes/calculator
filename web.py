from flask import Flask, render_template
import calculadora

app = Flask(__name__)

app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/somar')
def somar():
    number1 = 10.0
    number2 = 5.0
    resultado = calculadora.soma(number1, number2)

    return render_template('somar.html', v1=number1, v2=number2, r=resultado)
        
@app.route('/subtrair')
def subtrair():
    number1 = 10.0
    number2 = 5.0

    resultado = calculadora.subtracao(number1, number2)

    return render_template('subtrair.html', v1=number1, v2=number2, r=resultado)

@app.route('/multiplicar')
def multiplicar():
    number1 = 10.0
    number2 = 5.0

    resultado = calculadora.multiplicacao(number1, number2)

    return render_template('multiplicar.html', v1=number1, v2=number2, r=resultado)

@app.route('/dividir')
def dividir():
    number1 = 10.0
    number2 = 5.0

    resultado = calculadora.divisao(number1, number2)

    return render_template('dividir.html', v1=number1, v2=number2, r=resultado)