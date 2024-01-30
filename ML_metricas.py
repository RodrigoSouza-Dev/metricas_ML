def acuracia(vp, vn, fp, fn):
    return (vp + vn) / (vp + vn + fp + fn)


def sensibilidade(vp, fn):
    return vp / (vp + fn)


def especificidade(vn, fp):
    return vn / (vn + fp)


def precisao(vp, fp):
    return vp / (vp + fp)


def f1_score(precisao, sensibilidade):
    return 2 * (precisao * sensibilidade) / (precisao + sensibilidade)


# Matriz de Confusão
vp = 20
vn = 50
fp = 5
fn = 3

# Cálculando as métricas...
acuracia_modelo = acuracia(vp, vn, fp, fn)
sensibilidade_modelo = sensibilidade(vp, fn)
especificidade_modelo = especificidade(vn, fp)
precisao_modelo = precisao(vp, fp)
f1_score_modelo = f1_score(precisao_modelo, sensibilidade_modelo)

# Resultados
print("Acurácia do modelo:", acuracia_modelo)
print("Sensibilidade do modelo:", sensibilidade_modelo)
print("Especificidade do modelo:", especificidade_modelo)
print("Precisão do modelo:", precisao_modelo)
print("F1-score do modelo:", f1_score_modelo)
