'''from revisaoDic.menuOpcoes import solicitar_entrada_numerica


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
'''



 # codigo feito com ia, nao seja usado no projeto final, somente para estudo

import sys # Usado para encerrar o programa

# --- Funções de Utilitidade (já existentes e melhoradas) ---

def forca_opcao(msg, lista_opcoes):
    """Força o usuário a escolher uma opção válida de uma lista."""
    opcoes_str = '\n'.join(f"- {opcao}" for opcao in lista_opcoes)
    # Converte as opções da lista para minúsculas para comparação
    lista_opcoes_lower = [str(opt).lower() for opt in lista_opcoes]
    
    while True:
        escolha = input(f"{msg}\n{opcoes_str}\n-> ").lower()
        if escolha in lista_opcoes_lower:
            # Retorna a opção original (com maiúsculas se houver)
            indice = lista_opcoes_lower.index(escolha)
            return lista_opcoes[indice]
        print("\nOpção inválida! Por favor, tente novamente.")


def achar_indice(lista, elem):
    """Encontra o índice de um elemento em uma lista."""
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return -1

def maior_valor(lista_valores, lista_nomes):
    """Encontra o nome correspondente ao maior valor."""
    if not lista_valores: return None
    indice_maior = 0
    for i in range(1, len(lista_valores)):
        if lista_valores[i] > lista_valores[indice_maior]:
            indice_maior = i
    return lista_nomes[indice_maior]

def menor_valor(lista_valores, lista_nomes):
    """Encontra o nome correspondente ao menor valor."""
    if not lista_valores: return None
    indice_menor = 0
    for i in range(1, len(lista_valores)):
        if lista_valores[i] < lista_valores[indice_menor]:
            indice_menor = i
    return lista_nomes[indice_menor]

# --- Funções do Sistema da Loja ---

def inicializacao():
    """Dá as boas-vindas, verifica a idade e coleta dados do usuário."""
    print("=============================================")
    print(" BEM-VINDO À CONCESSIONÁRIA DANILAO CARS ")
    print("=============================================")
    
    nome = input("Para começar, qual o seu nome? ")
    try:
        idade = int(input(f"Olá, {nome}! Quantos anos você tem? "))
    except ValueError:
        print("Idade inválida. Por favor, insira um número.")
        return None

    if idade < 18:
        print("\nDesculpe, você precisa ter 18 anos ou mais para usar nosso sistema.")
        print("A loja será desligada. Volte em alguns anos!")
        return None # Indica que a verificação falhou
    
    print("\nÓtimo! Acesso permitido.")
    endereco = input("Por favor, digite seu endereço completo para futuras entregas: ")
    
    return {'nome': nome, 'idade': idade, 'endereco': endereco}


def cadastrar(dic):
    """Cadastra um novo carro no dicionário."""
    print("\n--- Cadastro de Novo Carro ---")
    try:
        nome = input("Diga o nome do novo carro: ").capitalize()
        portas = int(input(f"Diga o número de portas para {nome}: "))
        preco = float(input(f"Diga o preço para {nome}: "))
        ano = int(input(f"Diga o ano de fabricação para {nome}: "))

        dic['nomes'].append(nome)
        dic['portas'].append(portas)
        dic['preço'].append(preco)
        dic['ano de fabricação'].append(ano)
        print(f"\nCarro '{nome}' cadastrado com sucesso!")
    except ValueError:
        print("\nErro: Portas, preço e ano devem ser números. Tente novamente.")
    return dic

def remover(dic):
    """Remove um carro do inventário."""
    if not dic['nomes']:
        print("\nNão há carros para remover.")
        return dic
        
    print("\n--- Remover Carro do Inventário ---")
    escolha = forca_opcao("Qual carro você deseja remover?", dic['nomes'])
    indice_remover = achar_indice(dic['nomes'], escolha)
    
    if indice_remover != -1:
        for key in dic.keys():
            dic[key].pop(indice_remover)
        print(f"\nCarro '{escolha}' removido com sucesso!")
    return dic

def listar_carros(dic):
    """Exibe todos os carros cadastrados em um formato legível."""
    print("\n--- Lista de Carros Disponíveis ---")
    if not dic['nomes']:
        print("Nenhum carro em estoque no momento.")
        return

    print(f"{'Nome':<15} | {'Portas':<7} | {'Preço':<15} | {'Ano':<4}")
    print("-" * 50)
    for i in range(len(dic['nomes'])):
        nome = dic['nomes'][i]
        portas = dic['portas'][i]
        preco = f"R$ {dic['preço'][i]:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        ano = dic['ano de fabricação'][i]
        print(f"{nome:<15} | {portas:<7} | {preco:<15} | {ano:<4}")
    print("-" * 50)

# --- Novas Funções (Carrinho e Compra) ---

def comprar_carro(dic_carros, carrinho):
    """Adiciona um carro ao carrinho de compras."""
    if not dic_carros['nomes']:
        print("\nDesculpe, não temos carros em estoque no momento.")
        return carrinho
    
    listar_carros(dic_carros)
    escolha = forca_opcao("\nQual carro você deseja adicionar ao carrinho?", dic_carros['nomes'])
    
    indice_carro = achar_indice(dic_carros['nomes'], escolha)
    carro_selecionado = {
        'nome': dic_carros['nomes'][indice_carro],
        'preço': dic_carros['preço'][indice_carro]
    }
    
    carrinho.append(carro_selecionado)
    print(f"\n'{escolha}' foi adicionado ao seu carrinho!")
    return carrinho

