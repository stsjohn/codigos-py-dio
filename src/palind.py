palavra = "radar"  # Definindo uma palavra fixa

# Inverte a palavra
invertida = palavra[::-1]

# Verifica se é um palíndromo
if palavra == invertida:
    print(f'A palavra "{palavra}" é um palíndromo!')
else:
    print(f'A palavra "{palavra}" NÃO é um palíndromo.')
