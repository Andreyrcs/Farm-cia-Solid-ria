#include <stdio.h>
#include "medicamentos.h.c"

void menuPrincipal();


// Função principal - ponto de entrada do programa
int main() {
    menuPrincipal();  // Inicia o programa pelo menu principal
    return 0;
}

// Função que mostra o menu principal e lê a opção do usuário
void menuPrincipal() {
    int opcao;

    do {
       
        printf("===========================================\n");
        printf("        MENU PRINCIPAL - FARMÁCIA          \n");
        printf("===========================================\n");
        printf("1. Medicamentos\n");
        printf("0. Sair\n");
        printf("-------------------------------------------\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                menuMedicamentos();  // Chama o menu de medicamentos
                break;
            case 0:
                printf("Encerrando o sistema...\n");
                break;
            default:
                printf("Opção inválida! Tente novamente.\n");
        }
    } while (opcao != 0);
}