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

  c2 = net.addController('c2', controller=RemoteController, ip="10.0.0.2", port=6633)

  

  h11 = net.addHost('h11', ip='10.1.1.1')

  h12 = net.addHost('h12', ip='10.1.1.2')

  h13 = net.addHost('h13', ip='10.1.2.3')

  h14 = net.addHost('h14', ip='10.1.2.4')

  

  s11.addSwitch('s11')

  s12.addSwitch('s12')

  

  s11.linkTo(h11)

  s11.linkTo(h12)

  s11.linkTo(s12)

  s12.linkTo(h13)

  s12.lonkTo(h14)

  

  net.build()

  c1.start()

  c2.start()

  s11.start([c2,c1])

  s12.start([c2,c2])

  

  net.start()

  net.staticArp()

  CLI(net)

  net.stop()

  

if __name__ == '__main__':

  setLogLevel('info')

  subnet1()
