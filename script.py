per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада: "))
deposit = [round(money * (percent / 100)) for percent in per_cent.values()]
max_deposit = max(deposit)
print(f"Максимальная сумма, которую вы можете заработать: {max_deposit}")
