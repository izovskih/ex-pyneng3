# -*- coding: utf-8 -*-
'''
Задание 6.1

Аналогично заданию 3.1 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

colLeft = ['Protocol:','Prefix:','AD/Metric:','Next-Hop:','Last update:','Outbound Interface:']
with open('ospf.txt', 'r') as f:
    for line in f:
        print('\n')
        colRight = line.replace('O','OSPF').replace('via','').split()
        for i in range(len(colRight)):
            print('{:25}{:25}'.format(colLeft[i], colRight[i].strip('[],')))
