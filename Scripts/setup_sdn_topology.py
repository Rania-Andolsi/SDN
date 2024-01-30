from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def create_topology():
    # Initialisation de Mininet
    net = Mininet(controller=RemoteController)

    # Ajout des hôtes
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')

    # Ajout des commutateurs
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    s3 = net.addSwitch('s3')
    s4 = net.addSwitch('s4')
    s5 = net.addSwitch('s5')
    s6 = net.addSwitch('s6')
    s7 = net.addSwitch('s7')
    s8 = net.addSwitch('s8')
    s9 = net.addSwitch('s9')
    s10 = net.addSwitch('s10')
    s11 = net.addSwitch('s11')

    # Ajout des liaisons
    net.addLink(h1, s2)
    net.addLink(h2, s10)
    net.addLink(s1, s2)
    net.addLink(s1, s3)
    net.addLink(s2, s4)
    net.addLink(s2, s5)
    net.addLink(s3, s5)
    net.addLink(s3, s6)
    net.addLink(s4, s5)
    net.addLink(s4, s6)
    net.addLink(s5, s7)
    net.addLink(s5, s8)
    net.addLink(s6, s8)
    net.addLink(s6, s9)
    net.addLink(s7, s8)
    net.addLink(s7, s10)
    net.addLink(s8, s10)
    net.addLink(s8, s11)
    net.addLink(s9, s11)
    net.addLink(s10, s11)

    # Ajout des contrôleurs
    cA = net.addController('cA', controller=RemoteController, ip='127.0.0.1', port=6653)
    cB = net.addController('cB', controller=RemoteController, ip='127.0.0.1', port=6654)
    cC = net.addController('cC', controller=RemoteController, ip='127.0.0.1', port=6655)

    # Assignation des contrôleurs aux commutateurs
    net.build()
    s1.start([cA])
    s2.start([cA])
    s3.start([cA])
    s4.start([cB])
    s5.start([cA, cB])
    s6.start([cB])
    s7.start([cB, cC])
    s8.start([cB])
    s9.start([cC])
    s10.start([cC])
    s11.start([cC])

    # Activation de l'interface utilisateur Mininet
    CLI(net)

    # Arrêt de Mininet à la sortie de l'interface utilisateur
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_topology()

