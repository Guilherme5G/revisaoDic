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

#1
'''resposta = {'oi' : 'Ola','tchau' : 'flw fioti'}
resp = input("Diga oi ou tchau: ")
print(resposta[resp])'''

#2
'''carros = {
    'nomes' : ['celta','up','kombi','uno'],
    'portas' : [4,2,6,2],
    'preço' : [1000,200,300,100],
    'ano de fabricação' : [2014,2018,1970,2005]
}

escolha = forca_opcao("Qual carro voce quer escolher",carros['nomes'])
indice_escolha = achar_indice(carros['nomes'],escolha)
for key in carros.keys():
    print(f"{key} : {carros[key][indice_escolha]}")
'''
#3
'''carros = {
    'nomes' : ['celta','up','kombi','uno'],
    'portas' : [4,2,6,2],
    'preço' : [1000,200,300,100],
    'ano de fabricação' : [2014,2018,1970,2005]
}

maior = maior_valor(carros['preço'])
for key in carros.keys():
    print(f"{key} : {carros[key][maior]}")
'''


#4
'''carros = {
    'nomes' : ['celta','up','kombi','uno'],
    'portas' : [4,2,6,2],
    'preço' : [1000,200,300,100],
    'ano de fabricação' : [2014,2018,1970,2005]
}
menor = menor_valor(carros['preço'])
for key in carros.keys():
    print(f"{key} : {carros[key][menor]}")
'''

#5
def cadastrar(dic):
    for key in dic.keys():
        info = input(f"Diga o novo {key}")
        dic[key].append(info)
    return dic

#6
carros = {
    'nomes' : ['celta','up','kombi','uno'],
    'portas' : [4,2,6,2],
    'preço' : [1000,200,300,100],
    'ano de fabricação' : [2014,2018,1970,2005]
}
def remover(dic):
    escolha = forca_opcao("Qual carro voce deseja remover?", carros['nomes'])
    indice_remover = achar_indice(carros['nomes'],escolha)
    for key in carros.keys():
        carros[key].pop(indice_remover)
    return dic

#7
'''frase = 'A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha.'
for char in ',.!?:;':
    frase = frase.replace(char, '')
frase = frase.lower()
palavras = frase.split(' ')

contagem = {}
for palavra in palavras:
    if palavra not in contagem.keys():
        contagem[palavra] = 1
    else:
        contagem[palavra] += 1
print(contagem)
'''

#9
'''dic_1 ={
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4
}
dic_2 ={
    'c' : 5,
    'd' : 6,
    'e' : 7,
    'f' : 8,
    'g' : 9
}
comum = []
for key in dic_1.keys():
    if key in dic_2.keys():
        comum.append(key)


#10
nao_comum = []
for key in dic_1.keys():
    if key not in dic_2.keys():   
        nao_comum.append(key)
for key in dic_2.keys():
    if key not in dic_1.keys():
        nao_comum.append(key)

'''

#8
extenso = {
    'zero' : '0',
    'um' : '1',
    'dois' : '2',
    'tres' : '3',
    'quatro' : '4',
    'cinco' : '5',
    'seis' : '6',
    'sete' : '7',
    'oito' : '8',
    'nove' : '9'
}
sala = input("Qual sua sala\n->")
for numero in extenso.keys():
        sala = sala.replace(numero+' ',extenso[numero])
        sala = sala.replace(numero, extenso[numero])
print(sala)

