from fabric.api import env

os_username = 'admin'
os_password = 'contrail123'
os_tenant_name = 'demo'

host1 = 'root@10.204.217.6'
host2 = 'root@10.204.217.4'
host3 = 'root@10.204.217.5'
host4 = 'root@10.204.216.31'
host5 = 'root@10.204.217.128'
host6 = 'root@10.204.217.130'


ext_routers = [('blr-mx2', '192.168.10.254')]
router_asn = 64512
public_vn_rtgt = 33333
public_vn_subnet = '10.204.219.48/29'

host_build = 'stack@10.204.216.49'

env.roledefs = {
    'all': [host1, host2, host3, host4, host5, host6],
    'cfgm': [host1, host2, host3],
    'openstack': [host1, host2, host3],
    'webui': [host3],
    'control': [host1, host3],
    'compute': [host4, host5, host6],
    'collector': [host1, host2, host3],
    'database': [host1, host2, host3],
    'build': [host_build],
}

env.hostnames = {
    'all': ['nodec21', 'nodec19', 'nodec20', 'nodea35', 'nodei16', 'nodei18']
}

bond= {
    host4 : { 'name': 'bond0', 'member': ['p2p0p0','p2p0p1','p2p0p2','p2p0p3'],'mode':'802.3ad' },
    host5 : { 'name': 'bond0', 'member': ['p2p0p0','p2p0p1','p2p0p2','p2p0p3'],'mode':'802.3ad' },
    host6 : { 'name': 'bond0', 'member': ['p2p0p0','p2p0p1'],'mode':'balance-xor' },
}

#control = {
#    host1 : { 'ip': '192.168.30.1/24', 'gw' : '192.168.30.254', 'device':'eth1' },
#    host2 : { 'ip': '192.168.30.2/24', 'gw' : '192.168.30.254', 'device':'eth1' },
#    host3 : { 'ip': '192.168.30.3/24', 'gw' : '192.168.30.254', 'device':'eth1' },
#    host4 : { 'ip': '192.168.30.4/24', 'gw' : '192.168.30.254', 'device':'p1p0p1' },
#    host5 : { 'ip': '192.168.30.5/24', 'gw' : '192.168.30.254', 'device':'p1p0p1' },
#    host6 : { 'ip': '192.168.30.6/24', 'gw' : '192.168.30.254', 'device':'p1p0p1' },
#}

control_data= {

    host1 : { 'ip': '192.168.10.4/24', 'gw' : '192.168.10.254', 'device':'eth1' },
    host2 : { 'ip': '192.168.10.5/24', 'gw' : '192.168.10.254', 'device':'eth1' },
    host3 : { 'ip': '192.168.10.6/24', 'gw' : '192.168.10.254', 'device':'eth1' },
    host4 : { 'ip': '192.168.10.1/24', 'gw' : '192.168.10.254', 'device':'bond0' },
    host5 : { 'ip': '192.168.10.2/24', 'gw' : '192.168.10.254', 'device':'bond0' },
    host6 : { 'ip': '192.168.10.3/24', 'gw' : '192.168.10.254', 'device':'bond0' },
}

env.passwords = {
    host1: 'c0ntrail123',
    host2: 'c0ntrail123',
    host3: 'c0ntrail123',
    host4: 'c0ntrail123',
    host5: 'c0ntrail123',
    host6: 'c0ntrail123',

    host_build: 'stack@123',
}

env.physical_routers={
'blr-mx2'     : {       'vendor': 'juniper',
                     'model' : 'mx',
                     'asn'   : '64512',
                     'name'  : 'blr-mx2',
                     'ssh_username' : 'root',
                     'ssh_password' : 'c0ntrail123',
                     'mgmt_ip'  : '10.204.216.245',
             }
}

env.ha = {
    'internal_vip' : '192.168.10.7'
}
ha_setup = True

env.cluster_id=i'clusterc19c20c21a35i16i18'
minimum_diskGB=32
env.rsyslog_params = {'port':19876, 'proto':'udp', 'collector':'dynamic', 'status':'enable'}
env.test_repo_dir='/home/stack/centos_multi_node_github_sanity/contrail-test'
env.mail_from='contrail-build@juniper.net'
env.mail_to='dl-contrail-sw@juniper.net'
multi_tenancy=True
env.interface_rename = True 
env.encap_priority =  "'VXLAN, 'MPLSoUDP','MPLSoGRE'"
env.log_scenario = 'Multi-Interface HA Sanity[mgmt, ctrl=data]'
