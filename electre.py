import numpy as np

matrix = np.array([
    [0.8, 0.9, 0.6, 0.9, 0.9],
    [0.85, 0.8, 0.6, 0.75, 0.9],
    [0.9, 0.6, 0.75, 0.9, 0.9],
    [0.7, 0.8, 0.9, 0.8, 0.7]
])

weights = [0.15, 0.3, 0.15, 0.2, 0.2]
alternatives = ['T', 'Alfa', 'VTB', 'Ozon']
criteria = ['Качество услуг', 'Тех.поддержка', 'Доступность', 'Интерфейс', 'Производительность']

def electre(matrix, weights):
    results = []
    for i in range(len(matrix)):
        result = []
        for j in range(len(weights)):
            electreRes = matrix[i][j] * weights[j]
            result.append(electreRes)
        results.append(sum(result))
    return results

# Получение результатов
scores = electre(matrix, weights)

# Вывод результатов
results = list(zip(alternatives, scores))
sorted_results = sorted(results, key=lambda x: x[1], reverse=True)

print("\nРезультаты ELECTRE анализа:")
print("Банк\t\tОценка")
print("-" * 25)
for bank, score in sorted_results:
    print(f"{bank}\t\t{score:.4f}")

# Определение лучшего варианта
best_alternative = sorted_results[0]
print(f"\nЛучший вариант: {best_alternative[0]} с оценкой {best_alternative[1]:.4f}")




