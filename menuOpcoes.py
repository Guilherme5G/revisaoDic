def forca_opcao(msg,lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n->")
    while escolha not in lista_opcoes:
        print("Invalido")
        escolha = input(f"{msg}\n{opcoes}\n->")
    return escolha

def achar_indice(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

def maior_valor(lista):
    indice = 1
    for i in range(len(lista)):
        if lista[i] > lista[indice]:
            indice = i
    return indice

def menor_valor(lista):
    indice = 1
    for i in range(len(lista)):
        if lista[i] < lista[indice]:
            indice = i
    return indice

def cadastrar(dic):
    for key in dic.keys():
        info = input(f"Diga o novo {key}")
        dic[key].append(info)
    return dic

def remover(dic):
    escolha = forca_opcao("Qual carro voce deseja remover?", carros['nomes'])
    indice_remover = achar_indice(carros['nomes'],escolha)
    for key in carros.keys():
        carros[key].pop(indice_remover)
    return dic

carros = {
    'nomes' : ['celta','up','kombi','uno'],
    'portas' : [4,2,6,2],
    'preço' : [1000,200,300,100],
    'ano de fabricação' : [2014,2018,1970,2005]
}

''' print(pd.DataFrame(carros))''' #roubo, nao pode

print("Ola!, bem vindo a nossa loja")
print('-'*10)
idade = input("Qual sua idade? ")
if idade < '18':
    print("Ainda nao ha idade para ter um carro")
else:
    print(f"Essas sao nossas opcoes de carros na loja", carros['nomes'])



