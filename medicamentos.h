#ifndef MEDICAMENTOS_H
#define MEDICAMENTOS_H


// Definição da estrutura Medicamento
typedef struct {
    int codigo;              // Código do medicamento
    char nome[50];           // Nome do medicamento
    char principioAtivo[50]; // Princípio ativo do medicamento
    char fabricante[50];     // Fabricante do medicamento
    float preco;             // Preço do medicamento
    int quantidade;          // Quantidade em estoque
    char validade[11];       // Data de validade (formato dd/mm/aaaa)
} Medicamento;

// Protótipos das funções usadas no programa
void menuMedicamentos();
void cadastrarMedicamento();
void listarMedicamentos();

#endif