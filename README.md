# metricas_ML
Métricas de validação para modelos de Machine Learning.

Existem várias métricas de validação de modelos de machine learning, cada uma com seu propósito específico. Algumas das métricas mais comuns incluem:

# Acurácia: 
Mede a proporção de previsões corretas em relação ao total de previsões feitas pelo modelo. É uma métrica básica e amplamente utilizada, mas pode ser enganosa em conjuntos de dados desbalanceados.

# Precisão: 
Calcula a proporção de verdadeiros positivos em relação à soma de verdadeiros positivos e falsos positivos. É útil quando o foco está na minimização de falsos positivos.

#Sensibilidade (Recall): 
Calcula a proporção de verdadeiros positivos em relação à soma de verdadeiros positivos e falsos negativos. É importante quando o objetivo é identificar o máximo possível de positivos reais, minimizando os falsos negativos.

#Especificidade: 
Calcula a proporção de verdadeiros negativos em relação à soma de verdadeiros negativos e falsos positivos. É útil quando o foco está em minimizar os falsos positivos.

#F1-score: 
É uma média harmônica da precisão e da sensibilidade. É útil quando há um desequilíbrio significativo entre as classes do conjunto de dados.

# Curva ROC e Área sob a curva (ROC-AUC): 
A curva ROC mostra a taxa de verdadeiros positivos em relação à taxa de falsos positivos em vários limiares de classificação. A área sob a curva ROC (ROC-AUC) quantifica a habilidade do modelo de distinguir entre as classes. É útil para avaliar modelos de classificação binária em diferentes limiares de classificação.

Essas métricas são importantes para validar um modelo de machine learning porque fornecem informações sobre diferentes aspectos do desempenho do modelo. Por exemplo:

A acurácia dá uma visão geral da precisão geral do modelo.
A precisão e a sensibilidade ajudam a entender como o modelo está se saindo em cada classe de forma individual.
A especificidade é crucial quando o foco está em evitar falsos positivos.
O F1-score é útil para encontrar um equilíbrio entre precisão e sensibilidade, especialmente em conjuntos de dados desbalanceados.
A curva ROC e a área sob a curva fornecem uma visão mais detalhada do desempenho do modelo em diferentes limiares de classificação.
Em resumo, essas métricas permitem uma avaliação abrangente do desempenho do modelo de machine learning, ajudando os desenvolvedores a entender suas forças e fraquezas e a fazer melhorias conforme necessário.
