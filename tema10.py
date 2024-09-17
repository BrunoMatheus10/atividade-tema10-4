# Exemplo de lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]

# Inicializando a variável soma
soma = 0

# Percorrendo a lista e somando os elementos de índices pares
for i in range(len(lista)):
    if i % 2 == 0:
        soma += lista[i]

print(f"A soma de todos os elementos de índices pares é:" ,soma,)
