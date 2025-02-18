import numpy as np

# Исходные данные
alternatives = ['T', 'Alfa', 'VTB', 'Ozon']
criteria = ['Качество услуг', 'Тех.поддержка', 'Доступность', 'Интерфейс', 'Производительность']
weights = [0.15, 0.3, 0.15, 0.2, 0.2]  # веса критериев

# Матрица решений
decision_matrix = np.array([
    [0.8, 0.9, 0.6, 0.9, 0.9],
    [0.85, 0.8, 0.6, 0.75, 0.9],
    [0.9, 0.6, 0.75, 0.9, 0.9],
    [0.7, 0.8, 0.9, 0.8, 0.7]
])

def topsis(matrix, weights):
    # Нормализация матрицы
    normalized = matrix / np.sqrt(np.sum(matrix**2, axis=0))
    
    # Взвешенная нормализованная матрица
    weighted_normalized = normalized * weights
    
    # Определение идеального и анти-идеального решения
    ideal_best = np.max(weighted_normalized, axis=0)
    ideal_worst = np.min(weighted_normalized, axis=0)
    
    # Расчет расстояний до идеального и анти-идеального решения
    s_best = np.sqrt(np.sum((weighted_normalized - ideal_best)**2, axis=1))
    s_worst = np.sqrt(np.sum((weighted_normalized - ideal_worst)**2, axis=1))
    
    # Расчет относительной близости к идеальному решению
    performance_score = s_worst / (s_best + s_worst)
    
    return performance_score

# Получение результатов
scores = topsis(decision_matrix, weights)

# Вывод результатов
results = list(zip(alternatives, scores))
sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

print("\nРезультаты TOPSIS анализа:")
print("Банк\t\tОценка")
print("-" * 25)
for bank, score in sorted_results:
    print(f"{bank}\t\t{score:.4f}")

# Определение лучшего варианта
best_alternative = sorted_results[0]
print(f"\nЛучший вариант: {best_alternative[0]} с оценкой {best_alternative[1]:.4f}")
