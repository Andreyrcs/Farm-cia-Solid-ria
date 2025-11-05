# SISTEMA FARMÁCIA SOLIDÁRIA

medicamentos = []  # lista que vai armazenar todos os medicamentos cadastrados
clientes = []      # lista que vai armazenar os clientes doador ou requisitante
historico = []     # lista que vai guardar o histórico geral de doações e requisições


# CLASSE DO NÓ DA ÁRVORE BINÁRIA

import os  # importa biblioteca para executar comandos do sistema (como limpar a tela)

def limpar_tela():  
    os.system('cls' if os.name == 'nt' else 'clear')  # limpa a tela: 'cls' no Windows, 'clear' no Linux/Mac
    
while True:  
    limpar_tela()  # chama a função para limpar a tela
    print("\n      Farmacia Solidária     \n")  # imprime o título do sistema
    break  # sai do loop após limpar a tela e mostrar o título

class NoMedicamento:  
    def __init__(self, nome, dados):  
        self.nome = nome               # nome do medicamento que vai servir como chave na árvore
        self.dados = dados             # um dicionário com todos os dados do medicamento
        self.esquerda = None           # nó filho da esquerda (menor que o nome atual)
        self.direita = None            # nó filho da direita (maior que o nome atual)


# CLASSE ÁRVORE BINÁRIA DE MEDICAMENTOS

class ArvoreMedicamentos:  
    def __init__(self):  
        self.raiz = None  # define a raiz da árvore como vazia no começo

    def inserir(self, nome, dados):  
        self.raiz = self._inserir_recursivo(self.raiz, nome, dados)  # chama a função recursiva para inserir o nó

    def _inserir_recursivo(self, no, nome, dados):  
        if no is None:  
            return NoMedicamento(nome, dados)  # se não existir nó, cria um novo nó com o nome e dados
        if nome.lower() < no.nome.lower():  
            no.esquerda = self._inserir_recursivo(no.esquerda, nome, dados)  # se nome menor, vai para esquerda
        elif nome.lower() > no.nome.lower():  
            no.direita = self._inserir_recursivo(no.direita, nome, dados)   # se nome maior, vai para direita
        else:  
            no.dados = dados  # se o nome for igual, apenas atualiza os dados
        return no  # retorna o nó atualizado

    def buscar(self, nome):  
        return self._buscar_recursivo(self.raiz, nome)  # função pública que chama a recursiva para buscar o nome

    def _buscar_recursivo(self, no, nome):  
        if no is None:  
            return None  # se nó vazio, não encontrou o medicamento
        if nome.lower() == no.nome.lower():  
            return no.dados  # se encontrou o nome, retorna os dados
        elif nome.lower() < no.nome.lower():  
            return self._buscar_recursivo(no.esquerda, nome)  # se menor, vai para esquerda
        else:  
            return self._buscar_recursivo(no.direita, nome)  # se maior, vai para direita

    def listar_em_ordem(self, no):  
        if no:  
            self.listar_em_ordem(no.esquerda)  # percorre primeiro o lado esquerdo
            print(f"Nome: {no.nome} | Quantidade: {no.dados['quantidade']} | Validade: {no.dados['validade']} | Lote: {no.dados['lote']}")  # imprime o nó atual
            self.listar_em_ordem(no.direita)  # percorre depois o lado direito

arvore = ArvoreMedicamentos()  # cria a árvore de medicamentos vazia


# FUNÇÕES DO SISTEMA

def menu():  
    print("1 - Cadastrar Medicamento")  # opção 1 do menu
    print("2 - Listar Medicamentos em ordem")  # opção 2 do menu
    print("3 - Buscar Medicamento por Nome")  # opção 3 do menu
    print("4 - Requisitar Medicamento")  # opção 4 do menu
    print("5 - Cadastrar Nome e Tipo de Cliente")  # opção 5 do menu
    print("6 - Listar Clientes")  # opção 6 do menu
    print("7 - Histórico de Requisições e Doações")  # opção 7 do menu
    print("0 - Sair")  # opção 0 do menu

