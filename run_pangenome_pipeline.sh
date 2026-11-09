#!/bin/bash
# ==============================================================================
# Pipeline Automatizado de Análise Pan-Genômica
# Espécies: Cylindrospermopsis (Americas / Non-Americas) e Sphaerospermopsis (Global)
# Baseado em: Get_Homologues (Contreras-Moreira & Vinuesa, 2013)
# ==============================================================================

# Definir diretórios de entrada e saída
INPUT_DIR="./01_input_genomes"
OUTPUT_DIR="./04_results_statistics"

echo "[INFO] Iniciando o pipeline pan-genômico para cianobactérias (Americas, Non-Americas, Sphaerospermopsis Global)..."

# 1. Execução do algoritmo Best Database Hits (BDBH)
echo "[RUNNING] Executando BDBH..."
get_homologues.pl -d "$INPUT_DIR" -e 1e-05 -c 75 -t 0 -D

# 2. Execução do algoritmo Markov Cluster (OMCL)
echo "[RUNNING] Executando OMCL..."
get_homologues.pl -d "$INPUT_DIR" -e 1e-05 -c 75 -t 0 -M

# 3. Execução do algoritmo Low-Polynomial (COGtriangles)
echo "[RUNNING] Executando COGtriangles..."
get_homologues.pl -d "$INPUT_DIR" -e 1e-05 -c 75 -t 0 -G

# 4. Comparação e cruzamento de matrizes (Core vs Acessório)
echo "[RUNNING] Gerando matrizes de comparação de clusters..."
compare_clusters.pl -t 0 -m -n

echo "[SUCCESS] Processamento concluído com sucesso!"
