# -*- coding: utf-8 -*-
"""projeto_calc.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UqT4knyg9HW_dzkRn_VZO-kgw9OXRL7V

# CALCULADORA DO MÓDULO 1

> O intuito desta minha calculadora é o de cobrir todas as operaçoes tratadas em aula de modo que seja completo todas as possibilidades inseridas pelo usuario.

obs.: por falta de conhecimento aprofundado, fui consultar o "pai dos burros" sobre como solucionar alguns erros na estrutura do cód. Por esse motivo os comandos "try" e "except" aparecem na linha de cód.
"""

#apresentacao da calculadora

print("Essa é uma calculadora simples que usa os conceitos do modulo 1")

#receber as variaveis


#utilize mult para Multiplicaçao
#utilize som para Soma1
#utilize sub para Subtracao
#utilize div para Divisao
#utilize pot para potencializacao

try:
    num1 = int(input("digite um numero :"))
    var1 = input("qual operação você deseja realizar ? ")

    if var1 == "mult":
        resultado = num1 * int(input("digite outro numero :"))
    elif var1 == "som":
        resultado = num1 + int(input("digite outro numero :"))
    elif var1 == "sub":
        resultado = num1 - int(input("digite outro numero :"))
    elif var1 == "div":
        divisor = int(input("digite outro numero :"))
        if divisor == 0:
            resultado = "Erro: Divisão por zero!"
        else:
            resultado = num1 // divisor
    elif var1 == "pot":
        resultado = num1 ** int(input("digite a potencia :"))
    else:
        resultado = "Operação inválida"

    print("O resultado é:", resultado)

except ValueError:
    print("Erro: Entrada inválida. Por favor, digite números válidos.")