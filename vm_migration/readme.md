
## VM Migration

### For commercial cloud
- including EC2, Azure, GAE; None of them support vm live migration. 
- Google cloud does support vm live migration, which however is transparent to users and cannot be controlled by users. 
- For amazon cloud, cold migration may be doable by stopping a virtual machine and restarting it again so that it might be assigned to a new host, or might not.

### For research cloud
- vm migration is not supported yet in [[chameleoncloud]](https://github.com/hxwang/chameleoncloud)


### Alternatives
- [[VM migration in OpenStack]](https://github.com/hxwang/openstack)
- [VM migration in VMware vSphere](https://github.com/hxwang/vmware)
