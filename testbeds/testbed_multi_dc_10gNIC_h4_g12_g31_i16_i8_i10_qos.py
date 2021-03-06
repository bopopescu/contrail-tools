from fabric.api import env

#Management ip addresses of hosts in the cluster
host1 = 'root@10.204.217.108'
host2 = 'root@10.204.217.128'
host3 = 'root@10.204.217.52'
host4 = 'root@10.204.217.130'
host5 = 'root@10.204.217.71'
host6 = 'root@10.204.217.122'

#External routers if any
#for eg. 
#ext_routers = [('mx1', '10.204.216.253')]
ext_routers = []

#Autonomous system number
router_asn = 64512

#Host from which the fab commands are triggered to install and provision
host_build = 'stack@10.204.216.49'
env.roledefs = {
    #'all': [host1, host2, host3, host4, host6],
    'all': [host1, host2, host3, host4, host5, host6],
    'cfgm': [host1, host3, host5],
    'openstack': [host1],
    'webui': [host3],
    'control': [host1, host3, host5],
    'compute': [host2, host4, host6],
    'collector': [host1, host3, host5],
    'database': [host1, host3, host5], 
    'build': [host_build],
}
'''
env.roledefs = {
    #'all': [host1, host2, host3, host4, host6],
    'all': [host1, host2, host3, host4, host5, host6],
    'cfgm': [host1, host2, host3, host5],
    'openstack': [host1],
    'webui': [host3],
    'control': [host1, host2, host3, host5],
    'compute': [host4, host6],
    'collector': [host1, host3, host5],
    'database': [host3],
    'build': [host_build],
}
'''
#Openstack admin password
env.openstack_admin_password = 'contrail123'

#Hostnames
env.hostnames = {
   # 'all': ['nodeh4', 'nodeh8', 'nodeg12', 'nodeg31', 'nodec28']
     'all': ['nodeh4', 'nodei16', 'nodeg12', 'nodei18', 'nodeg31', 'nodei10']
}

# Passwords of each host
# for passwordless login's no need to set env.passwords,
# instead populate env.key_filename in testbed.py with public key.
env.password = 'c0ntrail123'
env.passwords = {
    host1: 'c0ntrail123',
    host2: 'c0ntrail123',
    host3: 'c0ntrail123',
    host4: 'c0ntrail123',
    host5: 'c0ntrail123',
    host6: 'c0ntrail123',

    host_build: 'stack@123',
}

# SSH Public key file path for passwordless logins
# if env.passwords is not specified.
#env.key_filename = '/root/.ssh/id_rsa.pub'

#For reimage purpose
env.ostypes = {
    host1:'ubuntu',
    host2:'ubuntu',
    host3:'ubuntu',
    host4:'ubuntu',
    host5:'ubuntu',
    host6:'ubuntu',
}

#ntp server the servers should point to
#env.ntp_server = 'ntp.juniper.net'

# OPTIONAL COMPUTE HYPERVISOR CHOICE:
#======================================
# Compute Hypervisor
#env.hypervisor = {
#    host1: 'docker',
#}
#  Specify the hypervisor to be provisioned in the compute node.(Default=libvirt)

# INFORMATION FOR DB BACKUP/RESTORE ..
#=======================================================
#Optional,Backup Host configuration if it is not available then it will put in localhost
#backup_node = 'root@2.2.2.2'

# Optional, Local/Remote location of backup_data path 
# if it is not passed it will use default path 
#backup_db_path= ['/home/','/root/']
#cassandra backup can be defined either "full" or "custom"  
#full -> take complete snapshot of cassandra DB 
#custom -> take snapshot except defined in skip_keyspace 
#cassandra_backup='custom'  [ MUST OPTION] 
#skip_keyspace=["ContrailAnalytics"]  IF cassandra_backup is selected as custom
#service token need to define to do  restore of  backup data
#service_token = '53468cf7552bbdc3b94f'

