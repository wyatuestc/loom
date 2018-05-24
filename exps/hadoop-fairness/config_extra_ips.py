#!/usr/bin/python

import socket
import platform
import subprocess
import shlex

IFACE = 'eno2'

# Helpers
def aton(ip):
    return socket.inet_aton(ip)
# CloudLab experiment platform specific code:
def node2id(node):
    node2id_dict = {
        'pinter': 1,
        'jarry': 2,
        'node-1.loomtest2.opennf-pg0.clemson.cloudlab.us': 1,
        'node-0.loomtest2.opennf-pg0.clemson.cloudlab.us': 2,
    }
    return node2id_dict[node]
node_name = platform.node()
node_id = node2id(node_name)

ips = ['10.10.10%d.%d' % (i, node_id) for i in range(1, 3)]
for ip in ips:
    cmd_keys = {'ip': ip, 'iface': IFACE}
    cmd = 'sudo ip addr add {ip}/24 dev {iface}'.format(**cmd_keys)
    print cmd
    subprocess.check_call(shlex.split(cmd))
