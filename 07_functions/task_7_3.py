# -*- coding: utf-8 -*-
'''
Задание 7.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(config):
    """
    config - имя конфигурационного файла коммутатора

    Возвращает кортеж словарей:
    - первый словарь: порты в режиме access
      { 'FastEthernet0/12': 10,
        'FastEthernet0/14': 11,
        'FastEthernet0/16': 17  }
    - второй словарь: порты в режиме trunk
      { 'FastEthernet0/1':[10, 20],
        'FastEthernet0/2':[11, 30],
        'FastEthernet0/4':[17] }

    """
    intLs = []
    intLsTrunk = []
    intLsAccess = []
    vlanLsAccess = []
    vlanLsTrunk = []
    with open(config) as f:
        for line in f:
            if line.startswith('interface Fast'):
                intLs.append(line[line.find('Fast'):-1:])
            elif 'access vlan' in line:
                vlanLsAccess += line.split()[-1:]
                intLsAccess.append(intLs.pop(-1))
            elif 'allowed vlan' in line:
                vlanLsTrunk.append(line.split()[-1:])
                intLsTrunk.append(intLs.pop(-1))
    dictAccess = dict(zip(intLsAccess,vlanLsAccess))
    dictTrunk = dict(zip(intLsTrunk,vlanLsTrunk))
    return dictAccess, dictTrunk


print(get_int_vlan_map('config_sw1.txt'))