#OPTIONAL ANALYTICS CONFIGURATION
#================================
# database_dir is the directory where cassandra data is stored
#
# If it is not passed, we will use cassandra's default
# /var/lib/cassandra/data
#
#database_dir = '<separate-partition>/cassandra'
#
# analytics_data_dir is the directory where cassandra data for analytics
# is stored. This is used to seperate cassandra's main data storage [internal
# use and config data] with analytics data. That way critical cassandra's 
# system data and config data are not overrun by analytis data
#
# If it is not passed, we will use cassandra's default
# /var/lib/cassandra/data
#
#analytics_data_dir = '<separate-partition>/analytics_data'
#
# ssd_data_dir is the directory where cassandra can store fast retrievable
# temporary files (commit_logs). Giving cassandra an ssd disk for this
# purpose improves cassandra performance
#
# If it is not passed, we will use cassandra's default
# /var/lib/cassandra/commit_logs
#
#ssd_data_dir = '<seperate-partition>/commit_logs_data'

#following variables allow analytics data to have different TTL in cassandra database
#analytics_config_audit_ttl controls TTL for config audit logs
#analytics_statistics_ttl controls TTL for stats
#analytics_flow_ttl controls TTL for flow data
#database_ttl controls TTL for rest of the data
#
#database_ttl = 48
#analytics_config_audit_ttl = 48
#analytics_statistics_ttl = 48
#analytics_flow_ttl = 48

#following parameter allows to specify minimum amount of disk space in the analytics
#database partition, if configured amount of space is not present, it will fail provisioning
minimum_diskGB = 32

#OPTIONAL BONDING CONFIGURATION
#==============================
#Inferface Bonding
#bond= {
#    host1 : { 'name': 'bond0', 'member': ['p2p0p0','p2p0p1','p2p0p2','p2p0p3'], 'mode': '802.3ad', 'xmit_hash_policy': 'layer3+4' },
#}

#OPTIONAL SEPARATION OF MANAGEMENT AND CONTROL + DATA and OPTIONAL VLAN INFORMATION
#==================================================================================
control_data = {
    host1 : { 'ip': '77.77.1.10/24', 'gw' : '77.77.1.254', 'device': 'p2p2' },
    host2 : { 'ip': '77.77.1.11/24', 'gw' : '77.77.1.254', 'device': 'p6p2' },
    host3 : { 'ip': '77.77.2.10/24', 'gw' : '77.77.2.254', 'device': 'p1p2' },
    host4 : { 'ip': '77.77.2.11/24', 'gw' : '77.77.2.254', 'device': 'p6p2' },
    host5 : { 'ip': '77.77.3.10/24', 'gw' : '77.77.3.254', 'device': 'p1p2' },
    host6 : { 'ip': '77.77.3.11/24', 'gw' : '77.77.3.254', 'device': 'p6p2' },
}

static_route  = {
    host1 : [{ 'ip': '77.77.2.0', 'netmask' : '255.255.255.0', 'gw':'77.77.1.254', 'intf': 'p2p2' },
             { 'ip': '77.77.3.0', 'netmask' : '255.255.255.0', 'gw':'77.77.1.254', 'intf': 'p2p2' }],
    host2 : [{ 'ip': '77.77.2.0', 'netmask' : '255.255.255.0', 'gw':'77.77.1.254', 'intf': 'p6p2' },
             { 'ip': '77.77.3.0', 'netmask' : '255.255.255.0', 'gw':'77.77.1.254', 'intf': 'p6p2' }],
    host3 : [{ 'ip': '77.77.1.0', 'netmask' : '255.255.255.0', 'gw':'77.77.2.254', 'intf': 'p1p2' },
             { 'ip': '77.77.3.0', 'netmask' : '255.255.255.0', 'gw':'77.77.2.254', 'intf': 'p1p2' }],
    host4 : [{ 'ip': '77.77.1.0', 'netmask' : '255.255.255.0', 'gw':'77.77.2.254', 'intf': 'p6p2' },
             { 'ip': '77.77.3.0', 'netmask' : '255.255.255.0', 'gw':'77.77.2.254', 'intf': 'p6p2' }],
    host5 : [{ 'ip': '77.77.1.0', 'netmask' : '255.255.255.0', 'gw':'77.77.3.254', 'intf': 'p1p2' },
             { 'ip': '77.77.2.0', 'netmask' : '255.255.255.0', 'gw':'77.77.3.254', 'intf': 'p1p2' }],
    host6 : [{ 'ip': '77.77.1.0', 'netmask' : '255.255.255.0', 'gw':'77.77.3.254', 'intf': 'p6p2' },
             { 'ip': '77.77.2.0', 'netmask' : '255.255.255.0', 'gw':'77.77.3.254', 'intf': 'p6p2' }]
}

