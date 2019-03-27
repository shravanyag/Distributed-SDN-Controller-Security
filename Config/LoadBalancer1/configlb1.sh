#! /bin/sh
ifconfig enp2s0 10.0.0.5 netmask 255.255.255.0
ifconfig enx00e04c360013 20.0.0.5 netmask 255.255.255.0
ip addr add 10.0.0.10/24 dev enp2s0
ip addr add 20.0.0.10/24 dev enx00e04c360013
sysctl -w net.ipv4.ip_forward=1
sysctl -w net.ipv4.conf.all.send_redirects=0
service haproxy stop
service haproxy start
