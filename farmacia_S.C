
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Estruturas básicas
typedef struct {
    int codigo;
    char nome[50];
    char principioAtivo[50];
    char fabricante[50];
    float preco;
    int quantidade;
    char validade[11];
} Medicamento;

typedef struct {
    int id;
    char nome[50];
    char telefone[20];
} Cliente;

// Protótipos de funções
void menuPrincipal();
void telaLogin();
void menuMedicamentos();
void menuVendas();
void menuRelatorios();
void cadastrarMedicamento();
void listarMedicamentos();
void limparTela();

// Variáveis globais (apenas para simulação)
Medicamento estoque[100];
int totalMedicamentos = 0;

int main() {
    telaLogin();
    return 0;
}

// ==== TELA DE LOGIN ====
void telaLogin() {
    char usuario[30], senha[20];

    limparTela();
    printf("===========================================\n");
    printf("     💊 SISTEMA DE FARMÁCIA COMUNITÁRIA     \n");
    printf("===========================================\n");
    printf("Usuário: ");
    scanf("%s", usuario);
    printf("Senha: ");
    scanf("%s", senha);

    // Validação simples
    if (strcmp(usuario, "admin") == 0 && strcmp(senha, "1234") == 0) {
        printf("\nLogin realizado com sucesso!\n");
        system("pause");
        menuPrincipal();
    } else {
        printf("\nUsuário ou senha incorretos!\n");
        system("pause");
        telaLogin();
    }
}

// ==== MENU PRINCIPAL ====
void menuPrincipal() {
    int opcao;

    do {
        limparTela();
        printf("===========================================\n");
        printf("        MENU PRINCIPAL - FARMÁCIA          \n");
        printf("===========================================\n");
        printf("1. Medicamentos\n");
        printf("2. Vendas\n");
        printf("3. Relatórios\n");
        printf("0. Sair\n");
        printf("-------------------------------------------\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1: menuMedicamentos(); break;
            case 2: menuVendas(); break;
            case 3: menuRelatorios(); break;
            case 0: printf("Encerrando o sistema...\n"); break;
            default: printf("Opção inválida!\n"); system("pause");
        }
    } while (opcao != 0);
}

// ==== MENU DE MEDICAMENTOS ====
void menuMedicamentos() {
    int opcao;

    do {
        limparTela();
        printf("===========================================\n");
        printf("         MENU DE MEDICAMENTOS              \n");
        printf("===========================================\n");
        printf("1. Cadastrar Medicamento\n");
        printf("2. Listar Medicamentos\n");
        printf("0. Voltar\n");
        printf("-------------------------------------------\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1: cadastrarMedicamento(); break;
            case 2: listarMedicamentos(); break;
            case 0: break;
            default: printf("Opção inválida!\n"); system("pause");
        }
    } while (opcao != 0);
}

// ==== CADASTRO DE MEDICAMENTO ====
void cadastrarMedicamento() {
    limparTela();
    printf("=== CADASTRAR NOVO MEDICAMENTO ===\n");
    Medicamento m;

    printf("Código: ");
    scanf("%d", &m.codigo);
    printf("Nome: ");
    scanf(" %[^\n]", m.nome);
    printf("Princípio ativo: ");
    scanf(" %[^\n]", m.principioAtivo);
    printf("Fabricante: ");
    scanf(" %[^\n]", m.fabricante);
    printf("Preço: R$ ");
    scanf("%f", &m.preco);
    printf("Quantidade: ");
    scanf("%d", &m.quantidade);
    printf("Data de validade (dd/mm/aaaa): ");
    scanf("%s", m.validade);

    estoque[totalMedicamentos++] = m;
    printf("\nMedicamento cadastrado com sucesso!\n");
    system("pause");
}

// ==== LISTAGEM DE MEDICAMENTOS ====
void listarMedicamentos() {
    limparTela();
    printf("=== LISTA DE MEDICAMENTOS ===\n\n");

    if (totalMedicamentos == 0) {
        printf("Nenhum medicamento cadastrado.\n");
    } else {
        printf("Cód | Nome                     | Qtde | Preço\n");
        printf("------------------------------------------------\n");
        for (int i = 0; i < totalMedicamentos; i++) {
            printf("%-3d | %-25s | %-4d | R$ %.2f\n",
                   estoque[i].codigo,
                   estoque[i].nome,
                   estoque[i].quantidade,
                   estoque[i].preco);
        }
    }
    printf("\n");
    system("pause");
}

// ==== MENU DE VENDAS ====
void menuVendas() {
    limparTela();
    printf("=== REGISTRO DE VENDA ===\n");
    printf("Função em prototipação...\n");
    printf("Futuramente: busca de produtos, inserção e pagamento.\n");
    system("pause");
}

// ==== MENU DE RELATÓRIOS ====
void menuRelatorios() {
    limparTela();
    printf("=== RELATÓRIOS ===\n");
    printf("1. Vendas do Dia\n");
    printf("2. Estoque Baixo\n");
    printf("3. Financeiro\n");
    printf("\nFunção em prototipação...\n");
    system("pause");
}

// ==== FUNÇÃO DE LIMPEZA DE TELA ====
void limparTela() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}