#! /bin/sh
ifconfig enp2s0 10.0.0.50 netmask 255.255.255.0
ip addr add 10.0.0.52/24 dev enp2s0
sysctl -w net.ipv4.conf.all.accept_redirects=0
ip route add 20.0.0.0/24 via 10.0.0.5