#OPTIONAL STATIC ROUTE CONFIGURATION
#===================================
#static_route  = {
#    host1 : [{ 'ip': '10.1.1.0', 'netmask' : '255.255.255.0', 'gw':'192.168.10.254', 'intf': 'bond0' },
#             { 'ip': '10.1.2.0', 'netmask' : '255.255.255.0', 'gw':'192.168.10.254', 'intf': 'bond0' }],
#}

#storage compute disk config
#storage_node_config = {
#    host1 : { 'disks' : ['sdc', 'sdd'] },
#}

#live migration config
#live_migration = True


#To disable installing contrail interface rename package
env.interface_rename = True

#In environments where keystone is deployed outside of Contrail provisioning
#scripts , you can use the below options 
#
# Note : 
# "insecure" is applicable only when protocol is https
# The entries in env.keystone overrides the below options which used 
# to be supported earlier :
#  service_token
#  keystone_ip
#  keystone_admin_user
#  keystone_admin_password
#  region_name
#
#env.keystone = {
#    'keystone_ip'   : 'x.y.z.a',
#    'auth_protocol' : 'http',                  #Default is http
#    'auth_port'     : '35357',                 #Default is 35357
#    'admin_token'   : '33c57636fbc2c5552fd2',  #admin_token in keystone.conf
#    'admin_user'    : 'admin',                 #Default is admin
#    'admin_password': 'contrail123',           #Default is contrail123
#    'service_tenant': 'service',               #Default is service
#    'admin_tenant'  : 'admin',                 #Default is admin
#    'region_name'   : 'RegionOne',             #Default is RegionOne
#    'insecure'      : 'True',                  #Default = False
#    'manage_neutron': 'no',                    #Default = 'yes' , Does configure neutron user/role in keystone required.
#}
#

#env.nova = {
#    'cpu_mode': 'host-passthrough', # Possible options: none, host-passthrough, host-model, and custom
#                                    # if cpu_mode is 'custom' specify cpu_model option too
#    'cpu_model': 'Nehalem',         # relevant only if cpu_mode is 'custom'
#}

# In High Availability setups.
#env.ha = {
#    'internal_vip'   : '1.1.1.1',               #Internal Virtual IP of the HA setup.
#    'external_vip'   : '2.2.2.2',               #External Virtual IP of the HA setup.
#    'nfs_server'      : '3.3.3.3',               #IP address of the NFS Server which will be mounted to /var/lib/glance/images of openstack Node, Defaults to env.roledefs['compute'][0]
#    'nfs_glance_path' : '/var/tmp/images/',      #NFS Server path to save images, Defaults to /var/tmp/glance-images/
#}

# In environments where openstack services are deployed independently 
# from contrail, you can use the below options 
# service_token : Common service token for for all services like nova,
#                 neutron, glance, cinder etc
# amqp_host     : IP of AMQP Server to be used in openstack
# manage_amqp   : Default = 'no', if set to 'yes' provision's amqp in openstack nodes and
#                 openstack services uses the amqp in openstack nodes instead of config nodes.
#                 amqp_host is neglected if manage_amqp is set
#
#env.openstack = {
#    'service_token' : '33c57636fbc2c5552fd2', #Common service token for for all openstack services
#    'amqp_host' : '10.204.217.19',            #IP of AMQP Server to be used in openstack
#    'manage_amqp' : 'yes',                    #Default no, Manage seperate AMQP for openstack services in openstack nodes.
#    'osapi_compute_workers' : 40,             #Default 40, For low memory system reduce the osapi compute workers thread.
#    'conductor_workers' : 40,                 #Default 40, For low memory system reduce the conductor workers thread.
#}

