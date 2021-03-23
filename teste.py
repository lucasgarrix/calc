from calculadora import somar
from calculadora import subtrair
from calculadora import multiplicar
from calculadora import dividir

def teste_somar():
    assert somar(2,4) == 6
def teste_subtrair():
    assert subtrair(4,2) == 2
def teste_multiplicar():
    assert multiplicar(2,4) == 8
def teste_dividir():
    assert dividir(4,2) == 2

