---
RHEL_VERSION: 7.4
RHEL_QCOW: /root/rhel-server-7.4-x86_64-kvm.qcow2 
IMAGE_DIRECTORY: /var/lib/libvirt/images
UNDERCLOUD_IMAGE_SIZE: 100G
UNDERCLOUD_NAME: undercloud 
UNDERCLOUD_ROOT_PWD: c0ntrail123
UNDERCLOUD_STACK_PWD: c0ntrail123
UNDERCLOUD_DEFAULT_NW: br-ex
UNDERCLOUD_MAC: 52:54:00:16:03:6a
UNDERCLOUD_STATIC_IP: 10.87.67.61
UNDERCLOUD_PROV_NW: br-ctrlplane 
UNDERCLOUD_INT_API_NW: br-int-api
UNDERCLOUD_VCPU: 8
UNDERCLOUD_RAM: 32348
UNDERCLOUD_IP: 192.168.24.1
UNDERCLOUD_PREFIX: 192.168.24.0
UNDERCLOUD_PREFIX_LENGTH: 24
UNDERCLOUD_GATEWAY: 192.168.24.1
UNDERCLOUD_DHCP_START: 192.168.24.5
UNDERCLOUD_DHCP_END: 192.168.24.24
UNDERCLOUD_INSPECTION_IP_RANGE: 192.168.24.100,192.168.24.120
RH_REG_METHOD: portal 
RH_PORTAL_USER: shajuvk
RH_PORTAL_PASSWORD: shajuvk123
RH_AUTO_ATTACH: 'no'
SATELLITE_FQDN: 
SATELLITE_IP: 
SATELLITE_KEY: 
SATELLITE_ORG: 
SATELLITE_VERSION: 
RH_POOL_ID: 8a85f9895cce2f3a015ccf0eb79749f8 
OPENSTACK_VERSION: newton
ROOT_SSH_KEY: /root/.ssh/id_rsa.pub
STACK_SSH_KEY: /home/stack/.ssh/id_rsa.pub
CONTRAIL_VERSION: contrail_exact_version
CONTRAIL_VERSION_BUILD: build_id
CONTRAIL_PACKAGE_LOCATION: http://10.84.5.120/cs-build/jenkins-jobs/CB-contrail_version-redhat70-newton/builds/build_id/archive/packages/

BUILD_DPDK_IMAGE: 'yes' 
