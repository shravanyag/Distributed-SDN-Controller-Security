#! /bin/sh
ip addr add 10.0.0.30/24 dev enp2s0
sysctl -w net.ipv4.conf.all.accept_redirects=0
ip route add 20.0.0.0/24 via 10.0.0.5
