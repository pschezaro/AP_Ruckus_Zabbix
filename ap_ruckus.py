#!/usr/bin/env python
# -*- coding: utf-8 -*-

#author: Janssen dos Reis Lima - http://blog.conectsys.com.br

from zabbix_api import ZabbixAPI
import csv

zapi = ZabbixAPI(server="http://127.0.0.1/zabbix")
zapi.login("Admin", "!@nhaca123")

f = csv.reader(open('/tmp/hosts.csv'), delimiter=';')
for [ip,macro,hostname] in f:
    print ("Cadastrando host da linha ", f.line_num)
    hostcriado = zapi.host.create({
        "host": hostname,
        "status": 0,
        "interfaces": [
            {
                "type": 2,
                "main": 1,
                "useip": 1,
                "ip": ip,
                "dns": "",
                "port":161 ,
                    "details": {
                    "version": 2,
                    "community": "{$SNMP_COMMUNITY}"
                }
            }
        ],
        "groups": [
            {
                "groupid": 148
            }
        ],
        "templates": [
            {
                "templateid": 10334
            }
        ],
        "macros": [
            {
                "macro": "{$RUCKUS_OID}",
                "value": macro
            },
            {
                "macro": "{$SNMP_COMMUNITY}",
                "value": "l1nkt3l"
            }
        ]
    })