# Neutron specific configuration 
#env.neutron = {
#   'protocol': 'http', # Default is http
#}

#To enable multi-tenancy feature
multi_tenancy = True

#To enable haproxy feature
#haproxy = True

#To Enable prallel execution of task in multiple nodes
do_parallel = True

# To configure the encapsulation priority. Default: MPLSoGRE 
env.encap_priority =  "'VXLAN','MPLSoUDP','MPLSoGRE'"

# Optional proxy settings.
# env.http_proxy = os.environ.get('http_proxy')

#To enable LBaaS feature
# Default Value: False
env.enable_lbaas = True

#OPTIONAL REMOTE SYSLOG CONFIGURATION
#===================================
#For R1.10 this needs to be specified to enable rsyslog.
#For Later releases this would be enabled as part of provisioning,
#with following default values.
#
#port = 19876
#protocol = tcp
#collector = dynamic i.e. rsyslog clients will connect to servers in a round
#                         robin fasion. For static collector all clients will
#                         connect to a single collector. static - is a test
#                         only option.
#status = enable
#
#env.rsyslog_params = {'port':19876, 'proto':'tcp', 'collector':'dynamic', 'status':'enable'}

#OPTIONAL Virtual gateway CONFIGURATION
#=======================================

#Section vgw is only relevant when you want to use virtual gateway feature. 
#You can use one of your compute node as  gateway .

#Definition for the Key used
#-------------------------------------
#vn: Virtual Network fully qualified name. This particular VN will be used by VGW.
#ipam-subnets: Subnets used by vn. It can be single or multiple
#gateway-routes: If any route is present then only those routes will be published
#by VGW or Default route (0.0.0.0) will be published

#env.vgw = {host1: {'vgw1':{'vn':'default-domain:admin:public:public', 'ipam-subnets': ['10.204.220.128/29', '10.204.220.136/29', 'gateway-routes': ['8.8.8.0/24', '1.1.1.0/24']}]},
#                   'vgw2':{'vn':'default-domain:admin:public1:public1', 'ipam-subnets': ['10.204.220.144/29']}
#          }

#OPTIONAL optional tor agent and tsn CONFIGURATION
#==================================================
#Section tor agent is only relevant when you want to use Tor Agent feature.
#You can use one of your compute node as  Tor Agent . Same or diffrent compute
#node should be enable as tsn

#Definition for the Key used
#-------------------------------------
# tor_ip: IP of the tor switch
# tor_id: Unique Id of the tor switch to identify. Typicaly a numeric value.
# tor_ovs_port: Port number to be used by ovs
# tor_ovs_protocol: Connection protocol to be used by ovs. Currently only TCP
# tor_tsn_ip: TSN node ip
#env.tor_agent =
#{host3:[{'tor_ip':'10.204.217.39','tor_id':'1','tor_ovs_port':'9999','tor_ovs_protocol':'tcp','tor_tsn_ip':'10.204.221.35'}]}

# OPTIONAL DPDK CONFIGURATION
# ===========================
# If some compute nodes should use DPDK vRouter version it has to be put in
# env.dpdk dictionary. The format is:
# env.dpdk = {
#     host1: { 'huge_pages' : '50', 'coremask' : '0xf' },
#     host2: { 'huge_pages' : '50', 'coremask' : '0,3-7' },
# }
# huge_pages - Specify what percentage of host memory should be reserved
#              for access with huge pages
# coremask   - Specify CPU affinity mask to run vRouter with. Supported formats:
#              hexadecimal, comma-sepparated list of CPUs, dash-separated range
#              of CPUs.
env.test_repo_dir='/root/contrail-test'
