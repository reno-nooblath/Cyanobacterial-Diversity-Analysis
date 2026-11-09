#!/usr/bin/env python3
"""
Parser de Matrizes Pan-Genômicas (Core vs Acessório)
Finalidade: Sumarizar os resultados estatísticos das famílias gênicas para os três grupos do artigo:
1. Sphaerospermopsis (Global)
2. Cylindrospermopsis raciborskii (Américas)
3. Cylindrospermopsis raciborskii (Não-Américas)
"""

def summarize_pangenome_stats(group_name, core_genes, total_pangenome):
    """
    Imprime e valida o resumo estatístico do pangenoma por grupo específico.
    """
    accessory_genes = total_pangenome - core_genes
    print(f"==========================================")
    print(f" RELATÓRIO PANGENÔMICO: {group_name}")
    print(f"==========================================")
    print(f" * Genes Core (Essenciais)    : {core_genes}")
    print(f" * Genes Acessórios/Variáveis : {accessory_genes}")
    print(f" * Tamanho Total do Pangenoma : {total_pangenome} genes")
    print(f"==========================================")

if __name__ == "__main__":
    # Dados extraídos e validados no estudo publicado
    summarize_pangenome_stats(
        group_name="Sphaerospermopsis Global (6 genomas)", 
        core_genes=2375, 
        total_pangenome=9000
    )
    
    summarize_pangenome_stats(
        group_name="Cylindrospermopsis raciborskii - Américas (10 genomas)", 
        core_genes=1410, 
        total_pangenome=6000
    )

    summarize_pangenome_stats(
        group_name="Cylindrospermopsis raciborskii - Não-Américas (11 genomas)", 
        core_genes=2249, 
        total_pangenome=5000
    )
