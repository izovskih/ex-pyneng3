# -*- coding: utf-8 -*-
'''
Задание 4.2b

Переделать скрипт из задания 4.2a таким образом, чтобы, при запросе параметра,
отображался список возможных параметров.

Вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:
$ python task_4_2b.py
Enter device name: r1
Enter parameter name (ios, model, vendor, location, ip): ip
10.255.0.1

Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if.
'''

london_co = {
    'r1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.1'
    },
    'r2' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '4451',
    'ios': '15.4',
    'ip': '10.255.0.2'
    },
    'sw1' : {
    'location': '21 New Globe Walk',
    'vendor': 'Cisco',
    'model': '3850',
    'ios': '3.6.XE',
    'ip': '10.255.0.101',
    'vlans': '10,20,30',
    'routing': True
    }
}

userInput_dn = input('Enter device name: ')
userInput_pn = input('Enter parameter name ('+','.join(london_co[userInput_dn].keys())+'):')
print(london_co[userInput_dn][userInput_pn])
