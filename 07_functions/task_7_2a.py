# -*- coding: utf-8 -*-

'''
Задание 7.2a

Сделать копию скрипта задания 7.2

Изменить скрипт таким образом, чтобы функция возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_dict.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

def generate_trunk_config(trunk):
    '''
    trunk - словарь trunk-портов,
    для которых необходимо сгенерировать конфигурацию, вида:
        { 'FastEthernet0/1':[10,20],
          'FastEthernet0/2':[11,30],
          'FastEthernet0/4':[17] }

    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    '''
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
    listOfLists = []
    ints = list(trunk.keys())
    vlans = list(trunk.values())
    for i in range(len(trunk)):
        listCmd = []
        listCmd.append('interface %s' % ints[i])
        for cmd in trunk_template:
            if cmd.endswith('allowed vlan'):
                listCmd.append('%s %s' % (cmd, str(vlans[i]).strip('[]')))
            else:
                listCmd.append(cmd)
        listOfLists.append(listCmd)
    return dict(zip(ints, listOfLists))


trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

resDict = generate_trunk_config(trunk_dict)
print(resDict)
for i in resDict:
    print(resDict[i])
