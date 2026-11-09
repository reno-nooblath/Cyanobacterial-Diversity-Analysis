#!/usr/bin/env python3
"""
Módulo de Pré-processamento de Genomas (FASTA/GFF)
Foco: Limpeza e filtragem de scaffolds para linhagens de Cylindrospermopsis (Americas / Non-Americas) 
e Sphaerospermopsis (Global).
Autoria: Reno S. Nooblath et al.
"""

import os
import sys

def filter_fasta_scaffolds(input_file, max_scaffolds=200):
    """
    Filtra arquivos FASTA garantindo o limite máximo de 200 scaffolds 
    estabelecido para maior confiabilidade analítica nas linhagens analisadas.
    """
    print(f"[INFO] Processando arquivo genômico: {input_file}")
    scaffold_count = 0
    
    if not os.path.exists(input_file):
        print(f"[ERROR] Arquivo {input_file} não encontrado.")
        return False

    with open(input_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                scaffold_count += 1

    print(f"[INFO] Total de scaffolds detectados: {scaffold_count}")
    
    if scaffold_count <= max_scaffolds:
        print("[CHECK] Dentro do limite recomendado (<= 200 scaffolds).")
        return True
    else:
        print("[WARNING] Acima do limite de scaffolds. Recomenda-se filtragem adicional.")
        return False

if __name__ == "__main__":
    print("--- Utilitário de Limpeza Genômica ---")
    if len(sys.argv) > 1:
        filter_fasta_scaffolds(sys.argv[1])
    else:
        print("Uso: python3 seq_cleaner.py <arquivo_fasta>")
