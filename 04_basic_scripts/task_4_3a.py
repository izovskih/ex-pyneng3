# -*- coding: utf-8 -*-

'''
Задание 4.3a

Дополнить скрипт из задания 4.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']

dictAT = dict(access=access_template, trunk=trunk_template)
intMode = input('Enter interface mode (access/trunk): ').lower()
intNum = input('Enter interface type and number: ').lower()
dictVlan = dict(access='Enter VLAN number: ', trunk='Enter allowed VLANs: ')
vlans = input(dictVlan[intMode])

print('\ninterface', intNum)
print(('\n'.join(dictAT[intMode])).format(vlans))