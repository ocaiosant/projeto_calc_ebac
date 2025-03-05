#!/bin/bash

# Apresentação da calculadora
echo "Essa é uma calculadora simples que usa os conceitos do modulo 1"

# Receber as variáveis
read -p "Digite um número: " num1
read -p "Qual operação você deseja realizar? (mult, som, sub, div, pot): " var1

# Verificar a operação e executar o cálculo
case $var1 in
    "mult")
        read -p "Digite outro número: " num2
        resultado=$((num1 * num2))
        ;;
    "som")
        read -p "Digite outro número: " num2
        resultado=$((num1 + num2))
        ;;
    "sub")
        read -p "Digite outro número: " num2
        resultado=$((num1 - num2))
        ;;
    "div")
        read -p "Digite outro número: " divisor
        if [ $divisor -eq 0 ]; then
            resultado="Erro: Divisão por zero!"
        else
            resultado=$((num1 / divisor))
        fi
        ;;
    "pot")
        read -p "Digite a potência: " potencia
        resultado=$((num1 ** potencia))
        ;;
    *)
        resultado="Operação inválida"
        ;;
esac

# Exibir o resultado
echo "O resultado é: $resultado"