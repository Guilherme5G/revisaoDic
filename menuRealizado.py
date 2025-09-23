from revisaoDic.menuOpcoes import solicitar_entrada_numerica


def solicitar_entrada_numerica(msg):
    while True:
        entrada = input(msg)
        if entrada.isnumeric():
            return int(entrada)
        else:
            print("Entrada invalida!")

def exibir_catalogo(dic):
    print("\nEsses sao nossos modelos: ")
    for i in range(len(dic)):
        print([carros])

def forca_opcao(msg,lista_opcoes):
    opcoes = '\n'.join(lista_opcoes)
    escolha = input(f"{msg}\n{opcoes}\n->")
    while escolha not in lista_opcoes:
        print("Invalido")
        escolha = input(f"{msg}\n{opcoes}\n->")
    return escolha

carros = {
    'nomes' : ['celta','up','kombi','uno'],
    'portas' : [4,2,6,2],
    'preço' : [1000,200,300,100],
    'ano de fabricação' : [2014,2018,1970,2005]
}

ano_atual = 2025
ano_nascimento = solicitar_entrada_numerica("Qual seu ano de nascimento: ")
idade = ano_atual - ano_nascimento

if idade <18:
    print("Nao ha maior-idade para dirigir")
else:
    endereco = input("Diga seu endereco para uma possivel entrega do seu veiculo: ")

    carrinho = []
    valor_total_itens = 0

    while True:
        exibir_catalogo(carros)

        escolha = False
        carro_selecionado = ""

        while not escolha:
            escolha_nome_input = forca_opcao("Qual modelo voce deseja?", carros['nomes'])