def ver_carrinho(carrinho):
    """Mostra os itens no carrinho e o subtotal."""
    print("\n--- Seu Carrinho de Compras ---")
    if not carrinho:
        print("Seu carrinho está vazio.")
        return

    subtotal = 0
    for item in carrinho:
        preco_formatado = f"R$ {item['preço']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
        print(f"- {item['nome']:<15} | {preco_formatado}")
        subtotal += item['preço']
    
    subtotal_formatado = f"R$ {subtotal:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    print("-" * 35)
    print(f"Subtotal: {subtotal_formatado}")
    print("-" * 35)

def finalizar_compra(dic_carros, carrinho, dados_usuario):
    """Processa o checkout, calcula frete e finaliza a compra."""
    if not carrinho:
        print("\nSeu carrinho está vazio. Adicione um carro antes de finalizar a compra.")
        return

    print("\n--- Finalizando Compra ---")
    subtotal = sum(item['preço'] for item in carrinho)
    
    # Lógica do Frete
    frete = 0
    carro_mais_barato = min(dic_carros['preço']) if dic_carros['preço'] else 0
    
    if subtotal < carro_mais_barato:
        frete = 500.00
        print(f"Sua compra (R$ {subtotal:,.2f}) é menor que o valor do nosso carro mais barato (R$ {carro_mais_barato:,.2f}).")
        print(f"Um frete de R$ {frete:,.2f} será adicionado.")
    else:
        print("Sua compra é elegível para FRETE GRÁTIS!")

    total = subtotal + frete
    
    # Resumo do Pedido
    print("\n--- Resumo do Pedido ---")
    print(f"Cliente: {dados_usuario['nome']}")
    print(f"Endereço de Entrega: {dados_usuario['endereco']}")
    print("\nItens:")
    for item in carrinho:
        print(f"- {item['nome']} (R$ {item['preço']:,.2f})")
    print("-" * 30)
    print(f"Subtotal: R$ {subtotal:,.2f}")
    print(f"Frete:    R$ {frete:,.2f}")
    print(f"TOTAL:    R$ {total:,.2f}")
    print("-" * 30)

    confirmacao = forca_opcao("Deseja confirmar a compra?", ["Sim", "Não"])
    if confirmacao == "Sim":
        # Remove os carros comprados do inventário
        for item_comprado in carrinho:
            if item_comprado['nome'] in dic_carros['nomes']:
                indice_remover = achar_indice(dic_carros['nomes'], item_comprado['nome'])
                for key in dic_carros.keys():
                    dic_carros[key].pop(indice_remover)
        
        carrinho.clear() # Esvazia o carrinho
        print("\nObrigado pela sua compra! Seu pedido foi processado com sucesso.")
    else:
        print("\nCompra cancelada. Seus itens continuam no carrinho.")


# --- Dicionário Inicial e Execução Principal ---
carros = {
    'nomes': ['Celta', 'Up', 'Kombi', 'Uno'],
    'portas': [4, 2, 6, 2],
    'preço': [15000.00, 35000.00, 12000.00, 10000.00],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}

def menu_principal():
    """Função que executa o menu principal do programa."""
    dados_usuario = inicializacao()
    if dados_usuario is None:
        sys.exit() # Encerra o script se a inicialização falhar

    carrinho_de_compras = []
    opcoes_menu = ['listar', 'comprar', 'ver carrinho', 'finalizar compra', 'cadastrar', 'remover', 'mais caro', 'mais barato', 'sair']
    
    while True:
        print("\n===== MENU CONCESSIONÁRIA =====")
        escolha = forca_opcao("Escolha uma das opções abaixo:", opcoes_menu)

        if escolha == 'listar':
            listar_carros(carros)
        elif escolha == 'comprar':
            comprar_carro(carros, carrinho_de_compras)
        elif escolha == 'ver carrinho':
            ver_carrinho(carrinho_de_compras)
        elif escolha == 'finalizar compra':
            finalizar_compra(carros, carrinho_de_compras, dados_usuario)
        elif escolha == 'cadastrar':
            cadastrar(carros)
        elif escolha == 'remover':
            remover(carros)
        elif escolha == 'mais caro':
            nome_carro_caro = maior_valor(carros['preço'], carros['nomes'])
            print(f"\nO carro mais caro é: {nome_carro_caro}" if nome_carro_caro else "\nNão há carros para comparar.")
        elif escolha == 'mais barato':
            nome_carro_barato = menor_valor(carros['preço'], carros['nomes'])
            print(f"\nO carro mais barato é: {nome_carro_barato}" if nome_carro_barato else "\nNão há carros para comparar.")
        elif escolha == 'sair':
            print(f"\nSaindo do sistema. Até logo, {dados_usuario['nome']}!")
            break

# Inicia o programa
if __name__ == "__main__":
    menu_principal()