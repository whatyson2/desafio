def fibonacci_sequence(n):
    sequencia = [0, 1]
    proximo_valor = sequencia[1]

    while proximo_valor < n:
        proximo_valor = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_valor)
    
    return sequencia

def is_fibonacci_number(number):
    sequencia = fibonacci_sequence(number)
    if number in sequencia:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} NÃO pertence à sequência de Fibonacci."

# Exemplo
numero_informado = int(input("Informe um número: "))
resultado = is_fibonacci_number(numero_informado)
print(resultado)
