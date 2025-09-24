# Menu realizado com as minhas funcoes originais
# Funções retiradas de menuOpcoes.py e ResolucaoDic.py

def solicitar_entrada_numerica(msg):
    while True:
        entrada = input(msg)
        if entrada.isnumeric():
            return int(entrada)
        else:
            print("Entrada Invalida! Por favor, digite um numero valido.")

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
    indice = 0  # Corrigido: começa do indice 0 ao invés de 1
    for i in range(len(lista)):
        if lista[i] > lista[indice]:
            indice = i
    return indice

def menor_valor(lista):
    indice = 0  # Corrigido: começa do indice 0 ao invés de 1
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
    if not dic['nomes']:
        print("Nao ha carros para remover.")
        return dic
    
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

# Dicionario principal
carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}

# Programa principal
print("=== CONCESSIONARIA DANILAO CARS ===")

ano_atual = 2025
ano_nascimento = solicitar_entrada_numerica("Qual seu ano de nascimento: ")
idade = ano_atual - ano_nascimento

if idade < 18:
    print("Nao ha maior-idade para dirigir")
else:
    print(f"Bem-vindo! Voce tem {idade} anos.")
    endereco = input("Diga seu endereco para uma possivel entrega do seu veiculo: ")

    carrinho = []
    valor_total_itens = 0

    while True:
        print("\n=== MENU PRINCIPAL ===")
        opcoes_menu = ['listar', 'escolher carro', 'mais caro', 'mais barato', 'cadastrar', 'remover', 'ver carrinho', 'sair']
        escolha_menu = forca_opcao("O que voce deseja fazer?", opcoes_menu)

        if escolha_menu == 'listar':
            exibir_catalogo(carros)
            
        elif escolha_menu == 'escolher carro':
            if not carros['nomes']:
                print("Nao ha carros disponiveis.")
            else:
                exibir_catalogo(carros)
                escolha_carro = forca_opcao("Qual modelo voce deseja?", carros['nomes'])
                exibir_info_carro(carros, escolha_carro)
                
                adicionar = forca_opcao("Deseja adicionar ao carrinho?", ['sim', 'nao'])
                if adicionar == 'sim':
                    indice_carro = achar_indice(carros['nomes'], escolha_carro)
                    carrinho.append({
                        'nome': escolha_carro,
                        'preco': carros['preço'][indice_carro]
                    })
                    valor_total_itens += carros['preço'][indice_carro]
                    print(f"{escolha_carro} adicionado ao carrinho!")

        elif escolha_menu == 'mais caro':
            if not carros['preço']:
                print("Nao ha carros para comparar.")
            else:
                indice_maior = maior_valor(carros['preço'])
                print(f"\nO carro mais caro e:")
                for key in carros.keys():
                    print(f"{key}: {carros[key][indice_maior]}")

        elif escolha_menu == 'mais barato':
            if not carros['preço']:
                print("Nao ha carros para comparar.")
            else:
                indice_menor = menor_valor(carros['preço'])
                print(f"\nO carro mais barato e:")
                for key in carros.keys():
                    print(f"{key}: {carros[key][indice_menor]}")

        elif escolha_menu == 'cadastrar':
            print("\n--- Cadastrar Novo Carro ---")
            carros = cadastrar(carros)
            print("Carro cadastrado com sucesso!")

        elif escolha_menu == 'remover':
            print("\n--- Remover Carro ---")
            carros = remover(carros)
            if carros['nomes']:
                print("Carro removido com sucesso!")

        elif escolha_menu == 'ver carrinho':
            print("\n--- SEU CARRINHO ---")
            if not carrinho:
                print("Seu carrinho esta vazio.")
            else:
                print("Itens no carrinho:")
                for item in carrinho:
                    print(f"- {item['nome']} - R${item['preco']}")
                print(f"\nValor total: R${valor_total_itens}")
                
                if carrinho:
                    finalizar = forca_opcao("Deseja finalizar a compra?", ['sim', 'nao'])
                    if finalizar == 'sim':
                        # Calculo do frete
                        valor_frete = 10
                        if valor_total_itens >= 500:
                            valor_frete = 0
                        
                        valor_final = valor_total_itens + valor_frete
                        
                        print(f"\n--- RESUMO DO PEDIDO ---")
                        print("Obrigado por comprar conosco!")
                        print("Voce comprou:")
                        for item in carrinho:
                            print(f"- {item['nome']} (R${item['preco']})")
                        
                        print(f"\nValor total dos produtos: R${valor_total_itens}")
                        print(f"Valor do frete: R${valor_frete}")
                        print(f"Valor total a pagar: R${valor_final}")
                        print(f"Sera entregue em: {endereco}")
                        
                        # Remove carros comprados do estoque
                        for item in carrinho:
                            if item['nome'] in carros['nomes']:
                                indice = achar_indice(carros['nomes'], item['nome'])
                                for key in carros.keys():
                                    carros[key].pop(indice)
                        
                        carrinho = []
                        valor_total_itens = 0
                        print("\nCompra finalizada com sucesso!")

        elif escolha_menu == 'sair':
            print("Obrigado por visitar nossa concessionaria! Ate logo!")
            break