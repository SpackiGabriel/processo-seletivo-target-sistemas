'''
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será 
a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...). 
Escreva um programa na linguagem que desejar onde, informado um número, ele calcule 
a sequência de Fibonacci e retorne uma mensagem avisando se o número informado 
pertence ou não a sequência.
'''

# Função para calcular a sequência de Fibonacci até o número informado
def fibonacci(num):
    
    # Verifica se o número informado é menor que 0
    if num < 0:
        return "O número informado deve ser maior ou igual a 0."
    
    # Inicia a sequência de Fibonacci com os primeiros dois números
    a, b = 0, 1
    
    # Inicia um laço de repetição que verifica se o código já chegou no número informado
    while a <= num:
        
        # Verifica se o número informado foi encontrado na sequência
        if a == num:
            return f"{num} pertence à sequência de Fibonacci."

        # Calcula o próximo número da sequência
        a, b = b, a + b
        
    # Se o número informado não estiver na sequência, retorna uma mensagem informando
    return f"{num} não pertence à sequência de Fibonacci."


# Solicita que o usuário informe um número via terminal
num = int(input("Informe um número: "))

# Chama a função fibonacci com o número informado e exibe o resultado
print(fibonacci(num))