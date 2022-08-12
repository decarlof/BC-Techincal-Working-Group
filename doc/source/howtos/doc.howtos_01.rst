NIC for FLIR 10Ge
=================

Step-by-step to configure a FLIR 10Gb camera with an Intel Network adapter:



1. Prerequisites:

64GB memory
Cat 6A cable
Intel X550T2 ETHERNET CONVERGED Network Adapter X550-T2

2. Enable jumbo packet
3. Disable DHCP and set a fixed IP address on the Ethernet port connecting to the FLIR
4. Increase the receive buffer size5. Increase the Network parameters in the kernel
6. Set the NIC tx queue length



1. is available from Sorcium as Part#: 3E9073
2. 3. and 4. are documented at `here <https://www.flir.com/support-center/iis/machine-vision/knowledge-base/lost-ethernet-data-packets-on-linux-systems/>`_
4. is documented both at `flir doc <https://www.flir.com/support-center/iis/machine-vision/knowledge-base/lost-ethernet-data-packets-on-linux-systems/>`_ 
and in the `areadetector doc <https://areadetector.github.io/master/ADGenICam/ADGenICam.html#linux-usb-and-gige-system-settings>`_
5. edit /etc/sysctl.conf and add:
net.core.rmem_default=26214400net.core.rmem_max=268435456

6. edit /etc/rc.local and add::

    /usr/sbin/ifconfig ens1f1 txqueuelen 3000

#NIC camera settings and  10GB nic settings  In this example the camera is attached to  ens1f1    
