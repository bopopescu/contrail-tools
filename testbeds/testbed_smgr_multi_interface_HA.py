from fabric.api import env

os_username = 'admin'
os_tenant_name = 'demo'
 
host1 = 'root@10.204.217.129'
host2 = 'root@10.204.217.131'
host3 = 'root@10.204.217.13'
host4 = 'root@10.204.217.77'
host5 = 'root@10.204.217.176'
host6 = 'root@10.204.217.132'
host7 = 'root@10.204.217.168'

ext_routers = [('blr-mx2','192.168.100.100')]
router_asn = 64512
public_vn_rtgt = 8168
public_vn_subnet = '10.204.219.168/29'
database_dir = '/home/cassandra'

 
#Host from which the fab commands are triggered to install and provision
host_build = 'stack@10.204.216.49'
 
env.roledefs = {

    'all': [host1, host2, host3, host4, host5, host6, host7],
    'contrail-controller': [host3, host5, host7],
    'openstack': [host2],
    'contrail-compute': [host1, host6],
    'contrail-analytics': [host3, host5, host7],
    'contrail-analyticsdb': [host3, host5, host7],
    'contrail-lb': [host4],
    'build': [host_build],
}
 
env.hostnames ={
    'all': ['nodei17', 'nodei19', 'nodec28', 'nodeg37', 'nodec10', 'nodei20', 'nodec33']
}

env.physical_routers={
'blr-mx2'     : {    'vendor': 'juniper',
                     'model' : 'mx',
                     'asn'   : '64512',
                     'name'  : 'blr-mx2',
                     'ssh_username' : 'root',
                     'ssh_password' : 'c0ntrail123',
                     'mgmt_ip'  : '10.204.216.245',
             }
}

#Openstack admin password
env.openstack_admin_password = 'contrail123'

env.password = 'c0ntrail123'

env.passwords = {
    host1: 'c0ntrail123',
    host2: 'c0ntrail123',
    host3: 'c0ntrail123',
    host4: 'c0ntrail123',
    host5: 'c0ntrail123',
    host6: 'c0ntrail123',
    host7: 'c0ntrail123',
    host_build: 'stack@123',
}

env.ostypes = {
    host1:'ubuntu',
    host2:'ubuntu',
    host3:'ubuntu',
    host4:'ubuntu',
    host5:'ubuntu',
    host6:'ubuntu',
    host7:'ubuntu',
}

bond= {
    host6 : { 'name': 'bond0', 'member': ['eth1','eth2','eth3'],'mode':'802.3ad' },
}

control_data = {
    host1 : { 'ip': '192.168.100.14/24', 'gw' : '', 'device':'eth1' },
    host2 : { 'ip': '192.168.100.15/24', 'gw' : '', 'device':'eth1' },
    host3 : { 'ip': '192.168.100.11/24', 'gw' : '', 'device':'eth1' },
    host4 : { 'ip': '192.168.100.12/24', 'gw' : '', 'device':'eth1' },
    host5 : { 'ip': '192.168.100.13/24', 'gw' : '', 'device':'eth1' },
    host6 : { 'ip': '192.168.100.16/24', 'gw' : '', 'device':'bond0' },
    host7 : { 'ip': '192.168.100.17/24', 'gw' : '', 'device':'p1p2' },
}

# VIP
env.ha = {
    'contrail_internal_vip' : '192.168.100.12',
    'contrail_external_vip' : '10.204.217.77',
}

#To enable multi-tenancy feature
enable_ceilometer = True
ceilometer_polling_interval = 60
env.enable_lbaas = True
ha_setup = True
multi_tenancy = True
env.encap_priority =  "'VXLAN','MPLSoUDP','MPLSoGRE'"
do_parallel = True
env.test_repo_dir='/home/stack/smgr_github_ubuntu_multi_node/contrail-test'
env.mail_from='contrail-build@juniper.net'
env.mail_to='dl-contrail-sw@juniper.net'
env.xmpp_auth_enable=True
env.xmpp_dns_auth_enable=True
env.log_scenario='SMLite Contrail Networking HA Sanity'
