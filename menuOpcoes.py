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

nomes_vinhos = ['Pergola', 'Sangue de Boi', 'Cantinho do Vale']
precos_vinhos = [10, 20, 30]

def solicitar_entrada_numerica(msg):
    while True:
        entrada = input(msg)
        if entrada.isnumeric():
            return int(entrada)
        else:
            print("Entrada Invalida! Por favor, digite um numero valido.")

def solicitar_continuar(msg):
    while True:
        resposta = input(msg)
        if resposta in ('s', 'n'):
            return resposta
        else:
            print("Entrada Invalida! Por favor, digite 's' para sim ou 'n' para nao.")

def exibir_catalogo(nomes, precos):
    print("\nEsses sao nossos vinhos: ")
    for i in range(len(nomes)):
        print(f"- {nomes[i]} - R${precos[i]:.2f}")

ano_atual = 2025
ano_nascimento = solicitar_entrada_numerica("Qual seu ano de nascimetno: ")
idade = ano_atual - ano_nascimento

if idade < 18:
    print("QUE FEIO! VENDA PROIBIDA PARA MENORES DE 18 ANOS!")
else:
    endereco = input("Diga seu endereco para entrega: ")

    carrinho_compras = []
    valor_total_itens = 0

    while True:
        exibir_catalogo(nomes_vinhos, precos_vinhos)

        escolha_valida = False
        vinho_selecionado_nome = ""
        vinho_selecionado_preco = 0

        while not escolha_valida:
            escolha_nome_input = input("QUal vinho voce quer (Digite o nome completo)?\n->")
            for i in range(len(nomes_vinhos)):
                if nomes_vinhos[i].lower() == escolha_nome_input.lower():
                    vinho_selecionado_nome = nomes_vinhos[i]
                    vinho_selecionado_preco = precos_vinhos[i]
                    escolha_valida = True
                    break
            if not escolha_valida:
                print("Vinho Invalido! Por favor, escolha um vinho da lista.")

        qtd = solicitar_entrada_numerica(f"Quantas garrafas de {vinho_selecionado_nome} voce quer?\n->")

        carrinho_compras.append([vinho_selecionado_nome, qtd, vinho_selecionado_preco])
        valor_total_itens += vinho_selecionado_preco * qtd

        continuar_comprando = solicitar_continuar("Voce quer continuar comprando (s/n)?\n->")
        if continuar_comprando == 'n':
            break

    valor_frete = 10
    if valor_total_itens >= 500:
        valor_frete = 0

    print(f"\nvoce pagara R${valor_frete:.2f} de frete!")
    valor_final_comfrete = valor_total_itens + valor_frete

    print("\n--- RESUMO DO SEU PEDIDO ---")
    print("Obrigado por comprar conosco!")
    print("Voce comprou: ")
    for item_comprado in carrinho_compras:
        nome_item = item_comprado[0]
        quantidade_item = item_comprado[1]
        preco_unitario_item = item_comprado[2]
        print(f"- {quantidade_item} garrafa(s) de {nome_item} (R${preco_unitario_item:.2f} cada)")

    print(f"\nValor total dos produtos: R${valor_total_itens:.2f}")
    print(f"Valor do frete: R${valor_frete:.2f}")
    print(f"O valor total a pagar sera de R${valor_final_comfrete:.2f} e sera entregue emm {endereco}")


