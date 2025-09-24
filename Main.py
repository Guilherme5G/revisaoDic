from functions import *

carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}

print("==== CONCESSIONARIA DO DANILAO ====")

ano_atual = 2025
ano_nascimento = solicitar_entrada("Qual o seu ano de nascimento?")
idade = ano_atual - ano_nascimento
if idade < 18:
    print("Voce nao pode usufruir de uma concessionaria, volte quando for maior de idade.")
else:
    print(f"Bem vindo, voce tem {idade} anos.")
    endereco = input("Diga seu endereco para uma possivel entrega de seu veiculo: ")
    
    carrinho = 0
    valor_total_carros = 0

    while True:
        print("==== MENU PRINCIPAL ====")
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
                        'preco': carros['preco'][indice_carro]
                    })
                    valor_total_carros += carros['preco'][indice_carro]
                    print(f"{escolha_carro} adicionado ao carrinho!")
        elif escolha_menu == 'mais caro':
            if not carros['preco']:
                print("Nao ha carros para comparar.")
            else:
                indice_maior = maior_valor(carros['preco'])
                print(f"\nO carro mais caro e: ")
                for key in carros.keys():
                    print(f"{key}: {carros[key][indice_maior]}")

        elif escolha_menu == 'mais barato':
            if not carros['preco']:
                print("Nao ha carros para comparar.")
            else:
                indice_menor = menor_valor(carros['preco'])
                print(f"\nO carro mais barato e: ")
                for key in carros.keys():
                    print(f"{key}: {carros[key][indice_menor]}")

        