'''
Escreva um programa que inverta os caracteres de um string.
'''

# Função para inverter a string
def inverte_string(texto):
    
    # Declara uma String vazia que será usada para armazenar a String invertida
    texto_invertido = ""
    
    # Laço de repetição que começa no número que representa a posição da última letra da String (tamanho - 1) e é decrementado até zero
    for i in range(len(texto), 0, -1):
        
        # Acessa a posição da string baseado no index do laço de repetição e adiciona o caracter da posição na string declara anteriormente
        texto_invertido += texto[i - 1]

    # Retorna a nova String
    return texto_invertido

# Pede para o usuário inserir uma String via terminal
texto = input('Insira a string que será invertida: ')

# Chama a função para inverter a string
texto_invertido = inverte_string(texto)

# Imprime a nova string na tela
print(f'A String {texto} invertida fica:\n{texto_invertido}')