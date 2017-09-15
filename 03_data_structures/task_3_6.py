# -*- coding: utf-8 -*-
'''
Задание 3.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

OR_LS_H = ['Protocol:','Prefix:','AD/Metric:','Next-Hop:','Last update:','Outbound Interface:']
OR_LS = ospf_route.replace('O','OSPF').replace('via','').split()

for i in range(len(OR_LS)):
    print('{:25}{:25}'.format(OR_LS_H[i], OR_LS[i].strip('[],')))
