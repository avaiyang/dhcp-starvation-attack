# dhcp-starvation-attack
## DHCP   (Dynamic Host configuration Protocol)

It is a TCP/IP network management protocol which is used to dynamically assign IP addresses and other parameter to the devices which are connected on the network. Whenever any device which tries to connect to the network, then the DHCP client software sends a broadcast query in order to request the IP and other other network parameters to assign to that device. The DHCP server maintaining the pool of IP addresses provides such details as configured by the administrator. This information is only valid for a particular time period for which the lease is valid.

In the given assignment, we are performing DHCP starvation attack, which denies IP address and the network parameters requested by the user/ the device which is trying to connect. It is a kind of denial of service attack to the user, so that the person is unable to connect to the network. It does so by exhausting all the IPs in the DHCP server by assigning them to spoofed MAC addresses.