def cadastrar_nome_e_tipo_cliente(clientes):  
    print("\n--- Cadastrar Nome e Tipo de Cliente ---")  # título da função
    nome_cliente = input("Nome completo do Cliente: ")  # pede o nome do cliente
    idade_cliente = input("Idade do Cliente: ")  # pede a idade do cliente
    rg_cliente = input("RG do Cliente: ")  # pede o RG do cliente
    escolha_tipo = input("Tipo de Cliente (1 - Doador, 2 - Requisitante): ")  # pede se é doador ou requisitante

    if escolha_tipo == '1':  
        tipo_cliente = 'Doador'  # se 1, define como doador
    elif escolha_tipo == '2':  
        tipo_cliente = 'Requisitante'  # se 2, define como requisitante
    else:  
        print("Tipo de cliente inválido.\n")  # se não for 1 ou 2, imprime aviso
        return  # retorna sem cadastrar

    novo_cliente = {  
        'nome_cliente': nome_cliente,  # adiciona o nome no dicionário
        'idade_cliente': idade_cliente,  # adiciona a idade
        'rg_cliente': rg_cliente,  # adiciona o RG
        'tipo_cliente': tipo_cliente  # adiciona o tipo do cliente
    }

    clientes.append(novo_cliente)  # adiciona o cliente na lista
    print(f"Cliente {nome_cliente} ({tipo_cliente}) cadastrado com sucesso!\n")  # confirma cadastro

def cadastrar_medicamentos(medicamentos, clientes, historico):  
    print("\n--- Cadastrar Medicamento ---")  # título da função

    doadores = [c for c in clientes if c['tipo_cliente'] == 'Doador']  # pega só os clientes doadores

    if not doadores:  
        print(" Nenhum doador cadastrado. Cadastre um primeiro.\n")  # se não tiver doadores, avisa
        return  # sai da função

    for i, d in enumerate(doadores, 1):  
        print(f"{i}. {d['nome_cliente']}")  # mostra a lista de doadores numerada

    try:  
        escolha = int(input("Selecione o número do doador: "))  # pede para escolher doador
        doador = doadores[escolha - 1]['nome_cliente']  # pega o nome do doador escolhido
    except (ValueError, IndexError):  
        print("Escolha inválida.\n")  # se digitar errado, avisa
        return  # sai da função

    id_medicamento = input("ID do Medicamento: ")  # pede ID do medicamento
    nome = input("Nome do Medicamento: ")  # pede nome
    quantidade = int(input("Quantidade: "))  # pede quantidade
    validade = input("Validade (DD/MM/AAAA): ")  # pede validade
    lote = input("Lote: ")  # pede lote

    novo_medicamento = {  
        'ID': id_medicamento,  # adiciona ID
        'nome': nome,  # adiciona nome
        'quantidade': quantidade,  # adiciona quantidade
        'validade': validade,  # adiciona validade
        'lote': lote,  # adiciona lote
        'doador': doador  # adiciona o doador
    }

    medicamentos.append(novo_medicamento)  # adiciona na lista principal
    arvore.inserir(nome, novo_medicamento)  # insere na árvore
    historico.append({'tipo': 'Doação', 'cliente': doador, 'medicamento': nome, 'quantidade': quantidade})  # adiciona no histórico

    print(f"\nMedicamento '{nome}' cadastrado com sucesso por {doador}!\n")  # confirma cadastro


# FUNÇÕES DE LISTAR, BUSCAR E REQUISITAR

def listar_medicamentos():  
    print("\n--- Lista de Medicamentos (Ordem Alfabética) ---")  # título
    if arvore.raiz is None:  
        print("Nenhum medicamento cadastrado.\n")  # se árvore vazia, avisa
    else:  
        arvore.listar_em_ordem(arvore.raiz)  # percorre a árvore em ordem alfabética

