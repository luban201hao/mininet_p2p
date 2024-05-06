import os
import time
from mininet.net import MininetE
from mininet.net import Mininet
from mininet.node import Node,ContainerHost
from mininet.topo import Topo
from mininet.node import Controller,RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')


class LinuxRouter( ContainerHost ):
    "A Node with IP forwarding enabled."
    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )
        self.cmd( 'ulimit -s unlimited' )
        self.cmd( 'sysctl net.ipv4.conf.all.rp_filter=2' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


class NetworkTopo( Topo ):
    def build( self, **_opts ):
        defaultIpleo0 = '172.16.0.1/30'
        defaultIpleo1 = '172.16.0.2/30'
        defaultIpleo2 = '172.16.0.6/30'
        defaultIpleo3 = '172.16.0.10/30'
        defaultIpleo4 = '172.16.0.14/30'
        defaultIpleo5 = '172.16.0.18/30'
        defaultIpleo6 = '172.16.0.25/30'
        defaultIpleo7 = '172.16.0.26/30'
        defaultIpleo8 = '172.16.0.30/30'
        defaultIpleo9 = '172.16.0.34/30'
        defaultIpleo10 = '172.16.0.38/30'
        defaultIpleo11 = '172.16.0.42/30'
        defaultIpleo12 = '172.16.16.1/30'
        defaultIpleo13 = '172.16.16.2/30'
        defaultIpleo14 = '172.16.16.6/30'
        defaultIpleo15 = '172.16.16.10/30'
        defaultIpleo16 = '172.16.16.14/30'
        defaultIpleo17 = '172.16.16.18/30'
        defaultIpleo18 = '172.16.16.25/30'
        defaultIpleo19 = '172.16.16.26/30'
        defaultIpleo20 = '172.16.16.30/30'
        defaultIpleo21 = '172.16.16.34/30'
        defaultIpleo22 = '172.16.16.38/30'
        defaultIpleo23 = '172.16.16.42/30'
        defaultIpleo24 = '172.16.32.1/30'
        defaultIpleo25 = '172.16.32.2/30'
        defaultIpleo26 = '172.16.32.6/30'
        defaultIpleo27 = '172.16.32.10/30'
        defaultIpleo28 = '172.16.32.14/30'
        defaultIpleo29 = '172.16.32.18/30'
        defaultIpleo30 = '172.16.32.25/30'
        defaultIpleo31 = '172.16.32.26/30'
        defaultIpleo32 = '172.16.32.30/30'
        defaultIpleo33 = '172.16.32.34/30'
        defaultIpleo34 = '172.16.32.38/30'
        defaultIpleo35 = '172.16.32.42/30'
        defaultIpleo36 = '172.16.48.1/30'
        defaultIpleo37 = '172.16.48.2/30'
        defaultIpleo38 = '172.16.48.6/30'
        defaultIpleo39 = '172.16.48.10/30'
        defaultIpleo40 = '172.16.48.14/30'
        defaultIpleo41 = '172.16.48.18/30'
        defaultIpleo42 = '172.16.48.25/30'
        defaultIpleo43 = '172.16.48.26/30'
        defaultIpleo44 = '172.16.48.30/30'
        defaultIpleo45 = '172.16.48.34/30'
        defaultIpleo46 = '172.16.48.38/30'
        defaultIpleo47 = '172.16.48.42/30'
        defaultIpleo48 = '172.16.64.1/30'
        defaultIpleo49 = '172.16.64.2/30'
        defaultIpleo50 = '172.16.64.6/30'
        defaultIpleo51 = '172.16.64.10/30'
        defaultIpleo52 = '172.16.64.14/30'
        defaultIpleo53 = '172.16.64.18/30'
        defaultIpleo54 = '172.16.64.25/30'
        defaultIpleo55 = '172.16.64.26/30'
        defaultIpleo56 = '172.16.64.30/30'
        defaultIpleo57 = '172.16.64.34/30'
        defaultIpleo58 = '172.16.64.38/30'
        defaultIpleo59 = '172.16.64.42/30'

        leo0= self.addNode('leo0', cls=LinuxRouter, ip=defaultIpleo0)
        leo1= self.addNode('leo1', cls=LinuxRouter, ip=defaultIpleo1)
        leo2= self.addNode('leo2', cls=LinuxRouter, ip=defaultIpleo2)
        leo3= self.addNode('leo3', cls=LinuxRouter, ip=defaultIpleo3)
        leo4= self.addNode('leo4', cls=LinuxRouter, ip=defaultIpleo4)
        leo5= self.addNode('leo5', cls=LinuxRouter, ip=defaultIpleo5)
        leo6= self.addNode('leo6', cls=LinuxRouter, ip=defaultIpleo6)
        leo7= self.addNode('leo7', cls=LinuxRouter, ip=defaultIpleo7)
        leo8= self.addNode('leo8', cls=LinuxRouter, ip=defaultIpleo8)
        leo9= self.addNode('leo9', cls=LinuxRouter, ip=defaultIpleo9)
        leo10= self.addNode('leo10', cls=LinuxRouter, ip=defaultIpleo10)
        leo11= self.addNode('leo11', cls=LinuxRouter, ip=defaultIpleo11)
        leo12= self.addNode('leo12', cls=LinuxRouter, ip=defaultIpleo12)
        leo13= self.addNode('leo13', cls=LinuxRouter, ip=defaultIpleo13)
        leo14= self.addNode('leo14', cls=LinuxRouter, ip=defaultIpleo14)
        leo15= self.addNode('leo15', cls=LinuxRouter, ip=defaultIpleo15)
        leo16= self.addNode('leo16', cls=LinuxRouter, ip=defaultIpleo16)
        leo17= self.addNode('leo17', cls=LinuxRouter, ip=defaultIpleo17)
        leo18= self.addNode('leo18', cls=LinuxRouter, ip=defaultIpleo18)
        leo19= self.addNode('leo19', cls=LinuxRouter, ip=defaultIpleo19)
        leo20= self.addNode('leo20', cls=LinuxRouter, ip=defaultIpleo20)
        leo21= self.addNode('leo21', cls=LinuxRouter, ip=defaultIpleo21)
        leo22= self.addNode('leo22', cls=LinuxRouter, ip=defaultIpleo22)
        leo23= self.addNode('leo23', cls=LinuxRouter, ip=defaultIpleo23)
        leo24= self.addNode('leo24', cls=LinuxRouter, ip=defaultIpleo24)
        leo25= self.addNode('leo25', cls=LinuxRouter, ip=defaultIpleo25)
        leo26= self.addNode('leo26', cls=LinuxRouter, ip=defaultIpleo26)
        leo27= self.addNode('leo27', cls=LinuxRouter, ip=defaultIpleo27)
        leo28= self.addNode('leo28', cls=LinuxRouter, ip=defaultIpleo28)
        leo29= self.addNode('leo29', cls=LinuxRouter, ip=defaultIpleo29)
        leo30= self.addNode('leo30', cls=LinuxRouter, ip=defaultIpleo30)
        leo31= self.addNode('leo31', cls=LinuxRouter, ip=defaultIpleo31)
        leo32= self.addNode('leo32', cls=LinuxRouter, ip=defaultIpleo32)
        leo33= self.addNode('leo33', cls=LinuxRouter, ip=defaultIpleo33)
        leo34= self.addNode('leo34', cls=LinuxRouter, ip=defaultIpleo34)
        leo35= self.addNode('leo35', cls=LinuxRouter, ip=defaultIpleo35)
        leo36= self.addNode('leo36', cls=LinuxRouter, ip=defaultIpleo36)
        leo37= self.addNode('leo37', cls=LinuxRouter, ip=defaultIpleo37)
        leo38= self.addNode('leo38', cls=LinuxRouter, ip=defaultIpleo38)
        leo39= self.addNode('leo39', cls=LinuxRouter, ip=defaultIpleo39)
        leo40= self.addNode('leo40', cls=LinuxRouter, ip=defaultIpleo40)
        leo41= self.addNode('leo41', cls=LinuxRouter, ip=defaultIpleo41)
        leo42= self.addNode('leo42', cls=LinuxRouter, ip=defaultIpleo42)
        leo43= self.addNode('leo43', cls=LinuxRouter, ip=defaultIpleo43)
        leo44= self.addNode('leo44', cls=LinuxRouter, ip=defaultIpleo44)
        leo45= self.addNode('leo45', cls=LinuxRouter, ip=defaultIpleo45)
        leo46= self.addNode('leo46', cls=LinuxRouter, ip=defaultIpleo46)
        leo47= self.addNode('leo47', cls=LinuxRouter, ip=defaultIpleo47)
        leo48= self.addNode('leo48', cls=LinuxRouter, ip=defaultIpleo48)
        leo49= self.addNode('leo49', cls=LinuxRouter, ip=defaultIpleo49)
        leo50= self.addNode('leo50', cls=LinuxRouter, ip=defaultIpleo50)
        leo51= self.addNode('leo51', cls=LinuxRouter, ip=defaultIpleo51)
        leo52= self.addNode('leo52', cls=LinuxRouter, ip=defaultIpleo52)
        leo53= self.addNode('leo53', cls=LinuxRouter, ip=defaultIpleo53)
        leo54= self.addNode('leo54', cls=LinuxRouter, ip=defaultIpleo54)
        leo55= self.addNode('leo55', cls=LinuxRouter, ip=defaultIpleo55)
        leo56= self.addNode('leo56', cls=LinuxRouter, ip=defaultIpleo56)
        leo57= self.addNode('leo57', cls=LinuxRouter, ip=defaultIpleo57)
        leo58= self.addNode('leo58', cls=LinuxRouter, ip=defaultIpleo58)
        leo59= self.addNode('leo59', cls=LinuxRouter, ip=defaultIpleo59)
        s1=self.addSwitch('s1')

        self.addLink(leo0,leo1,infName1='leo0-eth0',params1={'ip':'172.16.0.1/30'},infName2='leo1-eth0',params2={'ip':'172.16.0.2/30'})
        self.addLink(leo1,leo2,infName1='leo1-eth1',params1={'ip':'172.16.0.5/30'},infName2='leo2-eth0',params2={'ip':'172.16.0.6/30'})
        self.addLink(leo2,leo3,infName1='leo2-eth1',params1={'ip':'172.16.0.9/30'},infName2='leo3-eth0',params2={'ip':'172.16.0.10/30'})
        self.addLink(leo3,leo4,infName1='leo3-eth1',params1={'ip':'172.16.0.13/30'},infName2='leo4-eth0',params2={'ip':'172.16.0.14/30'})
        self.addLink(leo4,leo5,infName1='leo4-eth1',params1={'ip':'172.16.0.17/30'},infName2='leo5-eth0',params2={'ip':'172.16.0.18/30'})
        self.addLink(leo5,leo0,infName1='leo5-eth1',params1={'ip':'172.16.0.21/30'},infName2='leo0-eth1',params2={'ip':'172.16.0.22/30'})
        self.addLink(leo6,leo7,infName1='leo6-eth0',params1={'ip':'172.16.0.25/30'},infName2='leo7-eth0',params2={'ip':'172.16.0.26/30'})
        self.addLink(leo7,leo8,infName1='leo7-eth1',params1={'ip':'172.16.0.29/30'},infName2='leo8-eth0',params2={'ip':'172.16.0.30/30'})
        self.addLink(leo8,leo9,infName1='leo8-eth1',params1={'ip':'172.16.0.33/30'},infName2='leo9-eth0',params2={'ip':'172.16.0.34/30'})
        self.addLink(leo9,leo10,infName1='leo9-eth1',params1={'ip':'172.16.0.37/30'},infName2='leo10-eth0',params2={'ip':'172.16.0.38/30'})
        self.addLink(leo10,leo11,infName1='leo10-eth1',params1={'ip':'172.16.0.41/30'},infName2='leo11-eth0',params2={'ip':'172.16.0.42/30'})
        self.addLink(leo11,leo6,infName1='leo11-eth1',params1={'ip':'172.16.0.45/30'},infName2='leo6-eth1',params2={'ip':'172.16.0.46/30'})
        self.addLink(leo0,leo6,infName1='leo0-eth2',params1={'ip':'172.16.0.49/30'},infName2='leo6-eth2',params2={'ip':'172.16.0.50/30'})
        self.addLink(leo1,leo7,infName1='leo1-eth2',params1={'ip':'172.16.0.53/30'},infName2='leo7-eth2',params2={'ip':'172.16.0.54/30'})
        self.addLink(leo2,leo8,infName1='leo2-eth2',params1={'ip':'172.16.0.57/30'},infName2='leo8-eth2',params2={'ip':'172.16.0.58/30'})
        self.addLink(leo3,leo9,infName1='leo3-eth2',params1={'ip':'172.16.0.61/30'},infName2='leo9-eth2',params2={'ip':'172.16.0.62/30'})
        self.addLink(leo4,leo10,infName1='leo4-eth2',params1={'ip':'172.16.0.65/30'},infName2='leo10-eth2',params2={'ip':'172.16.0.66/30'})
        self.addLink(leo5,leo11,infName1='leo5-eth2',params1={'ip':'172.16.0.69/30'},infName2='leo11-eth2',params2={'ip':'172.16.0.70/30'})
        self.addLink(leo12,leo13,infName1='leo12-eth0',params1={'ip':'172.16.16.1/30'},infName2='leo13-eth0',params2={'ip':'172.16.16.2/30'})
        self.addLink(leo13,leo14,infName1='leo13-eth1',params1={'ip':'172.16.16.5/30'},infName2='leo14-eth0',params2={'ip':'172.16.16.6/30'})
        self.addLink(leo14,leo15,infName1='leo14-eth1',params1={'ip':'172.16.16.9/30'},infName2='leo15-eth0',params2={'ip':'172.16.16.10/30'})
        self.addLink(leo15,leo16,infName1='leo15-eth1',params1={'ip':'172.16.16.13/30'},infName2='leo16-eth0',params2={'ip':'172.16.16.14/30'})
        self.addLink(leo16,leo17,infName1='leo16-eth1',params1={'ip':'172.16.16.17/30'},infName2='leo17-eth0',params2={'ip':'172.16.16.18/30'})
        self.addLink(leo17,leo12,infName1='leo17-eth1',params1={'ip':'172.16.16.21/30'},infName2='leo12-eth1',params2={'ip':'172.16.16.22/30'})
        self.addLink(leo18,leo19,infName1='leo18-eth0',params1={'ip':'172.16.16.25/30'},infName2='leo19-eth0',params2={'ip':'172.16.16.26/30'})
        self.addLink(leo19,leo20,infName1='leo19-eth1',params1={'ip':'172.16.16.29/30'},infName2='leo20-eth0',params2={'ip':'172.16.16.30/30'})
        self.addLink(leo20,leo21,infName1='leo20-eth1',params1={'ip':'172.16.16.33/30'},infName2='leo21-eth0',params2={'ip':'172.16.16.34/30'})
        self.addLink(leo21,leo22,infName1='leo21-eth1',params1={'ip':'172.16.16.37/30'},infName2='leo22-eth0',params2={'ip':'172.16.16.38/30'})
        self.addLink(leo22,leo23,infName1='leo22-eth1',params1={'ip':'172.16.16.41/30'},infName2='leo23-eth0',params2={'ip':'172.16.16.42/30'})
        self.addLink(leo23,leo18,infName1='leo23-eth1',params1={'ip':'172.16.16.45/30'},infName2='leo18-eth1',params2={'ip':'172.16.16.46/30'})
        self.addLink(leo12,leo18,infName1='leo12-eth2',params1={'ip':'172.16.16.49/30'},infName2='leo18-eth2',params2={'ip':'172.16.16.50/30'})
        self.addLink(leo13,leo19,infName1='leo13-eth2',params1={'ip':'172.16.16.53/30'},infName2='leo19-eth2',params2={'ip':'172.16.16.54/30'})
        self.addLink(leo14,leo20,infName1='leo14-eth2',params1={'ip':'172.16.16.57/30'},infName2='leo20-eth2',params2={'ip':'172.16.16.58/30'})
        self.addLink(leo15,leo21,infName1='leo15-eth2',params1={'ip':'172.16.16.61/30'},infName2='leo21-eth2',params2={'ip':'172.16.16.62/30'})
        self.addLink(leo16,leo22,infName1='leo16-eth2',params1={'ip':'172.16.16.65/30'},infName2='leo22-eth2',params2={'ip':'172.16.16.66/30'})
        self.addLink(leo17,leo23,infName1='leo17-eth2',params1={'ip':'172.16.16.69/30'},infName2='leo23-eth2',params2={'ip':'172.16.16.70/30'})
        self.addLink(leo24,leo25,infName1='leo24-eth0',params1={'ip':'172.16.32.1/30'},infName2='leo25-eth0',params2={'ip':'172.16.32.2/30'})
        self.addLink(leo25,leo26,infName1='leo25-eth1',params1={'ip':'172.16.32.5/30'},infName2='leo26-eth0',params2={'ip':'172.16.32.6/30'})
        self.addLink(leo26,leo27,infName1='leo26-eth1',params1={'ip':'172.16.32.9/30'},infName2='leo27-eth0',params2={'ip':'172.16.32.10/30'})
        self.addLink(leo27,leo28,infName1='leo27-eth1',params1={'ip':'172.16.32.13/30'},infName2='leo28-eth0',params2={'ip':'172.16.32.14/30'})
        self.addLink(leo28,leo29,infName1='leo28-eth1',params1={'ip':'172.16.32.17/30'},infName2='leo29-eth0',params2={'ip':'172.16.32.18/30'})
        self.addLink(leo29,leo24,infName1='leo29-eth1',params1={'ip':'172.16.32.21/30'},infName2='leo24-eth1',params2={'ip':'172.16.32.22/30'})
        self.addLink(leo30,leo31,infName1='leo30-eth0',params1={'ip':'172.16.32.25/30'},infName2='leo31-eth0',params2={'ip':'172.16.32.26/30'})
        self.addLink(leo31,leo32,infName1='leo31-eth1',params1={'ip':'172.16.32.29/30'},infName2='leo32-eth0',params2={'ip':'172.16.32.30/30'})
        self.addLink(leo32,leo33,infName1='leo32-eth1',params1={'ip':'172.16.32.33/30'},infName2='leo33-eth0',params2={'ip':'172.16.32.34/30'})
        self.addLink(leo33,leo34,infName1='leo33-eth1',params1={'ip':'172.16.32.37/30'},infName2='leo34-eth0',params2={'ip':'172.16.32.38/30'})
        self.addLink(leo34,leo35,infName1='leo34-eth1',params1={'ip':'172.16.32.41/30'},infName2='leo35-eth0',params2={'ip':'172.16.32.42/30'})
        self.addLink(leo35,leo30,infName1='leo35-eth1',params1={'ip':'172.16.32.45/30'},infName2='leo30-eth1',params2={'ip':'172.16.32.46/30'})
        self.addLink(leo24,leo30,infName1='leo24-eth2',params1={'ip':'172.16.32.49/30'},infName2='leo30-eth2',params2={'ip':'172.16.32.50/30'})
        self.addLink(leo25,leo31,infName1='leo25-eth2',params1={'ip':'172.16.32.53/30'},infName2='leo31-eth2',params2={'ip':'172.16.32.54/30'})
        self.addLink(leo26,leo32,infName1='leo26-eth2',params1={'ip':'172.16.32.57/30'},infName2='leo32-eth2',params2={'ip':'172.16.32.58/30'})
        self.addLink(leo27,leo33,infName1='leo27-eth2',params1={'ip':'172.16.32.61/30'},infName2='leo33-eth2',params2={'ip':'172.16.32.62/30'})
        self.addLink(leo28,leo34,infName1='leo28-eth2',params1={'ip':'172.16.32.65/30'},infName2='leo34-eth2',params2={'ip':'172.16.32.66/30'})
        self.addLink(leo29,leo35,infName1='leo29-eth2',params1={'ip':'172.16.32.69/30'},infName2='leo35-eth2',params2={'ip':'172.16.32.70/30'})
        self.addLink(leo36,leo37,infName1='leo36-eth0',params1={'ip':'172.16.48.1/30'},infName2='leo37-eth0',params2={'ip':'172.16.48.2/30'})
        self.addLink(leo37,leo38,infName1='leo37-eth1',params1={'ip':'172.16.48.5/30'},infName2='leo38-eth0',params2={'ip':'172.16.48.6/30'})
        self.addLink(leo38,leo39,infName1='leo38-eth1',params1={'ip':'172.16.48.9/30'},infName2='leo39-eth0',params2={'ip':'172.16.48.10/30'})
        self.addLink(leo39,leo40,infName1='leo39-eth1',params1={'ip':'172.16.48.13/30'},infName2='leo40-eth0',params2={'ip':'172.16.48.14/30'})
        self.addLink(leo40,leo41,infName1='leo40-eth1',params1={'ip':'172.16.48.17/30'},infName2='leo41-eth0',params2={'ip':'172.16.48.18/30'})
        self.addLink(leo41,leo36,infName1='leo41-eth1',params1={'ip':'172.16.48.21/30'},infName2='leo36-eth1',params2={'ip':'172.16.48.22/30'})
        self.addLink(leo42,leo43,infName1='leo42-eth0',params1={'ip':'172.16.48.25/30'},infName2='leo43-eth0',params2={'ip':'172.16.48.26/30'})
        self.addLink(leo43,leo44,infName1='leo43-eth1',params1={'ip':'172.16.48.29/30'},infName2='leo44-eth0',params2={'ip':'172.16.48.30/30'})
        self.addLink(leo44,leo45,infName1='leo44-eth1',params1={'ip':'172.16.48.33/30'},infName2='leo45-eth0',params2={'ip':'172.16.48.34/30'})
        self.addLink(leo45,leo46,infName1='leo45-eth1',params1={'ip':'172.16.48.37/30'},infName2='leo46-eth0',params2={'ip':'172.16.48.38/30'})
        self.addLink(leo46,leo47,infName1='leo46-eth1',params1={'ip':'172.16.48.41/30'},infName2='leo47-eth0',params2={'ip':'172.16.48.42/30'})
        self.addLink(leo47,leo42,infName1='leo47-eth1',params1={'ip':'172.16.48.45/30'},infName2='leo42-eth1',params2={'ip':'172.16.48.46/30'})
        self.addLink(leo36,leo42,infName1='leo36-eth2',params1={'ip':'172.16.48.49/30'},infName2='leo42-eth2',params2={'ip':'172.16.48.50/30'})
        self.addLink(leo37,leo43,infName1='leo37-eth2',params1={'ip':'172.16.48.53/30'},infName2='leo43-eth2',params2={'ip':'172.16.48.54/30'})
        self.addLink(leo38,leo44,infName1='leo38-eth2',params1={'ip':'172.16.48.57/30'},infName2='leo44-eth2',params2={'ip':'172.16.48.58/30'})
        self.addLink(leo39,leo45,infName1='leo39-eth2',params1={'ip':'172.16.48.61/30'},infName2='leo45-eth2',params2={'ip':'172.16.48.62/30'})
        self.addLink(leo40,leo46,infName1='leo40-eth2',params1={'ip':'172.16.48.65/30'},infName2='leo46-eth2',params2={'ip':'172.16.48.66/30'})
        self.addLink(leo41,leo47,infName1='leo41-eth2',params1={'ip':'172.16.48.69/30'},infName2='leo47-eth2',params2={'ip':'172.16.48.70/30'})
        self.addLink(leo48,leo49,infName1='leo48-eth0',params1={'ip':'172.16.64.1/30'},infName2='leo49-eth0',params2={'ip':'172.16.64.2/30'})
        self.addLink(leo49,leo50,infName1='leo49-eth1',params1={'ip':'172.16.64.5/30'},infName2='leo50-eth0',params2={'ip':'172.16.64.6/30'})
        self.addLink(leo50,leo51,infName1='leo50-eth1',params1={'ip':'172.16.64.9/30'},infName2='leo51-eth0',params2={'ip':'172.16.64.10/30'})
        self.addLink(leo51,leo52,infName1='leo51-eth1',params1={'ip':'172.16.64.13/30'},infName2='leo52-eth0',params2={'ip':'172.16.64.14/30'})
        self.addLink(leo52,leo53,infName1='leo52-eth1',params1={'ip':'172.16.64.17/30'},infName2='leo53-eth0',params2={'ip':'172.16.64.18/30'})
        self.addLink(leo53,leo48,infName1='leo53-eth1',params1={'ip':'172.16.64.21/30'},infName2='leo48-eth1',params2={'ip':'172.16.64.22/30'})
        self.addLink(leo54,leo55,infName1='leo54-eth0',params1={'ip':'172.16.64.25/30'},infName2='leo55-eth0',params2={'ip':'172.16.64.26/30'})
        self.addLink(leo55,leo56,infName1='leo55-eth1',params1={'ip':'172.16.64.29/30'},infName2='leo56-eth0',params2={'ip':'172.16.64.30/30'})
        self.addLink(leo56,leo57,infName1='leo56-eth1',params1={'ip':'172.16.64.33/30'},infName2='leo57-eth0',params2={'ip':'172.16.64.34/30'})
        self.addLink(leo57,leo58,infName1='leo57-eth1',params1={'ip':'172.16.64.37/30'},infName2='leo58-eth0',params2={'ip':'172.16.64.38/30'})
        self.addLink(leo58,leo59,infName1='leo58-eth1',params1={'ip':'172.16.64.41/30'},infName2='leo59-eth0',params2={'ip':'172.16.64.42/30'})
        self.addLink(leo59,leo54,infName1='leo59-eth1',params1={'ip':'172.16.64.45/30'},infName2='leo54-eth1',params2={'ip':'172.16.64.46/30'})
        self.addLink(leo48,leo54,infName1='leo48-eth2',params1={'ip':'172.16.64.49/30'},infName2='leo54-eth2',params2={'ip':'172.16.64.50/30'})
        self.addLink(leo49,leo55,infName1='leo49-eth2',params1={'ip':'172.16.64.53/30'},infName2='leo55-eth2',params2={'ip':'172.16.64.54/30'})
        self.addLink(leo50,leo56,infName1='leo50-eth2',params1={'ip':'172.16.64.57/30'},infName2='leo56-eth2',params2={'ip':'172.16.64.58/30'})
        self.addLink(leo51,leo57,infName1='leo51-eth2',params1={'ip':'172.16.64.61/30'},infName2='leo57-eth2',params2={'ip':'172.16.64.62/30'})
        self.addLink(leo52,leo58,infName1='leo52-eth2',params1={'ip':'172.16.64.65/30'},infName2='leo58-eth2',params2={'ip':'172.16.64.66/30'})
        self.addLink(leo53,leo59,infName1='leo53-eth2',params1={'ip':'172.16.64.69/30'},infName2='leo59-eth2',params2={'ip':'172.16.64.70/30'})
        self.addLink(leo6,leo12,infName1='leo6-eth3',params1={'ip':'172.24.0.1/30'},infName2='leo12-eth3',params2={'ip':'172.24.0.2/30'})
        self.addLink(leo7,leo13,infName1='leo7-eth3',params1={'ip':'172.24.0.5/30'},infName2='leo13-eth3',params2={'ip':'172.24.0.6/30'})
        self.addLink(leo8,leo14,infName1='leo8-eth3',params1={'ip':'172.24.0.9/30'},infName2='leo14-eth3',params2={'ip':'172.24.0.10/30'})
        self.addLink(leo9,leo15,infName1='leo9-eth3',params1={'ip':'172.24.0.13/30'},infName2='leo15-eth3',params2={'ip':'172.24.0.14/30'})
        self.addLink(leo10,leo16,infName1='leo10-eth3',params1={'ip':'172.24.0.17/30'},infName2='leo16-eth3',params2={'ip':'172.24.0.18/30'})
        self.addLink(leo11,leo17,infName1='leo11-eth3',params1={'ip':'172.24.0.21/30'},infName2='leo17-eth3',params2={'ip':'172.24.0.22/30'})
        self.addLink(leo18,leo24,infName1='leo18-eth3',params1={'ip':'172.24.16.1/30'},infName2='leo24-eth3',params2={'ip':'172.24.16.2/30'})
        self.addLink(leo19,leo25,infName1='leo19-eth3',params1={'ip':'172.24.16.5/30'},infName2='leo25-eth3',params2={'ip':'172.24.16.6/30'})
        self.addLink(leo20,leo26,infName1='leo20-eth3',params1={'ip':'172.24.16.9/30'},infName2='leo26-eth3',params2={'ip':'172.24.16.10/30'})
        self.addLink(leo21,leo27,infName1='leo21-eth3',params1={'ip':'172.24.16.13/30'},infName2='leo27-eth3',params2={'ip':'172.24.16.14/30'})
        self.addLink(leo22,leo28,infName1='leo22-eth3',params1={'ip':'172.24.16.17/30'},infName2='leo28-eth3',params2={'ip':'172.24.16.18/30'})
        self.addLink(leo23,leo29,infName1='leo23-eth3',params1={'ip':'172.24.16.21/30'},infName2='leo29-eth3',params2={'ip':'172.24.16.22/30'})
        self.addLink(leo30,leo36,infName1='leo30-eth3',params1={'ip':'172.24.32.1/30'},infName2='leo36-eth3',params2={'ip':'172.24.32.2/30'})
        self.addLink(leo31,leo37,infName1='leo31-eth3',params1={'ip':'172.24.32.5/30'},infName2='leo37-eth3',params2={'ip':'172.24.32.6/30'})
        self.addLink(leo32,leo38,infName1='leo32-eth3',params1={'ip':'172.24.32.9/30'},infName2='leo38-eth3',params2={'ip':'172.24.32.10/30'})
        self.addLink(leo33,leo39,infName1='leo33-eth3',params1={'ip':'172.24.32.13/30'},infName2='leo39-eth3',params2={'ip':'172.24.32.14/30'})
        self.addLink(leo34,leo40,infName1='leo34-eth3',params1={'ip':'172.24.32.17/30'},infName2='leo40-eth3',params2={'ip':'172.24.32.18/30'})
        self.addLink(leo35,leo41,infName1='leo35-eth3',params1={'ip':'172.24.32.21/30'},infName2='leo41-eth3',params2={'ip':'172.24.32.22/30'})
        self.addLink(leo42,leo48,infName1='leo42-eth3',params1={'ip':'172.24.48.1/30'},infName2='leo48-eth3',params2={'ip':'172.24.48.2/30'})
        self.addLink(leo43,leo49,infName1='leo43-eth3',params1={'ip':'172.24.48.5/30'},infName2='leo49-eth3',params2={'ip':'172.24.48.6/30'})
        self.addLink(leo44,leo50,infName1='leo44-eth3',params1={'ip':'172.24.48.9/30'},infName2='leo50-eth3',params2={'ip':'172.24.48.10/30'})
        self.addLink(leo45,leo51,infName1='leo45-eth3',params1={'ip':'172.24.48.13/30'},infName2='leo51-eth3',params2={'ip':'172.24.48.14/30'})
        self.addLink(leo46,leo52,infName1='leo46-eth3',params1={'ip':'172.24.48.17/30'},infName2='leo52-eth3',params2={'ip':'172.24.48.18/30'})
        self.addLink(leo47,leo53,infName1='leo47-eth3',params1={'ip':'172.24.48.21/30'},infName2='leo53-eth3',params2={'ip':'172.24.48.22/30'})

        self.addLink(leo0,s1,intfName1='leo0-eth3',params1={'ip' : '10.0.0.1/24'}, port2=2000)
        self.addLink(leo1,s1,intfName1='leo1-eth3',params1={'ip' : '10.0.1.1/24'}, port2=2001)
        self.addLink(leo2,s1,intfName1='leo2-eth3',params1={'ip' : '10.0.2.1/24'}, port2=2002)
        self.addLink(leo3,s1,intfName1='leo3-eth3',params1={'ip' : '10.0.3.1/24'}, port2=2003)
        self.addLink(leo4,s1,intfName1='leo4-eth3',params1={'ip' : '10.0.4.1/24'}, port2=2004)
        self.addLink(leo5,s1,intfName1='leo5-eth3',params1={'ip' : '10.0.5.1/24'}, port2=2005)
        self.addLink(leo6,s1,intfName1='leo6-eth4',params1={'ip' : '10.1.0.1/24'}, port2=2006)
        self.addLink(leo7,s1,intfName1='leo7-eth4',params1={'ip' : '10.1.1.1/24'}, port2=2007)
        self.addLink(leo8,s1,intfName1='leo8-eth4',params1={'ip' : '10.1.2.1/24'}, port2=2008)
        self.addLink(leo9,s1,intfName1='leo9-eth4',params1={'ip' : '10.1.3.1/24'}, port2=2009)
        self.addLink(leo10,s1,intfName1='leo10-eth4',params1={'ip' : '10.1.4.1/24'}, port2=2010)
        self.addLink(leo11,s1,intfName1='leo11-eth4',params1={'ip' : '10.1.5.1/24'}, port2=2011)
        self.addLink(leo12,s1,intfName1='leo12-eth4',params1={'ip' : '10.2.5.1/24'}, port2=2012)
        self.addLink(leo13,s1,intfName1='leo13-eth4',params1={'ip' : '10.2.0.1/24'}, port2=2013)
        self.addLink(leo14,s1,intfName1='leo14-eth4',params1={'ip' : '10.2.1.1/24'}, port2=2014)
        self.addLink(leo15,s1,intfName1='leo15-eth4',params1={'ip' : '10.2.2.1/24'}, port2=2015)
        self.addLink(leo16,s1,intfName1='leo16-eth4',params1={'ip' : '10.2.3.1/24'}, port2=2016)
        self.addLink(leo17,s1,intfName1='leo17-eth4',params1={'ip' : '10.2.4.1/24'}, port2=2017)
        self.addLink(leo18,s1,intfName1='leo18-eth4',params1={'ip' : '10.3.5.1/24'}, port2=2018)
        self.addLink(leo19,s1,intfName1='leo19-eth4',params1={'ip' : '10.3.0.1/24'}, port2=2019)
        self.addLink(leo20,s1,intfName1='leo20-eth4',params1={'ip' : '10.3.1.1/24'}, port2=2020)
        self.addLink(leo21,s1,intfName1='leo21-eth4',params1={'ip' : '10.3.2.1/24'}, port2=2021)
        self.addLink(leo22,s1,intfName1='leo22-eth4',params1={'ip' : '10.3.3.1/24'}, port2=2022)
        self.addLink(leo23,s1,intfName1='leo23-eth4',params1={'ip' : '10.3.4.1/24'}, port2=2023)
        self.addLink(leo24,s1,intfName1='leo24-eth4',params1={'ip' : '10.4.4.1/24'}, port2=2024)
        self.addLink(leo25,s1,intfName1='leo25-eth4',params1={'ip' : '10.4.5.1/24'}, port2=2025)
        self.addLink(leo26,s1,intfName1='leo26-eth4',params1={'ip' : '10.4.0.1/24'}, port2=2026)
        self.addLink(leo27,s1,intfName1='leo27-eth4',params1={'ip' : '10.4.1.1/24'}, port2=2027)
        self.addLink(leo28,s1,intfName1='leo28-eth4',params1={'ip' : '10.4.2.1/24'}, port2=2028)
        self.addLink(leo29,s1,intfName1='leo29-eth4',params1={'ip' : '10.4.3.1/24'}, port2=2029)
        self.addLink(leo30,s1,intfName1='leo30-eth4',params1={'ip' : '10.5.4.1/24'}, port2=2030)
        self.addLink(leo31,s1,intfName1='leo31-eth4',params1={'ip' : '10.5.5.1/24'}, port2=2031)
        self.addLink(leo32,s1,intfName1='leo32-eth4',params1={'ip' : '10.5.0.1/24'}, port2=2032)
        self.addLink(leo33,s1,intfName1='leo33-eth4',params1={'ip' : '10.5.1.1/24'}, port2=2033)
        self.addLink(leo34,s1,intfName1='leo34-eth4',params1={'ip' : '10.5.2.1/24'}, port2=2034)
        self.addLink(leo35,s1,intfName1='leo35-eth4',params1={'ip' : '10.5.3.1/24'}, port2=2035)
        self.addLink(leo36,s1,intfName1='leo36-eth4',params1={'ip' : '10.6.3.1/24'}, port2=2036)
        self.addLink(leo37,s1,intfName1='leo37-eth4',params1={'ip' : '10.6.4.1/24'}, port2=2037)
        self.addLink(leo38,s1,intfName1='leo38-eth4',params1={'ip' : '10.6.5.1/24'}, port2=2038)
        self.addLink(leo39,s1,intfName1='leo39-eth4',params1={'ip' : '10.6.0.1/24'}, port2=2039)
        self.addLink(leo40,s1,intfName1='leo40-eth4',params1={'ip' : '10.6.1.1/24'}, port2=2040)
        self.addLink(leo41,s1,intfName1='leo41-eth4',params1={'ip' : '10.6.2.1/24'}, port2=2041)
        self.addLink(leo42,s1,intfName1='leo42-eth4',params1={'ip' : '10.7.3.1/24'}, port2=2042)
        self.addLink(leo43,s1,intfName1='leo43-eth4',params1={'ip' : '10.7.4.1/24'}, port2=2043)
        self.addLink(leo44,s1,intfName1='leo44-eth4',params1={'ip' : '10.7.5.1/24'}, port2=2044)
        self.addLink(leo45,s1,intfName1='leo45-eth4',params1={'ip' : '10.7.0.1/24'}, port2=2045)
        self.addLink(leo46,s1,intfName1='leo46-eth4',params1={'ip' : '10.7.1.1/24'}, port2=2046)
        self.addLink(leo47,s1,intfName1='leo47-eth4',params1={'ip' : '10.7.2.1/24'}, port2=2047)
        self.addLink(leo48,s1,intfName1='leo48-eth4',params1={'ip' : '10.8.2.1/24'}, port2=2048)
        self.addLink(leo49,s1,intfName1='leo49-eth4',params1={'ip' : '10.8.3.1/24'}, port2=2049)
        self.addLink(leo50,s1,intfName1='leo50-eth4',params1={'ip' : '10.8.4.1/24'}, port2=2050)
        self.addLink(leo51,s1,intfName1='leo51-eth4',params1={'ip' : '10.8.5.1/24'}, port2=2051)
        self.addLink(leo52,s1,intfName1='leo52-eth4',params1={'ip' : '10.8.0.1/24'}, port2=2052)
        self.addLink(leo53,s1,intfName1='leo53-eth4',params1={'ip' : '10.8.1.1/24'}, port2=2053)
        self.addLink(leo54,s1,intfName1='leo54-eth3',params1={'ip' : '10.9.2.1/24'}, port2=2054)
        self.addLink(leo55,s1,intfName1='leo55-eth3',params1={'ip' : '10.9.3.1/24'}, port2=2055)
        self.addLink(leo56,s1,intfName1='leo56-eth3',params1={'ip' : '10.9.4.1/24'}, port2=2056)
        self.addLink(leo57,s1,intfName1='leo57-eth3',params1={'ip' : '10.9.5.1/24'}, port2=2057)
        self.addLink(leo58,s1,intfName1='leo58-eth3',params1={'ip' : '10.9.0.1/24'}, port2=2058)
        self.addLink(leo59,s1,intfName1='leo59-eth3',params1={'ip' : '10.9.1.1/24'}, port2=2059)



        station0 = self.addNode('station0', cls = LinuxRouter, ip = '10.0.0.100/24')
        self.addLink(station0, s1, intfName1 = 'station0-eth0', params1 = {'ip' : '10.0.0.100/24'}, port2=60)
        station1 = self.addNode('station1', cls = LinuxRouter, ip = '10.0.2.100/24')
        self.addLink(station1, s1, intfName1 = 'station1-eth0', params1 = {'ip' : '10.0.2.100/24'}, port2=61)
        station2 = self.addNode('station2', cls = LinuxRouter, ip = '10.5.0.100/24')
        self.addLink(station2, s1, intfName1 = 'station2-eth0', params1 = {'ip' : '10.5.0.100/24'}, port2=62)

        self.addLink(station0, s1, intfName1 = 'station0-eth1', params1 = {'ip' : '114.114.114.1/24'}, port2=63)
        self.addLink(station1, s1, intfName1 = 'station1-eth1', params1 = {'ip' : '114.114.114.2/24'}, port2=64)
        self.addLink(station2, s1, intfName1 = 'station2-eth1', params1 = {'ip' : '114.114.114.3/24'}, port2=65)

        stationNAT = self.addNode('stationNAT', cls = LinuxRouter, ip = '114.114.114.114/24')
        self.addLink(stationNAT, s1, intfName1 = 'stationNAT-eth0', params1 = {'ip' : '114.114.114.114/24'}, port2 = 66)



class tc_info(object):
    num1=0
    num2=0
    ethname1=''
    ethname2=''
    linkinfo=[]
    def __init__(self,num1,num2,ethname1,ethname2,linkinfo):
        self.num1=num1
        self.num2=num2
        self.ethname1=ethname1
        self.ethname2=ethname2
        self.linkinfo=linkinfo



class TestMininet(Mininet):
    def __init__(self,controller,topo):
        Mininet.__init__(self,controller=controller, topo=topo, link=TCLink)
        self.leo0=self.getNodeByName('leo0')
        self.leo1=self.getNodeByName('leo1')
        self.leo2=self.getNodeByName('leo2')
        self.leo3=self.getNodeByName('leo3')
        self.leo4=self.getNodeByName('leo4')
        self.leo5=self.getNodeByName('leo5')
        self.leo6=self.getNodeByName('leo6')
        self.leo7=self.getNodeByName('leo7')
        self.leo8=self.getNodeByName('leo8')
        self.leo9=self.getNodeByName('leo9')
        self.leo10=self.getNodeByName('leo10')
        self.leo11=self.getNodeByName('leo11')
        self.leo12=self.getNodeByName('leo12')
        self.leo13=self.getNodeByName('leo13')
        self.leo14=self.getNodeByName('leo14')
        self.leo15=self.getNodeByName('leo15')
        self.leo16=self.getNodeByName('leo16')
        self.leo17=self.getNodeByName('leo17')
        self.leo18=self.getNodeByName('leo18')
        self.leo19=self.getNodeByName('leo19')
        self.leo20=self.getNodeByName('leo20')
        self.leo21=self.getNodeByName('leo21')
        self.leo22=self.getNodeByName('leo22')
        self.leo23=self.getNodeByName('leo23')
        self.leo24=self.getNodeByName('leo24')
        self.leo25=self.getNodeByName('leo25')
        self.leo26=self.getNodeByName('leo26')
        self.leo27=self.getNodeByName('leo27')
        self.leo28=self.getNodeByName('leo28')
        self.leo29=self.getNodeByName('leo29')
        self.leo30=self.getNodeByName('leo30')
        self.leo31=self.getNodeByName('leo31')
        self.leo32=self.getNodeByName('leo32')
        self.leo33=self.getNodeByName('leo33')
        self.leo34=self.getNodeByName('leo34')
        self.leo35=self.getNodeByName('leo35')
        self.leo36=self.getNodeByName('leo36')
        self.leo37=self.getNodeByName('leo37')
        self.leo38=self.getNodeByName('leo38')
        self.leo39=self.getNodeByName('leo39')
        self.leo40=self.getNodeByName('leo40')
        self.leo41=self.getNodeByName('leo41')
        self.leo42=self.getNodeByName('leo42')
        self.leo43=self.getNodeByName('leo43')
        self.leo44=self.getNodeByName('leo44')
        self.leo45=self.getNodeByName('leo45')
        self.leo46=self.getNodeByName('leo46')
        self.leo47=self.getNodeByName('leo47')
        self.leo48=self.getNodeByName('leo48')
        self.leo49=self.getNodeByName('leo49')
        self.leo50=self.getNodeByName('leo50')
        self.leo51=self.getNodeByName('leo51')
        self.leo52=self.getNodeByName('leo52')
        self.leo53=self.getNodeByName('leo53')
        self.leo54=self.getNodeByName('leo54')
        self.leo55=self.getNodeByName('leo55')
        self.leo56=self.getNodeByName('leo56')
        self.leo57=self.getNodeByName('leo57')
        self.leo58=self.getNodeByName('leo58')
        self.leo59=self.getNodeByName('leo59')


        self.n=6
        self.P=10
        self.k=2
        self.phase=0
        self.phaseAll=12

        self.leodic={}
        self.leodic[0]=self.leo0
        self.leodic[1]=self.leo1
        self.leodic[2]=self.leo2
        self.leodic[3]=self.leo3
        self.leodic[4]=self.leo4
        self.leodic[5]=self.leo5
        self.leodic[6]=self.leo6
        self.leodic[7]=self.leo7
        self.leodic[8]=self.leo8
        self.leodic[9]=self.leo9
        self.leodic[10]=self.leo10
        self.leodic[11]=self.leo11
        self.leodic[12]=self.leo12
        self.leodic[13]=self.leo13
        self.leodic[14]=self.leo14
        self.leodic[15]=self.leo15
        self.leodic[16]=self.leo16
        self.leodic[17]=self.leo17
        self.leodic[18]=self.leo18
        self.leodic[19]=self.leo19
        self.leodic[20]=self.leo20
        self.leodic[21]=self.leo21
        self.leodic[22]=self.leo22
        self.leodic[23]=self.leo23
        self.leodic[24]=self.leo24
        self.leodic[25]=self.leo25
        self.leodic[26]=self.leo26
        self.leodic[27]=self.leo27
        self.leodic[28]=self.leo28
        self.leodic[29]=self.leo29
        self.leodic[30]=self.leo30
        self.leodic[31]=self.leo31
        self.leodic[32]=self.leo32
        self.leodic[33]=self.leo33
        self.leodic[34]=self.leo34
        self.leodic[35]=self.leo35
        self.leodic[36]=self.leo36
        self.leodic[37]=self.leo37
        self.leodic[38]=self.leo38
        self.leodic[39]=self.leo39
        self.leodic[40]=self.leo40
        self.leodic[41]=self.leo41
        self.leodic[42]=self.leo42
        self.leodic[43]=self.leo43
        self.leodic[44]=self.leo44
        self.leodic[45]=self.leo45
        self.leodic[46]=self.leo46
        self.leodic[47]=self.leo47
        self.leodic[48]=self.leo48
        self.leodic[49]=self.leo49
        self.leodic[50]=self.leo50
        self.leodic[51]=self.leo51
        self.leodic[52]=self.leo52
        self.leodic[53]=self.leo53
        self.leodic[54]=self.leo54
        self.leodic[55]=self.leo55
        self.leodic[56]=self.leo56
        self.leodic[57]=self.leo57
        self.leodic[58]=self.leo58
        self.leodic[59]=self.leo59

        self.se_addr={}
        self.se_addr[0]='10.0.0.1/24'
        self.se_addr[1]='10.0.1.1/24'
        self.se_addr[2]='10.0.2.1/24'
        self.se_addr[3]='10.0.3.1/24'
        self.se_addr[4]='10.0.4.1/24'
        self.se_addr[5]='10.0.5.1/24'
        self.se_addr[6]='10.1.0.1/24'
        self.se_addr[7]='10.1.1.1/24'
        self.se_addr[8]='10.1.2.1/24'
        self.se_addr[9]='10.1.3.1/24'
        self.se_addr[10]='10.1.4.1/24'
        self.se_addr[11]='10.1.5.1/24'
        self.se_addr[12]='10.2.5.1/24'
        self.se_addr[13]='10.2.0.1/24'
        self.se_addr[14]='10.2.1.1/24'
        self.se_addr[15]='10.2.2.1/24'
        self.se_addr[16]='10.2.3.1/24'
        self.se_addr[17]='10.2.4.1/24'
        self.se_addr[18]='10.3.5.1/24'
        self.se_addr[19]='10.3.0.1/24'
        self.se_addr[20]='10.3.1.1/24'
        self.se_addr[21]='10.3.2.1/24'
        self.se_addr[22]='10.3.3.1/24'
        self.se_addr[23]='10.3.4.1/24'
        self.se_addr[24]='10.4.4.1/24'
        self.se_addr[25]='10.4.5.1/24'
        self.se_addr[26]='10.4.0.1/24'
        self.se_addr[27]='10.4.1.1/24'
        self.se_addr[28]='10.4.2.1/24'
        self.se_addr[29]='10.4.3.1/24'
        self.se_addr[30]='10.5.4.1/24'
        self.se_addr[31]='10.5.5.1/24'
        self.se_addr[32]='10.5.0.1/24'
        self.se_addr[33]='10.5.1.1/24'
        self.se_addr[34]='10.5.2.1/24'
        self.se_addr[35]='10.5.3.1/24'
        self.se_addr[36]='10.6.3.1/24'
        self.se_addr[37]='10.6.4.1/24'
        self.se_addr[38]='10.6.5.1/24'
        self.se_addr[39]='10.6.0.1/24'
        self.se_addr[40]='10.6.1.1/24'
        self.se_addr[41]='10.6.2.1/24'
        self.se_addr[42]='10.7.3.1/24'
        self.se_addr[43]='10.7.4.1/24'
        self.se_addr[44]='10.7.5.1/24'
        self.se_addr[45]='10.7.0.1/24'
        self.se_addr[46]='10.7.1.1/24'
        self.se_addr[47]='10.7.2.1/24'
        self.se_addr[48]='10.8.2.1/24'
        self.se_addr[49]='10.8.3.1/24'
        self.se_addr[50]='10.8.4.1/24'
        self.se_addr[51]='10.8.5.1/24'
        self.se_addr[52]='10.8.0.1/24'
        self.se_addr[53]='10.8.1.1/24'
        self.se_addr[54]='10.9.2.1/24'
        self.se_addr[55]='10.9.3.1/24'
        self.se_addr[56]='10.9.4.1/24'
        self.se_addr[57]='10.9.5.1/24'
        self.se_addr[58]='10.9.0.1/24'
        self.se_addr[59]='10.9.1.1/24'

        self.se_ethname={}
        self.se_ethname[0]='leo0-eth3'
        self.se_ethname[1]='leo1-eth3'
        self.se_ethname[2]='leo2-eth3'
        self.se_ethname[3]='leo3-eth3'
        self.se_ethname[4]='leo4-eth3'
        self.se_ethname[5]='leo5-eth3'
        self.se_ethname[6]='leo6-eth4'
        self.se_ethname[7]='leo7-eth4'
        self.se_ethname[8]='leo8-eth4'
        self.se_ethname[9]='leo9-eth4'
        self.se_ethname[10]='leo10-eth4'
        self.se_ethname[11]='leo11-eth4'
        self.se_ethname[12]='leo12-eth4'
        self.se_ethname[13]='leo13-eth4'
        self.se_ethname[14]='leo14-eth4'
        self.se_ethname[15]='leo15-eth4'
        self.se_ethname[16]='leo16-eth4'
        self.se_ethname[17]='leo17-eth4'
        self.se_ethname[18]='leo18-eth4'
        self.se_ethname[19]='leo19-eth4'
        self.se_ethname[20]='leo20-eth4'
        self.se_ethname[21]='leo21-eth4'
        self.se_ethname[22]='leo22-eth4'
        self.se_ethname[23]='leo23-eth4'
        self.se_ethname[24]='leo24-eth4'
        self.se_ethname[25]='leo25-eth4'
        self.se_ethname[26]='leo26-eth4'
        self.se_ethname[27]='leo27-eth4'
        self.se_ethname[28]='leo28-eth4'
        self.se_ethname[29]='leo29-eth4'
        self.se_ethname[30]='leo30-eth4'
        self.se_ethname[31]='leo31-eth4'
        self.se_ethname[32]='leo32-eth4'
        self.se_ethname[33]='leo33-eth4'
        self.se_ethname[34]='leo34-eth4'
        self.se_ethname[35]='leo35-eth4'
        self.se_ethname[36]='leo36-eth4'
        self.se_ethname[37]='leo37-eth4'
        self.se_ethname[38]='leo38-eth4'
        self.se_ethname[39]='leo39-eth4'
        self.se_ethname[40]='leo40-eth4'
        self.se_ethname[41]='leo41-eth4'
        self.se_ethname[42]='leo42-eth4'
        self.se_ethname[43]='leo43-eth4'
        self.se_ethname[44]='leo44-eth4'
        self.se_ethname[45]='leo45-eth4'
        self.se_ethname[46]='leo46-eth4'
        self.se_ethname[47]='leo47-eth4'
        self.se_ethname[48]='leo48-eth4'
        self.se_ethname[49]='leo49-eth4'
        self.se_ethname[50]='leo50-eth4'
        self.se_ethname[51]='leo51-eth4'
        self.se_ethname[52]='leo52-eth4'
        self.se_ethname[53]='leo53-eth4'
        self.se_ethname[54]='leo54-eth3'
        self.se_ethname[55]='leo55-eth3'
        self.se_ethname[56]='leo56-eth3'
        self.se_ethname[57]='leo57-eth3'
        self.se_ethname[58]='leo58-eth3'
        self.se_ethname[59]='leo59-eth3'

        self.orbit_k={}
        self.orbit_k[0]=0
        self.orbit_k[1]=1
        self.orbit_k[2]=0
        self.orbit_k[3]=1
        self.orbit_k[4]=0
        self.orbit_k[5]=1
        self.orbit_k[6]=0
        self.orbit_k[7]=1
        self.orbit_k[8]=0
        self.orbit_k[9]=1


        self.tc_info_array={}
        self.tc_info_array[0]=tc_info(0,6,'leo0-eth2','leo6-eth2',[1,1,0,0,0,0,1,1,0,0,0,0])
        self.tc_info_array[1]=tc_info(1,7,'leo1-eth2','leo7-eth2',[0,0,1,1,0,0,0,0,1,1,0,0])
        self.tc_info_array[2]=tc_info(2,8,'leo2-eth2','leo8-eth2',[0,0,0,0,1,1,0,0,0,0,1,1])
        self.tc_info_array[3]=tc_info(3,9,'leo3-eth2','leo9-eth2',[1,1,0,0,0,0,1,1,0,0,0,0])
        self.tc_info_array[4]=tc_info(4,10,'leo4-eth2','leo10-eth2',[0,0,1,1,0,0,0,0,1,1,0,0])
        self.tc_info_array[5]=tc_info(5,11,'leo5-eth2','leo11-eth2',[0,0,0,0,1,1,0,0,0,0,1,1])
        self.tc_info_array[6]=tc_info(6,12,'leo6-eth3','leo12-eth3',[1,0,0,0,0,1,1,0,0,0,0,1])
        self.tc_info_array[7]=tc_info(7,13,'leo7-eth3','leo13-eth3',[0,1,1,0,0,0,0,1,1,0,0,0])
        self.tc_info_array[8]=tc_info(8,14,'leo8-eth3','leo14-eth3',[0,0,0,1,1,0,0,0,0,1,1,0])
        self.tc_info_array[9]=tc_info(9,15,'leo9-eth3','leo15-eth3',[1,0,0,0,0,1,1,0,0,0,0,1])
        self.tc_info_array[10]=tc_info(10,16,'leo10-eth3','leo16-eth3',[0,1,1,0,0,0,0,1,1,0,0,0])
        self.tc_info_array[11]=tc_info(11,17,'leo11-eth3','leo17-eth3',[0,0,0,1,1,0,0,0,0,1,1,0])
        self.tc_info_array[12]=tc_info(12,18,'leo12-eth2','leo18-eth2',[0,0,1,1,0,0,0,0,1,1,0,0])
        self.tc_info_array[13]=tc_info(13,19,'leo13-eth2','leo19-eth2',[0,0,0,0,1,1,0,0,0,0,1,1])
        self.tc_info_array[14]=tc_info(14,20,'leo14-eth2','leo20-eth2',[1,1,0,0,0,0,1,1,0,0,0,0])
        self.tc_info_array[15]=tc_info(15,21,'leo15-eth2','leo21-eth2',[0,0,1,1,0,0,0,0,1,1,0,0])
        self.tc_info_array[16]=tc_info(16,22,'leo16-eth2','leo22-eth2',[0,0,0,0,1,1,0,0,0,0,1,1])
        self.tc_info_array[17]=tc_info(17,23,'leo17-eth2','leo23-eth2',[1,1,0,0,0,0,1,1,0,0,0,0])
        self.tc_info_array[18]=tc_info(18,24,'leo18-eth3','leo24-eth3',[0,1,1,0,0,0,0,1,1,0,0,0])
        self.tc_info_array[19]=tc_info(19,25,'leo19-eth3','leo25-eth3',[0,0,0,1,1,0,0,0,0,1,1,0])
        self.tc_info_array[20]=tc_info(20,26,'leo20-eth3','leo26-eth3',[1,0,0,0,0,1,1,0,0,0,0,1])
        self.tc_info_array[21]=tc_info(21,27,'leo21-eth3','leo27-eth3',[0,1,1,0,0,0,0,1,1,0,0,0])
        self.tc_info_array[22]=tc_info(22,28,'leo22-eth3','leo28-eth3',[0,0,0,1,1,0,0,0,0,1,1,0])
        self.tc_info_array[23]=tc_info(23,29,'leo23-eth3','leo29-eth3',[1,0,0,0,0,1,1,0,0,0,0,1])
        self.tc_info_array[24]=tc_info(24,30,'leo24-eth2','leo30-eth2',[0,0,0,0,1,1,0,0,0,0,1,1])
        self.tc_info_array[25]=tc_info(25,31,'leo25-eth2','leo31-eth2',[1,1,0,0,0,0,1,1,0,0,0,0])
        self.tc_info_array[26]=tc_info(26,32,'leo26-eth2','leo32-eth2',[0,0,1,1,0,0,0,0,1,1,0,0])
        self.tc_info_array[27]=tc_info(27,33,'leo27-eth2','leo33-eth2',[0,0,0,0,1,1,0,0,0,0,1,1])
        self.tc_info_array[28]=tc_info(28,34,'leo28-eth2','leo34-eth2',[1,1,0,0,0,0,1,1,0,0,0,0])
        self.tc_info_array[29]=tc_info(29,35,'leo29-eth2','leo35-eth2',[0,0,1,1,0,0,0,0,1,1,0,0])
        self.tc_info_array[30]=tc_info(30,36,'leo30-eth3','leo36-eth3',[0,0,0,1,1,0,0,0,0,1,1,0])
        self.tc_info_array[31]=tc_info(31,37,'leo31-eth3','leo37-eth3',[1,0,0,0,0,1,1,0,0,0,0,1])
        self.tc_info_array[32]=tc_info(32,38,'leo32-eth3','leo38-eth3',[0,1,1,0,0,0,0,1,1,0,0,0])
        self.tc_info_array[33]=tc_info(33,39,'leo33-eth3','leo39-eth3',[0,0,0,1,1,0,0,0,0,1,1,0])
        self.tc_info_array[34]=tc_info(34,40,'leo34-eth3','leo40-eth3',[1,0,0,0,0,1,1,0,0,0,0,1])
        self.tc_info_array[35]=tc_info(35,41,'leo35-eth3','leo41-eth3',[0,1,1,0,0,0,0,1,1,0,0,0])
        self.tc_info_array[36]=tc_info(36,42,'leo36-eth2','leo42-eth2',[1,1,0,0,0,0,1,1,0,0,0,0])
        self.tc_info_array[37]=tc_info(37,43,'leo37-eth2','leo43-eth2',[0,0,1,1,0,0,0,0,1,1,0,0])
        self.tc_info_array[38]=tc_info(38,44,'leo38-eth2','leo44-eth2',[0,0,0,0,1,1,0,0,0,0,1,1])
        self.tc_info_array[39]=tc_info(39,45,'leo39-eth2','leo45-eth2',[1,1,0,0,0,0,1,1,0,0,0,0])
        self.tc_info_array[40]=tc_info(40,46,'leo40-eth2','leo46-eth2',[0,0,1,1,0,0,0,0,1,1,0,0])
        self.tc_info_array[41]=tc_info(41,47,'leo41-eth2','leo47-eth2',[0,0,0,0,1,1,0,0,0,0,1,1])
        self.tc_info_array[42]=tc_info(42,48,'leo42-eth3','leo48-eth3',[1,0,0,0,0,1,1,0,0,0,0,1])
        self.tc_info_array[43]=tc_info(43,49,'leo43-eth3','leo49-eth3',[0,1,1,0,0,0,0,1,1,0,0,0])
        self.tc_info_array[44]=tc_info(44,50,'leo44-eth3','leo50-eth3',[0,0,0,1,1,0,0,0,0,1,1,0])
        self.tc_info_array[45]=tc_info(45,51,'leo45-eth3','leo51-eth3',[1,0,0,0,0,1,1,0,0,0,0,1])
        self.tc_info_array[46]=tc_info(46,52,'leo46-eth3','leo52-eth3',[0,1,1,0,0,0,0,1,1,0,0,0])
        self.tc_info_array[47]=tc_info(47,53,'leo47-eth3','leo53-eth3',[0,0,0,1,1,0,0,0,0,1,1,0])
        self.tc_info_array[48]=tc_info(48,54,'leo48-eth2','leo54-eth2',[0,0,1,1,0,0,0,0,1,1,0,0])
        self.tc_info_array[49]=tc_info(49,55,'leo49-eth2','leo55-eth2',[0,0,0,0,1,1,0,0,0,0,1,1])
        self.tc_info_array[50]=tc_info(50,56,'leo50-eth2','leo56-eth2',[1,1,0,0,0,0,1,1,0,0,0,0])
        self.tc_info_array[51]=tc_info(51,57,'leo51-eth2','leo57-eth2',[0,0,1,1,0,0,0,0,1,1,0,0])
        self.tc_info_array[52]=tc_info(52,58,'leo52-eth2','leo58-eth2',[0,0,0,0,1,1,0,0,0,0,1,1])
        self.tc_info_array[53]=tc_info(53,59,'leo53-eth2','leo59-eth2',[1,1,0,0,0,0,1,1,0,0,0,0])



    def ipaddr_sub_ip3(self,ipaddr):
        ipaddr_arr=ipaddr.split('.')
        tmp= int(ipaddr_arr[2])-1
        if tmp<0:
            tmp+=self.n
        return ipaddr_arr[0]+'.'+ipaddr_arr[1]+'.'+str(tmp)+'.'+ipaddr_arr[3]

    def ipaddr_add_ip2(self,ipaddr):
        ipaddr_arr=ipaddr.split('.')
        tmp= int(ipaddr_arr[1])+1
        if tmp>=self.P:
            tmp-=self.P
        return ipaddr_arr[0]+'.'+ str(tmp) + '.' + ipaddr_arr[2]+'.'+ipaddr_arr[3]

    def add_y(self):
        for i in range(0,self.P):
            self.orbit_k[i]+=1
            if self.orbit_k[i] >= self.k:
                self.orbit_k[i]=0
                for j in range(0,self.n):
                    self.se_addr[i*self.n+j]=self.ipaddr_sub_ip3(self.se_addr[i*self.n+j])
                    cmd_y='ifconfig ' + self.se_ethname[i*self.n+j]+' '+self.se_addr[i*self.n+j]
                    self.leodic[i*self.n+j].cmd(cmd_y)
                    print(cmd_y)
            for j in range(0,self.n):
                cmd_y = 'vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/se_add_y.conf -w /home/wyc/vtyzebra'+ str(i*self.n+j) +'.api -q /home/wyc/vtyospfd'+ str(i*self.n+j)  +'.api -r'
                self.leodic[i*self.n+j].cmd(cmd_y)
                print(cmd_y)


    def add_x(self):
        for i in range(0,self.P):
            for j in range(0,self.n):
                leo_num=i*self.n+j
                self.se_addr[leo_num]=self.ipaddr_add_ip2(self.se_addr[leo_num])
                cmd_x='ifconfig '+self.se_ethname[leo_num]+' '+self.se_addr[leo_num]
                self.leodic[leo_num].cmd(cmd_x)
                print(cmd_x)
                cmd_x = 'vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/se_add_x.conf -w /home/wyc/vtyzebra'+ str(leo_num) +'.api -q /home/wyc/vtyospfd'+ str(leo_num)  +'.api -r'
                self.leodic[leo_num].cmd(cmd_x)
                print(cmd_x)


    def oa(self):
        self.leo0.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa0.conf -w /home/wyc/vtyzebra0.api -q /home/wyc/vtyospfd0.api -r")
        self.leo1.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa1.conf -w /home/wyc/vtyzebra1.api -q /home/wyc/vtyospfd1.api -r")
        self.leo2.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa2.conf -w /home/wyc/vtyzebra2.api -q /home/wyc/vtyospfd2.api -r")
        self.leo3.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa3.conf -w /home/wyc/vtyzebra3.api -q /home/wyc/vtyospfd3.api -r")
        self.leo4.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa4.conf -w /home/wyc/vtyzebra4.api -q /home/wyc/vtyospfd4.api -r")
        self.leo5.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa5.conf -w /home/wyc/vtyzebra5.api -q /home/wyc/vtyospfd5.api -r")
        self.leo6.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa6.conf -w /home/wyc/vtyzebra6.api -q /home/wyc/vtyospfd6.api -r")
        self.leo7.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa7.conf -w /home/wyc/vtyzebra7.api -q /home/wyc/vtyospfd7.api -r")
        self.leo8.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa8.conf -w /home/wyc/vtyzebra8.api -q /home/wyc/vtyospfd8.api -r")
        self.leo9.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa9.conf -w /home/wyc/vtyzebra9.api -q /home/wyc/vtyospfd9.api -r")
        self.leo10.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa10.conf -w /home/wyc/vtyzebra10.api -q /home/wyc/vtyospfd10.api -r")
        self.leo11.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa11.conf -w /home/wyc/vtyzebra11.api -q /home/wyc/vtyospfd11.api -r")
        self.leo12.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa12.conf -w /home/wyc/vtyzebra12.api -q /home/wyc/vtyospfd12.api -r")
        self.leo13.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa13.conf -w /home/wyc/vtyzebra13.api -q /home/wyc/vtyospfd13.api -r")
        self.leo14.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa14.conf -w /home/wyc/vtyzebra14.api -q /home/wyc/vtyospfd14.api -r")
        self.leo15.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa15.conf -w /home/wyc/vtyzebra15.api -q /home/wyc/vtyospfd15.api -r")
        self.leo16.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa16.conf -w /home/wyc/vtyzebra16.api -q /home/wyc/vtyospfd16.api -r")
        self.leo17.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa17.conf -w /home/wyc/vtyzebra17.api -q /home/wyc/vtyospfd17.api -r")
        self.leo18.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa18.conf -w /home/wyc/vtyzebra18.api -q /home/wyc/vtyospfd18.api -r")
        self.leo19.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa19.conf -w /home/wyc/vtyzebra19.api -q /home/wyc/vtyospfd19.api -r")
        self.leo20.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa20.conf -w /home/wyc/vtyzebra20.api -q /home/wyc/vtyospfd20.api -r")
        self.leo21.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa21.conf -w /home/wyc/vtyzebra21.api -q /home/wyc/vtyospfd21.api -r")
        self.leo22.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa22.conf -w /home/wyc/vtyzebra22.api -q /home/wyc/vtyospfd22.api -r")
        self.leo23.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa23.conf -w /home/wyc/vtyzebra23.api -q /home/wyc/vtyospfd23.api -r")
        self.leo24.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa24.conf -w /home/wyc/vtyzebra24.api -q /home/wyc/vtyospfd24.api -r")
        self.leo25.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa25.conf -w /home/wyc/vtyzebra25.api -q /home/wyc/vtyospfd25.api -r")
        self.leo26.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa26.conf -w /home/wyc/vtyzebra26.api -q /home/wyc/vtyospfd26.api -r")
        self.leo27.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa27.conf -w /home/wyc/vtyzebra27.api -q /home/wyc/vtyospfd27.api -r")
        self.leo28.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa28.conf -w /home/wyc/vtyzebra28.api -q /home/wyc/vtyospfd28.api -r")
        self.leo29.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa29.conf -w /home/wyc/vtyzebra29.api -q /home/wyc/vtyospfd29.api -r")
        self.leo30.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa30.conf -w /home/wyc/vtyzebra30.api -q /home/wyc/vtyospfd30.api -r")
        self.leo31.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa31.conf -w /home/wyc/vtyzebra31.api -q /home/wyc/vtyospfd31.api -r")
        self.leo32.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa32.conf -w /home/wyc/vtyzebra32.api -q /home/wyc/vtyospfd32.api -r")
        self.leo33.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa33.conf -w /home/wyc/vtyzebra33.api -q /home/wyc/vtyospfd33.api -r")
        self.leo34.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa34.conf -w /home/wyc/vtyzebra34.api -q /home/wyc/vtyospfd34.api -r")
        self.leo35.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa35.conf -w /home/wyc/vtyzebra35.api -q /home/wyc/vtyospfd35.api -r")
        self.leo36.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa36.conf -w /home/wyc/vtyzebra36.api -q /home/wyc/vtyospfd36.api -r")
        self.leo37.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa37.conf -w /home/wyc/vtyzebra37.api -q /home/wyc/vtyospfd37.api -r")
        self.leo38.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa38.conf -w /home/wyc/vtyzebra38.api -q /home/wyc/vtyospfd38.api -r")
        self.leo39.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa39.conf -w /home/wyc/vtyzebra39.api -q /home/wyc/vtyospfd39.api -r")
        self.leo40.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa40.conf -w /home/wyc/vtyzebra40.api -q /home/wyc/vtyospfd40.api -r")
        self.leo41.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa41.conf -w /home/wyc/vtyzebra41.api -q /home/wyc/vtyospfd41.api -r")
        self.leo42.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa42.conf -w /home/wyc/vtyzebra42.api -q /home/wyc/vtyospfd42.api -r")
        self.leo43.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa43.conf -w /home/wyc/vtyzebra43.api -q /home/wyc/vtyospfd43.api -r")
        self.leo44.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa44.conf -w /home/wyc/vtyzebra44.api -q /home/wyc/vtyospfd44.api -r")
        self.leo45.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa45.conf -w /home/wyc/vtyzebra45.api -q /home/wyc/vtyospfd45.api -r")
        self.leo46.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa46.conf -w /home/wyc/vtyzebra46.api -q /home/wyc/vtyospfd46.api -r")
        self.leo47.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa47.conf -w /home/wyc/vtyzebra47.api -q /home/wyc/vtyospfd47.api -r")
        self.leo48.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa48.conf -w /home/wyc/vtyzebra48.api -q /home/wyc/vtyospfd48.api -r")
        self.leo49.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa49.conf -w /home/wyc/vtyzebra49.api -q /home/wyc/vtyospfd49.api -r")
        self.leo50.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa50.conf -w /home/wyc/vtyzebra50.api -q /home/wyc/vtyospfd50.api -r")
        self.leo51.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa51.conf -w /home/wyc/vtyzebra51.api -q /home/wyc/vtyospfd51.api -r")
        self.leo52.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa52.conf -w /home/wyc/vtyzebra52.api -q /home/wyc/vtyospfd52.api -r")
        self.leo53.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa53.conf -w /home/wyc/vtyzebra53.api -q /home/wyc/vtyospfd53.api -r")
        self.leo54.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa54.conf -w /home/wyc/vtyzebra54.api -q /home/wyc/vtyospfd54.api -r")
        self.leo55.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa55.conf -w /home/wyc/vtyzebra55.api -q /home/wyc/vtyospfd55.api -r")
        self.leo56.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa56.conf -w /home/wyc/vtyzebra56.api -q /home/wyc/vtyospfd56.api -r")
        self.leo57.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa57.conf -w /home/wyc/vtyzebra57.api -q /home/wyc/vtyospfd57.api -r")
        self.leo58.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa58.conf -w /home/wyc/vtyzebra58.api -q /home/wyc/vtyospfd58.api -r")
        self.leo59.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/inter_oa/inter_oa59.conf -w /home/wyc/vtyzebra59.api -q /home/wyc/vtyospfd59.api -r")


    def load(self):
        self.leo0.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra0.api -q /home/wyc/vtyospfd0.api -r")
        self.leo1.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra1.api -q /home/wyc/vtyospfd1.api -r")
        self.leo2.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra2.api -q /home/wyc/vtyospfd2.api -r")
        self.leo3.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra3.api -q /home/wyc/vtyospfd3.api -r")
        self.leo4.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra4.api -q /home/wyc/vtyospfd4.api -r")
        self.leo5.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra5.api -q /home/wyc/vtyospfd5.api -r")
        self.leo6.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra6.api -q /home/wyc/vtyospfd6.api -r")
        self.leo7.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra7.api -q /home/wyc/vtyospfd7.api -r")
        self.leo8.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra8.api -q /home/wyc/vtyospfd8.api -r")
        self.leo9.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra9.api -q /home/wyc/vtyospfd9.api -r")
        self.leo10.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra10.api -q /home/wyc/vtyospfd10.api -r")
        self.leo11.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra11.api -q /home/wyc/vtyospfd11.api -r")
        self.leo12.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra12.api -q /home/wyc/vtyospfd12.api -r")
        self.leo13.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra13.api -q /home/wyc/vtyospfd13.api -r")
        self.leo14.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra14.api -q /home/wyc/vtyospfd14.api -r")
        self.leo15.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra15.api -q /home/wyc/vtyospfd15.api -r")
        self.leo16.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra16.api -q /home/wyc/vtyospfd16.api -r")
        self.leo17.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra17.api -q /home/wyc/vtyospfd17.api -r")
        self.leo18.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra18.api -q /home/wyc/vtyospfd18.api -r")
        self.leo19.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra19.api -q /home/wyc/vtyospfd19.api -r")
        self.leo20.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra20.api -q /home/wyc/vtyospfd20.api -r")
        self.leo21.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra21.api -q /home/wyc/vtyospfd21.api -r")
        self.leo22.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra22.api -q /home/wyc/vtyospfd22.api -r")
        self.leo23.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra23.api -q /home/wyc/vtyospfd23.api -r")
        self.leo24.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra24.api -q /home/wyc/vtyospfd24.api -r")
        self.leo25.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra25.api -q /home/wyc/vtyospfd25.api -r")
        self.leo26.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra26.api -q /home/wyc/vtyospfd26.api -r")
        self.leo27.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra27.api -q /home/wyc/vtyospfd27.api -r")
        self.leo28.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra28.api -q /home/wyc/vtyospfd28.api -r")
        self.leo29.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra29.api -q /home/wyc/vtyospfd29.api -r")
        self.leo30.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra30.api -q /home/wyc/vtyospfd30.api -r")
        self.leo31.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra31.api -q /home/wyc/vtyospfd31.api -r")
        self.leo32.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra32.api -q /home/wyc/vtyospfd32.api -r")
        self.leo33.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra33.api -q /home/wyc/vtyospfd33.api -r")
        self.leo34.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra34.api -q /home/wyc/vtyospfd34.api -r")
        self.leo35.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra35.api -q /home/wyc/vtyospfd35.api -r")
        self.leo36.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra36.api -q /home/wyc/vtyospfd36.api -r")
        self.leo37.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra37.api -q /home/wyc/vtyospfd37.api -r")
        self.leo38.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra38.api -q /home/wyc/vtyospfd38.api -r")
        self.leo39.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra39.api -q /home/wyc/vtyospfd39.api -r")
        self.leo40.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra40.api -q /home/wyc/vtyospfd40.api -r")
        self.leo41.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra41.api -q /home/wyc/vtyospfd41.api -r")
        self.leo42.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra42.api -q /home/wyc/vtyospfd42.api -r")
        self.leo43.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra43.api -q /home/wyc/vtyospfd43.api -r")
        self.leo44.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra44.api -q /home/wyc/vtyospfd44.api -r")
        self.leo45.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra45.api -q /home/wyc/vtyospfd45.api -r")
        self.leo46.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra46.api -q /home/wyc/vtyospfd46.api -r")
        self.leo47.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra47.api -q /home/wyc/vtyospfd47.api -r")
        self.leo48.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra48.api -q /home/wyc/vtyospfd48.api -r")
        self.leo49.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra49.api -q /home/wyc/vtyospfd49.api -r")
        self.leo50.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra50.api -q /home/wyc/vtyospfd50.api -r")
        self.leo51.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra51.api -q /home/wyc/vtyospfd51.api -r")
        self.leo52.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra52.api -q /home/wyc/vtyospfd52.api -r")
        self.leo53.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra53.api -q /home/wyc/vtyospfd53.api -r")
        self.leo54.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra54.api -q /home/wyc/vtyospfd54.api -r")
        self.leo55.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra55.api -q /home/wyc/vtyospfd55.api -r")
        self.leo56.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra56.api -q /home/wyc/vtyospfd56.api -r")
        self.leo57.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra57.api -q /home/wyc/vtyospfd57.api -r")
        self.leo58.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra58.api -q /home/wyc/vtyospfd58.api -r")
        self.leo59.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/loadlsdb.conf -w /home/wyc/vtyzebra59.api -q /home/wyc/vtyospfd59.api -r")


    def add_phase(self):
        last_phase=self.phase
        self.phase+=1
        print(str(self.phase)+","+str(last_phase))
        if self.phase>=self.phaseAll:
            self.phase=0
        self.leo0.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra0.api -q /home/wyc/vtyospfd0.api -r")
        self.leo1.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra1.api -q /home/wyc/vtyospfd1.api -r")
        self.leo2.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra2.api -q /home/wyc/vtyospfd2.api -r")
        self.leo3.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra3.api -q /home/wyc/vtyospfd3.api -r")
        self.leo4.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra4.api -q /home/wyc/vtyospfd4.api -r")
        self.leo5.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra5.api -q /home/wyc/vtyospfd5.api -r")
        self.leo6.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra6.api -q /home/wyc/vtyospfd6.api -r")
        self.leo7.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra7.api -q /home/wyc/vtyospfd7.api -r")
        self.leo8.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra8.api -q /home/wyc/vtyospfd8.api -r")
        self.leo9.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra9.api -q /home/wyc/vtyospfd9.api -r")
        self.leo10.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra10.api -q /home/wyc/vtyospfd10.api -r")
        self.leo11.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra11.api -q /home/wyc/vtyospfd11.api -r")
        self.leo12.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra12.api -q /home/wyc/vtyospfd12.api -r")
        self.leo13.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra13.api -q /home/wyc/vtyospfd13.api -r")
        self.leo14.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra14.api -q /home/wyc/vtyospfd14.api -r")
        self.leo15.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra15.api -q /home/wyc/vtyospfd15.api -r")
        self.leo16.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra16.api -q /home/wyc/vtyospfd16.api -r")
        self.leo17.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra17.api -q /home/wyc/vtyospfd17.api -r")
        self.leo18.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra18.api -q /home/wyc/vtyospfd18.api -r")
        self.leo19.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra19.api -q /home/wyc/vtyospfd19.api -r")
        self.leo20.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra20.api -q /home/wyc/vtyospfd20.api -r")
        self.leo21.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra21.api -q /home/wyc/vtyospfd21.api -r")
        self.leo22.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra22.api -q /home/wyc/vtyospfd22.api -r")
        self.leo23.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra23.api -q /home/wyc/vtyospfd23.api -r")
        self.leo24.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra24.api -q /home/wyc/vtyospfd24.api -r")
        self.leo25.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra25.api -q /home/wyc/vtyospfd25.api -r")
        self.leo26.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra26.api -q /home/wyc/vtyospfd26.api -r")
        self.leo27.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra27.api -q /home/wyc/vtyospfd27.api -r")
        self.leo28.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra28.api -q /home/wyc/vtyospfd28.api -r")
        self.leo29.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra29.api -q /home/wyc/vtyospfd29.api -r")
        self.leo30.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra30.api -q /home/wyc/vtyospfd30.api -r")
        self.leo31.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra31.api -q /home/wyc/vtyospfd31.api -r")
        self.leo32.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra32.api -q /home/wyc/vtyospfd32.api -r")
        self.leo33.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra33.api -q /home/wyc/vtyospfd33.api -r")
        self.leo34.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra34.api -q /home/wyc/vtyospfd34.api -r")
        self.leo35.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra35.api -q /home/wyc/vtyospfd35.api -r")
        self.leo36.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra36.api -q /home/wyc/vtyospfd36.api -r")
        self.leo37.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra37.api -q /home/wyc/vtyospfd37.api -r")
        self.leo38.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra38.api -q /home/wyc/vtyospfd38.api -r")
        self.leo39.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra39.api -q /home/wyc/vtyospfd39.api -r")
        self.leo40.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra40.api -q /home/wyc/vtyospfd40.api -r")
        self.leo41.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra41.api -q /home/wyc/vtyospfd41.api -r")
        self.leo42.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra42.api -q /home/wyc/vtyospfd42.api -r")
        self.leo43.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra43.api -q /home/wyc/vtyospfd43.api -r")
        self.leo44.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra44.api -q /home/wyc/vtyospfd44.api -r")
        self.leo45.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra45.api -q /home/wyc/vtyospfd45.api -r")
        self.leo46.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra46.api -q /home/wyc/vtyospfd46.api -r")
        self.leo47.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra47.api -q /home/wyc/vtyospfd47.api -r")
        self.leo48.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra48.api -q /home/wyc/vtyospfd48.api -r")
        self.leo49.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra49.api -q /home/wyc/vtyospfd49.api -r")
        self.leo50.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra50.api -q /home/wyc/vtyospfd50.api -r")
        self.leo51.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra51.api -q /home/wyc/vtyospfd51.api -r")
        self.leo52.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra52.api -q /home/wyc/vtyospfd52.api -r")
        self.leo53.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra53.api -q /home/wyc/vtyospfd53.api -r")
        self.leo54.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra54.api -q /home/wyc/vtyospfd54.api -r")
        self.leo55.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra55.api -q /home/wyc/vtyospfd55.api -r")
        self.leo56.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra56.api -q /home/wyc/vtyospfd56.api -r")
        self.leo57.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra57.api -q /home/wyc/vtyospfd57.api -r")
        self.leo58.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra58.api -q /home/wyc/vtyospfd58.api -r")
        self.leo59.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/add_phase.conf -w /home/wyc/vtyzebra59.api -q /home/wyc/vtyospfd59.api -r")
        time.sleep(10)


    def begin_running(self):
        self.leo0.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra0.api -q /home/wyc/vtyospfd0.api -r")
        self.leo1.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra1.api -q /home/wyc/vtyospfd1.api -r")
        self.leo2.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra2.api -q /home/wyc/vtyospfd2.api -r")
        self.leo3.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra3.api -q /home/wyc/vtyospfd3.api -r")
        self.leo4.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra4.api -q /home/wyc/vtyospfd4.api -r")
        self.leo5.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra5.api -q /home/wyc/vtyospfd5.api -r")
        self.leo6.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra6.api -q /home/wyc/vtyospfd6.api -r")
        self.leo7.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra7.api -q /home/wyc/vtyospfd7.api -r")
        self.leo8.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra8.api -q /home/wyc/vtyospfd8.api -r")
        self.leo9.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra9.api -q /home/wyc/vtyospfd9.api -r")
        self.leo10.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra10.api -q /home/wyc/vtyospfd10.api -r")
        self.leo11.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra11.api -q /home/wyc/vtyospfd11.api -r")
        self.leo12.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra12.api -q /home/wyc/vtyospfd12.api -r")
        self.leo13.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra13.api -q /home/wyc/vtyospfd13.api -r")
        self.leo14.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra14.api -q /home/wyc/vtyospfd14.api -r")
        self.leo15.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra15.api -q /home/wyc/vtyospfd15.api -r")
        self.leo16.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra16.api -q /home/wyc/vtyospfd16.api -r")
        self.leo17.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra17.api -q /home/wyc/vtyospfd17.api -r")
        self.leo18.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra18.api -q /home/wyc/vtyospfd18.api -r")
        self.leo19.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra19.api -q /home/wyc/vtyospfd19.api -r")
        self.leo20.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra20.api -q /home/wyc/vtyospfd20.api -r")
        self.leo21.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra21.api -q /home/wyc/vtyospfd21.api -r")
        self.leo22.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra22.api -q /home/wyc/vtyospfd22.api -r")
        self.leo23.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra23.api -q /home/wyc/vtyospfd23.api -r")
        self.leo24.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra24.api -q /home/wyc/vtyospfd24.api -r")
        self.leo25.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra25.api -q /home/wyc/vtyospfd25.api -r")
        self.leo26.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra26.api -q /home/wyc/vtyospfd26.api -r")
        self.leo27.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra27.api -q /home/wyc/vtyospfd27.api -r")
        self.leo28.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra28.api -q /home/wyc/vtyospfd28.api -r")
        self.leo29.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra29.api -q /home/wyc/vtyospfd29.api -r")
        self.leo30.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra30.api -q /home/wyc/vtyospfd30.api -r")
        self.leo31.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra31.api -q /home/wyc/vtyospfd31.api -r")
        self.leo32.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra32.api -q /home/wyc/vtyospfd32.api -r")
        self.leo33.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra33.api -q /home/wyc/vtyospfd33.api -r")
        self.leo34.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra34.api -q /home/wyc/vtyospfd34.api -r")
        self.leo35.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra35.api -q /home/wyc/vtyospfd35.api -r")
        self.leo36.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra36.api -q /home/wyc/vtyospfd36.api -r")
        self.leo37.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra37.api -q /home/wyc/vtyospfd37.api -r")
        self.leo38.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra38.api -q /home/wyc/vtyospfd38.api -r")
        self.leo39.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra39.api -q /home/wyc/vtyospfd39.api -r")
        self.leo40.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra40.api -q /home/wyc/vtyospfd40.api -r")
        self.leo41.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra41.api -q /home/wyc/vtyospfd41.api -r")
        self.leo42.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra42.api -q /home/wyc/vtyospfd42.api -r")
        self.leo43.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra43.api -q /home/wyc/vtyospfd43.api -r")
        self.leo44.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra44.api -q /home/wyc/vtyospfd44.api -r")
        self.leo45.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra45.api -q /home/wyc/vtyospfd45.api -r")
        self.leo46.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra46.api -q /home/wyc/vtyospfd46.api -r")
        self.leo47.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra47.api -q /home/wyc/vtyospfd47.api -r")
        self.leo48.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra48.api -q /home/wyc/vtyospfd48.api -r")
        self.leo49.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra49.api -q /home/wyc/vtyospfd49.api -r")
        self.leo50.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra50.api -q /home/wyc/vtyospfd50.api -r")
        self.leo51.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra51.api -q /home/wyc/vtyospfd51.api -r")
        self.leo52.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra52.api -q /home/wyc/vtyospfd52.api -r")
        self.leo53.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra53.api -q /home/wyc/vtyospfd53.api -r")
        self.leo54.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra54.api -q /home/wyc/vtyospfd54.api -r")
        self.leo55.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra55.api -q /home/wyc/vtyospfd55.api -r")
        self.leo56.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra56.api -q /home/wyc/vtyospfd56.api -r")
        self.leo57.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra57.api -q /home/wyc/vtyospfd57.api -r")
        self.leo58.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra58.api -q /home/wyc/vtyospfd58.api -r")
        self.leo59.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_60_5/cmd/begin_running.conf -w /home/wyc/vtyzebra59.api -q /home/wyc/vtyospfd59.api -r")
        time.sleep(10)
def run():
    topo = NetworkTopo()
    net = TestMininet(controller=RemoteController,topo=topo)
    #c = net.addController('c0',controller=RemoteController,port=6633)
    net.start()
    info( '*** Routing Table on Router:\n' )
    leo0=net.getNodeByName('leo0')
    leo1=net.getNodeByName('leo1')
    leo2=net.getNodeByName('leo2')
    leo3=net.getNodeByName('leo3')
    leo4=net.getNodeByName('leo4')
    leo5=net.getNodeByName('leo5')
    leo6=net.getNodeByName('leo6')
    leo7=net.getNodeByName('leo7')
    leo8=net.getNodeByName('leo8')
    leo9=net.getNodeByName('leo9')
    leo10=net.getNodeByName('leo10')
    leo11=net.getNodeByName('leo11')
    leo12=net.getNodeByName('leo12')
    leo13=net.getNodeByName('leo13')
    leo14=net.getNodeByName('leo14')
    leo15=net.getNodeByName('leo15')
    leo16=net.getNodeByName('leo16')
    leo17=net.getNodeByName('leo17')
    leo18=net.getNodeByName('leo18')
    leo19=net.getNodeByName('leo19')
    leo20=net.getNodeByName('leo20')
    leo21=net.getNodeByName('leo21')
    leo22=net.getNodeByName('leo22')
    leo23=net.getNodeByName('leo23')
    leo24=net.getNodeByName('leo24')
    leo25=net.getNodeByName('leo25')
    leo26=net.getNodeByName('leo26')
    leo27=net.getNodeByName('leo27')
    leo28=net.getNodeByName('leo28')
    leo29=net.getNodeByName('leo29')
    leo30=net.getNodeByName('leo30')
    leo31=net.getNodeByName('leo31')
    leo32=net.getNodeByName('leo32')
    leo33=net.getNodeByName('leo33')
    leo34=net.getNodeByName('leo34')
    leo35=net.getNodeByName('leo35')
    leo36=net.getNodeByName('leo36')
    leo37=net.getNodeByName('leo37')
    leo38=net.getNodeByName('leo38')
    leo39=net.getNodeByName('leo39')
    leo40=net.getNodeByName('leo40')
    leo41=net.getNodeByName('leo41')
    leo42=net.getNodeByName('leo42')
    leo43=net.getNodeByName('leo43')
    leo44=net.getNodeByName('leo44')
    leo45=net.getNodeByName('leo45')
    leo46=net.getNodeByName('leo46')
    leo47=net.getNodeByName('leo47')
    leo48=net.getNodeByName('leo48')
    leo49=net.getNodeByName('leo49')
    leo50=net.getNodeByName('leo50')
    leo51=net.getNodeByName('leo51')
    leo52=net.getNodeByName('leo52')
    leo53=net.getNodeByName('leo53')
    leo54=net.getNodeByName('leo54')
    leo55=net.getNodeByName('leo55')
    leo56=net.getNodeByName('leo56')
    leo57=net.getNodeByName('leo57')
    leo58=net.getNodeByName('leo58')
    leo59=net.getNodeByName('leo59')
    station0=net.getNodeByName('station0')
    station1=net.getNodeByName('station1')
    station2=net.getNodeByName('station2')
    leo0.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo0zebra.conf -d -z /home/wyc/leo0zebra.api -i /home/wyc/leo0zebra.interface -w /home/wyc/vtyzebra0.api')
    leo1.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo1zebra.conf -d -z /home/wyc/leo1zebra.api -i /home/wyc/leo1zebra.interface -w /home/wyc/vtyzebra1.api')
    leo2.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo2zebra.conf -d -z /home/wyc/leo2zebra.api -i /home/wyc/leo2zebra.interface -w /home/wyc/vtyzebra2.api')
    leo3.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo3zebra.conf -d -z /home/wyc/leo3zebra.api -i /home/wyc/leo3zebra.interface -w /home/wyc/vtyzebra3.api')
    leo4.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo4zebra.conf -d -z /home/wyc/leo4zebra.api -i /home/wyc/leo4zebra.interface -w /home/wyc/vtyzebra4.api')
    leo5.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo5zebra.conf -d -z /home/wyc/leo5zebra.api -i /home/wyc/leo5zebra.interface -w /home/wyc/vtyzebra5.api')
    leo6.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo6zebra.conf -d -z /home/wyc/leo6zebra.api -i /home/wyc/leo6zebra.interface -w /home/wyc/vtyzebra6.api')
    leo7.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo7zebra.conf -d -z /home/wyc/leo7zebra.api -i /home/wyc/leo7zebra.interface -w /home/wyc/vtyzebra7.api')
    leo8.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo8zebra.conf -d -z /home/wyc/leo8zebra.api -i /home/wyc/leo8zebra.interface -w /home/wyc/vtyzebra8.api')
    leo9.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo9zebra.conf -d -z /home/wyc/leo9zebra.api -i /home/wyc/leo9zebra.interface -w /home/wyc/vtyzebra9.api')
    leo10.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo10zebra.conf -d -z /home/wyc/leo10zebra.api -i /home/wyc/leo10zebra.interface -w /home/wyc/vtyzebra10.api')
    leo11.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo11zebra.conf -d -z /home/wyc/leo11zebra.api -i /home/wyc/leo11zebra.interface -w /home/wyc/vtyzebra11.api')
    leo12.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo12zebra.conf -d -z /home/wyc/leo12zebra.api -i /home/wyc/leo12zebra.interface -w /home/wyc/vtyzebra12.api')
    leo13.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo13zebra.conf -d -z /home/wyc/leo13zebra.api -i /home/wyc/leo13zebra.interface -w /home/wyc/vtyzebra13.api')
    leo14.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo14zebra.conf -d -z /home/wyc/leo14zebra.api -i /home/wyc/leo14zebra.interface -w /home/wyc/vtyzebra14.api')
    leo15.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo15zebra.conf -d -z /home/wyc/leo15zebra.api -i /home/wyc/leo15zebra.interface -w /home/wyc/vtyzebra15.api')
    leo16.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo16zebra.conf -d -z /home/wyc/leo16zebra.api -i /home/wyc/leo16zebra.interface -w /home/wyc/vtyzebra16.api')
    leo17.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo17zebra.conf -d -z /home/wyc/leo17zebra.api -i /home/wyc/leo17zebra.interface -w /home/wyc/vtyzebra17.api')
    leo18.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo18zebra.conf -d -z /home/wyc/leo18zebra.api -i /home/wyc/leo18zebra.interface -w /home/wyc/vtyzebra18.api')
    leo19.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo19zebra.conf -d -z /home/wyc/leo19zebra.api -i /home/wyc/leo19zebra.interface -w /home/wyc/vtyzebra19.api')
    leo20.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo20zebra.conf -d -z /home/wyc/leo20zebra.api -i /home/wyc/leo20zebra.interface -w /home/wyc/vtyzebra20.api')
    leo21.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo21zebra.conf -d -z /home/wyc/leo21zebra.api -i /home/wyc/leo21zebra.interface -w /home/wyc/vtyzebra21.api')
    leo22.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo22zebra.conf -d -z /home/wyc/leo22zebra.api -i /home/wyc/leo22zebra.interface -w /home/wyc/vtyzebra22.api')
    leo23.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo23zebra.conf -d -z /home/wyc/leo23zebra.api -i /home/wyc/leo23zebra.interface -w /home/wyc/vtyzebra23.api')
    leo24.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo24zebra.conf -d -z /home/wyc/leo24zebra.api -i /home/wyc/leo24zebra.interface -w /home/wyc/vtyzebra24.api')
    leo25.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo25zebra.conf -d -z /home/wyc/leo25zebra.api -i /home/wyc/leo25zebra.interface -w /home/wyc/vtyzebra25.api')
    leo26.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo26zebra.conf -d -z /home/wyc/leo26zebra.api -i /home/wyc/leo26zebra.interface -w /home/wyc/vtyzebra26.api')
    leo27.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo27zebra.conf -d -z /home/wyc/leo27zebra.api -i /home/wyc/leo27zebra.interface -w /home/wyc/vtyzebra27.api')
    leo28.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo28zebra.conf -d -z /home/wyc/leo28zebra.api -i /home/wyc/leo28zebra.interface -w /home/wyc/vtyzebra28.api')
    leo29.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo29zebra.conf -d -z /home/wyc/leo29zebra.api -i /home/wyc/leo29zebra.interface -w /home/wyc/vtyzebra29.api')
    leo30.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo30zebra.conf -d -z /home/wyc/leo30zebra.api -i /home/wyc/leo30zebra.interface -w /home/wyc/vtyzebra30.api')
    leo31.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo31zebra.conf -d -z /home/wyc/leo31zebra.api -i /home/wyc/leo31zebra.interface -w /home/wyc/vtyzebra31.api')
    leo32.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo32zebra.conf -d -z /home/wyc/leo32zebra.api -i /home/wyc/leo32zebra.interface -w /home/wyc/vtyzebra32.api')
    leo33.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo33zebra.conf -d -z /home/wyc/leo33zebra.api -i /home/wyc/leo33zebra.interface -w /home/wyc/vtyzebra33.api')
    leo34.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo34zebra.conf -d -z /home/wyc/leo34zebra.api -i /home/wyc/leo34zebra.interface -w /home/wyc/vtyzebra34.api')
    leo35.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo35zebra.conf -d -z /home/wyc/leo35zebra.api -i /home/wyc/leo35zebra.interface -w /home/wyc/vtyzebra35.api')
    leo36.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo36zebra.conf -d -z /home/wyc/leo36zebra.api -i /home/wyc/leo36zebra.interface -w /home/wyc/vtyzebra36.api')
    leo37.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo37zebra.conf -d -z /home/wyc/leo37zebra.api -i /home/wyc/leo37zebra.interface -w /home/wyc/vtyzebra37.api')
    leo38.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo38zebra.conf -d -z /home/wyc/leo38zebra.api -i /home/wyc/leo38zebra.interface -w /home/wyc/vtyzebra38.api')
    leo39.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo39zebra.conf -d -z /home/wyc/leo39zebra.api -i /home/wyc/leo39zebra.interface -w /home/wyc/vtyzebra39.api')
    leo40.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo40zebra.conf -d -z /home/wyc/leo40zebra.api -i /home/wyc/leo40zebra.interface -w /home/wyc/vtyzebra40.api')
    leo41.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo41zebra.conf -d -z /home/wyc/leo41zebra.api -i /home/wyc/leo41zebra.interface -w /home/wyc/vtyzebra41.api')
    leo42.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo42zebra.conf -d -z /home/wyc/leo42zebra.api -i /home/wyc/leo42zebra.interface -w /home/wyc/vtyzebra42.api')
    leo43.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo43zebra.conf -d -z /home/wyc/leo43zebra.api -i /home/wyc/leo43zebra.interface -w /home/wyc/vtyzebra43.api')
    leo44.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo44zebra.conf -d -z /home/wyc/leo44zebra.api -i /home/wyc/leo44zebra.interface -w /home/wyc/vtyzebra44.api')
    leo45.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo45zebra.conf -d -z /home/wyc/leo45zebra.api -i /home/wyc/leo45zebra.interface -w /home/wyc/vtyzebra45.api')
    leo46.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo46zebra.conf -d -z /home/wyc/leo46zebra.api -i /home/wyc/leo46zebra.interface -w /home/wyc/vtyzebra46.api')
    leo47.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo47zebra.conf -d -z /home/wyc/leo47zebra.api -i /home/wyc/leo47zebra.interface -w /home/wyc/vtyzebra47.api')
    leo48.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo48zebra.conf -d -z /home/wyc/leo48zebra.api -i /home/wyc/leo48zebra.interface -w /home/wyc/vtyzebra48.api')
    leo49.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo49zebra.conf -d -z /home/wyc/leo49zebra.api -i /home/wyc/leo49zebra.interface -w /home/wyc/vtyzebra49.api')
    leo50.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo50zebra.conf -d -z /home/wyc/leo50zebra.api -i /home/wyc/leo50zebra.interface -w /home/wyc/vtyzebra50.api')
    leo51.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo51zebra.conf -d -z /home/wyc/leo51zebra.api -i /home/wyc/leo51zebra.interface -w /home/wyc/vtyzebra51.api')
    leo52.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo52zebra.conf -d -z /home/wyc/leo52zebra.api -i /home/wyc/leo52zebra.interface -w /home/wyc/vtyzebra52.api')
    leo53.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo53zebra.conf -d -z /home/wyc/leo53zebra.api -i /home/wyc/leo53zebra.interface -w /home/wyc/vtyzebra53.api')
    leo54.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo54zebra.conf -d -z /home/wyc/leo54zebra.api -i /home/wyc/leo54zebra.interface -w /home/wyc/vtyzebra54.api')
    leo55.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo55zebra.conf -d -z /home/wyc/leo55zebra.api -i /home/wyc/leo55zebra.interface -w /home/wyc/vtyzebra55.api')
    leo56.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo56zebra.conf -d -z /home/wyc/leo56zebra.api -i /home/wyc/leo56zebra.interface -w /home/wyc/vtyzebra56.api')
    leo57.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo57zebra.conf -d -z /home/wyc/leo57zebra.api -i /home/wyc/leo57zebra.interface -w /home/wyc/vtyzebra57.api')
    leo58.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo58zebra.conf -d -z /home/wyc/leo58zebra.api -i /home/wyc/leo58zebra.interface -w /home/wyc/vtyzebra58.api')
    leo59.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo59zebra.conf -d -z /home/wyc/leo59zebra.api -i /home/wyc/leo59zebra.interface -w /home/wyc/vtyzebra59.api')
    time.sleep(2)
    leo0.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo0ospfd.conf -d -z /home/wyc/leo0zebra.api -i /home/wyc/leo0ospfd.interface -q /home/wyc/vtyospfd0.api')
    leo1.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo1ospfd.conf -d -z /home/wyc/leo1zebra.api -i /home/wyc/leo1ospfd.interface -q /home/wyc/vtyospfd1.api')
    leo2.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo2ospfd.conf -d -z /home/wyc/leo2zebra.api -i /home/wyc/leo2ospfd.interface -q /home/wyc/vtyospfd2.api')
    leo3.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo3ospfd.conf -d -z /home/wyc/leo3zebra.api -i /home/wyc/leo3ospfd.interface -q /home/wyc/vtyospfd3.api')
    leo4.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo4ospfd.conf -d -z /home/wyc/leo4zebra.api -i /home/wyc/leo4ospfd.interface -q /home/wyc/vtyospfd4.api')
    leo5.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo5ospfd.conf -d -z /home/wyc/leo5zebra.api -i /home/wyc/leo5ospfd.interface -q /home/wyc/vtyospfd5.api')
    leo6.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo6ospfd.conf -d -z /home/wyc/leo6zebra.api -i /home/wyc/leo6ospfd.interface -q /home/wyc/vtyospfd6.api')
    leo7.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo7ospfd.conf -d -z /home/wyc/leo7zebra.api -i /home/wyc/leo7ospfd.interface -q /home/wyc/vtyospfd7.api')
    leo8.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo8ospfd.conf -d -z /home/wyc/leo8zebra.api -i /home/wyc/leo8ospfd.interface -q /home/wyc/vtyospfd8.api')
    leo9.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo9ospfd.conf -d -z /home/wyc/leo9zebra.api -i /home/wyc/leo9ospfd.interface -q /home/wyc/vtyospfd9.api')
    leo10.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo10ospfd.conf -d -z /home/wyc/leo10zebra.api -i /home/wyc/leo10ospfd.interface -q /home/wyc/vtyospfd10.api')
    leo11.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo11ospfd.conf -d -z /home/wyc/leo11zebra.api -i /home/wyc/leo11ospfd.interface -q /home/wyc/vtyospfd11.api')
    leo12.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo12ospfd.conf -d -z /home/wyc/leo12zebra.api -i /home/wyc/leo12ospfd.interface -q /home/wyc/vtyospfd12.api')
    leo13.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo13ospfd.conf -d -z /home/wyc/leo13zebra.api -i /home/wyc/leo13ospfd.interface -q /home/wyc/vtyospfd13.api')
    leo14.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo14ospfd.conf -d -z /home/wyc/leo14zebra.api -i /home/wyc/leo14ospfd.interface -q /home/wyc/vtyospfd14.api')
    leo15.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo15ospfd.conf -d -z /home/wyc/leo15zebra.api -i /home/wyc/leo15ospfd.interface -q /home/wyc/vtyospfd15.api')
    leo16.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo16ospfd.conf -d -z /home/wyc/leo16zebra.api -i /home/wyc/leo16ospfd.interface -q /home/wyc/vtyospfd16.api')
    leo17.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo17ospfd.conf -d -z /home/wyc/leo17zebra.api -i /home/wyc/leo17ospfd.interface -q /home/wyc/vtyospfd17.api')
    leo18.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo18ospfd.conf -d -z /home/wyc/leo18zebra.api -i /home/wyc/leo18ospfd.interface -q /home/wyc/vtyospfd18.api')
    leo19.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo19ospfd.conf -d -z /home/wyc/leo19zebra.api -i /home/wyc/leo19ospfd.interface -q /home/wyc/vtyospfd19.api')
    leo20.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo20ospfd.conf -d -z /home/wyc/leo20zebra.api -i /home/wyc/leo20ospfd.interface -q /home/wyc/vtyospfd20.api')
    leo21.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo21ospfd.conf -d -z /home/wyc/leo21zebra.api -i /home/wyc/leo21ospfd.interface -q /home/wyc/vtyospfd21.api')
    leo22.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo22ospfd.conf -d -z /home/wyc/leo22zebra.api -i /home/wyc/leo22ospfd.interface -q /home/wyc/vtyospfd22.api')
    leo23.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo23ospfd.conf -d -z /home/wyc/leo23zebra.api -i /home/wyc/leo23ospfd.interface -q /home/wyc/vtyospfd23.api')
    leo24.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo24ospfd.conf -d -z /home/wyc/leo24zebra.api -i /home/wyc/leo24ospfd.interface -q /home/wyc/vtyospfd24.api')
    leo25.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo25ospfd.conf -d -z /home/wyc/leo25zebra.api -i /home/wyc/leo25ospfd.interface -q /home/wyc/vtyospfd25.api')
    leo26.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo26ospfd.conf -d -z /home/wyc/leo26zebra.api -i /home/wyc/leo26ospfd.interface -q /home/wyc/vtyospfd26.api')
    leo27.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo27ospfd.conf -d -z /home/wyc/leo27zebra.api -i /home/wyc/leo27ospfd.interface -q /home/wyc/vtyospfd27.api')
    leo28.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo28ospfd.conf -d -z /home/wyc/leo28zebra.api -i /home/wyc/leo28ospfd.interface -q /home/wyc/vtyospfd28.api')
    leo29.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo29ospfd.conf -d -z /home/wyc/leo29zebra.api -i /home/wyc/leo29ospfd.interface -q /home/wyc/vtyospfd29.api')
    leo30.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo30ospfd.conf -d -z /home/wyc/leo30zebra.api -i /home/wyc/leo30ospfd.interface -q /home/wyc/vtyospfd30.api')
    leo31.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo31ospfd.conf -d -z /home/wyc/leo31zebra.api -i /home/wyc/leo31ospfd.interface -q /home/wyc/vtyospfd31.api')
    leo32.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo32ospfd.conf -d -z /home/wyc/leo32zebra.api -i /home/wyc/leo32ospfd.interface -q /home/wyc/vtyospfd32.api')
    leo33.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo33ospfd.conf -d -z /home/wyc/leo33zebra.api -i /home/wyc/leo33ospfd.interface -q /home/wyc/vtyospfd33.api')
    leo34.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo34ospfd.conf -d -z /home/wyc/leo34zebra.api -i /home/wyc/leo34ospfd.interface -q /home/wyc/vtyospfd34.api')
    leo35.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo35ospfd.conf -d -z /home/wyc/leo35zebra.api -i /home/wyc/leo35ospfd.interface -q /home/wyc/vtyospfd35.api')
    leo36.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo36ospfd.conf -d -z /home/wyc/leo36zebra.api -i /home/wyc/leo36ospfd.interface -q /home/wyc/vtyospfd36.api')
    leo37.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo37ospfd.conf -d -z /home/wyc/leo37zebra.api -i /home/wyc/leo37ospfd.interface -q /home/wyc/vtyospfd37.api')
    leo38.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo38ospfd.conf -d -z /home/wyc/leo38zebra.api -i /home/wyc/leo38ospfd.interface -q /home/wyc/vtyospfd38.api')
    leo39.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo39ospfd.conf -d -z /home/wyc/leo39zebra.api -i /home/wyc/leo39ospfd.interface -q /home/wyc/vtyospfd39.api')
    leo40.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo40ospfd.conf -d -z /home/wyc/leo40zebra.api -i /home/wyc/leo40ospfd.interface -q /home/wyc/vtyospfd40.api')
    leo41.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo41ospfd.conf -d -z /home/wyc/leo41zebra.api -i /home/wyc/leo41ospfd.interface -q /home/wyc/vtyospfd41.api')
    leo42.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo42ospfd.conf -d -z /home/wyc/leo42zebra.api -i /home/wyc/leo42ospfd.interface -q /home/wyc/vtyospfd42.api')
    leo43.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo43ospfd.conf -d -z /home/wyc/leo43zebra.api -i /home/wyc/leo43ospfd.interface -q /home/wyc/vtyospfd43.api')
    leo44.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo44ospfd.conf -d -z /home/wyc/leo44zebra.api -i /home/wyc/leo44ospfd.interface -q /home/wyc/vtyospfd44.api')
    leo45.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo45ospfd.conf -d -z /home/wyc/leo45zebra.api -i /home/wyc/leo45ospfd.interface -q /home/wyc/vtyospfd45.api')
    leo46.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo46ospfd.conf -d -z /home/wyc/leo46zebra.api -i /home/wyc/leo46ospfd.interface -q /home/wyc/vtyospfd46.api')
    leo47.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo47ospfd.conf -d -z /home/wyc/leo47zebra.api -i /home/wyc/leo47ospfd.interface -q /home/wyc/vtyospfd47.api')
    leo48.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo48ospfd.conf -d -z /home/wyc/leo48zebra.api -i /home/wyc/leo48ospfd.interface -q /home/wyc/vtyospfd48.api')
    leo49.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo49ospfd.conf -d -z /home/wyc/leo49zebra.api -i /home/wyc/leo49ospfd.interface -q /home/wyc/vtyospfd49.api')
    leo50.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo50ospfd.conf -d -z /home/wyc/leo50zebra.api -i /home/wyc/leo50ospfd.interface -q /home/wyc/vtyospfd50.api')
    leo51.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo51ospfd.conf -d -z /home/wyc/leo51zebra.api -i /home/wyc/leo51ospfd.interface -q /home/wyc/vtyospfd51.api')
    leo52.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo52ospfd.conf -d -z /home/wyc/leo52zebra.api -i /home/wyc/leo52ospfd.interface -q /home/wyc/vtyospfd52.api')
    leo53.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo53ospfd.conf -d -z /home/wyc/leo53zebra.api -i /home/wyc/leo53ospfd.interface -q /home/wyc/vtyospfd53.api')
    leo54.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo54ospfd.conf -d -z /home/wyc/leo54zebra.api -i /home/wyc/leo54ospfd.interface -q /home/wyc/vtyospfd54.api')
    leo55.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo55ospfd.conf -d -z /home/wyc/leo55zebra.api -i /home/wyc/leo55ospfd.interface -q /home/wyc/vtyospfd55.api')
    leo56.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo56ospfd.conf -d -z /home/wyc/leo56zebra.api -i /home/wyc/leo56ospfd.interface -q /home/wyc/vtyospfd56.api')
    leo57.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo57ospfd.conf -d -z /home/wyc/leo57zebra.api -i /home/wyc/leo57ospfd.interface -q /home/wyc/vtyospfd57.api')
    leo58.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo58ospfd.conf -d -z /home/wyc/leo58zebra.api -i /home/wyc/leo58ospfd.interface -q /home/wyc/vtyospfd58.api')
    leo59.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_60_5/ospf_conf/leo59ospfd.conf -d -z /home/wyc/leo59zebra.api -i /home/wyc/leo59ospfd.interface -q /home/wyc/vtyospfd59.api')

    station0.cmd('ip route add 172.16.0.0/12 via 10.0.0.1')
    station0.cmd('ip route add 10.0.0.0/8 via 10.0.0.1')
    station0.cmd('iptables -t nat -I POSTROUTING -o station0-eth1 -s 172.16.0.0/12 -j SNAT --to-source 114.114.114.1')
    station0.cmd('iptables -t nat -I POSTROUTING -o station0-eth1 -s 10.0.0.0/8 -j SNAT --to-source 114.114.114.1')
    station1.cmd('ip route add 172.16.0.0/12 via 10.0.2.1')
    station1.cmd('ip route add 10.0.0.0/8 via 10.0.2.1')
    station1.cmd('iptables -t nat -I POSTROUTING -o station1-eth1 -s 172.16.0.0/12 -j SNAT --to-source 114.114.114.2')
    station1.cmd('iptables -t nat -I POSTROUTING -o station1-eth1 -s 10.0.0.0/8 -j SNAT --to-source 114.114.114.2')
    station2.cmd('ip route add 172.16.0.0/12 via 10.5.0.1')
    station2.cmd('ip route add 10.0.0.0/8 via 10.5.0.1')
    station2.cmd('iptables -t nat -I POSTROUTING -o station2-eth1 -s 172.16.0.0/12 -j SNAT --to-source 114.114.114.3')
    station2.cmd('iptables -t nat -I POSTROUTING -o station2-eth1 -s 10.0.0.0/8 -j SNAT --to-source 114.114.114.3')
    os.system("ovs-ofctl add-flow s1 actions=NORMAL")
    leo0.cmd('wireshark -i leo0-eth0 -k &')
    os.system("ovs-ofctl add-flow s1 actions=NORMAL")
    CLI( net )
    net.stop()
    os.system("killall -9 ospfd zebra")
    os.system("cd /home/wyc && rm -f *api*")
    os.system("cd /home/wyc && rm -f *interface*")

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
