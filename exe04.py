'''
Dado os valores de faturamento mensal de uma distribuidora, detalhado por estado:
Escreva um programa que calcule o percentual de representação que cada estado 
teve dentro do valor total mensal da distribuidora.
'''

# Função para calcular a porcentagem
def calcular_porcentagem(valor, total):
    
    # Retorna a porcentagem com a operação (valor x 100) / total
    # A porcentagem retorna com duas casas decimais
    return round((valor * 100) / total, 2)


# Declara os faturamentos em um dicionário
faturamento = {
    "sp": 67836.43,
    "rj": 36678.66,
    "mg": 29229.88,
    "es": 27165.48,
    "outros": 19849.53
}

# Variável para armazenar o faturamento total
faturamento_total = 0

# Calcula o faturamento total
for valor in faturamento.values():
    faturamento_total += valor

# Dicionário que irá guardar o faturamento em porcentagem
faturamento_porcentual = {}

# Chama a função para calcular a porcentagem de cada valor
for estado in faturamento.keys():
    faturamento_porcentual[estado] = calcular_porcentagem(faturamento[estado], faturamento_total)

# Mostra o faturamento total
print(f'O faturamento total foi de R${faturamento_total}\n')

# Mostra a porcentagem que cada estado representa no faturamento total
for estado in faturamento_porcentual.keys():
    
    # Verifica se o faturamento vem de um estado ou da chave "outros"
    if estado != "outros":
        print(f'O estado {estado} representa {faturamento_porcentual[estado]}% do faturamento total!')
        continue
    
    print(f'\nO restando dos faturamentos representam {faturamento_porcentual[estado]}% do faturamento total!')
    