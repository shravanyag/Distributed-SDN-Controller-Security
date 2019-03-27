#! /bin/bash

for value in {1..100000}
do
	sudo tcpdump -G 15 -W 1 -n src host 10.0.0.5 -v -w capturec2.pcap
	sudo tcpliveplay enp2s0 capturec2.pcap 10.0.0.50 94:de:80:42:a6:49 6633
done
