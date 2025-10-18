'''import os  # Importa o módulo 'os' para poder usar o comando de limpar tela (cls)

# Lista onde serão armazenados todos os ativos cadastrados
listaAtivos = []



# Função principal com o menu de opções
def menu():
    escolha = -1  # Inicializa a variável de escolha com um valor que não encerra o programa

    # Loop principal que exibe o menu até o usuário escolher sair
    while escolha != 0:
        os.system('cls')  # Limpa a tela
        print(
 Sistema de Gestão de Ativos 

1 - Cadastrar
2 - Alterar Status Ativos/Inativos
3 - Excluir
4 - Consultar
5 - Listar
0 - Sair
)
        try:
            escolha = int(input("Escolha uma opção: "))  # Solicita a escolha do usuário
        except ValueError:
            print("O número está invalido")  # Trata erro se digitar letra
            input()
            continue

        # Chama a função correspondente à opção escolhida
        if escolha == 1:
            cadastrar()
        elif escolha == 2:
            alterar()
        elif escolha == 3:
            excluir()
        elif escolha == 4:
            consultar()
        elif escolha == 5:
            listar()
        elif escolha == 0:
            print("Saindo do sistema")  # Encerra o programa
            input()
        else:
            print("Opção inválida.")  # Opção fora do menu
            input()
# Função para cadastrar um novo ativo
def cadastrar():
    os.system('cls')  # Limpa a tela
    print(" Cadastrar")
    ativo = {}  # Cria um dicionário vazio para armazenar os dados do ativo

    ativo['id'] = input("ID: ")  # Solicita o ID do ativo ao usuário

    # Verifica se já existe um ativo com o mesmo ID
    for atv in listaAtivos:
        if atv['id'] == ativo['id']:
            print(" Já existe um ativo com esse ID.")
            input()  # Pausa para o usuário ver a mensagem
            return  # Sai da função sem cadastrar

    ativo['descricao'] = input("Descrição: ")  # Solicita a descrição
 	

# Tenta converter os dados para os tipos corretos (float e int)
# Se o usuário digitar algo inválido (exemplo: letras ao invés de números), o bloco 'except' é ativado para evitar que o programa trave
    try:
        ativo['modelo'] = input("Modelo: ")  # Solicita a descrição
        ativo['valor'] = float(input("Valor: "))  # Solicita e converte o valor para float
        ativo['quantidade'] = int(input("Quantidade: "))  # Solicita e converte a quantidade para inteiro
    except ValueError:  # Caso o usuário digite letras em vez de números causando um erro no programa 
        print(" Valor ou quantidade inválidos.")
        input()
        return  # Sai da função sem cadastrar

    ativo['nota_fiscal'] = input("Número da nota fiscal: ")  # Solicita a nota fiscal
    ativo['status'] = "Ativo"  # Define o status padrão como "Ativo"

    listaAtivos.append(ativo)  # Adiciona o ativo na lista principal
    print("Ativo cadastrado com sucesso")
    input()  # Pausa para o usuário ver a mensagem

# Função para alterar o status do ativo (Ativo ↔ Inativo)
def alterar():
    os.system('cls')  # Limpa a tela
    print(" Alterar Status do Ativo ")
    id_busca = input("Digite o ID do ativo: ")  # Solicita o ID a ser alterado

    # Procura o ativo pelo ID
    for atv in listaAtivos:
        if atv['id'] == id_busca:
            # Altera o status para o contrário do atual
            atv['status'] = "Inativo" if atv['status'] == "Ativo" else "Ativo"
            print(f" Status alterado para {atv['status']}")
            input()
            return  # Sai da função após alterar
    print(" Ativo não encontrado.")
    input()

# Função para excluir um ativo
def excluir():
    os.system('cls')  # Limpa a tela
    print(" Excluir Ativo ")
    id_excluir = input("Digite o ID do ativo: ")  # Solicita o ID do ativo a ser excluído

    # Procura o ativo na lista
    for atv in listaAtivos:
        if atv['id'] == id_excluir:
            listaAtivos.remove(atv)  # Remove o ativo da lista
            print("Ativo excluído com sucesso")
            input()
            return
    print("Ativo não encontrado.")
    input()

# Função para consultar um ativo específico por ID
def consultar():
    os.system('cls')  # Limpa a tela
    print(" Consultar Ativo")
    id_consulta = input("Digite o ID do ativo: ")  # Solicita o ID

    # Procura o ativo na lista
    for atv in listaAtivos:
        if atv['id'] == id_consulta:
            # Exibe os dados do ativo
            print(f"ID: {atv['id']}")
            print(f"Descrição: {atv['descricao']}")
            print(f"Modelo: {atv['modelo']}")
            print(f"Valor: R$ {atv['valor']:.2f}")
            print(f"Quantidade: {atv['quantidade']}")
            print(f"Nota Fiscal: {atv['nota_fiscal']}")
            print(f"Status: {atv['status']}")
            input()
            return
    print("Ativo não encontrado.")
    input()

# Função para listar todos os ativos cadastrados
def listar():
    os.system('cls')  # Limpa a tela
    print(" Lista de Ativos ")

    # Verifica se a lista está vazia
    if not listaAtivos:
        print("Nenhum ativo cadastrado.")
    else:
        # Exibe todos os ativos da lista
        for atv in listaAtivos:
            print(f"ID: {atv['id']}  | Descrição: {atv['descricao']}  | Modelo: {atv['modelo']} | Valor: R$ {atv['valor']:.2f} | "
                  f"Qtd: {atv['quantidade']} | Nota Fiscal: {atv['nota_fiscal']} | Status: {atv['status']}")
    input()

# Inicia o programa executando o menu
menu()'''


def menu():
    print("\n      Farmacia Solidária     \n")
    print("1 - Cadastrar Medicamento")
    print("2 - Listar Medicamentos")
    print("3 - Buscar Medicamento por Nome")
    print("4 - requisitar Medicamento")
    print("0 - Sair")

def cadastrar(medicamentos):
    print("\n--- Cadastrar Medicamento ---")
    id_medicamento = input("ID do Medicamento: ")
    nome = input("Nome do Medicamento: ")
    quantidade = int(input("Quantidade: "))
    validade = int(input("Validade (DD/MM/AAAA): "))
    lote = input("Lote: ")
    medicamentos = {'ID': id_medicamento, 'nome': nome, 'quantidade': quantidade, 'validade': validade, 'lote': lote}
    medicamentos.append(medicamentos)
    print(f"Medicamento {nome} cadastrado com sucesso!\n")
    
def listar(medicamentos):
    print("\n--- Lista de Medicamentos ---")
    if len(medicamentos) == 0:
        print("Nenhum medicamento cadastrado.\n")
        return
    
    for med in medicamentos:
        print(f"ID: {med[1]} | Nome: {med[2]} | Quantidade: {med[3]} | Validade: {med[4]} | Lote: {med[5]} ")
    
    def buscar(medicamentos):
        print("\n--- Buscar Medicamento por Nome ---")
        nome_busca = input("Digite o nome do medicamento: ")
        encontrados = [med for med in medicamentos if med['nome'].lower() == nome_busca.lower()]
        
        if encontrados:
            for med in encontrados:
                print(f"ID: {med['ID']} | Nome: {med['nome']} | Quantidade: {med['quantidade']} | Validade: {med['validade']} | Lote: {med['lote']}")
        else:
            print("Medicamento não encontrado.\n")