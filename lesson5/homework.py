# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import collections

quantity = int(input('Количество предприятий: '))
defdict = collections.defaultdict(list)
for i in range(quantity):
    defdict['name_' + str(i)].append(input('Название предприятия: '))
    for j in range(4):
        defdict['kv_' + str(i)].append(int(input(f'Квартал {j+1}: ')))

total_ev = int()
for i in range(quantity):
    total_ev += sum(defdict['kv_' + str(i)])
    pass
total_ev = total_ev / quantity
for i in range(quantity):
    if sum(defdict['kv_' + str(i)]) > total_ev:
        name = defdict['name_' + str(i)][0]
        print(f'У предприятия {name} прибыль выше среднего')
    elif sum(defdict['kv_' + str(i)]) < total_ev:
        name = defdict['name_' + str(i)][0]
        print(f'У предприятия {name} прибыль ниже среднего')
