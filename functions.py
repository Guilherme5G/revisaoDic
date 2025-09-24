def solicitar_entrada(msg):
    while True:
        entrada = input(msg)
        if entrada.isnumeric():
            return int(entrada)
        else:
            print("Entrada Invalida!")

def forca_opcao(msg, lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n->")
    while escolha not in lista_opcoes:
        print("Invalido")
        escolha = input(f"{msg}\n{opcoes}\n->")
    return escolha

def achar_indice(lista, elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i


def maior_valor(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[i] > lista[indice]:
            indice = i
    return indice

def menor_valor(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[i] < lista[indice]:
            indice = i
    return indice

def cadastrar(dic):
    for key in dic.keys():
        info = input(f"Diga o novo {key}: ")
        dic[key].append(info)
    return dic

def remover(dic):
    escolha = forca_opcao("Qual carro voce deseja remover?", dic['nomes'])
    indice_remover = achar_indice(dic['nomes'], escolha)
    for key in dic.keys():
        dic[key].pop(indice_remover)
    return dic

def exibir_catalogo(dic):
    print("\nEsses sao nossos modelos: ")
    for i in range(len(dic['nomes'])):
        print(f"- {dic['nomes'][i]} - Portas: {dic['portas'][i]} - Preço: R${dic['preço'][i]} - Ano: {dic['ano de fabricação'][i]}")

def exibir_info_carro(dic, escolha):
    indice_escolha = achar_indice(dic['nomes'], escolha)
    print(f"\nInformacoes do {escolha}:")
    for key in dic.keys():
        print(f"{key}: {dic[key][indice_escolha]}")


