import matplotlib.pyplot as plt

def true_positive_rate(vp, fn):
    """
    Calcula a taxa de verdadeiros positivos (TPR) do modelo de classificação.
    """
    return vp / (vp + fn)

def false_positive_rate(fp, vn):
    """
    Calcula a taxa de falsos positivos (FPR) do modelo de classificação.
    """
    return fp / (fp + vn)

# Definir uma lista de diferentes valores de VP, VN, FP e FN
# Aqui, estou usando uma lista para simular diferentes pontos de corte
# Nos valores reais, você usaria os resultados do seu modelo para diferentes pontos de corte
vp_list = [100, 95, 90, 85, 80, 75, 70, 65, 60, 55, 50]
vn_list = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
fp_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
fn_list = [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5]

# Calcular as taxas de verdadeiros positivos (TPR) e taxas de falsos positivos (FPR) para cada ponto de corte
tpr_list = [true_positive_rate(vp, fn) for vp, fn in zip(vp_list, fn_list)]
fpr_list = [false_positive_rate(fp, vn) for fp, vn in zip(fp_list, vn_list)]

# Plotar a curva ROC
plt.plot(fpr_list, tpr_list, marker='o')
plt.title('Curva ROC')
plt.xlabel('Taxa de Falsos Positivos (FPR)')
plt.ylabel('Taxa de Verdadeiros Positivos (TPR)')
plt.grid(True)
plt.show()
