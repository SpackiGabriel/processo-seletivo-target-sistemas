'''
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
'''

import json

# Função para calcular o maior faturamento
def coletar_maior_valor(faturamento):

    # Variável maior_valor declarada com número negativo para que o maior valor seja de fato encontrado 
    maior_valor = -1
    
    # Encontra o maior valor
    for valor in faturamento:
        
        # Verifica se o valor é maior do que o maior valor atual 
        if valor > maior_valor:
            maior_valor = valor
        
    return maior_valor

def coletar_menor_valor(faturamento):

    # Variável menor_valor declarada com número negativo para que o menor valor seja de fato encontrado 
    menor_valor = -1
    
    # Encontra o menor valor
    for valor in faturamento:
        
        # Ignora dias sem faturamento
        if valor == 0:
            continue 
            
        # Verifica se o valor é menor do que o menor valor atual
        # Também verifica se é o primeiro valor que está sendo verificado 
        if (menor_valor < 0) or (valor < menor_valor):
            menor_valor = valor
        
    return menor_valor


# Abre o arquivo json sobre o faturamento
with open('faturamento.json') as arquivo:
    info = json.load(arquivo)
    
# Obtém a lista de faturamentos do mês de Junho
faturamento_junto = info['faturamento']['junho']

# Coleta o menor e o maior valor do faturamento

# Na linguagem Python existem os métodos min() e max() que retornariam, respectivamente, o menor e maior valor
# Mas para esse exercício, considei que os mesmos não eram válidos
menor_valor = coletar_menor_valor(faturamento_junto)
maior_valor = coletar_maior_valor(faturamento_junto)

# Calcula a média de faturamento, ignorando os dias sem faturamento
dias_com_faturamento = [valor for valor in faturamento_junto if valor > 0]
media = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Calcula o número de dias em que o faturamento diário foi superior à média
dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media)


# Mostra os resultados
print(f"Menor valor de faturamento em junho: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento em junho: R$ {maior_valor:.2f}")
print(f"Média de faturamento em junho: R$ {media:.2f}")
print(f"Dias em que o faturamento diário foi superior à média: {dias_acima_da_media}")