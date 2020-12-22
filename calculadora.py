def valida_float(numero:float)->bool:
    if isinstance(numero, float):
        return True
    raise ValueError(f'Valor informado {numero} não é numerico')

def valida_nao_zero(numero:float)->bool:
    if numero != 0:
        return True
    raise ValueError(f'Valor informado {numero} é igual que zero')

def soma(numero1:float, numero2:float)->float:
    if valida_float(numero1) and valida_float(numero2) :   
        soma = numero1 + numero2
        return soma

def subtracao(numero1:float, numero2:float)->float:
    if valida_float(numero1) and valida_float(numero2) :   
        subtracao = numero1 - numero2
        return subtracao

def multiplicacao(numero1:float, numero2:float)->float:
    if valida_float(numero1) and valida_float(numero2) :   
        multiplicacao = numero1 * numero2
        return multiplicacao

def divisao(numero1:float, numero2:float)->float:
    if valida_nao_zero(numero1) and valida_nao_zero(numero2):
        if valida_float(numero1) and valida_float(numero2) :   
            divisao = numero1 / numero2
            return divisao
    