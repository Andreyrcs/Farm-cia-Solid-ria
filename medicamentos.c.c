#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "medicamentos.h.c"




// Variáveis globais para armazenar os medicamentos
Medicamento estoque[100];   // Array para guardar até 100 medicamentos
int totalMedicamentos = 0;  // Quantidade de medicamentos cadastrados


// Função que mostra o menu de medicamentos
void menuMedicamentos() {
    int opcao;

    do {
        
        printf("\n\n===========================================\n");
        printf("         MENU DE MEDICAMENTOS              \n");
        printf("===========================================\n");
        printf("1. Cadastrar Medicamento\n");
        printf("2. Listar Medicamentos\n");
        printf("0. Voltar\n");
        printf("-------------------------------------------\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                cadastrarMedicamento();  // Chama função para cadastrar um medicamento
                break;
            case 2:
                listarMedicamentos();    // Chama função para listar os medicamentos cadastrados
                break;
            case 0:
                // Voltar para o menu principal
                break;
            default:
                printf("Opção inválida! Tente novamente.\n");
              
        }
    } while (opcao != 0);
}

// Função para cadastrar um novo medicamento no estoque
void cadastrarMedicamento() {
    
    printf("=== CADASTRAR NOVO MEDICAMENTO ===\n");
    Medicamento m;

    // Leitura dos dados do medicamento
    printf("Código: ");
    scanf("%d", &m.codigo);
    printf("Nome: ");
    scanf(" %[^\n]", m.nome); // Leitura que aceita espaços
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

    // Armazena o medicamento no array e atualiza o total
    estoque[totalMedicamentos++] = m;

    printf("\nMedicamento cadastrado com sucesso!\n");
}

// Função para mostrar a lista de medicamentos cadastrados
void listarMedicamentos() {
    
    printf("=== LISTA DE MEDICAMENTOS ===\n\n");

    // Verifica se há medicamentos cadastrados
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
  
}