def buscar_medicamento():  
    print("\n--- Buscar Medicamento ---")  # título
    nome_busca = input("Digite o nome do medicamento: ")  # pede o nome
    resultado = arvore.buscar(nome_busca)  # busca na árvore

    if resultado:  
        print(f"Encontrado: {resultado['nome']} | Quantidade: {resultado['quantidade']} | Validade: {resultado['validade']} | Lote: {resultado['lote']}")  # se achou, imprime
    else:  
        print("Medicamento não encontrado.\n")  # se não achou, avisa

def listar_clientes(clientes):  
    print("\n--- Lista de Clientes ---")  # título
    if not clientes:  
        print("Nenhum cliente cadastrado.\n")  # se lista vazia, avisa
        return  
    for c in clientes:  
        print(f"Nome: {c['nome_cliente']} | Idade: {c['idade_cliente']} | RG: {c['rg_cliente']} | Tipo: {c['tipo_cliente']}")  # imprime cada cliente

def requisitar(medicamentos, clientes, historico):  
    print("\n--- Requisitar Medicamento ---")  # título
    requisitantes = [c for c in clientes if c['tipo_cliente'] == 'Requisitante']  # pega só requisitantes

    if not requisitantes:  
        print("⚠️ Nenhum requisitante cadastrado.\n")  # se não houver, avisa
        return  

    for i, c in enumerate(requisitantes, 1):  
        print(f"{i}. {c['nome_cliente']}")  # imprime a lista numerada de requisitantes

    try:  
        escolha = int(input("Selecione o número do requisitante: "))  # pede escolha
        requisitante = requisitantes[escolha - 1]['nome_cliente']  # pega o nome
    except (ValueError, IndexError):  
        print("Escolha inválida.\n")  # se digitar errado, avisa
        return  

    nome = input("Nome do medicamento: ")  # pede o nome do medicamento
    id_med = input("ID do medicamento: ")  # pede o ID
    qtd = int(input("Quantidade: "))  # pede quantidade a requisitar

    for med in medicamentos:  
        if med['nome'].lower() == nome.lower() and med['ID'] == id_med:  # se encontrou o medicamento correto
            if med['quantidade'] >= qtd:  
                med['quantidade'] -= qtd  # subtrai quantidade requisitada
                historico.append({'tipo': 'Requisição', 'cliente': requisitante, 'medicamento': nome, 'quantidade': qtd})  # adiciona no histórico
        
                print(f"\nRequisição de {qtd} unidades do medicamento '{nome}' realizada com sucesso!\n")  # confirma
                return  
            else:  
                print("Quantidade insuficiente.\n")  # se estoque não tiver suficiente
                return  
    print("Medicamento não encontrado.\n")  # se não encontrou no final

def historico_requisicoes_e_doacoes(historico):  
    print("\n--- Histórico de Requisições e Doações ---")  # título
    if not historico:  
        print("Nenhum registro encontrado.\n")  # se vazio
        return  
    for h in historico:  
        print(f"{h['tipo']}: {h['cliente']} → {h['medicamento']} ({h['quantidade']} unidades)")  # imprime cada registro




# LOOP PRINCIPAL DO PROGRAMA

while True:  
    menu()  # mostra o menu
    opcao = input("Escolha uma opção: ")  # lê opção do usuário

    if opcao == '1':  
        cadastrar_medicamentos(medicamentos, clientes, historico)  # chama cadastro de medicamentos
    elif opcao == '2':  
        listar_medicamentos()  # chama listagem em ordem
    elif opcao == '3':  
        buscar_medicamento()  # chama busca
    elif opcao == '4':  
        requisitar(medicamentos, clientes, historico)  # chama requisição
    elif opcao == '5':  
        cadastrar_nome_e_tipo_cliente(clientes)  # chama cadastro de cliente
    elif opcao == '6':  
        listar_clientes(clientes)  # lista clientes
    elif opcao == '7':  
        historico_requisicoes_e_doacoes(historico)  # mostra histórico completo
    elif opcao == '0':  
        print("Saindo do sistema...")  # mensagem de saída
        break  # sai do loop
    else:  
        print("Opção inválida.\n")  # caso escolha inválida

    input("Pressione Enter para continuar...")  # pausa para o usuário ver o resultado antes de continuar
