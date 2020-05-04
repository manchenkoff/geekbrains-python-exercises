"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом
работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).

Если фирма отработала с прибылью, вычислите рентабельность продаж (соотношение прибыли к выручке)
и запросите численность сотрудников фирмы, определите прибыль фирмы в расчете на одного сотрудника.

Вывести результаты в формате:

>> прибыль
>> рентабельность X
>> прибыль на сотрудника Y

или

>> убыток


где,
X - значение рентабельности, округленное до 2-х знаков после запятой
Y - значение прибыли на сотрудника (без округления)
"""

revenue = int(input())
costs = int(input())
headcount = int(input())

profit = revenue - costs
is_profitable = profit > 0

profitable_state = "прибыль" if is_profitable else "убыток"
print(profitable_state)

if not is_profitable:
    exit()

profitability = round(profit / revenue, 2)
profit_per_head = profit / headcount if headcount > 0 else profit

print(f"рентабельность {profitability}")
print(f"прибыль на человека {profit_per_head}")
