def busca(lista, alvo):
    for i in range (len(lista)):
        if lista [i] == alvo:
            return i
    return -1
minhalista = list(range(11))
print(busca(minhalista,11))

def buscabinaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim)// 2
        if lista [meio] == alvo:
            return alvo
        elif lista [meio] > alvo:
            fim = meio + 1
        elif lista [meio] < alvo:
            inicio = meio - 1

    return -1

def buscatodos()


minhalista = [7,6,3,4,65,65,2,45,5,33,1,8]
minhalista.sort()
print(buscabinaria(minhalista, 65))

