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
  c4 = net.addController('c4', controller=RemoteController, ip="10.0.0.4", port=6633)
  
  h31 = net.addHost('h11', ip='10.3.1.1')
  h32 = net.addHost('h12', ip='10.3.1.2')
  
  s31.addSwitch('s31')
  
  s31.linkTo(h31)
  s31.linkTo(h32)
  
  net.build()
  c1.start()
  c4.start()
  s31.start([c4,c1])
  
  net.start()
  net.staticArp()
  CLI(net)
  net.stop()
  
if __name__ == '__main__':
  setLogLevel('info')
  subnet1()
