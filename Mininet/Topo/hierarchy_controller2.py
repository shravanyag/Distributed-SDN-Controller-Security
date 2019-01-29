#the below code is a custom topology to build a master - slave sort of distributed sdn controller architecture
#this code is run on each of the controllers which are already connected through a TCP communication
#!usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def subnet1():
  net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)
  
  c1 = net.addController('c1', controller=RemoteController, ip="10.0.0.1", port=6633)
  c3 = net.addController('c3', controller=RemoteController, ip="10.0.0.3", port=6633)
  
  h21 = net.addHost('h11', ip='10.2.1.1')
  h22 = net.addHost('h12', ip='10.2.1.2')
  
  s21.addSwitch('s21')
  
  s21.linkTo(h21)
  s21.linkTo(h22)
  
  net.build()
  c1.start()
  c3.start()
  s21.start([c3,c1])
  
  net.start()
  net.staticArp()
  CLI(net)
  net.stop()
  
if __name__ == '__main__':
  setLogLevel('info')
  subnet1()
