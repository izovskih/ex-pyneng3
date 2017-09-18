# -*- coding: utf-8 -*-
'''
Задание 6.3b

Сделать копию скрипта задания 6.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

lsStrs = []
vlanPrnt = input('Please, Enter a vlan which you want see: ')

with open('CAM_table.txt') as f:
    for i, line in enumerate(f):
        if '0.7000' in line:
            lsStrs.append(line.strip().replace('DYNAMIC','').split())
        else:
            continue
    for i,ls in enumerate(lsStrs):
        if vlanPrnt in ls:
            print('{:5}{:16}{:5}'.format(*lsStrs[i]))
        else:
            continue