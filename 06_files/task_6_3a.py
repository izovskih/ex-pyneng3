# -*- coding: utf-8 -*-
'''
Задание 6.3a

Сделать копию скрипта задания 6.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

lsStrs = []
with open('CAM_table.txt') as f:
    for i, line in enumerate(f):
        if '0.7000' in line:
            lsStrs.append(line.strip().replace('DYNAMIC','').split())
        else:
            continue
    lsStrs = sorted(lsStrs)
    for i in range(len(lsStrs)):
        print('{:5}{:16}{:5}'.format(*lsStrs[i]))
