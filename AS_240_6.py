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
        defaultIpleo6 = '172.16.0.22/30'
        defaultIpleo7 = '172.16.0.26/30'
        defaultIpleo8 = '172.16.0.30/30'
        defaultIpleo9 = '172.16.0.34/30'
        defaultIpleo10 = '172.16.0.38/30'
        defaultIpleo11 = '172.16.0.42/30'
        defaultIpleo12 = '172.16.0.46/30'
        defaultIpleo13 = '172.16.0.50/30'
        defaultIpleo14 = '172.16.0.54/30'
        defaultIpleo15 = '172.16.0.58/30'
        defaultIpleo16 = '172.16.0.62/30'
        defaultIpleo17 = '172.16.0.66/30'
        defaultIpleo18 = '172.16.0.70/30'
        defaultIpleo19 = '172.16.0.74/30'
        defaultIpleo20 = '172.16.0.81/30'
        defaultIpleo21 = '172.16.0.82/30'
        defaultIpleo22 = '172.16.0.86/30'
        defaultIpleo23 = '172.16.0.90/30'
        defaultIpleo24 = '172.16.0.94/30'
        defaultIpleo25 = '172.16.0.98/30'
        defaultIpleo26 = '172.16.0.102/30'
        defaultIpleo27 = '172.16.0.106/30'
        defaultIpleo28 = '172.16.0.110/30'
        defaultIpleo29 = '172.16.0.114/30'
        defaultIpleo30 = '172.16.0.118/30'
        defaultIpleo31 = '172.16.0.122/30'
        defaultIpleo32 = '172.16.0.126/30'
        defaultIpleo33 = '172.16.0.130/30'
        defaultIpleo34 = '172.16.0.134/30'
        defaultIpleo35 = '172.16.0.138/30'
        defaultIpleo36 = '172.16.0.142/30'
        defaultIpleo37 = '172.16.0.146/30'
        defaultIpleo38 = '172.16.0.150/30'
        defaultIpleo39 = '172.16.0.154/30'
        defaultIpleo40 = '172.16.16.1/30'
        defaultIpleo41 = '172.16.16.2/30'
        defaultIpleo42 = '172.16.16.6/30'
        defaultIpleo43 = '172.16.16.10/30'
        defaultIpleo44 = '172.16.16.14/30'
        defaultIpleo45 = '172.16.16.18/30'
        defaultIpleo46 = '172.16.16.22/30'
        defaultIpleo47 = '172.16.16.26/30'
        defaultIpleo48 = '172.16.16.30/30'
        defaultIpleo49 = '172.16.16.34/30'
        defaultIpleo50 = '172.16.16.38/30'
        defaultIpleo51 = '172.16.16.42/30'
        defaultIpleo52 = '172.16.16.46/30'
        defaultIpleo53 = '172.16.16.50/30'
        defaultIpleo54 = '172.16.16.54/30'
        defaultIpleo55 = '172.16.16.58/30'
        defaultIpleo56 = '172.16.16.62/30'
        defaultIpleo57 = '172.16.16.66/30'
        defaultIpleo58 = '172.16.16.70/30'
        defaultIpleo59 = '172.16.16.74/30'
        defaultIpleo60 = '172.16.16.81/30'
        defaultIpleo61 = '172.16.16.82/30'
        defaultIpleo62 = '172.16.16.86/30'
        defaultIpleo63 = '172.16.16.90/30'
        defaultIpleo64 = '172.16.16.94/30'
        defaultIpleo65 = '172.16.16.98/30'
        defaultIpleo66 = '172.16.16.102/30'
        defaultIpleo67 = '172.16.16.106/30'
        defaultIpleo68 = '172.16.16.110/30'
        defaultIpleo69 = '172.16.16.114/30'
        defaultIpleo70 = '172.16.16.118/30'
        defaultIpleo71 = '172.16.16.122/30'
        defaultIpleo72 = '172.16.16.126/30'
        defaultIpleo73 = '172.16.16.130/30'
        defaultIpleo74 = '172.16.16.134/30'
        defaultIpleo75 = '172.16.16.138/30'
        defaultIpleo76 = '172.16.16.142/30'
        defaultIpleo77 = '172.16.16.146/30'
        defaultIpleo78 = '172.16.16.150/30'
        defaultIpleo79 = '172.16.16.154/30'
        defaultIpleo80 = '172.16.32.1/30'
        defaultIpleo81 = '172.16.32.2/30'
        defaultIpleo82 = '172.16.32.6/30'
        defaultIpleo83 = '172.16.32.10/30'
        defaultIpleo84 = '172.16.32.14/30'
        defaultIpleo85 = '172.16.32.18/30'
        defaultIpleo86 = '172.16.32.22/30'
        defaultIpleo87 = '172.16.32.26/30'
        defaultIpleo88 = '172.16.32.30/30'
        defaultIpleo89 = '172.16.32.34/30'
        defaultIpleo90 = '172.16.32.38/30'
        defaultIpleo91 = '172.16.32.42/30'
        defaultIpleo92 = '172.16.32.46/30'
        defaultIpleo93 = '172.16.32.50/30'
        defaultIpleo94 = '172.16.32.54/30'
        defaultIpleo95 = '172.16.32.58/30'
        defaultIpleo96 = '172.16.32.62/30'
        defaultIpleo97 = '172.16.32.66/30'
        defaultIpleo98 = '172.16.32.70/30'
        defaultIpleo99 = '172.16.32.74/30'
        defaultIpleo100 = '172.16.32.81/30'
        defaultIpleo101 = '172.16.32.82/30'
        defaultIpleo102 = '172.16.32.86/30'
        defaultIpleo103 = '172.16.32.90/30'
        defaultIpleo104 = '172.16.32.94/30'
        defaultIpleo105 = '172.16.32.98/30'
        defaultIpleo106 = '172.16.32.102/30'
        defaultIpleo107 = '172.16.32.106/30'
        defaultIpleo108 = '172.16.32.110/30'
        defaultIpleo109 = '172.16.32.114/30'
        defaultIpleo110 = '172.16.32.118/30'
        defaultIpleo111 = '172.16.32.122/30'
        defaultIpleo112 = '172.16.32.126/30'
        defaultIpleo113 = '172.16.32.130/30'
        defaultIpleo114 = '172.16.32.134/30'
        defaultIpleo115 = '172.16.32.138/30'
        defaultIpleo116 = '172.16.32.142/30'
        defaultIpleo117 = '172.16.32.146/30'
        defaultIpleo118 = '172.16.32.150/30'
        defaultIpleo119 = '172.16.32.154/30'
        defaultIpleo120 = '172.16.48.1/30'
        defaultIpleo121 = '172.16.48.2/30'
        defaultIpleo122 = '172.16.48.6/30'
        defaultIpleo123 = '172.16.48.10/30'
        defaultIpleo124 = '172.16.48.14/30'
        defaultIpleo125 = '172.16.48.18/30'
        defaultIpleo126 = '172.16.48.22/30'
        defaultIpleo127 = '172.16.48.26/30'
        defaultIpleo128 = '172.16.48.30/30'
        defaultIpleo129 = '172.16.48.34/30'
        defaultIpleo130 = '172.16.48.38/30'
        defaultIpleo131 = '172.16.48.42/30'
        defaultIpleo132 = '172.16.48.46/30'
        defaultIpleo133 = '172.16.48.50/30'
        defaultIpleo134 = '172.16.48.54/30'
        defaultIpleo135 = '172.16.48.58/30'
        defaultIpleo136 = '172.16.48.62/30'
        defaultIpleo137 = '172.16.48.66/30'
        defaultIpleo138 = '172.16.48.70/30'
        defaultIpleo139 = '172.16.48.74/30'
        defaultIpleo140 = '172.16.48.81/30'
        defaultIpleo141 = '172.16.48.82/30'
        defaultIpleo142 = '172.16.48.86/30'
        defaultIpleo143 = '172.16.48.90/30'
        defaultIpleo144 = '172.16.48.94/30'
        defaultIpleo145 = '172.16.48.98/30'
        defaultIpleo146 = '172.16.48.102/30'
        defaultIpleo147 = '172.16.48.106/30'
        defaultIpleo148 = '172.16.48.110/30'
        defaultIpleo149 = '172.16.48.114/30'
        defaultIpleo150 = '172.16.48.118/30'
        defaultIpleo151 = '172.16.48.122/30'
        defaultIpleo152 = '172.16.48.126/30'
        defaultIpleo153 = '172.16.48.130/30'
        defaultIpleo154 = '172.16.48.134/30'
        defaultIpleo155 = '172.16.48.138/30'
        defaultIpleo156 = '172.16.48.142/30'
        defaultIpleo157 = '172.16.48.146/30'
        defaultIpleo158 = '172.16.48.150/30'
        defaultIpleo159 = '172.16.48.154/30'
        defaultIpleo160 = '172.16.64.1/30'
        defaultIpleo161 = '172.16.64.2/30'
        defaultIpleo162 = '172.16.64.6/30'
        defaultIpleo163 = '172.16.64.10/30'
        defaultIpleo164 = '172.16.64.14/30'
        defaultIpleo165 = '172.16.64.18/30'
        defaultIpleo166 = '172.16.64.22/30'
        defaultIpleo167 = '172.16.64.26/30'
        defaultIpleo168 = '172.16.64.30/30'
        defaultIpleo169 = '172.16.64.34/30'
        defaultIpleo170 = '172.16.64.38/30'
        defaultIpleo171 = '172.16.64.42/30'
        defaultIpleo172 = '172.16.64.46/30'
        defaultIpleo173 = '172.16.64.50/30'
        defaultIpleo174 = '172.16.64.54/30'
        defaultIpleo175 = '172.16.64.58/30'
        defaultIpleo176 = '172.16.64.62/30'
        defaultIpleo177 = '172.16.64.66/30'
        defaultIpleo178 = '172.16.64.70/30'
        defaultIpleo179 = '172.16.64.74/30'
        defaultIpleo180 = '172.16.64.81/30'
        defaultIpleo181 = '172.16.64.82/30'
        defaultIpleo182 = '172.16.64.86/30'
        defaultIpleo183 = '172.16.64.90/30'
        defaultIpleo184 = '172.16.64.94/30'
        defaultIpleo185 = '172.16.64.98/30'
        defaultIpleo186 = '172.16.64.102/30'
        defaultIpleo187 = '172.16.64.106/30'
        defaultIpleo188 = '172.16.64.110/30'
        defaultIpleo189 = '172.16.64.114/30'
        defaultIpleo190 = '172.16.64.118/30'
        defaultIpleo191 = '172.16.64.122/30'
        defaultIpleo192 = '172.16.64.126/30'
        defaultIpleo193 = '172.16.64.130/30'
        defaultIpleo194 = '172.16.64.134/30'
        defaultIpleo195 = '172.16.64.138/30'
        defaultIpleo196 = '172.16.64.142/30'
        defaultIpleo197 = '172.16.64.146/30'
        defaultIpleo198 = '172.16.64.150/30'
        defaultIpleo199 = '172.16.64.154/30'
        defaultIpleo200 = '172.16.80.1/30'
        defaultIpleo201 = '172.16.80.2/30'
        defaultIpleo202 = '172.16.80.6/30'
        defaultIpleo203 = '172.16.80.10/30'
        defaultIpleo204 = '172.16.80.14/30'
        defaultIpleo205 = '172.16.80.18/30'
        defaultIpleo206 = '172.16.80.22/30'
        defaultIpleo207 = '172.16.80.26/30'
        defaultIpleo208 = '172.16.80.30/30'
        defaultIpleo209 = '172.16.80.34/30'
        defaultIpleo210 = '172.16.80.38/30'
        defaultIpleo211 = '172.16.80.42/30'
        defaultIpleo212 = '172.16.80.46/30'
        defaultIpleo213 = '172.16.80.50/30'
        defaultIpleo214 = '172.16.80.54/30'
        defaultIpleo215 = '172.16.80.58/30'
        defaultIpleo216 = '172.16.80.62/30'
        defaultIpleo217 = '172.16.80.66/30'
        defaultIpleo218 = '172.16.80.70/30'
        defaultIpleo219 = '172.16.80.74/30'
        defaultIpleo220 = '172.16.80.81/30'
        defaultIpleo221 = '172.16.80.82/30'
        defaultIpleo222 = '172.16.80.86/30'
        defaultIpleo223 = '172.16.80.90/30'
        defaultIpleo224 = '172.16.80.94/30'
        defaultIpleo225 = '172.16.80.98/30'
        defaultIpleo226 = '172.16.80.102/30'
        defaultIpleo227 = '172.16.80.106/30'
        defaultIpleo228 = '172.16.80.110/30'
        defaultIpleo229 = '172.16.80.114/30'
        defaultIpleo230 = '172.16.80.118/30'
        defaultIpleo231 = '172.16.80.122/30'
        defaultIpleo232 = '172.16.80.126/30'
        defaultIpleo233 = '172.16.80.130/30'
        defaultIpleo234 = '172.16.80.134/30'
        defaultIpleo235 = '172.16.80.138/30'
        defaultIpleo236 = '172.16.80.142/30'
        defaultIpleo237 = '172.16.80.146/30'
        defaultIpleo238 = '172.16.80.150/30'
        defaultIpleo239 = '172.16.80.154/30'

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
        leo60= self.addNode('leo60', cls=LinuxRouter, ip=defaultIpleo60)
        leo61= self.addNode('leo61', cls=LinuxRouter, ip=defaultIpleo61)
        leo62= self.addNode('leo62', cls=LinuxRouter, ip=defaultIpleo62)
        leo63= self.addNode('leo63', cls=LinuxRouter, ip=defaultIpleo63)
        leo64= self.addNode('leo64', cls=LinuxRouter, ip=defaultIpleo64)
        leo65= self.addNode('leo65', cls=LinuxRouter, ip=defaultIpleo65)
        leo66= self.addNode('leo66', cls=LinuxRouter, ip=defaultIpleo66)
        leo67= self.addNode('leo67', cls=LinuxRouter, ip=defaultIpleo67)
        leo68= self.addNode('leo68', cls=LinuxRouter, ip=defaultIpleo68)
        leo69= self.addNode('leo69', cls=LinuxRouter, ip=defaultIpleo69)
        leo70= self.addNode('leo70', cls=LinuxRouter, ip=defaultIpleo70)
        leo71= self.addNode('leo71', cls=LinuxRouter, ip=defaultIpleo71)
        leo72= self.addNode('leo72', cls=LinuxRouter, ip=defaultIpleo72)
        leo73= self.addNode('leo73', cls=LinuxRouter, ip=defaultIpleo73)
        leo74= self.addNode('leo74', cls=LinuxRouter, ip=defaultIpleo74)
        leo75= self.addNode('leo75', cls=LinuxRouter, ip=defaultIpleo75)
        leo76= self.addNode('leo76', cls=LinuxRouter, ip=defaultIpleo76)
        leo77= self.addNode('leo77', cls=LinuxRouter, ip=defaultIpleo77)
        leo78= self.addNode('leo78', cls=LinuxRouter, ip=defaultIpleo78)
        leo79= self.addNode('leo79', cls=LinuxRouter, ip=defaultIpleo79)
        leo80= self.addNode('leo80', cls=LinuxRouter, ip=defaultIpleo80)
        leo81= self.addNode('leo81', cls=LinuxRouter, ip=defaultIpleo81)
        leo82= self.addNode('leo82', cls=LinuxRouter, ip=defaultIpleo82)
        leo83= self.addNode('leo83', cls=LinuxRouter, ip=defaultIpleo83)
        leo84= self.addNode('leo84', cls=LinuxRouter, ip=defaultIpleo84)
        leo85= self.addNode('leo85', cls=LinuxRouter, ip=defaultIpleo85)
        leo86= self.addNode('leo86', cls=LinuxRouter, ip=defaultIpleo86)
        leo87= self.addNode('leo87', cls=LinuxRouter, ip=defaultIpleo87)
        leo88= self.addNode('leo88', cls=LinuxRouter, ip=defaultIpleo88)
        leo89= self.addNode('leo89', cls=LinuxRouter, ip=defaultIpleo89)
        leo90= self.addNode('leo90', cls=LinuxRouter, ip=defaultIpleo90)
        leo91= self.addNode('leo91', cls=LinuxRouter, ip=defaultIpleo91)
        leo92= self.addNode('leo92', cls=LinuxRouter, ip=defaultIpleo92)
        leo93= self.addNode('leo93', cls=LinuxRouter, ip=defaultIpleo93)
        leo94= self.addNode('leo94', cls=LinuxRouter, ip=defaultIpleo94)
        leo95= self.addNode('leo95', cls=LinuxRouter, ip=defaultIpleo95)
        leo96= self.addNode('leo96', cls=LinuxRouter, ip=defaultIpleo96)
        leo97= self.addNode('leo97', cls=LinuxRouter, ip=defaultIpleo97)
        leo98= self.addNode('leo98', cls=LinuxRouter, ip=defaultIpleo98)
        leo99= self.addNode('leo99', cls=LinuxRouter, ip=defaultIpleo99)
        leo100= self.addNode('leo100', cls=LinuxRouter, ip=defaultIpleo100)
        leo101= self.addNode('leo101', cls=LinuxRouter, ip=defaultIpleo101)
        leo102= self.addNode('leo102', cls=LinuxRouter, ip=defaultIpleo102)
        leo103= self.addNode('leo103', cls=LinuxRouter, ip=defaultIpleo103)
        leo104= self.addNode('leo104', cls=LinuxRouter, ip=defaultIpleo104)
        leo105= self.addNode('leo105', cls=LinuxRouter, ip=defaultIpleo105)
        leo106= self.addNode('leo106', cls=LinuxRouter, ip=defaultIpleo106)
        leo107= self.addNode('leo107', cls=LinuxRouter, ip=defaultIpleo107)
        leo108= self.addNode('leo108', cls=LinuxRouter, ip=defaultIpleo108)
        leo109= self.addNode('leo109', cls=LinuxRouter, ip=defaultIpleo109)
        leo110= self.addNode('leo110', cls=LinuxRouter, ip=defaultIpleo110)
        leo111= self.addNode('leo111', cls=LinuxRouter, ip=defaultIpleo111)
        leo112= self.addNode('leo112', cls=LinuxRouter, ip=defaultIpleo112)
        leo113= self.addNode('leo113', cls=LinuxRouter, ip=defaultIpleo113)
        leo114= self.addNode('leo114', cls=LinuxRouter, ip=defaultIpleo114)
        leo115= self.addNode('leo115', cls=LinuxRouter, ip=defaultIpleo115)
        leo116= self.addNode('leo116', cls=LinuxRouter, ip=defaultIpleo116)
        leo117= self.addNode('leo117', cls=LinuxRouter, ip=defaultIpleo117)
        leo118= self.addNode('leo118', cls=LinuxRouter, ip=defaultIpleo118)
        leo119= self.addNode('leo119', cls=LinuxRouter, ip=defaultIpleo119)
        leo120= self.addNode('leo120', cls=LinuxRouter, ip=defaultIpleo120)
        leo121= self.addNode('leo121', cls=LinuxRouter, ip=defaultIpleo121)
        leo122= self.addNode('leo122', cls=LinuxRouter, ip=defaultIpleo122)
        leo123= self.addNode('leo123', cls=LinuxRouter, ip=defaultIpleo123)
        leo124= self.addNode('leo124', cls=LinuxRouter, ip=defaultIpleo124)
        leo125= self.addNode('leo125', cls=LinuxRouter, ip=defaultIpleo125)
        leo126= self.addNode('leo126', cls=LinuxRouter, ip=defaultIpleo126)
        leo127= self.addNode('leo127', cls=LinuxRouter, ip=defaultIpleo127)
        leo128= self.addNode('leo128', cls=LinuxRouter, ip=defaultIpleo128)
        leo129= self.addNode('leo129', cls=LinuxRouter, ip=defaultIpleo129)
        leo130= self.addNode('leo130', cls=LinuxRouter, ip=defaultIpleo130)
        leo131= self.addNode('leo131', cls=LinuxRouter, ip=defaultIpleo131)
        leo132= self.addNode('leo132', cls=LinuxRouter, ip=defaultIpleo132)
        leo133= self.addNode('leo133', cls=LinuxRouter, ip=defaultIpleo133)
        leo134= self.addNode('leo134', cls=LinuxRouter, ip=defaultIpleo134)
        leo135= self.addNode('leo135', cls=LinuxRouter, ip=defaultIpleo135)
        leo136= self.addNode('leo136', cls=LinuxRouter, ip=defaultIpleo136)
        leo137= self.addNode('leo137', cls=LinuxRouter, ip=defaultIpleo137)
        leo138= self.addNode('leo138', cls=LinuxRouter, ip=defaultIpleo138)
        leo139= self.addNode('leo139', cls=LinuxRouter, ip=defaultIpleo139)
        leo140= self.addNode('leo140', cls=LinuxRouter, ip=defaultIpleo140)
        leo141= self.addNode('leo141', cls=LinuxRouter, ip=defaultIpleo141)
        leo142= self.addNode('leo142', cls=LinuxRouter, ip=defaultIpleo142)
        leo143= self.addNode('leo143', cls=LinuxRouter, ip=defaultIpleo143)
        leo144= self.addNode('leo144', cls=LinuxRouter, ip=defaultIpleo144)
        leo145= self.addNode('leo145', cls=LinuxRouter, ip=defaultIpleo145)
        leo146= self.addNode('leo146', cls=LinuxRouter, ip=defaultIpleo146)
        leo147= self.addNode('leo147', cls=LinuxRouter, ip=defaultIpleo147)
        leo148= self.addNode('leo148', cls=LinuxRouter, ip=defaultIpleo148)
        leo149= self.addNode('leo149', cls=LinuxRouter, ip=defaultIpleo149)
        leo150= self.addNode('leo150', cls=LinuxRouter, ip=defaultIpleo150)
        leo151= self.addNode('leo151', cls=LinuxRouter, ip=defaultIpleo151)
        leo152= self.addNode('leo152', cls=LinuxRouter, ip=defaultIpleo152)
        leo153= self.addNode('leo153', cls=LinuxRouter, ip=defaultIpleo153)
        leo154= self.addNode('leo154', cls=LinuxRouter, ip=defaultIpleo154)
        leo155= self.addNode('leo155', cls=LinuxRouter, ip=defaultIpleo155)
        leo156= self.addNode('leo156', cls=LinuxRouter, ip=defaultIpleo156)
        leo157= self.addNode('leo157', cls=LinuxRouter, ip=defaultIpleo157)
        leo158= self.addNode('leo158', cls=LinuxRouter, ip=defaultIpleo158)
        leo159= self.addNode('leo159', cls=LinuxRouter, ip=defaultIpleo159)
        leo160= self.addNode('leo160', cls=LinuxRouter, ip=defaultIpleo160)
        leo161= self.addNode('leo161', cls=LinuxRouter, ip=defaultIpleo161)
        leo162= self.addNode('leo162', cls=LinuxRouter, ip=defaultIpleo162)
        leo163= self.addNode('leo163', cls=LinuxRouter, ip=defaultIpleo163)
        leo164= self.addNode('leo164', cls=LinuxRouter, ip=defaultIpleo164)
        leo165= self.addNode('leo165', cls=LinuxRouter, ip=defaultIpleo165)
        leo166= self.addNode('leo166', cls=LinuxRouter, ip=defaultIpleo166)
        leo167= self.addNode('leo167', cls=LinuxRouter, ip=defaultIpleo167)
        leo168= self.addNode('leo168', cls=LinuxRouter, ip=defaultIpleo168)
        leo169= self.addNode('leo169', cls=LinuxRouter, ip=defaultIpleo169)
        leo170= self.addNode('leo170', cls=LinuxRouter, ip=defaultIpleo170)
        leo171= self.addNode('leo171', cls=LinuxRouter, ip=defaultIpleo171)
        leo172= self.addNode('leo172', cls=LinuxRouter, ip=defaultIpleo172)
        leo173= self.addNode('leo173', cls=LinuxRouter, ip=defaultIpleo173)
        leo174= self.addNode('leo174', cls=LinuxRouter, ip=defaultIpleo174)
        leo175= self.addNode('leo175', cls=LinuxRouter, ip=defaultIpleo175)
        leo176= self.addNode('leo176', cls=LinuxRouter, ip=defaultIpleo176)
        leo177= self.addNode('leo177', cls=LinuxRouter, ip=defaultIpleo177)
        leo178= self.addNode('leo178', cls=LinuxRouter, ip=defaultIpleo178)
        leo179= self.addNode('leo179', cls=LinuxRouter, ip=defaultIpleo179)
        leo180= self.addNode('leo180', cls=LinuxRouter, ip=defaultIpleo180)
        leo181= self.addNode('leo181', cls=LinuxRouter, ip=defaultIpleo181)
        leo182= self.addNode('leo182', cls=LinuxRouter, ip=defaultIpleo182)
        leo183= self.addNode('leo183', cls=LinuxRouter, ip=defaultIpleo183)
        leo184= self.addNode('leo184', cls=LinuxRouter, ip=defaultIpleo184)
        leo185= self.addNode('leo185', cls=LinuxRouter, ip=defaultIpleo185)
        leo186= self.addNode('leo186', cls=LinuxRouter, ip=defaultIpleo186)
        leo187= self.addNode('leo187', cls=LinuxRouter, ip=defaultIpleo187)
        leo188= self.addNode('leo188', cls=LinuxRouter, ip=defaultIpleo188)
        leo189= self.addNode('leo189', cls=LinuxRouter, ip=defaultIpleo189)
        leo190= self.addNode('leo190', cls=LinuxRouter, ip=defaultIpleo190)
        leo191= self.addNode('leo191', cls=LinuxRouter, ip=defaultIpleo191)
        leo192= self.addNode('leo192', cls=LinuxRouter, ip=defaultIpleo192)
        leo193= self.addNode('leo193', cls=LinuxRouter, ip=defaultIpleo193)
        leo194= self.addNode('leo194', cls=LinuxRouter, ip=defaultIpleo194)
        leo195= self.addNode('leo195', cls=LinuxRouter, ip=defaultIpleo195)
        leo196= self.addNode('leo196', cls=LinuxRouter, ip=defaultIpleo196)
        leo197= self.addNode('leo197', cls=LinuxRouter, ip=defaultIpleo197)
        leo198= self.addNode('leo198', cls=LinuxRouter, ip=defaultIpleo198)
        leo199= self.addNode('leo199', cls=LinuxRouter, ip=defaultIpleo199)
        leo200= self.addNode('leo200', cls=LinuxRouter, ip=defaultIpleo200)
        leo201= self.addNode('leo201', cls=LinuxRouter, ip=defaultIpleo201)
        leo202= self.addNode('leo202', cls=LinuxRouter, ip=defaultIpleo202)
        leo203= self.addNode('leo203', cls=LinuxRouter, ip=defaultIpleo203)
        leo204= self.addNode('leo204', cls=LinuxRouter, ip=defaultIpleo204)
        leo205= self.addNode('leo205', cls=LinuxRouter, ip=defaultIpleo205)
        leo206= self.addNode('leo206', cls=LinuxRouter, ip=defaultIpleo206)
        leo207= self.addNode('leo207', cls=LinuxRouter, ip=defaultIpleo207)
        leo208= self.addNode('leo208', cls=LinuxRouter, ip=defaultIpleo208)
        leo209= self.addNode('leo209', cls=LinuxRouter, ip=defaultIpleo209)
        leo210= self.addNode('leo210', cls=LinuxRouter, ip=defaultIpleo210)
        leo211= self.addNode('leo211', cls=LinuxRouter, ip=defaultIpleo211)
        leo212= self.addNode('leo212', cls=LinuxRouter, ip=defaultIpleo212)
        leo213= self.addNode('leo213', cls=LinuxRouter, ip=defaultIpleo213)
        leo214= self.addNode('leo214', cls=LinuxRouter, ip=defaultIpleo214)
        leo215= self.addNode('leo215', cls=LinuxRouter, ip=defaultIpleo215)
        leo216= self.addNode('leo216', cls=LinuxRouter, ip=defaultIpleo216)
        leo217= self.addNode('leo217', cls=LinuxRouter, ip=defaultIpleo217)
        leo218= self.addNode('leo218', cls=LinuxRouter, ip=defaultIpleo218)
        leo219= self.addNode('leo219', cls=LinuxRouter, ip=defaultIpleo219)
        leo220= self.addNode('leo220', cls=LinuxRouter, ip=defaultIpleo220)
        leo221= self.addNode('leo221', cls=LinuxRouter, ip=defaultIpleo221)
        leo222= self.addNode('leo222', cls=LinuxRouter, ip=defaultIpleo222)
        leo223= self.addNode('leo223', cls=LinuxRouter, ip=defaultIpleo223)
        leo224= self.addNode('leo224', cls=LinuxRouter, ip=defaultIpleo224)
        leo225= self.addNode('leo225', cls=LinuxRouter, ip=defaultIpleo225)
        leo226= self.addNode('leo226', cls=LinuxRouter, ip=defaultIpleo226)
        leo227= self.addNode('leo227', cls=LinuxRouter, ip=defaultIpleo227)
        leo228= self.addNode('leo228', cls=LinuxRouter, ip=defaultIpleo228)
        leo229= self.addNode('leo229', cls=LinuxRouter, ip=defaultIpleo229)
        leo230= self.addNode('leo230', cls=LinuxRouter, ip=defaultIpleo230)
        leo231= self.addNode('leo231', cls=LinuxRouter, ip=defaultIpleo231)
        leo232= self.addNode('leo232', cls=LinuxRouter, ip=defaultIpleo232)
        leo233= self.addNode('leo233', cls=LinuxRouter, ip=defaultIpleo233)
        leo234= self.addNode('leo234', cls=LinuxRouter, ip=defaultIpleo234)
        leo235= self.addNode('leo235', cls=LinuxRouter, ip=defaultIpleo235)
        leo236= self.addNode('leo236', cls=LinuxRouter, ip=defaultIpleo236)
        leo237= self.addNode('leo237', cls=LinuxRouter, ip=defaultIpleo237)
        leo238= self.addNode('leo238', cls=LinuxRouter, ip=defaultIpleo238)
        leo239= self.addNode('leo239', cls=LinuxRouter, ip=defaultIpleo239)
        s1=self.addSwitch('s1')

        self.addLink(leo0,leo1,infName1='leo0-eth0',params1={'ip':'172.16.0.1/30'},infName2='leo1-eth0',params2={'ip':'172.16.0.2/30'})
        self.addLink(leo1,leo2,infName1='leo1-eth1',params1={'ip':'172.16.0.5/30'},infName2='leo2-eth0',params2={'ip':'172.16.0.6/30'})
        self.addLink(leo2,leo3,infName1='leo2-eth1',params1={'ip':'172.16.0.9/30'},infName2='leo3-eth0',params2={'ip':'172.16.0.10/30'})
        self.addLink(leo3,leo4,infName1='leo3-eth1',params1={'ip':'172.16.0.13/30'},infName2='leo4-eth0',params2={'ip':'172.16.0.14/30'})
        self.addLink(leo4,leo5,infName1='leo4-eth1',params1={'ip':'172.16.0.17/30'},infName2='leo5-eth0',params2={'ip':'172.16.0.18/30'})
        self.addLink(leo5,leo6,infName1='leo5-eth1',params1={'ip':'172.16.0.21/30'},infName2='leo6-eth0',params2={'ip':'172.16.0.22/30'})
        self.addLink(leo6,leo7,infName1='leo6-eth1',params1={'ip':'172.16.0.25/30'},infName2='leo7-eth0',params2={'ip':'172.16.0.26/30'})
        self.addLink(leo7,leo8,infName1='leo7-eth1',params1={'ip':'172.16.0.29/30'},infName2='leo8-eth0',params2={'ip':'172.16.0.30/30'})
        self.addLink(leo8,leo9,infName1='leo8-eth1',params1={'ip':'172.16.0.33/30'},infName2='leo9-eth0',params2={'ip':'172.16.0.34/30'})
        self.addLink(leo9,leo10,infName1='leo9-eth1',params1={'ip':'172.16.0.37/30'},infName2='leo10-eth0',params2={'ip':'172.16.0.38/30'})
        self.addLink(leo10,leo11,infName1='leo10-eth1',params1={'ip':'172.16.0.41/30'},infName2='leo11-eth0',params2={'ip':'172.16.0.42/30'})
        self.addLink(leo11,leo12,infName1='leo11-eth1',params1={'ip':'172.16.0.45/30'},infName2='leo12-eth0',params2={'ip':'172.16.0.46/30'})
        self.addLink(leo12,leo13,infName1='leo12-eth1',params1={'ip':'172.16.0.49/30'},infName2='leo13-eth0',params2={'ip':'172.16.0.50/30'})
        self.addLink(leo13,leo14,infName1='leo13-eth1',params1={'ip':'172.16.0.53/30'},infName2='leo14-eth0',params2={'ip':'172.16.0.54/30'})
        self.addLink(leo14,leo15,infName1='leo14-eth1',params1={'ip':'172.16.0.57/30'},infName2='leo15-eth0',params2={'ip':'172.16.0.58/30'})
        self.addLink(leo15,leo16,infName1='leo15-eth1',params1={'ip':'172.16.0.61/30'},infName2='leo16-eth0',params2={'ip':'172.16.0.62/30'})
        self.addLink(leo16,leo17,infName1='leo16-eth1',params1={'ip':'172.16.0.65/30'},infName2='leo17-eth0',params2={'ip':'172.16.0.66/30'})
        self.addLink(leo17,leo18,infName1='leo17-eth1',params1={'ip':'172.16.0.69/30'},infName2='leo18-eth0',params2={'ip':'172.16.0.70/30'})
        self.addLink(leo18,leo19,infName1='leo18-eth1',params1={'ip':'172.16.0.73/30'},infName2='leo19-eth0',params2={'ip':'172.16.0.74/30'})
        self.addLink(leo19,leo0,infName1='leo19-eth1',params1={'ip':'172.16.0.77/30'},infName2='leo0-eth1',params2={'ip':'172.16.0.78/30'})
        self.addLink(leo20,leo21,infName1='leo20-eth0',params1={'ip':'172.16.0.81/30'},infName2='leo21-eth0',params2={'ip':'172.16.0.82/30'})
        self.addLink(leo21,leo22,infName1='leo21-eth1',params1={'ip':'172.16.0.85/30'},infName2='leo22-eth0',params2={'ip':'172.16.0.86/30'})
        self.addLink(leo22,leo23,infName1='leo22-eth1',params1={'ip':'172.16.0.89/30'},infName2='leo23-eth0',params2={'ip':'172.16.0.90/30'})
        self.addLink(leo23,leo24,infName1='leo23-eth1',params1={'ip':'172.16.0.93/30'},infName2='leo24-eth0',params2={'ip':'172.16.0.94/30'})
        self.addLink(leo24,leo25,infName1='leo24-eth1',params1={'ip':'172.16.0.97/30'},infName2='leo25-eth0',params2={'ip':'172.16.0.98/30'})
        self.addLink(leo25,leo26,infName1='leo25-eth1',params1={'ip':'172.16.0.101/30'},infName2='leo26-eth0',params2={'ip':'172.16.0.102/30'})
        self.addLink(leo26,leo27,infName1='leo26-eth1',params1={'ip':'172.16.0.105/30'},infName2='leo27-eth0',params2={'ip':'172.16.0.106/30'})
        self.addLink(leo27,leo28,infName1='leo27-eth1',params1={'ip':'172.16.0.109/30'},infName2='leo28-eth0',params2={'ip':'172.16.0.110/30'})
        self.addLink(leo28,leo29,infName1='leo28-eth1',params1={'ip':'172.16.0.113/30'},infName2='leo29-eth0',params2={'ip':'172.16.0.114/30'})
        self.addLink(leo29,leo30,infName1='leo29-eth1',params1={'ip':'172.16.0.117/30'},infName2='leo30-eth0',params2={'ip':'172.16.0.118/30'})
        self.addLink(leo30,leo31,infName1='leo30-eth1',params1={'ip':'172.16.0.121/30'},infName2='leo31-eth0',params2={'ip':'172.16.0.122/30'})
        self.addLink(leo31,leo32,infName1='leo31-eth1',params1={'ip':'172.16.0.125/30'},infName2='leo32-eth0',params2={'ip':'172.16.0.126/30'})
        self.addLink(leo32,leo33,infName1='leo32-eth1',params1={'ip':'172.16.0.129/30'},infName2='leo33-eth0',params2={'ip':'172.16.0.130/30'})
        self.addLink(leo33,leo34,infName1='leo33-eth1',params1={'ip':'172.16.0.133/30'},infName2='leo34-eth0',params2={'ip':'172.16.0.134/30'})
        self.addLink(leo34,leo35,infName1='leo34-eth1',params1={'ip':'172.16.0.137/30'},infName2='leo35-eth0',params2={'ip':'172.16.0.138/30'})
        self.addLink(leo35,leo36,infName1='leo35-eth1',params1={'ip':'172.16.0.141/30'},infName2='leo36-eth0',params2={'ip':'172.16.0.142/30'})
        self.addLink(leo36,leo37,infName1='leo36-eth1',params1={'ip':'172.16.0.145/30'},infName2='leo37-eth0',params2={'ip':'172.16.0.146/30'})
        self.addLink(leo37,leo38,infName1='leo37-eth1',params1={'ip':'172.16.0.149/30'},infName2='leo38-eth0',params2={'ip':'172.16.0.150/30'})
        self.addLink(leo38,leo39,infName1='leo38-eth1',params1={'ip':'172.16.0.153/30'},infName2='leo39-eth0',params2={'ip':'172.16.0.154/30'})
        self.addLink(leo39,leo20,infName1='leo39-eth1',params1={'ip':'172.16.0.157/30'},infName2='leo20-eth1',params2={'ip':'172.16.0.158/30'})
        self.addLink(leo0,leo20,infName1='leo0-eth2',params1={'ip':'172.16.0.161/30'},infName2='leo20-eth2',params2={'ip':'172.16.0.162/30'})
        self.addLink(leo1,leo21,infName1='leo1-eth2',params1={'ip':'172.16.0.165/30'},infName2='leo21-eth2',params2={'ip':'172.16.0.166/30'})
        self.addLink(leo2,leo22,infName1='leo2-eth2',params1={'ip':'172.16.0.169/30'},infName2='leo22-eth2',params2={'ip':'172.16.0.170/30'})
        self.addLink(leo3,leo23,infName1='leo3-eth2',params1={'ip':'172.16.0.173/30'},infName2='leo23-eth2',params2={'ip':'172.16.0.174/30'})
        self.addLink(leo4,leo24,infName1='leo4-eth2',params1={'ip':'172.16.0.177/30'},infName2='leo24-eth2',params2={'ip':'172.16.0.178/30'})
        self.addLink(leo5,leo25,infName1='leo5-eth2',params1={'ip':'172.16.0.181/30'},infName2='leo25-eth2',params2={'ip':'172.16.0.182/30'})
        self.addLink(leo6,leo26,infName1='leo6-eth2',params1={'ip':'172.16.0.185/30'},infName2='leo26-eth2',params2={'ip':'172.16.0.186/30'})
        self.addLink(leo7,leo27,infName1='leo7-eth2',params1={'ip':'172.16.0.189/30'},infName2='leo27-eth2',params2={'ip':'172.16.0.190/30'})
        self.addLink(leo8,leo28,infName1='leo8-eth2',params1={'ip':'172.16.0.193/30'},infName2='leo28-eth2',params2={'ip':'172.16.0.194/30'})
        self.addLink(leo9,leo29,infName1='leo9-eth2',params1={'ip':'172.16.0.197/30'},infName2='leo29-eth2',params2={'ip':'172.16.0.198/30'})
        self.addLink(leo10,leo30,infName1='leo10-eth2',params1={'ip':'172.16.0.201/30'},infName2='leo30-eth2',params2={'ip':'172.16.0.202/30'})
        self.addLink(leo11,leo31,infName1='leo11-eth2',params1={'ip':'172.16.0.205/30'},infName2='leo31-eth2',params2={'ip':'172.16.0.206/30'})
        self.addLink(leo12,leo32,infName1='leo12-eth2',params1={'ip':'172.16.0.209/30'},infName2='leo32-eth2',params2={'ip':'172.16.0.210/30'})
        self.addLink(leo13,leo33,infName1='leo13-eth2',params1={'ip':'172.16.0.213/30'},infName2='leo33-eth2',params2={'ip':'172.16.0.214/30'})
        self.addLink(leo14,leo34,infName1='leo14-eth2',params1={'ip':'172.16.0.217/30'},infName2='leo34-eth2',params2={'ip':'172.16.0.218/30'})
        self.addLink(leo15,leo35,infName1='leo15-eth2',params1={'ip':'172.16.0.221/30'},infName2='leo35-eth2',params2={'ip':'172.16.0.222/30'})
        self.addLink(leo16,leo36,infName1='leo16-eth2',params1={'ip':'172.16.0.225/30'},infName2='leo36-eth2',params2={'ip':'172.16.0.226/30'})
        self.addLink(leo17,leo37,infName1='leo17-eth2',params1={'ip':'172.16.0.229/30'},infName2='leo37-eth2',params2={'ip':'172.16.0.230/30'})
        self.addLink(leo18,leo38,infName1='leo18-eth2',params1={'ip':'172.16.0.233/30'},infName2='leo38-eth2',params2={'ip':'172.16.0.234/30'})
        self.addLink(leo19,leo39,infName1='leo19-eth2',params1={'ip':'172.16.0.237/30'},infName2='leo39-eth2',params2={'ip':'172.16.0.238/30'})
        self.addLink(leo40,leo41,infName1='leo40-eth0',params1={'ip':'172.16.16.1/30'},infName2='leo41-eth0',params2={'ip':'172.16.16.2/30'})
        self.addLink(leo41,leo42,infName1='leo41-eth1',params1={'ip':'172.16.16.5/30'},infName2='leo42-eth0',params2={'ip':'172.16.16.6/30'})
        self.addLink(leo42,leo43,infName1='leo42-eth1',params1={'ip':'172.16.16.9/30'},infName2='leo43-eth0',params2={'ip':'172.16.16.10/30'})
        self.addLink(leo43,leo44,infName1='leo43-eth1',params1={'ip':'172.16.16.13/30'},infName2='leo44-eth0',params2={'ip':'172.16.16.14/30'})
        self.addLink(leo44,leo45,infName1='leo44-eth1',params1={'ip':'172.16.16.17/30'},infName2='leo45-eth0',params2={'ip':'172.16.16.18/30'})
        self.addLink(leo45,leo46,infName1='leo45-eth1',params1={'ip':'172.16.16.21/30'},infName2='leo46-eth0',params2={'ip':'172.16.16.22/30'})
        self.addLink(leo46,leo47,infName1='leo46-eth1',params1={'ip':'172.16.16.25/30'},infName2='leo47-eth0',params2={'ip':'172.16.16.26/30'})
        self.addLink(leo47,leo48,infName1='leo47-eth1',params1={'ip':'172.16.16.29/30'},infName2='leo48-eth0',params2={'ip':'172.16.16.30/30'})
        self.addLink(leo48,leo49,infName1='leo48-eth1',params1={'ip':'172.16.16.33/30'},infName2='leo49-eth0',params2={'ip':'172.16.16.34/30'})
        self.addLink(leo49,leo50,infName1='leo49-eth1',params1={'ip':'172.16.16.37/30'},infName2='leo50-eth0',params2={'ip':'172.16.16.38/30'})
        self.addLink(leo50,leo51,infName1='leo50-eth1',params1={'ip':'172.16.16.41/30'},infName2='leo51-eth0',params2={'ip':'172.16.16.42/30'})
        self.addLink(leo51,leo52,infName1='leo51-eth1',params1={'ip':'172.16.16.45/30'},infName2='leo52-eth0',params2={'ip':'172.16.16.46/30'})
        self.addLink(leo52,leo53,infName1='leo52-eth1',params1={'ip':'172.16.16.49/30'},infName2='leo53-eth0',params2={'ip':'172.16.16.50/30'})
        self.addLink(leo53,leo54,infName1='leo53-eth1',params1={'ip':'172.16.16.53/30'},infName2='leo54-eth0',params2={'ip':'172.16.16.54/30'})
        self.addLink(leo54,leo55,infName1='leo54-eth1',params1={'ip':'172.16.16.57/30'},infName2='leo55-eth0',params2={'ip':'172.16.16.58/30'})
        self.addLink(leo55,leo56,infName1='leo55-eth1',params1={'ip':'172.16.16.61/30'},infName2='leo56-eth0',params2={'ip':'172.16.16.62/30'})
        self.addLink(leo56,leo57,infName1='leo56-eth1',params1={'ip':'172.16.16.65/30'},infName2='leo57-eth0',params2={'ip':'172.16.16.66/30'})
        self.addLink(leo57,leo58,infName1='leo57-eth1',params1={'ip':'172.16.16.69/30'},infName2='leo58-eth0',params2={'ip':'172.16.16.70/30'})
        self.addLink(leo58,leo59,infName1='leo58-eth1',params1={'ip':'172.16.16.73/30'},infName2='leo59-eth0',params2={'ip':'172.16.16.74/30'})
        self.addLink(leo59,leo40,infName1='leo59-eth1',params1={'ip':'172.16.16.77/30'},infName2='leo40-eth1',params2={'ip':'172.16.16.78/30'})
        self.addLink(leo60,leo61,infName1='leo60-eth0',params1={'ip':'172.16.16.81/30'},infName2='leo61-eth0',params2={'ip':'172.16.16.82/30'})
        self.addLink(leo61,leo62,infName1='leo61-eth1',params1={'ip':'172.16.16.85/30'},infName2='leo62-eth0',params2={'ip':'172.16.16.86/30'})
        self.addLink(leo62,leo63,infName1='leo62-eth1',params1={'ip':'172.16.16.89/30'},infName2='leo63-eth0',params2={'ip':'172.16.16.90/30'})
        self.addLink(leo63,leo64,infName1='leo63-eth1',params1={'ip':'172.16.16.93/30'},infName2='leo64-eth0',params2={'ip':'172.16.16.94/30'})
        self.addLink(leo64,leo65,infName1='leo64-eth1',params1={'ip':'172.16.16.97/30'},infName2='leo65-eth0',params2={'ip':'172.16.16.98/30'})
        self.addLink(leo65,leo66,infName1='leo65-eth1',params1={'ip':'172.16.16.101/30'},infName2='leo66-eth0',params2={'ip':'172.16.16.102/30'})
        self.addLink(leo66,leo67,infName1='leo66-eth1',params1={'ip':'172.16.16.105/30'},infName2='leo67-eth0',params2={'ip':'172.16.16.106/30'})
        self.addLink(leo67,leo68,infName1='leo67-eth1',params1={'ip':'172.16.16.109/30'},infName2='leo68-eth0',params2={'ip':'172.16.16.110/30'})
        self.addLink(leo68,leo69,infName1='leo68-eth1',params1={'ip':'172.16.16.113/30'},infName2='leo69-eth0',params2={'ip':'172.16.16.114/30'})
        self.addLink(leo69,leo70,infName1='leo69-eth1',params1={'ip':'172.16.16.117/30'},infName2='leo70-eth0',params2={'ip':'172.16.16.118/30'})
        self.addLink(leo70,leo71,infName1='leo70-eth1',params1={'ip':'172.16.16.121/30'},infName2='leo71-eth0',params2={'ip':'172.16.16.122/30'})
        self.addLink(leo71,leo72,infName1='leo71-eth1',params1={'ip':'172.16.16.125/30'},infName2='leo72-eth0',params2={'ip':'172.16.16.126/30'})
        self.addLink(leo72,leo73,infName1='leo72-eth1',params1={'ip':'172.16.16.129/30'},infName2='leo73-eth0',params2={'ip':'172.16.16.130/30'})
        self.addLink(leo73,leo74,infName1='leo73-eth1',params1={'ip':'172.16.16.133/30'},infName2='leo74-eth0',params2={'ip':'172.16.16.134/30'})
        self.addLink(leo74,leo75,infName1='leo74-eth1',params1={'ip':'172.16.16.137/30'},infName2='leo75-eth0',params2={'ip':'172.16.16.138/30'})
        self.addLink(leo75,leo76,infName1='leo75-eth1',params1={'ip':'172.16.16.141/30'},infName2='leo76-eth0',params2={'ip':'172.16.16.142/30'})
        self.addLink(leo76,leo77,infName1='leo76-eth1',params1={'ip':'172.16.16.145/30'},infName2='leo77-eth0',params2={'ip':'172.16.16.146/30'})
        self.addLink(leo77,leo78,infName1='leo77-eth1',params1={'ip':'172.16.16.149/30'},infName2='leo78-eth0',params2={'ip':'172.16.16.150/30'})
        self.addLink(leo78,leo79,infName1='leo78-eth1',params1={'ip':'172.16.16.153/30'},infName2='leo79-eth0',params2={'ip':'172.16.16.154/30'})
        self.addLink(leo79,leo60,infName1='leo79-eth1',params1={'ip':'172.16.16.157/30'},infName2='leo60-eth1',params2={'ip':'172.16.16.158/30'})
        self.addLink(leo40,leo60,infName1='leo40-eth2',params1={'ip':'172.16.16.161/30'},infName2='leo60-eth2',params2={'ip':'172.16.16.162/30'})
        self.addLink(leo41,leo61,infName1='leo41-eth2',params1={'ip':'172.16.16.165/30'},infName2='leo61-eth2',params2={'ip':'172.16.16.166/30'})
        self.addLink(leo42,leo62,infName1='leo42-eth2',params1={'ip':'172.16.16.169/30'},infName2='leo62-eth2',params2={'ip':'172.16.16.170/30'})
        self.addLink(leo43,leo63,infName1='leo43-eth2',params1={'ip':'172.16.16.173/30'},infName2='leo63-eth2',params2={'ip':'172.16.16.174/30'})
        self.addLink(leo44,leo64,infName1='leo44-eth2',params1={'ip':'172.16.16.177/30'},infName2='leo64-eth2',params2={'ip':'172.16.16.178/30'})
        self.addLink(leo45,leo65,infName1='leo45-eth2',params1={'ip':'172.16.16.181/30'},infName2='leo65-eth2',params2={'ip':'172.16.16.182/30'})
        self.addLink(leo46,leo66,infName1='leo46-eth2',params1={'ip':'172.16.16.185/30'},infName2='leo66-eth2',params2={'ip':'172.16.16.186/30'})
        self.addLink(leo47,leo67,infName1='leo47-eth2',params1={'ip':'172.16.16.189/30'},infName2='leo67-eth2',params2={'ip':'172.16.16.190/30'})
        self.addLink(leo48,leo68,infName1='leo48-eth2',params1={'ip':'172.16.16.193/30'},infName2='leo68-eth2',params2={'ip':'172.16.16.194/30'})
        self.addLink(leo49,leo69,infName1='leo49-eth2',params1={'ip':'172.16.16.197/30'},infName2='leo69-eth2',params2={'ip':'172.16.16.198/30'})
        self.addLink(leo50,leo70,infName1='leo50-eth2',params1={'ip':'172.16.16.201/30'},infName2='leo70-eth2',params2={'ip':'172.16.16.202/30'})
        self.addLink(leo51,leo71,infName1='leo51-eth2',params1={'ip':'172.16.16.205/30'},infName2='leo71-eth2',params2={'ip':'172.16.16.206/30'})
        self.addLink(leo52,leo72,infName1='leo52-eth2',params1={'ip':'172.16.16.209/30'},infName2='leo72-eth2',params2={'ip':'172.16.16.210/30'})
        self.addLink(leo53,leo73,infName1='leo53-eth2',params1={'ip':'172.16.16.213/30'},infName2='leo73-eth2',params2={'ip':'172.16.16.214/30'})
        self.addLink(leo54,leo74,infName1='leo54-eth2',params1={'ip':'172.16.16.217/30'},infName2='leo74-eth2',params2={'ip':'172.16.16.218/30'})
        self.addLink(leo55,leo75,infName1='leo55-eth2',params1={'ip':'172.16.16.221/30'},infName2='leo75-eth2',params2={'ip':'172.16.16.222/30'})
        self.addLink(leo56,leo76,infName1='leo56-eth2',params1={'ip':'172.16.16.225/30'},infName2='leo76-eth2',params2={'ip':'172.16.16.226/30'})
        self.addLink(leo57,leo77,infName1='leo57-eth2',params1={'ip':'172.16.16.229/30'},infName2='leo77-eth2',params2={'ip':'172.16.16.230/30'})
        self.addLink(leo58,leo78,infName1='leo58-eth2',params1={'ip':'172.16.16.233/30'},infName2='leo78-eth2',params2={'ip':'172.16.16.234/30'})
        self.addLink(leo59,leo79,infName1='leo59-eth2',params1={'ip':'172.16.16.237/30'},infName2='leo79-eth2',params2={'ip':'172.16.16.238/30'})
        self.addLink(leo80,leo81,infName1='leo80-eth0',params1={'ip':'172.16.32.1/30'},infName2='leo81-eth0',params2={'ip':'172.16.32.2/30'})
        self.addLink(leo81,leo82,infName1='leo81-eth1',params1={'ip':'172.16.32.5/30'},infName2='leo82-eth0',params2={'ip':'172.16.32.6/30'})
        self.addLink(leo82,leo83,infName1='leo82-eth1',params1={'ip':'172.16.32.9/30'},infName2='leo83-eth0',params2={'ip':'172.16.32.10/30'})
        self.addLink(leo83,leo84,infName1='leo83-eth1',params1={'ip':'172.16.32.13/30'},infName2='leo84-eth0',params2={'ip':'172.16.32.14/30'})
        self.addLink(leo84,leo85,infName1='leo84-eth1',params1={'ip':'172.16.32.17/30'},infName2='leo85-eth0',params2={'ip':'172.16.32.18/30'})
        self.addLink(leo85,leo86,infName1='leo85-eth1',params1={'ip':'172.16.32.21/30'},infName2='leo86-eth0',params2={'ip':'172.16.32.22/30'})
        self.addLink(leo86,leo87,infName1='leo86-eth1',params1={'ip':'172.16.32.25/30'},infName2='leo87-eth0',params2={'ip':'172.16.32.26/30'})
        self.addLink(leo87,leo88,infName1='leo87-eth1',params1={'ip':'172.16.32.29/30'},infName2='leo88-eth0',params2={'ip':'172.16.32.30/30'})
        self.addLink(leo88,leo89,infName1='leo88-eth1',params1={'ip':'172.16.32.33/30'},infName2='leo89-eth0',params2={'ip':'172.16.32.34/30'})
        self.addLink(leo89,leo90,infName1='leo89-eth1',params1={'ip':'172.16.32.37/30'},infName2='leo90-eth0',params2={'ip':'172.16.32.38/30'})
        self.addLink(leo90,leo91,infName1='leo90-eth1',params1={'ip':'172.16.32.41/30'},infName2='leo91-eth0',params2={'ip':'172.16.32.42/30'})
        self.addLink(leo91,leo92,infName1='leo91-eth1',params1={'ip':'172.16.32.45/30'},infName2='leo92-eth0',params2={'ip':'172.16.32.46/30'})
        self.addLink(leo92,leo93,infName1='leo92-eth1',params1={'ip':'172.16.32.49/30'},infName2='leo93-eth0',params2={'ip':'172.16.32.50/30'})
        self.addLink(leo93,leo94,infName1='leo93-eth1',params1={'ip':'172.16.32.53/30'},infName2='leo94-eth0',params2={'ip':'172.16.32.54/30'})
        self.addLink(leo94,leo95,infName1='leo94-eth1',params1={'ip':'172.16.32.57/30'},infName2='leo95-eth0',params2={'ip':'172.16.32.58/30'})
        self.addLink(leo95,leo96,infName1='leo95-eth1',params1={'ip':'172.16.32.61/30'},infName2='leo96-eth0',params2={'ip':'172.16.32.62/30'})
        self.addLink(leo96,leo97,infName1='leo96-eth1',params1={'ip':'172.16.32.65/30'},infName2='leo97-eth0',params2={'ip':'172.16.32.66/30'})
        self.addLink(leo97,leo98,infName1='leo97-eth1',params1={'ip':'172.16.32.69/30'},infName2='leo98-eth0',params2={'ip':'172.16.32.70/30'})
        self.addLink(leo98,leo99,infName1='leo98-eth1',params1={'ip':'172.16.32.73/30'},infName2='leo99-eth0',params2={'ip':'172.16.32.74/30'})
        self.addLink(leo99,leo80,infName1='leo99-eth1',params1={'ip':'172.16.32.77/30'},infName2='leo80-eth1',params2={'ip':'172.16.32.78/30'})
        self.addLink(leo100,leo101,infName1='leo100-eth0',params1={'ip':'172.16.32.81/30'},infName2='leo101-eth0',params2={'ip':'172.16.32.82/30'})
        self.addLink(leo101,leo102,infName1='leo101-eth1',params1={'ip':'172.16.32.85/30'},infName2='leo102-eth0',params2={'ip':'172.16.32.86/30'})
        self.addLink(leo102,leo103,infName1='leo102-eth1',params1={'ip':'172.16.32.89/30'},infName2='leo103-eth0',params2={'ip':'172.16.32.90/30'})
        self.addLink(leo103,leo104,infName1='leo103-eth1',params1={'ip':'172.16.32.93/30'},infName2='leo104-eth0',params2={'ip':'172.16.32.94/30'})
        self.addLink(leo104,leo105,infName1='leo104-eth1',params1={'ip':'172.16.32.97/30'},infName2='leo105-eth0',params2={'ip':'172.16.32.98/30'})
        self.addLink(leo105,leo106,infName1='leo105-eth1',params1={'ip':'172.16.32.101/30'},infName2='leo106-eth0',params2={'ip':'172.16.32.102/30'})
        self.addLink(leo106,leo107,infName1='leo106-eth1',params1={'ip':'172.16.32.105/30'},infName2='leo107-eth0',params2={'ip':'172.16.32.106/30'})
        self.addLink(leo107,leo108,infName1='leo107-eth1',params1={'ip':'172.16.32.109/30'},infName2='leo108-eth0',params2={'ip':'172.16.32.110/30'})
        self.addLink(leo108,leo109,infName1='leo108-eth1',params1={'ip':'172.16.32.113/30'},infName2='leo109-eth0',params2={'ip':'172.16.32.114/30'})
        self.addLink(leo109,leo110,infName1='leo109-eth1',params1={'ip':'172.16.32.117/30'},infName2='leo110-eth0',params2={'ip':'172.16.32.118/30'})
        self.addLink(leo110,leo111,infName1='leo110-eth1',params1={'ip':'172.16.32.121/30'},infName2='leo111-eth0',params2={'ip':'172.16.32.122/30'})
        self.addLink(leo111,leo112,infName1='leo111-eth1',params1={'ip':'172.16.32.125/30'},infName2='leo112-eth0',params2={'ip':'172.16.32.126/30'})
        self.addLink(leo112,leo113,infName1='leo112-eth1',params1={'ip':'172.16.32.129/30'},infName2='leo113-eth0',params2={'ip':'172.16.32.130/30'})
        self.addLink(leo113,leo114,infName1='leo113-eth1',params1={'ip':'172.16.32.133/30'},infName2='leo114-eth0',params2={'ip':'172.16.32.134/30'})
        self.addLink(leo114,leo115,infName1='leo114-eth1',params1={'ip':'172.16.32.137/30'},infName2='leo115-eth0',params2={'ip':'172.16.32.138/30'})
        self.addLink(leo115,leo116,infName1='leo115-eth1',params1={'ip':'172.16.32.141/30'},infName2='leo116-eth0',params2={'ip':'172.16.32.142/30'})
        self.addLink(leo116,leo117,infName1='leo116-eth1',params1={'ip':'172.16.32.145/30'},infName2='leo117-eth0',params2={'ip':'172.16.32.146/30'})
        self.addLink(leo117,leo118,infName1='leo117-eth1',params1={'ip':'172.16.32.149/30'},infName2='leo118-eth0',params2={'ip':'172.16.32.150/30'})
        self.addLink(leo118,leo119,infName1='leo118-eth1',params1={'ip':'172.16.32.153/30'},infName2='leo119-eth0',params2={'ip':'172.16.32.154/30'})
        self.addLink(leo119,leo100,infName1='leo119-eth1',params1={'ip':'172.16.32.157/30'},infName2='leo100-eth1',params2={'ip':'172.16.32.158/30'})
        self.addLink(leo80,leo100,infName1='leo80-eth2',params1={'ip':'172.16.32.161/30'},infName2='leo100-eth2',params2={'ip':'172.16.32.162/30'})
        self.addLink(leo81,leo101,infName1='leo81-eth2',params1={'ip':'172.16.32.165/30'},infName2='leo101-eth2',params2={'ip':'172.16.32.166/30'})
        self.addLink(leo82,leo102,infName1='leo82-eth2',params1={'ip':'172.16.32.169/30'},infName2='leo102-eth2',params2={'ip':'172.16.32.170/30'})
        self.addLink(leo83,leo103,infName1='leo83-eth2',params1={'ip':'172.16.32.173/30'},infName2='leo103-eth2',params2={'ip':'172.16.32.174/30'})
        self.addLink(leo84,leo104,infName1='leo84-eth2',params1={'ip':'172.16.32.177/30'},infName2='leo104-eth2',params2={'ip':'172.16.32.178/30'})
        self.addLink(leo85,leo105,infName1='leo85-eth2',params1={'ip':'172.16.32.181/30'},infName2='leo105-eth2',params2={'ip':'172.16.32.182/30'})
        self.addLink(leo86,leo106,infName1='leo86-eth2',params1={'ip':'172.16.32.185/30'},infName2='leo106-eth2',params2={'ip':'172.16.32.186/30'})
        self.addLink(leo87,leo107,infName1='leo87-eth2',params1={'ip':'172.16.32.189/30'},infName2='leo107-eth2',params2={'ip':'172.16.32.190/30'})
        self.addLink(leo88,leo108,infName1='leo88-eth2',params1={'ip':'172.16.32.193/30'},infName2='leo108-eth2',params2={'ip':'172.16.32.194/30'})
        self.addLink(leo89,leo109,infName1='leo89-eth2',params1={'ip':'172.16.32.197/30'},infName2='leo109-eth2',params2={'ip':'172.16.32.198/30'})
        self.addLink(leo90,leo110,infName1='leo90-eth2',params1={'ip':'172.16.32.201/30'},infName2='leo110-eth2',params2={'ip':'172.16.32.202/30'})
        self.addLink(leo91,leo111,infName1='leo91-eth2',params1={'ip':'172.16.32.205/30'},infName2='leo111-eth2',params2={'ip':'172.16.32.206/30'})
        self.addLink(leo92,leo112,infName1='leo92-eth2',params1={'ip':'172.16.32.209/30'},infName2='leo112-eth2',params2={'ip':'172.16.32.210/30'})
        self.addLink(leo93,leo113,infName1='leo93-eth2',params1={'ip':'172.16.32.213/30'},infName2='leo113-eth2',params2={'ip':'172.16.32.214/30'})
        self.addLink(leo94,leo114,infName1='leo94-eth2',params1={'ip':'172.16.32.217/30'},infName2='leo114-eth2',params2={'ip':'172.16.32.218/30'})
        self.addLink(leo95,leo115,infName1='leo95-eth2',params1={'ip':'172.16.32.221/30'},infName2='leo115-eth2',params2={'ip':'172.16.32.222/30'})
        self.addLink(leo96,leo116,infName1='leo96-eth2',params1={'ip':'172.16.32.225/30'},infName2='leo116-eth2',params2={'ip':'172.16.32.226/30'})
        self.addLink(leo97,leo117,infName1='leo97-eth2',params1={'ip':'172.16.32.229/30'},infName2='leo117-eth2',params2={'ip':'172.16.32.230/30'})
        self.addLink(leo98,leo118,infName1='leo98-eth2',params1={'ip':'172.16.32.233/30'},infName2='leo118-eth2',params2={'ip':'172.16.32.234/30'})
        self.addLink(leo99,leo119,infName1='leo99-eth2',params1={'ip':'172.16.32.237/30'},infName2='leo119-eth2',params2={'ip':'172.16.32.238/30'})
        self.addLink(leo120,leo121,infName1='leo120-eth0',params1={'ip':'172.16.48.1/30'},infName2='leo121-eth0',params2={'ip':'172.16.48.2/30'})
        self.addLink(leo121,leo122,infName1='leo121-eth1',params1={'ip':'172.16.48.5/30'},infName2='leo122-eth0',params2={'ip':'172.16.48.6/30'})
        self.addLink(leo122,leo123,infName1='leo122-eth1',params1={'ip':'172.16.48.9/30'},infName2='leo123-eth0',params2={'ip':'172.16.48.10/30'})
        self.addLink(leo123,leo124,infName1='leo123-eth1',params1={'ip':'172.16.48.13/30'},infName2='leo124-eth0',params2={'ip':'172.16.48.14/30'})
        self.addLink(leo124,leo125,infName1='leo124-eth1',params1={'ip':'172.16.48.17/30'},infName2='leo125-eth0',params2={'ip':'172.16.48.18/30'})
        self.addLink(leo125,leo126,infName1='leo125-eth1',params1={'ip':'172.16.48.21/30'},infName2='leo126-eth0',params2={'ip':'172.16.48.22/30'})
        self.addLink(leo126,leo127,infName1='leo126-eth1',params1={'ip':'172.16.48.25/30'},infName2='leo127-eth0',params2={'ip':'172.16.48.26/30'})
        self.addLink(leo127,leo128,infName1='leo127-eth1',params1={'ip':'172.16.48.29/30'},infName2='leo128-eth0',params2={'ip':'172.16.48.30/30'})
        self.addLink(leo128,leo129,infName1='leo128-eth1',params1={'ip':'172.16.48.33/30'},infName2='leo129-eth0',params2={'ip':'172.16.48.34/30'})
        self.addLink(leo129,leo130,infName1='leo129-eth1',params1={'ip':'172.16.48.37/30'},infName2='leo130-eth0',params2={'ip':'172.16.48.38/30'})
        self.addLink(leo130,leo131,infName1='leo130-eth1',params1={'ip':'172.16.48.41/30'},infName2='leo131-eth0',params2={'ip':'172.16.48.42/30'})
        self.addLink(leo131,leo132,infName1='leo131-eth1',params1={'ip':'172.16.48.45/30'},infName2='leo132-eth0',params2={'ip':'172.16.48.46/30'})
        self.addLink(leo132,leo133,infName1='leo132-eth1',params1={'ip':'172.16.48.49/30'},infName2='leo133-eth0',params2={'ip':'172.16.48.50/30'})
        self.addLink(leo133,leo134,infName1='leo133-eth1',params1={'ip':'172.16.48.53/30'},infName2='leo134-eth0',params2={'ip':'172.16.48.54/30'})
        self.addLink(leo134,leo135,infName1='leo134-eth1',params1={'ip':'172.16.48.57/30'},infName2='leo135-eth0',params2={'ip':'172.16.48.58/30'})
        self.addLink(leo135,leo136,infName1='leo135-eth1',params1={'ip':'172.16.48.61/30'},infName2='leo136-eth0',params2={'ip':'172.16.48.62/30'})
        self.addLink(leo136,leo137,infName1='leo136-eth1',params1={'ip':'172.16.48.65/30'},infName2='leo137-eth0',params2={'ip':'172.16.48.66/30'})
        self.addLink(leo137,leo138,infName1='leo137-eth1',params1={'ip':'172.16.48.69/30'},infName2='leo138-eth0',params2={'ip':'172.16.48.70/30'})
        self.addLink(leo138,leo139,infName1='leo138-eth1',params1={'ip':'172.16.48.73/30'},infName2='leo139-eth0',params2={'ip':'172.16.48.74/30'})
        self.addLink(leo139,leo120,infName1='leo139-eth1',params1={'ip':'172.16.48.77/30'},infName2='leo120-eth1',params2={'ip':'172.16.48.78/30'})
        self.addLink(leo140,leo141,infName1='leo140-eth0',params1={'ip':'172.16.48.81/30'},infName2='leo141-eth0',params2={'ip':'172.16.48.82/30'})
        self.addLink(leo141,leo142,infName1='leo141-eth1',params1={'ip':'172.16.48.85/30'},infName2='leo142-eth0',params2={'ip':'172.16.48.86/30'})
        self.addLink(leo142,leo143,infName1='leo142-eth1',params1={'ip':'172.16.48.89/30'},infName2='leo143-eth0',params2={'ip':'172.16.48.90/30'})
        self.addLink(leo143,leo144,infName1='leo143-eth1',params1={'ip':'172.16.48.93/30'},infName2='leo144-eth0',params2={'ip':'172.16.48.94/30'})
        self.addLink(leo144,leo145,infName1='leo144-eth1',params1={'ip':'172.16.48.97/30'},infName2='leo145-eth0',params2={'ip':'172.16.48.98/30'})
        self.addLink(leo145,leo146,infName1='leo145-eth1',params1={'ip':'172.16.48.101/30'},infName2='leo146-eth0',params2={'ip':'172.16.48.102/30'})
        self.addLink(leo146,leo147,infName1='leo146-eth1',params1={'ip':'172.16.48.105/30'},infName2='leo147-eth0',params2={'ip':'172.16.48.106/30'})
        self.addLink(leo147,leo148,infName1='leo147-eth1',params1={'ip':'172.16.48.109/30'},infName2='leo148-eth0',params2={'ip':'172.16.48.110/30'})
        self.addLink(leo148,leo149,infName1='leo148-eth1',params1={'ip':'172.16.48.113/30'},infName2='leo149-eth0',params2={'ip':'172.16.48.114/30'})
        self.addLink(leo149,leo150,infName1='leo149-eth1',params1={'ip':'172.16.48.117/30'},infName2='leo150-eth0',params2={'ip':'172.16.48.118/30'})
        self.addLink(leo150,leo151,infName1='leo150-eth1',params1={'ip':'172.16.48.121/30'},infName2='leo151-eth0',params2={'ip':'172.16.48.122/30'})
        self.addLink(leo151,leo152,infName1='leo151-eth1',params1={'ip':'172.16.48.125/30'},infName2='leo152-eth0',params2={'ip':'172.16.48.126/30'})
        self.addLink(leo152,leo153,infName1='leo152-eth1',params1={'ip':'172.16.48.129/30'},infName2='leo153-eth0',params2={'ip':'172.16.48.130/30'})
        self.addLink(leo153,leo154,infName1='leo153-eth1',params1={'ip':'172.16.48.133/30'},infName2='leo154-eth0',params2={'ip':'172.16.48.134/30'})
        self.addLink(leo154,leo155,infName1='leo154-eth1',params1={'ip':'172.16.48.137/30'},infName2='leo155-eth0',params2={'ip':'172.16.48.138/30'})
        self.addLink(leo155,leo156,infName1='leo155-eth1',params1={'ip':'172.16.48.141/30'},infName2='leo156-eth0',params2={'ip':'172.16.48.142/30'})
        self.addLink(leo156,leo157,infName1='leo156-eth1',params1={'ip':'172.16.48.145/30'},infName2='leo157-eth0',params2={'ip':'172.16.48.146/30'})
        self.addLink(leo157,leo158,infName1='leo157-eth1',params1={'ip':'172.16.48.149/30'},infName2='leo158-eth0',params2={'ip':'172.16.48.150/30'})
        self.addLink(leo158,leo159,infName1='leo158-eth1',params1={'ip':'172.16.48.153/30'},infName2='leo159-eth0',params2={'ip':'172.16.48.154/30'})
        self.addLink(leo159,leo140,infName1='leo159-eth1',params1={'ip':'172.16.48.157/30'},infName2='leo140-eth1',params2={'ip':'172.16.48.158/30'})
        self.addLink(leo120,leo140,infName1='leo120-eth2',params1={'ip':'172.16.48.161/30'},infName2='leo140-eth2',params2={'ip':'172.16.48.162/30'})
        self.addLink(leo121,leo141,infName1='leo121-eth2',params1={'ip':'172.16.48.165/30'},infName2='leo141-eth2',params2={'ip':'172.16.48.166/30'})
        self.addLink(leo122,leo142,infName1='leo122-eth2',params1={'ip':'172.16.48.169/30'},infName2='leo142-eth2',params2={'ip':'172.16.48.170/30'})
        self.addLink(leo123,leo143,infName1='leo123-eth2',params1={'ip':'172.16.48.173/30'},infName2='leo143-eth2',params2={'ip':'172.16.48.174/30'})
        self.addLink(leo124,leo144,infName1='leo124-eth2',params1={'ip':'172.16.48.177/30'},infName2='leo144-eth2',params2={'ip':'172.16.48.178/30'})
        self.addLink(leo125,leo145,infName1='leo125-eth2',params1={'ip':'172.16.48.181/30'},infName2='leo145-eth2',params2={'ip':'172.16.48.182/30'})
        self.addLink(leo126,leo146,infName1='leo126-eth2',params1={'ip':'172.16.48.185/30'},infName2='leo146-eth2',params2={'ip':'172.16.48.186/30'})
        self.addLink(leo127,leo147,infName1='leo127-eth2',params1={'ip':'172.16.48.189/30'},infName2='leo147-eth2',params2={'ip':'172.16.48.190/30'})
        self.addLink(leo128,leo148,infName1='leo128-eth2',params1={'ip':'172.16.48.193/30'},infName2='leo148-eth2',params2={'ip':'172.16.48.194/30'})
        self.addLink(leo129,leo149,infName1='leo129-eth2',params1={'ip':'172.16.48.197/30'},infName2='leo149-eth2',params2={'ip':'172.16.48.198/30'})
        self.addLink(leo130,leo150,infName1='leo130-eth2',params1={'ip':'172.16.48.201/30'},infName2='leo150-eth2',params2={'ip':'172.16.48.202/30'})
        self.addLink(leo131,leo151,infName1='leo131-eth2',params1={'ip':'172.16.48.205/30'},infName2='leo151-eth2',params2={'ip':'172.16.48.206/30'})
        self.addLink(leo132,leo152,infName1='leo132-eth2',params1={'ip':'172.16.48.209/30'},infName2='leo152-eth2',params2={'ip':'172.16.48.210/30'})
        self.addLink(leo133,leo153,infName1='leo133-eth2',params1={'ip':'172.16.48.213/30'},infName2='leo153-eth2',params2={'ip':'172.16.48.214/30'})
        self.addLink(leo134,leo154,infName1='leo134-eth2',params1={'ip':'172.16.48.217/30'},infName2='leo154-eth2',params2={'ip':'172.16.48.218/30'})
        self.addLink(leo135,leo155,infName1='leo135-eth2',params1={'ip':'172.16.48.221/30'},infName2='leo155-eth2',params2={'ip':'172.16.48.222/30'})
        self.addLink(leo136,leo156,infName1='leo136-eth2',params1={'ip':'172.16.48.225/30'},infName2='leo156-eth2',params2={'ip':'172.16.48.226/30'})
        self.addLink(leo137,leo157,infName1='leo137-eth2',params1={'ip':'172.16.48.229/30'},infName2='leo157-eth2',params2={'ip':'172.16.48.230/30'})
        self.addLink(leo138,leo158,infName1='leo138-eth2',params1={'ip':'172.16.48.233/30'},infName2='leo158-eth2',params2={'ip':'172.16.48.234/30'})
        self.addLink(leo139,leo159,infName1='leo139-eth2',params1={'ip':'172.16.48.237/30'},infName2='leo159-eth2',params2={'ip':'172.16.48.238/30'})
        self.addLink(leo160,leo161,infName1='leo160-eth0',params1={'ip':'172.16.64.1/30'},infName2='leo161-eth0',params2={'ip':'172.16.64.2/30'})
        self.addLink(leo161,leo162,infName1='leo161-eth1',params1={'ip':'172.16.64.5/30'},infName2='leo162-eth0',params2={'ip':'172.16.64.6/30'})
        self.addLink(leo162,leo163,infName1='leo162-eth1',params1={'ip':'172.16.64.9/30'},infName2='leo163-eth0',params2={'ip':'172.16.64.10/30'})
        self.addLink(leo163,leo164,infName1='leo163-eth1',params1={'ip':'172.16.64.13/30'},infName2='leo164-eth0',params2={'ip':'172.16.64.14/30'})
        self.addLink(leo164,leo165,infName1='leo164-eth1',params1={'ip':'172.16.64.17/30'},infName2='leo165-eth0',params2={'ip':'172.16.64.18/30'})
        self.addLink(leo165,leo166,infName1='leo165-eth1',params1={'ip':'172.16.64.21/30'},infName2='leo166-eth0',params2={'ip':'172.16.64.22/30'})
        self.addLink(leo166,leo167,infName1='leo166-eth1',params1={'ip':'172.16.64.25/30'},infName2='leo167-eth0',params2={'ip':'172.16.64.26/30'})
        self.addLink(leo167,leo168,infName1='leo167-eth1',params1={'ip':'172.16.64.29/30'},infName2='leo168-eth0',params2={'ip':'172.16.64.30/30'})
        self.addLink(leo168,leo169,infName1='leo168-eth1',params1={'ip':'172.16.64.33/30'},infName2='leo169-eth0',params2={'ip':'172.16.64.34/30'})
        self.addLink(leo169,leo170,infName1='leo169-eth1',params1={'ip':'172.16.64.37/30'},infName2='leo170-eth0',params2={'ip':'172.16.64.38/30'})
        self.addLink(leo170,leo171,infName1='leo170-eth1',params1={'ip':'172.16.64.41/30'},infName2='leo171-eth0',params2={'ip':'172.16.64.42/30'})
        self.addLink(leo171,leo172,infName1='leo171-eth1',params1={'ip':'172.16.64.45/30'},infName2='leo172-eth0',params2={'ip':'172.16.64.46/30'})
        self.addLink(leo172,leo173,infName1='leo172-eth1',params1={'ip':'172.16.64.49/30'},infName2='leo173-eth0',params2={'ip':'172.16.64.50/30'})
        self.addLink(leo173,leo174,infName1='leo173-eth1',params1={'ip':'172.16.64.53/30'},infName2='leo174-eth0',params2={'ip':'172.16.64.54/30'})
        self.addLink(leo174,leo175,infName1='leo174-eth1',params1={'ip':'172.16.64.57/30'},infName2='leo175-eth0',params2={'ip':'172.16.64.58/30'})
        self.addLink(leo175,leo176,infName1='leo175-eth1',params1={'ip':'172.16.64.61/30'},infName2='leo176-eth0',params2={'ip':'172.16.64.62/30'})
        self.addLink(leo176,leo177,infName1='leo176-eth1',params1={'ip':'172.16.64.65/30'},infName2='leo177-eth0',params2={'ip':'172.16.64.66/30'})
        self.addLink(leo177,leo178,infName1='leo177-eth1',params1={'ip':'172.16.64.69/30'},infName2='leo178-eth0',params2={'ip':'172.16.64.70/30'})
        self.addLink(leo178,leo179,infName1='leo178-eth1',params1={'ip':'172.16.64.73/30'},infName2='leo179-eth0',params2={'ip':'172.16.64.74/30'})
        self.addLink(leo179,leo160,infName1='leo179-eth1',params1={'ip':'172.16.64.77/30'},infName2='leo160-eth1',params2={'ip':'172.16.64.78/30'})
        self.addLink(leo180,leo181,infName1='leo180-eth0',params1={'ip':'172.16.64.81/30'},infName2='leo181-eth0',params2={'ip':'172.16.64.82/30'})
        self.addLink(leo181,leo182,infName1='leo181-eth1',params1={'ip':'172.16.64.85/30'},infName2='leo182-eth0',params2={'ip':'172.16.64.86/30'})
        self.addLink(leo182,leo183,infName1='leo182-eth1',params1={'ip':'172.16.64.89/30'},infName2='leo183-eth0',params2={'ip':'172.16.64.90/30'})
        self.addLink(leo183,leo184,infName1='leo183-eth1',params1={'ip':'172.16.64.93/30'},infName2='leo184-eth0',params2={'ip':'172.16.64.94/30'})
        self.addLink(leo184,leo185,infName1='leo184-eth1',params1={'ip':'172.16.64.97/30'},infName2='leo185-eth0',params2={'ip':'172.16.64.98/30'})
        self.addLink(leo185,leo186,infName1='leo185-eth1',params1={'ip':'172.16.64.101/30'},infName2='leo186-eth0',params2={'ip':'172.16.64.102/30'})
        self.addLink(leo186,leo187,infName1='leo186-eth1',params1={'ip':'172.16.64.105/30'},infName2='leo187-eth0',params2={'ip':'172.16.64.106/30'})
        self.addLink(leo187,leo188,infName1='leo187-eth1',params1={'ip':'172.16.64.109/30'},infName2='leo188-eth0',params2={'ip':'172.16.64.110/30'})
        self.addLink(leo188,leo189,infName1='leo188-eth1',params1={'ip':'172.16.64.113/30'},infName2='leo189-eth0',params2={'ip':'172.16.64.114/30'})
        self.addLink(leo189,leo190,infName1='leo189-eth1',params1={'ip':'172.16.64.117/30'},infName2='leo190-eth0',params2={'ip':'172.16.64.118/30'})
        self.addLink(leo190,leo191,infName1='leo190-eth1',params1={'ip':'172.16.64.121/30'},infName2='leo191-eth0',params2={'ip':'172.16.64.122/30'})
        self.addLink(leo191,leo192,infName1='leo191-eth1',params1={'ip':'172.16.64.125/30'},infName2='leo192-eth0',params2={'ip':'172.16.64.126/30'})
        self.addLink(leo192,leo193,infName1='leo192-eth1',params1={'ip':'172.16.64.129/30'},infName2='leo193-eth0',params2={'ip':'172.16.64.130/30'})
        self.addLink(leo193,leo194,infName1='leo193-eth1',params1={'ip':'172.16.64.133/30'},infName2='leo194-eth0',params2={'ip':'172.16.64.134/30'})
        self.addLink(leo194,leo195,infName1='leo194-eth1',params1={'ip':'172.16.64.137/30'},infName2='leo195-eth0',params2={'ip':'172.16.64.138/30'})
        self.addLink(leo195,leo196,infName1='leo195-eth1',params1={'ip':'172.16.64.141/30'},infName2='leo196-eth0',params2={'ip':'172.16.64.142/30'})
        self.addLink(leo196,leo197,infName1='leo196-eth1',params1={'ip':'172.16.64.145/30'},infName2='leo197-eth0',params2={'ip':'172.16.64.146/30'})
        self.addLink(leo197,leo198,infName1='leo197-eth1',params1={'ip':'172.16.64.149/30'},infName2='leo198-eth0',params2={'ip':'172.16.64.150/30'})
        self.addLink(leo198,leo199,infName1='leo198-eth1',params1={'ip':'172.16.64.153/30'},infName2='leo199-eth0',params2={'ip':'172.16.64.154/30'})
        self.addLink(leo199,leo180,infName1='leo199-eth1',params1={'ip':'172.16.64.157/30'},infName2='leo180-eth1',params2={'ip':'172.16.64.158/30'})
        self.addLink(leo160,leo180,infName1='leo160-eth2',params1={'ip':'172.16.64.161/30'},infName2='leo180-eth2',params2={'ip':'172.16.64.162/30'})
        self.addLink(leo161,leo181,infName1='leo161-eth2',params1={'ip':'172.16.64.165/30'},infName2='leo181-eth2',params2={'ip':'172.16.64.166/30'})
        self.addLink(leo162,leo182,infName1='leo162-eth2',params1={'ip':'172.16.64.169/30'},infName2='leo182-eth2',params2={'ip':'172.16.64.170/30'})
        self.addLink(leo163,leo183,infName1='leo163-eth2',params1={'ip':'172.16.64.173/30'},infName2='leo183-eth2',params2={'ip':'172.16.64.174/30'})
        self.addLink(leo164,leo184,infName1='leo164-eth2',params1={'ip':'172.16.64.177/30'},infName2='leo184-eth2',params2={'ip':'172.16.64.178/30'})
        self.addLink(leo165,leo185,infName1='leo165-eth2',params1={'ip':'172.16.64.181/30'},infName2='leo185-eth2',params2={'ip':'172.16.64.182/30'})
        self.addLink(leo166,leo186,infName1='leo166-eth2',params1={'ip':'172.16.64.185/30'},infName2='leo186-eth2',params2={'ip':'172.16.64.186/30'})
        self.addLink(leo167,leo187,infName1='leo167-eth2',params1={'ip':'172.16.64.189/30'},infName2='leo187-eth2',params2={'ip':'172.16.64.190/30'})
        self.addLink(leo168,leo188,infName1='leo168-eth2',params1={'ip':'172.16.64.193/30'},infName2='leo188-eth2',params2={'ip':'172.16.64.194/30'})
        self.addLink(leo169,leo189,infName1='leo169-eth2',params1={'ip':'172.16.64.197/30'},infName2='leo189-eth2',params2={'ip':'172.16.64.198/30'})
        self.addLink(leo170,leo190,infName1='leo170-eth2',params1={'ip':'172.16.64.201/30'},infName2='leo190-eth2',params2={'ip':'172.16.64.202/30'})
        self.addLink(leo171,leo191,infName1='leo171-eth2',params1={'ip':'172.16.64.205/30'},infName2='leo191-eth2',params2={'ip':'172.16.64.206/30'})
        self.addLink(leo172,leo192,infName1='leo172-eth2',params1={'ip':'172.16.64.209/30'},infName2='leo192-eth2',params2={'ip':'172.16.64.210/30'})
        self.addLink(leo173,leo193,infName1='leo173-eth2',params1={'ip':'172.16.64.213/30'},infName2='leo193-eth2',params2={'ip':'172.16.64.214/30'})
        self.addLink(leo174,leo194,infName1='leo174-eth2',params1={'ip':'172.16.64.217/30'},infName2='leo194-eth2',params2={'ip':'172.16.64.218/30'})
        self.addLink(leo175,leo195,infName1='leo175-eth2',params1={'ip':'172.16.64.221/30'},infName2='leo195-eth2',params2={'ip':'172.16.64.222/30'})
        self.addLink(leo176,leo196,infName1='leo176-eth2',params1={'ip':'172.16.64.225/30'},infName2='leo196-eth2',params2={'ip':'172.16.64.226/30'})
        self.addLink(leo177,leo197,infName1='leo177-eth2',params1={'ip':'172.16.64.229/30'},infName2='leo197-eth2',params2={'ip':'172.16.64.230/30'})
        self.addLink(leo178,leo198,infName1='leo178-eth2',params1={'ip':'172.16.64.233/30'},infName2='leo198-eth2',params2={'ip':'172.16.64.234/30'})
        self.addLink(leo179,leo199,infName1='leo179-eth2',params1={'ip':'172.16.64.237/30'},infName2='leo199-eth2',params2={'ip':'172.16.64.238/30'})
        self.addLink(leo200,leo201,infName1='leo200-eth0',params1={'ip':'172.16.80.1/30'},infName2='leo201-eth0',params2={'ip':'172.16.80.2/30'})
        self.addLink(leo201,leo202,infName1='leo201-eth1',params1={'ip':'172.16.80.5/30'},infName2='leo202-eth0',params2={'ip':'172.16.80.6/30'})
        self.addLink(leo202,leo203,infName1='leo202-eth1',params1={'ip':'172.16.80.9/30'},infName2='leo203-eth0',params2={'ip':'172.16.80.10/30'})
        self.addLink(leo203,leo204,infName1='leo203-eth1',params1={'ip':'172.16.80.13/30'},infName2='leo204-eth0',params2={'ip':'172.16.80.14/30'})
        self.addLink(leo204,leo205,infName1='leo204-eth1',params1={'ip':'172.16.80.17/30'},infName2='leo205-eth0',params2={'ip':'172.16.80.18/30'})
        self.addLink(leo205,leo206,infName1='leo205-eth1',params1={'ip':'172.16.80.21/30'},infName2='leo206-eth0',params2={'ip':'172.16.80.22/30'})
        self.addLink(leo206,leo207,infName1='leo206-eth1',params1={'ip':'172.16.80.25/30'},infName2='leo207-eth0',params2={'ip':'172.16.80.26/30'})
        self.addLink(leo207,leo208,infName1='leo207-eth1',params1={'ip':'172.16.80.29/30'},infName2='leo208-eth0',params2={'ip':'172.16.80.30/30'})
        self.addLink(leo208,leo209,infName1='leo208-eth1',params1={'ip':'172.16.80.33/30'},infName2='leo209-eth0',params2={'ip':'172.16.80.34/30'})
        self.addLink(leo209,leo210,infName1='leo209-eth1',params1={'ip':'172.16.80.37/30'},infName2='leo210-eth0',params2={'ip':'172.16.80.38/30'})
        self.addLink(leo210,leo211,infName1='leo210-eth1',params1={'ip':'172.16.80.41/30'},infName2='leo211-eth0',params2={'ip':'172.16.80.42/30'})
        self.addLink(leo211,leo212,infName1='leo211-eth1',params1={'ip':'172.16.80.45/30'},infName2='leo212-eth0',params2={'ip':'172.16.80.46/30'})
        self.addLink(leo212,leo213,infName1='leo212-eth1',params1={'ip':'172.16.80.49/30'},infName2='leo213-eth0',params2={'ip':'172.16.80.50/30'})
        self.addLink(leo213,leo214,infName1='leo213-eth1',params1={'ip':'172.16.80.53/30'},infName2='leo214-eth0',params2={'ip':'172.16.80.54/30'})
        self.addLink(leo214,leo215,infName1='leo214-eth1',params1={'ip':'172.16.80.57/30'},infName2='leo215-eth0',params2={'ip':'172.16.80.58/30'})
        self.addLink(leo215,leo216,infName1='leo215-eth1',params1={'ip':'172.16.80.61/30'},infName2='leo216-eth0',params2={'ip':'172.16.80.62/30'})
        self.addLink(leo216,leo217,infName1='leo216-eth1',params1={'ip':'172.16.80.65/30'},infName2='leo217-eth0',params2={'ip':'172.16.80.66/30'})
        self.addLink(leo217,leo218,infName1='leo217-eth1',params1={'ip':'172.16.80.69/30'},infName2='leo218-eth0',params2={'ip':'172.16.80.70/30'})
        self.addLink(leo218,leo219,infName1='leo218-eth1',params1={'ip':'172.16.80.73/30'},infName2='leo219-eth0',params2={'ip':'172.16.80.74/30'})
        self.addLink(leo219,leo200,infName1='leo219-eth1',params1={'ip':'172.16.80.77/30'},infName2='leo200-eth1',params2={'ip':'172.16.80.78/30'})
        self.addLink(leo220,leo221,infName1='leo220-eth0',params1={'ip':'172.16.80.81/30'},infName2='leo221-eth0',params2={'ip':'172.16.80.82/30'})
        self.addLink(leo221,leo222,infName1='leo221-eth1',params1={'ip':'172.16.80.85/30'},infName2='leo222-eth0',params2={'ip':'172.16.80.86/30'})
        self.addLink(leo222,leo223,infName1='leo222-eth1',params1={'ip':'172.16.80.89/30'},infName2='leo223-eth0',params2={'ip':'172.16.80.90/30'})
        self.addLink(leo223,leo224,infName1='leo223-eth1',params1={'ip':'172.16.80.93/30'},infName2='leo224-eth0',params2={'ip':'172.16.80.94/30'})
        self.addLink(leo224,leo225,infName1='leo224-eth1',params1={'ip':'172.16.80.97/30'},infName2='leo225-eth0',params2={'ip':'172.16.80.98/30'})
        self.addLink(leo225,leo226,infName1='leo225-eth1',params1={'ip':'172.16.80.101/30'},infName2='leo226-eth0',params2={'ip':'172.16.80.102/30'})
        self.addLink(leo226,leo227,infName1='leo226-eth1',params1={'ip':'172.16.80.105/30'},infName2='leo227-eth0',params2={'ip':'172.16.80.106/30'})
        self.addLink(leo227,leo228,infName1='leo227-eth1',params1={'ip':'172.16.80.109/30'},infName2='leo228-eth0',params2={'ip':'172.16.80.110/30'})
        self.addLink(leo228,leo229,infName1='leo228-eth1',params1={'ip':'172.16.80.113/30'},infName2='leo229-eth0',params2={'ip':'172.16.80.114/30'})
        self.addLink(leo229,leo230,infName1='leo229-eth1',params1={'ip':'172.16.80.117/30'},infName2='leo230-eth0',params2={'ip':'172.16.80.118/30'})
        self.addLink(leo230,leo231,infName1='leo230-eth1',params1={'ip':'172.16.80.121/30'},infName2='leo231-eth0',params2={'ip':'172.16.80.122/30'})
        self.addLink(leo231,leo232,infName1='leo231-eth1',params1={'ip':'172.16.80.125/30'},infName2='leo232-eth0',params2={'ip':'172.16.80.126/30'})
        self.addLink(leo232,leo233,infName1='leo232-eth1',params1={'ip':'172.16.80.129/30'},infName2='leo233-eth0',params2={'ip':'172.16.80.130/30'})
        self.addLink(leo233,leo234,infName1='leo233-eth1',params1={'ip':'172.16.80.133/30'},infName2='leo234-eth0',params2={'ip':'172.16.80.134/30'})
        self.addLink(leo234,leo235,infName1='leo234-eth1',params1={'ip':'172.16.80.137/30'},infName2='leo235-eth0',params2={'ip':'172.16.80.138/30'})
        self.addLink(leo235,leo236,infName1='leo235-eth1',params1={'ip':'172.16.80.141/30'},infName2='leo236-eth0',params2={'ip':'172.16.80.142/30'})
        self.addLink(leo236,leo237,infName1='leo236-eth1',params1={'ip':'172.16.80.145/30'},infName2='leo237-eth0',params2={'ip':'172.16.80.146/30'})
        self.addLink(leo237,leo238,infName1='leo237-eth1',params1={'ip':'172.16.80.149/30'},infName2='leo238-eth0',params2={'ip':'172.16.80.150/30'})
        self.addLink(leo238,leo239,infName1='leo238-eth1',params1={'ip':'172.16.80.153/30'},infName2='leo239-eth0',params2={'ip':'172.16.80.154/30'})
        self.addLink(leo239,leo220,infName1='leo239-eth1',params1={'ip':'172.16.80.157/30'},infName2='leo220-eth1',params2={'ip':'172.16.80.158/30'})
        self.addLink(leo200,leo220,infName1='leo200-eth2',params1={'ip':'172.16.80.161/30'},infName2='leo220-eth2',params2={'ip':'172.16.80.162/30'})
        self.addLink(leo201,leo221,infName1='leo201-eth2',params1={'ip':'172.16.80.165/30'},infName2='leo221-eth2',params2={'ip':'172.16.80.166/30'})
        self.addLink(leo202,leo222,infName1='leo202-eth2',params1={'ip':'172.16.80.169/30'},infName2='leo222-eth2',params2={'ip':'172.16.80.170/30'})
        self.addLink(leo203,leo223,infName1='leo203-eth2',params1={'ip':'172.16.80.173/30'},infName2='leo223-eth2',params2={'ip':'172.16.80.174/30'})
        self.addLink(leo204,leo224,infName1='leo204-eth2',params1={'ip':'172.16.80.177/30'},infName2='leo224-eth2',params2={'ip':'172.16.80.178/30'})
        self.addLink(leo205,leo225,infName1='leo205-eth2',params1={'ip':'172.16.80.181/30'},infName2='leo225-eth2',params2={'ip':'172.16.80.182/30'})
        self.addLink(leo206,leo226,infName1='leo206-eth2',params1={'ip':'172.16.80.185/30'},infName2='leo226-eth2',params2={'ip':'172.16.80.186/30'})
        self.addLink(leo207,leo227,infName1='leo207-eth2',params1={'ip':'172.16.80.189/30'},infName2='leo227-eth2',params2={'ip':'172.16.80.190/30'})
        self.addLink(leo208,leo228,infName1='leo208-eth2',params1={'ip':'172.16.80.193/30'},infName2='leo228-eth2',params2={'ip':'172.16.80.194/30'})
        self.addLink(leo209,leo229,infName1='leo209-eth2',params1={'ip':'172.16.80.197/30'},infName2='leo229-eth2',params2={'ip':'172.16.80.198/30'})
        self.addLink(leo210,leo230,infName1='leo210-eth2',params1={'ip':'172.16.80.201/30'},infName2='leo230-eth2',params2={'ip':'172.16.80.202/30'})
        self.addLink(leo211,leo231,infName1='leo211-eth2',params1={'ip':'172.16.80.205/30'},infName2='leo231-eth2',params2={'ip':'172.16.80.206/30'})
        self.addLink(leo212,leo232,infName1='leo212-eth2',params1={'ip':'172.16.80.209/30'},infName2='leo232-eth2',params2={'ip':'172.16.80.210/30'})
        self.addLink(leo213,leo233,infName1='leo213-eth2',params1={'ip':'172.16.80.213/30'},infName2='leo233-eth2',params2={'ip':'172.16.80.214/30'})
        self.addLink(leo214,leo234,infName1='leo214-eth2',params1={'ip':'172.16.80.217/30'},infName2='leo234-eth2',params2={'ip':'172.16.80.218/30'})
        self.addLink(leo215,leo235,infName1='leo215-eth2',params1={'ip':'172.16.80.221/30'},infName2='leo235-eth2',params2={'ip':'172.16.80.222/30'})
        self.addLink(leo216,leo236,infName1='leo216-eth2',params1={'ip':'172.16.80.225/30'},infName2='leo236-eth2',params2={'ip':'172.16.80.226/30'})
        self.addLink(leo217,leo237,infName1='leo217-eth2',params1={'ip':'172.16.80.229/30'},infName2='leo237-eth2',params2={'ip':'172.16.80.230/30'})
        self.addLink(leo218,leo238,infName1='leo218-eth2',params1={'ip':'172.16.80.233/30'},infName2='leo238-eth2',params2={'ip':'172.16.80.234/30'})
        self.addLink(leo219,leo239,infName1='leo219-eth2',params1={'ip':'172.16.80.237/30'},infName2='leo239-eth2',params2={'ip':'172.16.80.238/30'})
        self.addLink(leo20,leo40,infName1='leo20-eth3',params1={'ip':'172.24.0.1/30'},infName2='leo40-eth3',params2={'ip':'172.24.0.2/30'})
        self.addLink(leo21,leo41,infName1='leo21-eth3',params1={'ip':'172.24.0.5/30'},infName2='leo41-eth3',params2={'ip':'172.24.0.6/30'})
        self.addLink(leo22,leo42,infName1='leo22-eth3',params1={'ip':'172.24.0.9/30'},infName2='leo42-eth3',params2={'ip':'172.24.0.10/30'})
        self.addLink(leo23,leo43,infName1='leo23-eth3',params1={'ip':'172.24.0.13/30'},infName2='leo43-eth3',params2={'ip':'172.24.0.14/30'})
        self.addLink(leo24,leo44,infName1='leo24-eth3',params1={'ip':'172.24.0.17/30'},infName2='leo44-eth3',params2={'ip':'172.24.0.18/30'})
        self.addLink(leo25,leo45,infName1='leo25-eth3',params1={'ip':'172.24.0.21/30'},infName2='leo45-eth3',params2={'ip':'172.24.0.22/30'})
        self.addLink(leo26,leo46,infName1='leo26-eth3',params1={'ip':'172.24.0.25/30'},infName2='leo46-eth3',params2={'ip':'172.24.0.26/30'})
        self.addLink(leo27,leo47,infName1='leo27-eth3',params1={'ip':'172.24.0.29/30'},infName2='leo47-eth3',params2={'ip':'172.24.0.30/30'})
        self.addLink(leo28,leo48,infName1='leo28-eth3',params1={'ip':'172.24.0.33/30'},infName2='leo48-eth3',params2={'ip':'172.24.0.34/30'})
        self.addLink(leo29,leo49,infName1='leo29-eth3',params1={'ip':'172.24.0.37/30'},infName2='leo49-eth3',params2={'ip':'172.24.0.38/30'})
        self.addLink(leo30,leo50,infName1='leo30-eth3',params1={'ip':'172.24.0.41/30'},infName2='leo50-eth3',params2={'ip':'172.24.0.42/30'})
        self.addLink(leo31,leo51,infName1='leo31-eth3',params1={'ip':'172.24.0.45/30'},infName2='leo51-eth3',params2={'ip':'172.24.0.46/30'})
        self.addLink(leo32,leo52,infName1='leo32-eth3',params1={'ip':'172.24.0.49/30'},infName2='leo52-eth3',params2={'ip':'172.24.0.50/30'})
        self.addLink(leo33,leo53,infName1='leo33-eth3',params1={'ip':'172.24.0.53/30'},infName2='leo53-eth3',params2={'ip':'172.24.0.54/30'})
        self.addLink(leo34,leo54,infName1='leo34-eth3',params1={'ip':'172.24.0.57/30'},infName2='leo54-eth3',params2={'ip':'172.24.0.58/30'})
        self.addLink(leo35,leo55,infName1='leo35-eth3',params1={'ip':'172.24.0.61/30'},infName2='leo55-eth3',params2={'ip':'172.24.0.62/30'})
        self.addLink(leo36,leo56,infName1='leo36-eth3',params1={'ip':'172.24.0.65/30'},infName2='leo56-eth3',params2={'ip':'172.24.0.66/30'})
        self.addLink(leo37,leo57,infName1='leo37-eth3',params1={'ip':'172.24.0.69/30'},infName2='leo57-eth3',params2={'ip':'172.24.0.70/30'})
        self.addLink(leo38,leo58,infName1='leo38-eth3',params1={'ip':'172.24.0.73/30'},infName2='leo58-eth3',params2={'ip':'172.24.0.74/30'})
        self.addLink(leo39,leo59,infName1='leo39-eth3',params1={'ip':'172.24.0.77/30'},infName2='leo59-eth3',params2={'ip':'172.24.0.78/30'})
        self.addLink(leo60,leo80,infName1='leo60-eth3',params1={'ip':'172.24.16.1/30'},infName2='leo80-eth3',params2={'ip':'172.24.16.2/30'})
        self.addLink(leo61,leo81,infName1='leo61-eth3',params1={'ip':'172.24.16.5/30'},infName2='leo81-eth3',params2={'ip':'172.24.16.6/30'})
        self.addLink(leo62,leo82,infName1='leo62-eth3',params1={'ip':'172.24.16.9/30'},infName2='leo82-eth3',params2={'ip':'172.24.16.10/30'})
        self.addLink(leo63,leo83,infName1='leo63-eth3',params1={'ip':'172.24.16.13/30'},infName2='leo83-eth3',params2={'ip':'172.24.16.14/30'})
        self.addLink(leo64,leo84,infName1='leo64-eth3',params1={'ip':'172.24.16.17/30'},infName2='leo84-eth3',params2={'ip':'172.24.16.18/30'})
        self.addLink(leo65,leo85,infName1='leo65-eth3',params1={'ip':'172.24.16.21/30'},infName2='leo85-eth3',params2={'ip':'172.24.16.22/30'})
        self.addLink(leo66,leo86,infName1='leo66-eth3',params1={'ip':'172.24.16.25/30'},infName2='leo86-eth3',params2={'ip':'172.24.16.26/30'})
        self.addLink(leo67,leo87,infName1='leo67-eth3',params1={'ip':'172.24.16.29/30'},infName2='leo87-eth3',params2={'ip':'172.24.16.30/30'})
        self.addLink(leo68,leo88,infName1='leo68-eth3',params1={'ip':'172.24.16.33/30'},infName2='leo88-eth3',params2={'ip':'172.24.16.34/30'})
        self.addLink(leo69,leo89,infName1='leo69-eth3',params1={'ip':'172.24.16.37/30'},infName2='leo89-eth3',params2={'ip':'172.24.16.38/30'})
        self.addLink(leo70,leo90,infName1='leo70-eth3',params1={'ip':'172.24.16.41/30'},infName2='leo90-eth3',params2={'ip':'172.24.16.42/30'})
        self.addLink(leo71,leo91,infName1='leo71-eth3',params1={'ip':'172.24.16.45/30'},infName2='leo91-eth3',params2={'ip':'172.24.16.46/30'})
        self.addLink(leo72,leo92,infName1='leo72-eth3',params1={'ip':'172.24.16.49/30'},infName2='leo92-eth3',params2={'ip':'172.24.16.50/30'})
        self.addLink(leo73,leo93,infName1='leo73-eth3',params1={'ip':'172.24.16.53/30'},infName2='leo93-eth3',params2={'ip':'172.24.16.54/30'})
        self.addLink(leo74,leo94,infName1='leo74-eth3',params1={'ip':'172.24.16.57/30'},infName2='leo94-eth3',params2={'ip':'172.24.16.58/30'})
        self.addLink(leo75,leo95,infName1='leo75-eth3',params1={'ip':'172.24.16.61/30'},infName2='leo95-eth3',params2={'ip':'172.24.16.62/30'})
        self.addLink(leo76,leo96,infName1='leo76-eth3',params1={'ip':'172.24.16.65/30'},infName2='leo96-eth3',params2={'ip':'172.24.16.66/30'})
        self.addLink(leo77,leo97,infName1='leo77-eth3',params1={'ip':'172.24.16.69/30'},infName2='leo97-eth3',params2={'ip':'172.24.16.70/30'})
        self.addLink(leo78,leo98,infName1='leo78-eth3',params1={'ip':'172.24.16.73/30'},infName2='leo98-eth3',params2={'ip':'172.24.16.74/30'})
        self.addLink(leo79,leo99,infName1='leo79-eth3',params1={'ip':'172.24.16.77/30'},infName2='leo99-eth3',params2={'ip':'172.24.16.78/30'})
        self.addLink(leo100,leo120,infName1='leo100-eth3',params1={'ip':'172.24.32.1/30'},infName2='leo120-eth3',params2={'ip':'172.24.32.2/30'})
        self.addLink(leo101,leo121,infName1='leo101-eth3',params1={'ip':'172.24.32.5/30'},infName2='leo121-eth3',params2={'ip':'172.24.32.6/30'})
        self.addLink(leo102,leo122,infName1='leo102-eth3',params1={'ip':'172.24.32.9/30'},infName2='leo122-eth3',params2={'ip':'172.24.32.10/30'})
        self.addLink(leo103,leo123,infName1='leo103-eth3',params1={'ip':'172.24.32.13/30'},infName2='leo123-eth3',params2={'ip':'172.24.32.14/30'})
        self.addLink(leo104,leo124,infName1='leo104-eth3',params1={'ip':'172.24.32.17/30'},infName2='leo124-eth3',params2={'ip':'172.24.32.18/30'})
        self.addLink(leo105,leo125,infName1='leo105-eth3',params1={'ip':'172.24.32.21/30'},infName2='leo125-eth3',params2={'ip':'172.24.32.22/30'})
        self.addLink(leo106,leo126,infName1='leo106-eth3',params1={'ip':'172.24.32.25/30'},infName2='leo126-eth3',params2={'ip':'172.24.32.26/30'})
        self.addLink(leo107,leo127,infName1='leo107-eth3',params1={'ip':'172.24.32.29/30'},infName2='leo127-eth3',params2={'ip':'172.24.32.30/30'})
        self.addLink(leo108,leo128,infName1='leo108-eth3',params1={'ip':'172.24.32.33/30'},infName2='leo128-eth3',params2={'ip':'172.24.32.34/30'})
        self.addLink(leo109,leo129,infName1='leo109-eth3',params1={'ip':'172.24.32.37/30'},infName2='leo129-eth3',params2={'ip':'172.24.32.38/30'})
        self.addLink(leo110,leo130,infName1='leo110-eth3',params1={'ip':'172.24.32.41/30'},infName2='leo130-eth3',params2={'ip':'172.24.32.42/30'})
        self.addLink(leo111,leo131,infName1='leo111-eth3',params1={'ip':'172.24.32.45/30'},infName2='leo131-eth3',params2={'ip':'172.24.32.46/30'})
        self.addLink(leo112,leo132,infName1='leo112-eth3',params1={'ip':'172.24.32.49/30'},infName2='leo132-eth3',params2={'ip':'172.24.32.50/30'})
        self.addLink(leo113,leo133,infName1='leo113-eth3',params1={'ip':'172.24.32.53/30'},infName2='leo133-eth3',params2={'ip':'172.24.32.54/30'})
        self.addLink(leo114,leo134,infName1='leo114-eth3',params1={'ip':'172.24.32.57/30'},infName2='leo134-eth3',params2={'ip':'172.24.32.58/30'})
        self.addLink(leo115,leo135,infName1='leo115-eth3',params1={'ip':'172.24.32.61/30'},infName2='leo135-eth3',params2={'ip':'172.24.32.62/30'})
        self.addLink(leo116,leo136,infName1='leo116-eth3',params1={'ip':'172.24.32.65/30'},infName2='leo136-eth3',params2={'ip':'172.24.32.66/30'})
        self.addLink(leo117,leo137,infName1='leo117-eth3',params1={'ip':'172.24.32.69/30'},infName2='leo137-eth3',params2={'ip':'172.24.32.70/30'})
        self.addLink(leo118,leo138,infName1='leo118-eth3',params1={'ip':'172.24.32.73/30'},infName2='leo138-eth3',params2={'ip':'172.24.32.74/30'})
        self.addLink(leo119,leo139,infName1='leo119-eth3',params1={'ip':'172.24.32.77/30'},infName2='leo139-eth3',params2={'ip':'172.24.32.78/30'})
        self.addLink(leo140,leo160,infName1='leo140-eth3',params1={'ip':'172.24.48.1/30'},infName2='leo160-eth3',params2={'ip':'172.24.48.2/30'})
        self.addLink(leo141,leo161,infName1='leo141-eth3',params1={'ip':'172.24.48.5/30'},infName2='leo161-eth3',params2={'ip':'172.24.48.6/30'})
        self.addLink(leo142,leo162,infName1='leo142-eth3',params1={'ip':'172.24.48.9/30'},infName2='leo162-eth3',params2={'ip':'172.24.48.10/30'})
        self.addLink(leo143,leo163,infName1='leo143-eth3',params1={'ip':'172.24.48.13/30'},infName2='leo163-eth3',params2={'ip':'172.24.48.14/30'})
        self.addLink(leo144,leo164,infName1='leo144-eth3',params1={'ip':'172.24.48.17/30'},infName2='leo164-eth3',params2={'ip':'172.24.48.18/30'})
        self.addLink(leo145,leo165,infName1='leo145-eth3',params1={'ip':'172.24.48.21/30'},infName2='leo165-eth3',params2={'ip':'172.24.48.22/30'})
        self.addLink(leo146,leo166,infName1='leo146-eth3',params1={'ip':'172.24.48.25/30'},infName2='leo166-eth3',params2={'ip':'172.24.48.26/30'})
        self.addLink(leo147,leo167,infName1='leo147-eth3',params1={'ip':'172.24.48.29/30'},infName2='leo167-eth3',params2={'ip':'172.24.48.30/30'})
        self.addLink(leo148,leo168,infName1='leo148-eth3',params1={'ip':'172.24.48.33/30'},infName2='leo168-eth3',params2={'ip':'172.24.48.34/30'})
        self.addLink(leo149,leo169,infName1='leo149-eth3',params1={'ip':'172.24.48.37/30'},infName2='leo169-eth3',params2={'ip':'172.24.48.38/30'})
        self.addLink(leo150,leo170,infName1='leo150-eth3',params1={'ip':'172.24.48.41/30'},infName2='leo170-eth3',params2={'ip':'172.24.48.42/30'})
        self.addLink(leo151,leo171,infName1='leo151-eth3',params1={'ip':'172.24.48.45/30'},infName2='leo171-eth3',params2={'ip':'172.24.48.46/30'})
        self.addLink(leo152,leo172,infName1='leo152-eth3',params1={'ip':'172.24.48.49/30'},infName2='leo172-eth3',params2={'ip':'172.24.48.50/30'})
        self.addLink(leo153,leo173,infName1='leo153-eth3',params1={'ip':'172.24.48.53/30'},infName2='leo173-eth3',params2={'ip':'172.24.48.54/30'})
        self.addLink(leo154,leo174,infName1='leo154-eth3',params1={'ip':'172.24.48.57/30'},infName2='leo174-eth3',params2={'ip':'172.24.48.58/30'})
        self.addLink(leo155,leo175,infName1='leo155-eth3',params1={'ip':'172.24.48.61/30'},infName2='leo175-eth3',params2={'ip':'172.24.48.62/30'})
        self.addLink(leo156,leo176,infName1='leo156-eth3',params1={'ip':'172.24.48.65/30'},infName2='leo176-eth3',params2={'ip':'172.24.48.66/30'})
        self.addLink(leo157,leo177,infName1='leo157-eth3',params1={'ip':'172.24.48.69/30'},infName2='leo177-eth3',params2={'ip':'172.24.48.70/30'})
        self.addLink(leo158,leo178,infName1='leo158-eth3',params1={'ip':'172.24.48.73/30'},infName2='leo178-eth3',params2={'ip':'172.24.48.74/30'})
        self.addLink(leo159,leo179,infName1='leo159-eth3',params1={'ip':'172.24.48.77/30'},infName2='leo179-eth3',params2={'ip':'172.24.48.78/30'})
        self.addLink(leo180,leo200,infName1='leo180-eth3',params1={'ip':'172.24.64.1/30'},infName2='leo200-eth3',params2={'ip':'172.24.64.2/30'})
        self.addLink(leo181,leo201,infName1='leo181-eth3',params1={'ip':'172.24.64.5/30'},infName2='leo201-eth3',params2={'ip':'172.24.64.6/30'})
        self.addLink(leo182,leo202,infName1='leo182-eth3',params1={'ip':'172.24.64.9/30'},infName2='leo202-eth3',params2={'ip':'172.24.64.10/30'})
        self.addLink(leo183,leo203,infName1='leo183-eth3',params1={'ip':'172.24.64.13/30'},infName2='leo203-eth3',params2={'ip':'172.24.64.14/30'})
        self.addLink(leo184,leo204,infName1='leo184-eth3',params1={'ip':'172.24.64.17/30'},infName2='leo204-eth3',params2={'ip':'172.24.64.18/30'})
        self.addLink(leo185,leo205,infName1='leo185-eth3',params1={'ip':'172.24.64.21/30'},infName2='leo205-eth3',params2={'ip':'172.24.64.22/30'})
        self.addLink(leo186,leo206,infName1='leo186-eth3',params1={'ip':'172.24.64.25/30'},infName2='leo206-eth3',params2={'ip':'172.24.64.26/30'})
        self.addLink(leo187,leo207,infName1='leo187-eth3',params1={'ip':'172.24.64.29/30'},infName2='leo207-eth3',params2={'ip':'172.24.64.30/30'})
        self.addLink(leo188,leo208,infName1='leo188-eth3',params1={'ip':'172.24.64.33/30'},infName2='leo208-eth3',params2={'ip':'172.24.64.34/30'})
        self.addLink(leo189,leo209,infName1='leo189-eth3',params1={'ip':'172.24.64.37/30'},infName2='leo209-eth3',params2={'ip':'172.24.64.38/30'})
        self.addLink(leo190,leo210,infName1='leo190-eth3',params1={'ip':'172.24.64.41/30'},infName2='leo210-eth3',params2={'ip':'172.24.64.42/30'})
        self.addLink(leo191,leo211,infName1='leo191-eth3',params1={'ip':'172.24.64.45/30'},infName2='leo211-eth3',params2={'ip':'172.24.64.46/30'})
        self.addLink(leo192,leo212,infName1='leo192-eth3',params1={'ip':'172.24.64.49/30'},infName2='leo212-eth3',params2={'ip':'172.24.64.50/30'})
        self.addLink(leo193,leo213,infName1='leo193-eth3',params1={'ip':'172.24.64.53/30'},infName2='leo213-eth3',params2={'ip':'172.24.64.54/30'})
        self.addLink(leo194,leo214,infName1='leo194-eth3',params1={'ip':'172.24.64.57/30'},infName2='leo214-eth3',params2={'ip':'172.24.64.58/30'})
        self.addLink(leo195,leo215,infName1='leo195-eth3',params1={'ip':'172.24.64.61/30'},infName2='leo215-eth3',params2={'ip':'172.24.64.62/30'})
        self.addLink(leo196,leo216,infName1='leo196-eth3',params1={'ip':'172.24.64.65/30'},infName2='leo216-eth3',params2={'ip':'172.24.64.66/30'})
        self.addLink(leo197,leo217,infName1='leo197-eth3',params1={'ip':'172.24.64.69/30'},infName2='leo217-eth3',params2={'ip':'172.24.64.70/30'})
        self.addLink(leo198,leo218,infName1='leo198-eth3',params1={'ip':'172.24.64.73/30'},infName2='leo218-eth3',params2={'ip':'172.24.64.74/30'})
        self.addLink(leo199,leo219,infName1='leo199-eth3',params1={'ip':'172.24.64.77/30'},infName2='leo219-eth3',params2={'ip':'172.24.64.78/30'})

        self.addLink(leo0,s1,intfName1='leo0-eth3',params1={'ip' : '10.0.0.1/24'}, port2=2000)
        self.addLink(leo1,s1,intfName1='leo1-eth3',params1={'ip' : '10.0.1.1/24'}, port2=2001)
        self.addLink(leo2,s1,intfName1='leo2-eth3',params1={'ip' : '10.0.2.1/24'}, port2=2002)
        self.addLink(leo3,s1,intfName1='leo3-eth3',params1={'ip' : '10.0.3.1/24'}, port2=2003)
        self.addLink(leo4,s1,intfName1='leo4-eth3',params1={'ip' : '10.0.4.1/24'}, port2=2004)
        self.addLink(leo5,s1,intfName1='leo5-eth3',params1={'ip' : '10.0.5.1/24'}, port2=2005)
        self.addLink(leo6,s1,intfName1='leo6-eth3',params1={'ip' : '10.0.6.1/24'}, port2=2006)
        self.addLink(leo7,s1,intfName1='leo7-eth3',params1={'ip' : '10.0.7.1/24'}, port2=2007)
        self.addLink(leo8,s1,intfName1='leo8-eth3',params1={'ip' : '10.0.8.1/24'}, port2=2008)
        self.addLink(leo9,s1,intfName1='leo9-eth3',params1={'ip' : '10.0.9.1/24'}, port2=2009)
        self.addLink(leo10,s1,intfName1='leo10-eth3',params1={'ip' : '10.0.10.1/24'}, port2=2010)
        self.addLink(leo11,s1,intfName1='leo11-eth3',params1={'ip' : '10.0.11.1/24'}, port2=2011)
        self.addLink(leo12,s1,intfName1='leo12-eth3',params1={'ip' : '10.0.12.1/24'}, port2=2012)
        self.addLink(leo13,s1,intfName1='leo13-eth3',params1={'ip' : '10.0.13.1/24'}, port2=2013)
        self.addLink(leo14,s1,intfName1='leo14-eth3',params1={'ip' : '10.0.14.1/24'}, port2=2014)
        self.addLink(leo15,s1,intfName1='leo15-eth3',params1={'ip' : '10.0.15.1/24'}, port2=2015)
        self.addLink(leo16,s1,intfName1='leo16-eth3',params1={'ip' : '10.0.16.1/24'}, port2=2016)
        self.addLink(leo17,s1,intfName1='leo17-eth3',params1={'ip' : '10.0.17.1/24'}, port2=2017)
        self.addLink(leo18,s1,intfName1='leo18-eth3',params1={'ip' : '10.0.18.1/24'}, port2=2018)
        self.addLink(leo19,s1,intfName1='leo19-eth3',params1={'ip' : '10.0.19.1/24'}, port2=2019)
        self.addLink(leo20,s1,intfName1='leo20-eth4',params1={'ip' : '10.1.0.1/24'}, port2=2020)
        self.addLink(leo21,s1,intfName1='leo21-eth4',params1={'ip' : '10.1.1.1/24'}, port2=2021)
        self.addLink(leo22,s1,intfName1='leo22-eth4',params1={'ip' : '10.1.2.1/24'}, port2=2022)
        self.addLink(leo23,s1,intfName1='leo23-eth4',params1={'ip' : '10.1.3.1/24'}, port2=2023)
        self.addLink(leo24,s1,intfName1='leo24-eth4',params1={'ip' : '10.1.4.1/24'}, port2=2024)
        self.addLink(leo25,s1,intfName1='leo25-eth4',params1={'ip' : '10.1.5.1/24'}, port2=2025)
        self.addLink(leo26,s1,intfName1='leo26-eth4',params1={'ip' : '10.1.6.1/24'}, port2=2026)
        self.addLink(leo27,s1,intfName1='leo27-eth4',params1={'ip' : '10.1.7.1/24'}, port2=2027)
        self.addLink(leo28,s1,intfName1='leo28-eth4',params1={'ip' : '10.1.8.1/24'}, port2=2028)
        self.addLink(leo29,s1,intfName1='leo29-eth4',params1={'ip' : '10.1.9.1/24'}, port2=2029)
        self.addLink(leo30,s1,intfName1='leo30-eth4',params1={'ip' : '10.1.10.1/24'}, port2=2030)
        self.addLink(leo31,s1,intfName1='leo31-eth4',params1={'ip' : '10.1.11.1/24'}, port2=2031)
        self.addLink(leo32,s1,intfName1='leo32-eth4',params1={'ip' : '10.1.12.1/24'}, port2=2032)
        self.addLink(leo33,s1,intfName1='leo33-eth4',params1={'ip' : '10.1.13.1/24'}, port2=2033)
        self.addLink(leo34,s1,intfName1='leo34-eth4',params1={'ip' : '10.1.14.1/24'}, port2=2034)
        self.addLink(leo35,s1,intfName1='leo35-eth4',params1={'ip' : '10.1.15.1/24'}, port2=2035)
        self.addLink(leo36,s1,intfName1='leo36-eth4',params1={'ip' : '10.1.16.1/24'}, port2=2036)
        self.addLink(leo37,s1,intfName1='leo37-eth4',params1={'ip' : '10.1.17.1/24'}, port2=2037)
        self.addLink(leo38,s1,intfName1='leo38-eth4',params1={'ip' : '10.1.18.1/24'}, port2=2038)
        self.addLink(leo39,s1,intfName1='leo39-eth4',params1={'ip' : '10.1.19.1/24'}, port2=2039)
        self.addLink(leo40,s1,intfName1='leo40-eth4',params1={'ip' : '10.2.19.1/24'}, port2=2040)
        self.addLink(leo41,s1,intfName1='leo41-eth4',params1={'ip' : '10.2.0.1/24'}, port2=2041)
        self.addLink(leo42,s1,intfName1='leo42-eth4',params1={'ip' : '10.2.1.1/24'}, port2=2042)
        self.addLink(leo43,s1,intfName1='leo43-eth4',params1={'ip' : '10.2.2.1/24'}, port2=2043)
        self.addLink(leo44,s1,intfName1='leo44-eth4',params1={'ip' : '10.2.3.1/24'}, port2=2044)
        self.addLink(leo45,s1,intfName1='leo45-eth4',params1={'ip' : '10.2.4.1/24'}, port2=2045)
        self.addLink(leo46,s1,intfName1='leo46-eth4',params1={'ip' : '10.2.5.1/24'}, port2=2046)
        self.addLink(leo47,s1,intfName1='leo47-eth4',params1={'ip' : '10.2.6.1/24'}, port2=2047)
        self.addLink(leo48,s1,intfName1='leo48-eth4',params1={'ip' : '10.2.7.1/24'}, port2=2048)
        self.addLink(leo49,s1,intfName1='leo49-eth4',params1={'ip' : '10.2.8.1/24'}, port2=2049)
        self.addLink(leo50,s1,intfName1='leo50-eth4',params1={'ip' : '10.2.9.1/24'}, port2=2050)
        self.addLink(leo51,s1,intfName1='leo51-eth4',params1={'ip' : '10.2.10.1/24'}, port2=2051)
        self.addLink(leo52,s1,intfName1='leo52-eth4',params1={'ip' : '10.2.11.1/24'}, port2=2052)
        self.addLink(leo53,s1,intfName1='leo53-eth4',params1={'ip' : '10.2.12.1/24'}, port2=2053)
        self.addLink(leo54,s1,intfName1='leo54-eth4',params1={'ip' : '10.2.13.1/24'}, port2=2054)
        self.addLink(leo55,s1,intfName1='leo55-eth4',params1={'ip' : '10.2.14.1/24'}, port2=2055)
        self.addLink(leo56,s1,intfName1='leo56-eth4',params1={'ip' : '10.2.15.1/24'}, port2=2056)
        self.addLink(leo57,s1,intfName1='leo57-eth4',params1={'ip' : '10.2.16.1/24'}, port2=2057)
        self.addLink(leo58,s1,intfName1='leo58-eth4',params1={'ip' : '10.2.17.1/24'}, port2=2058)
        self.addLink(leo59,s1,intfName1='leo59-eth4',params1={'ip' : '10.2.18.1/24'}, port2=2059)
        self.addLink(leo60,s1,intfName1='leo60-eth4',params1={'ip' : '10.3.19.1/24'}, port2=2060)
        self.addLink(leo61,s1,intfName1='leo61-eth4',params1={'ip' : '10.3.0.1/24'}, port2=2061)
        self.addLink(leo62,s1,intfName1='leo62-eth4',params1={'ip' : '10.3.1.1/24'}, port2=2062)
        self.addLink(leo63,s1,intfName1='leo63-eth4',params1={'ip' : '10.3.2.1/24'}, port2=2063)
        self.addLink(leo64,s1,intfName1='leo64-eth4',params1={'ip' : '10.3.3.1/24'}, port2=2064)
        self.addLink(leo65,s1,intfName1='leo65-eth4',params1={'ip' : '10.3.4.1/24'}, port2=2065)
        self.addLink(leo66,s1,intfName1='leo66-eth4',params1={'ip' : '10.3.5.1/24'}, port2=2066)
        self.addLink(leo67,s1,intfName1='leo67-eth4',params1={'ip' : '10.3.6.1/24'}, port2=2067)
        self.addLink(leo68,s1,intfName1='leo68-eth4',params1={'ip' : '10.3.7.1/24'}, port2=2068)
        self.addLink(leo69,s1,intfName1='leo69-eth4',params1={'ip' : '10.3.8.1/24'}, port2=2069)
        self.addLink(leo70,s1,intfName1='leo70-eth4',params1={'ip' : '10.3.9.1/24'}, port2=2070)
        self.addLink(leo71,s1,intfName1='leo71-eth4',params1={'ip' : '10.3.10.1/24'}, port2=2071)
        self.addLink(leo72,s1,intfName1='leo72-eth4',params1={'ip' : '10.3.11.1/24'}, port2=2072)
        self.addLink(leo73,s1,intfName1='leo73-eth4',params1={'ip' : '10.3.12.1/24'}, port2=2073)
        self.addLink(leo74,s1,intfName1='leo74-eth4',params1={'ip' : '10.3.13.1/24'}, port2=2074)
        self.addLink(leo75,s1,intfName1='leo75-eth4',params1={'ip' : '10.3.14.1/24'}, port2=2075)
        self.addLink(leo76,s1,intfName1='leo76-eth4',params1={'ip' : '10.3.15.1/24'}, port2=2076)
        self.addLink(leo77,s1,intfName1='leo77-eth4',params1={'ip' : '10.3.16.1/24'}, port2=2077)
        self.addLink(leo78,s1,intfName1='leo78-eth4',params1={'ip' : '10.3.17.1/24'}, port2=2078)
        self.addLink(leo79,s1,intfName1='leo79-eth4',params1={'ip' : '10.3.18.1/24'}, port2=2079)
        self.addLink(leo80,s1,intfName1='leo80-eth4',params1={'ip' : '10.4.18.1/24'}, port2=2080)
        self.addLink(leo81,s1,intfName1='leo81-eth4',params1={'ip' : '10.4.19.1/24'}, port2=2081)
        self.addLink(leo82,s1,intfName1='leo82-eth4',params1={'ip' : '10.4.0.1/24'}, port2=2082)
        self.addLink(leo83,s1,intfName1='leo83-eth4',params1={'ip' : '10.4.1.1/24'}, port2=2083)
        self.addLink(leo84,s1,intfName1='leo84-eth4',params1={'ip' : '10.4.2.1/24'}, port2=2084)
        self.addLink(leo85,s1,intfName1='leo85-eth4',params1={'ip' : '10.4.3.1/24'}, port2=2085)
        self.addLink(leo86,s1,intfName1='leo86-eth4',params1={'ip' : '10.4.4.1/24'}, port2=2086)
        self.addLink(leo87,s1,intfName1='leo87-eth4',params1={'ip' : '10.4.5.1/24'}, port2=2087)
        self.addLink(leo88,s1,intfName1='leo88-eth4',params1={'ip' : '10.4.6.1/24'}, port2=2088)
        self.addLink(leo89,s1,intfName1='leo89-eth4',params1={'ip' : '10.4.7.1/24'}, port2=2089)
        self.addLink(leo90,s1,intfName1='leo90-eth4',params1={'ip' : '10.4.8.1/24'}, port2=2090)
        self.addLink(leo91,s1,intfName1='leo91-eth4',params1={'ip' : '10.4.9.1/24'}, port2=2091)
        self.addLink(leo92,s1,intfName1='leo92-eth4',params1={'ip' : '10.4.10.1/24'}, port2=2092)
        self.addLink(leo93,s1,intfName1='leo93-eth4',params1={'ip' : '10.4.11.1/24'}, port2=2093)
        self.addLink(leo94,s1,intfName1='leo94-eth4',params1={'ip' : '10.4.12.1/24'}, port2=2094)
        self.addLink(leo95,s1,intfName1='leo95-eth4',params1={'ip' : '10.4.13.1/24'}, port2=2095)
        self.addLink(leo96,s1,intfName1='leo96-eth4',params1={'ip' : '10.4.14.1/24'}, port2=2096)
        self.addLink(leo97,s1,intfName1='leo97-eth4',params1={'ip' : '10.4.15.1/24'}, port2=2097)
        self.addLink(leo98,s1,intfName1='leo98-eth4',params1={'ip' : '10.4.16.1/24'}, port2=2098)
        self.addLink(leo99,s1,intfName1='leo99-eth4',params1={'ip' : '10.4.17.1/24'}, port2=2099)
        self.addLink(leo100,s1,intfName1='leo100-eth4',params1={'ip' : '10.5.18.1/24'}, port2=2100)
        self.addLink(leo101,s1,intfName1='leo101-eth4',params1={'ip' : '10.5.19.1/24'}, port2=2101)
        self.addLink(leo102,s1,intfName1='leo102-eth4',params1={'ip' : '10.5.0.1/24'}, port2=2102)
        self.addLink(leo103,s1,intfName1='leo103-eth4',params1={'ip' : '10.5.1.1/24'}, port2=2103)
        self.addLink(leo104,s1,intfName1='leo104-eth4',params1={'ip' : '10.5.2.1/24'}, port2=2104)
        self.addLink(leo105,s1,intfName1='leo105-eth4',params1={'ip' : '10.5.3.1/24'}, port2=2105)
        self.addLink(leo106,s1,intfName1='leo106-eth4',params1={'ip' : '10.5.4.1/24'}, port2=2106)
        self.addLink(leo107,s1,intfName1='leo107-eth4',params1={'ip' : '10.5.5.1/24'}, port2=2107)
        self.addLink(leo108,s1,intfName1='leo108-eth4',params1={'ip' : '10.5.6.1/24'}, port2=2108)
        self.addLink(leo109,s1,intfName1='leo109-eth4',params1={'ip' : '10.5.7.1/24'}, port2=2109)
        self.addLink(leo110,s1,intfName1='leo110-eth4',params1={'ip' : '10.5.8.1/24'}, port2=2110)
        self.addLink(leo111,s1,intfName1='leo111-eth4',params1={'ip' : '10.5.9.1/24'}, port2=2111)
        self.addLink(leo112,s1,intfName1='leo112-eth4',params1={'ip' : '10.5.10.1/24'}, port2=2112)
        self.addLink(leo113,s1,intfName1='leo113-eth4',params1={'ip' : '10.5.11.1/24'}, port2=2113)
        self.addLink(leo114,s1,intfName1='leo114-eth4',params1={'ip' : '10.5.12.1/24'}, port2=2114)
        self.addLink(leo115,s1,intfName1='leo115-eth4',params1={'ip' : '10.5.13.1/24'}, port2=2115)
        self.addLink(leo116,s1,intfName1='leo116-eth4',params1={'ip' : '10.5.14.1/24'}, port2=2116)
        self.addLink(leo117,s1,intfName1='leo117-eth4',params1={'ip' : '10.5.15.1/24'}, port2=2117)
        self.addLink(leo118,s1,intfName1='leo118-eth4',params1={'ip' : '10.5.16.1/24'}, port2=2118)
        self.addLink(leo119,s1,intfName1='leo119-eth4',params1={'ip' : '10.5.17.1/24'}, port2=2119)
        self.addLink(leo120,s1,intfName1='leo120-eth4',params1={'ip' : '10.6.17.1/24'}, port2=2120)
        self.addLink(leo121,s1,intfName1='leo121-eth4',params1={'ip' : '10.6.18.1/24'}, port2=2121)
        self.addLink(leo122,s1,intfName1='leo122-eth4',params1={'ip' : '10.6.19.1/24'}, port2=2122)
        self.addLink(leo123,s1,intfName1='leo123-eth4',params1={'ip' : '10.6.0.1/24'}, port2=2123)
        self.addLink(leo124,s1,intfName1='leo124-eth4',params1={'ip' : '10.6.1.1/24'}, port2=2124)
        self.addLink(leo125,s1,intfName1='leo125-eth4',params1={'ip' : '10.6.2.1/24'}, port2=2125)
        self.addLink(leo126,s1,intfName1='leo126-eth4',params1={'ip' : '10.6.3.1/24'}, port2=2126)
        self.addLink(leo127,s1,intfName1='leo127-eth4',params1={'ip' : '10.6.4.1/24'}, port2=2127)
        self.addLink(leo128,s1,intfName1='leo128-eth4',params1={'ip' : '10.6.5.1/24'}, port2=2128)
        self.addLink(leo129,s1,intfName1='leo129-eth4',params1={'ip' : '10.6.6.1/24'}, port2=2129)
        self.addLink(leo130,s1,intfName1='leo130-eth4',params1={'ip' : '10.6.7.1/24'}, port2=2130)
        self.addLink(leo131,s1,intfName1='leo131-eth4',params1={'ip' : '10.6.8.1/24'}, port2=2131)
        self.addLink(leo132,s1,intfName1='leo132-eth4',params1={'ip' : '10.6.9.1/24'}, port2=2132)
        self.addLink(leo133,s1,intfName1='leo133-eth4',params1={'ip' : '10.6.10.1/24'}, port2=2133)
        self.addLink(leo134,s1,intfName1='leo134-eth4',params1={'ip' : '10.6.11.1/24'}, port2=2134)
        self.addLink(leo135,s1,intfName1='leo135-eth4',params1={'ip' : '10.6.12.1/24'}, port2=2135)
        self.addLink(leo136,s1,intfName1='leo136-eth4',params1={'ip' : '10.6.13.1/24'}, port2=2136)
        self.addLink(leo137,s1,intfName1='leo137-eth4',params1={'ip' : '10.6.14.1/24'}, port2=2137)
        self.addLink(leo138,s1,intfName1='leo138-eth4',params1={'ip' : '10.6.15.1/24'}, port2=2138)
        self.addLink(leo139,s1,intfName1='leo139-eth4',params1={'ip' : '10.6.16.1/24'}, port2=2139)
        self.addLink(leo140,s1,intfName1='leo140-eth4',params1={'ip' : '10.7.17.1/24'}, port2=2140)
        self.addLink(leo141,s1,intfName1='leo141-eth4',params1={'ip' : '10.7.18.1/24'}, port2=2141)
        self.addLink(leo142,s1,intfName1='leo142-eth4',params1={'ip' : '10.7.19.1/24'}, port2=2142)
        self.addLink(leo143,s1,intfName1='leo143-eth4',params1={'ip' : '10.7.0.1/24'}, port2=2143)
        self.addLink(leo144,s1,intfName1='leo144-eth4',params1={'ip' : '10.7.1.1/24'}, port2=2144)
        self.addLink(leo145,s1,intfName1='leo145-eth4',params1={'ip' : '10.7.2.1/24'}, port2=2145)
        self.addLink(leo146,s1,intfName1='leo146-eth4',params1={'ip' : '10.7.3.1/24'}, port2=2146)
        self.addLink(leo147,s1,intfName1='leo147-eth4',params1={'ip' : '10.7.4.1/24'}, port2=2147)
        self.addLink(leo148,s1,intfName1='leo148-eth4',params1={'ip' : '10.7.5.1/24'}, port2=2148)
        self.addLink(leo149,s1,intfName1='leo149-eth4',params1={'ip' : '10.7.6.1/24'}, port2=2149)
        self.addLink(leo150,s1,intfName1='leo150-eth4',params1={'ip' : '10.7.7.1/24'}, port2=2150)
        self.addLink(leo151,s1,intfName1='leo151-eth4',params1={'ip' : '10.7.8.1/24'}, port2=2151)
        self.addLink(leo152,s1,intfName1='leo152-eth4',params1={'ip' : '10.7.9.1/24'}, port2=2152)
        self.addLink(leo153,s1,intfName1='leo153-eth4',params1={'ip' : '10.7.10.1/24'}, port2=2153)
        self.addLink(leo154,s1,intfName1='leo154-eth4',params1={'ip' : '10.7.11.1/24'}, port2=2154)
        self.addLink(leo155,s1,intfName1='leo155-eth4',params1={'ip' : '10.7.12.1/24'}, port2=2155)
        self.addLink(leo156,s1,intfName1='leo156-eth4',params1={'ip' : '10.7.13.1/24'}, port2=2156)
        self.addLink(leo157,s1,intfName1='leo157-eth4',params1={'ip' : '10.7.14.1/24'}, port2=2157)
        self.addLink(leo158,s1,intfName1='leo158-eth4',params1={'ip' : '10.7.15.1/24'}, port2=2158)
        self.addLink(leo159,s1,intfName1='leo159-eth4',params1={'ip' : '10.7.16.1/24'}, port2=2159)
        self.addLink(leo160,s1,intfName1='leo160-eth4',params1={'ip' : '10.8.16.1/24'}, port2=2160)
        self.addLink(leo161,s1,intfName1='leo161-eth4',params1={'ip' : '10.8.17.1/24'}, port2=2161)
        self.addLink(leo162,s1,intfName1='leo162-eth4',params1={'ip' : '10.8.18.1/24'}, port2=2162)
        self.addLink(leo163,s1,intfName1='leo163-eth4',params1={'ip' : '10.8.19.1/24'}, port2=2163)
        self.addLink(leo164,s1,intfName1='leo164-eth4',params1={'ip' : '10.8.0.1/24'}, port2=2164)
        self.addLink(leo165,s1,intfName1='leo165-eth4',params1={'ip' : '10.8.1.1/24'}, port2=2165)
        self.addLink(leo166,s1,intfName1='leo166-eth4',params1={'ip' : '10.8.2.1/24'}, port2=2166)
        self.addLink(leo167,s1,intfName1='leo167-eth4',params1={'ip' : '10.8.3.1/24'}, port2=2167)
        self.addLink(leo168,s1,intfName1='leo168-eth4',params1={'ip' : '10.8.4.1/24'}, port2=2168)
        self.addLink(leo169,s1,intfName1='leo169-eth4',params1={'ip' : '10.8.5.1/24'}, port2=2169)
        self.addLink(leo170,s1,intfName1='leo170-eth4',params1={'ip' : '10.8.6.1/24'}, port2=2170)
        self.addLink(leo171,s1,intfName1='leo171-eth4',params1={'ip' : '10.8.7.1/24'}, port2=2171)
        self.addLink(leo172,s1,intfName1='leo172-eth4',params1={'ip' : '10.8.8.1/24'}, port2=2172)
        self.addLink(leo173,s1,intfName1='leo173-eth4',params1={'ip' : '10.8.9.1/24'}, port2=2173)
        self.addLink(leo174,s1,intfName1='leo174-eth4',params1={'ip' : '10.8.10.1/24'}, port2=2174)
        self.addLink(leo175,s1,intfName1='leo175-eth4',params1={'ip' : '10.8.11.1/24'}, port2=2175)
        self.addLink(leo176,s1,intfName1='leo176-eth4',params1={'ip' : '10.8.12.1/24'}, port2=2176)
        self.addLink(leo177,s1,intfName1='leo177-eth4',params1={'ip' : '10.8.13.1/24'}, port2=2177)
        self.addLink(leo178,s1,intfName1='leo178-eth4',params1={'ip' : '10.8.14.1/24'}, port2=2178)
        self.addLink(leo179,s1,intfName1='leo179-eth4',params1={'ip' : '10.8.15.1/24'}, port2=2179)
        self.addLink(leo180,s1,intfName1='leo180-eth4',params1={'ip' : '10.9.16.1/24'}, port2=2180)
        self.addLink(leo181,s1,intfName1='leo181-eth4',params1={'ip' : '10.9.17.1/24'}, port2=2181)
        self.addLink(leo182,s1,intfName1='leo182-eth4',params1={'ip' : '10.9.18.1/24'}, port2=2182)
        self.addLink(leo183,s1,intfName1='leo183-eth4',params1={'ip' : '10.9.19.1/24'}, port2=2183)
        self.addLink(leo184,s1,intfName1='leo184-eth4',params1={'ip' : '10.9.0.1/24'}, port2=2184)
        self.addLink(leo185,s1,intfName1='leo185-eth4',params1={'ip' : '10.9.1.1/24'}, port2=2185)
        self.addLink(leo186,s1,intfName1='leo186-eth4',params1={'ip' : '10.9.2.1/24'}, port2=2186)
        self.addLink(leo187,s1,intfName1='leo187-eth4',params1={'ip' : '10.9.3.1/24'}, port2=2187)
        self.addLink(leo188,s1,intfName1='leo188-eth4',params1={'ip' : '10.9.4.1/24'}, port2=2188)
        self.addLink(leo189,s1,intfName1='leo189-eth4',params1={'ip' : '10.9.5.1/24'}, port2=2189)
        self.addLink(leo190,s1,intfName1='leo190-eth4',params1={'ip' : '10.9.6.1/24'}, port2=2190)
        self.addLink(leo191,s1,intfName1='leo191-eth4',params1={'ip' : '10.9.7.1/24'}, port2=2191)
        self.addLink(leo192,s1,intfName1='leo192-eth4',params1={'ip' : '10.9.8.1/24'}, port2=2192)
        self.addLink(leo193,s1,intfName1='leo193-eth4',params1={'ip' : '10.9.9.1/24'}, port2=2193)
        self.addLink(leo194,s1,intfName1='leo194-eth4',params1={'ip' : '10.9.10.1/24'}, port2=2194)
        self.addLink(leo195,s1,intfName1='leo195-eth4',params1={'ip' : '10.9.11.1/24'}, port2=2195)
        self.addLink(leo196,s1,intfName1='leo196-eth4',params1={'ip' : '10.9.12.1/24'}, port2=2196)
        self.addLink(leo197,s1,intfName1='leo197-eth4',params1={'ip' : '10.9.13.1/24'}, port2=2197)
        self.addLink(leo198,s1,intfName1='leo198-eth4',params1={'ip' : '10.9.14.1/24'}, port2=2198)
        self.addLink(leo199,s1,intfName1='leo199-eth4',params1={'ip' : '10.9.15.1/24'}, port2=2199)
        self.addLink(leo200,s1,intfName1='leo200-eth4',params1={'ip' : '10.10.15.1/24'}, port2=2200)
        self.addLink(leo201,s1,intfName1='leo201-eth4',params1={'ip' : '10.10.16.1/24'}, port2=2201)
        self.addLink(leo202,s1,intfName1='leo202-eth4',params1={'ip' : '10.10.17.1/24'}, port2=2202)
        self.addLink(leo203,s1,intfName1='leo203-eth4',params1={'ip' : '10.10.18.1/24'}, port2=2203)
        self.addLink(leo204,s1,intfName1='leo204-eth4',params1={'ip' : '10.10.19.1/24'}, port2=2204)
        self.addLink(leo205,s1,intfName1='leo205-eth4',params1={'ip' : '10.10.0.1/24'}, port2=2205)
        self.addLink(leo206,s1,intfName1='leo206-eth4',params1={'ip' : '10.10.1.1/24'}, port2=2206)
        self.addLink(leo207,s1,intfName1='leo207-eth4',params1={'ip' : '10.10.2.1/24'}, port2=2207)
        self.addLink(leo208,s1,intfName1='leo208-eth4',params1={'ip' : '10.10.3.1/24'}, port2=2208)
        self.addLink(leo209,s1,intfName1='leo209-eth4',params1={'ip' : '10.10.4.1/24'}, port2=2209)
        self.addLink(leo210,s1,intfName1='leo210-eth4',params1={'ip' : '10.10.5.1/24'}, port2=2210)
        self.addLink(leo211,s1,intfName1='leo211-eth4',params1={'ip' : '10.10.6.1/24'}, port2=2211)
        self.addLink(leo212,s1,intfName1='leo212-eth4',params1={'ip' : '10.10.7.1/24'}, port2=2212)
        self.addLink(leo213,s1,intfName1='leo213-eth4',params1={'ip' : '10.10.8.1/24'}, port2=2213)
        self.addLink(leo214,s1,intfName1='leo214-eth4',params1={'ip' : '10.10.9.1/24'}, port2=2214)
        self.addLink(leo215,s1,intfName1='leo215-eth4',params1={'ip' : '10.10.10.1/24'}, port2=2215)
        self.addLink(leo216,s1,intfName1='leo216-eth4',params1={'ip' : '10.10.11.1/24'}, port2=2216)
        self.addLink(leo217,s1,intfName1='leo217-eth4',params1={'ip' : '10.10.12.1/24'}, port2=2217)
        self.addLink(leo218,s1,intfName1='leo218-eth4',params1={'ip' : '10.10.13.1/24'}, port2=2218)
        self.addLink(leo219,s1,intfName1='leo219-eth4',params1={'ip' : '10.10.14.1/24'}, port2=2219)
        self.addLink(leo220,s1,intfName1='leo220-eth3',params1={'ip' : '10.11.15.1/24'}, port2=2220)
        self.addLink(leo221,s1,intfName1='leo221-eth3',params1={'ip' : '10.11.16.1/24'}, port2=2221)
        self.addLink(leo222,s1,intfName1='leo222-eth3',params1={'ip' : '10.11.17.1/24'}, port2=2222)
        self.addLink(leo223,s1,intfName1='leo223-eth3',params1={'ip' : '10.11.18.1/24'}, port2=2223)
        self.addLink(leo224,s1,intfName1='leo224-eth3',params1={'ip' : '10.11.19.1/24'}, port2=2224)
        self.addLink(leo225,s1,intfName1='leo225-eth3',params1={'ip' : '10.11.0.1/24'}, port2=2225)
        self.addLink(leo226,s1,intfName1='leo226-eth3',params1={'ip' : '10.11.1.1/24'}, port2=2226)
        self.addLink(leo227,s1,intfName1='leo227-eth3',params1={'ip' : '10.11.2.1/24'}, port2=2227)
        self.addLink(leo228,s1,intfName1='leo228-eth3',params1={'ip' : '10.11.3.1/24'}, port2=2228)
        self.addLink(leo229,s1,intfName1='leo229-eth3',params1={'ip' : '10.11.4.1/24'}, port2=2229)
        self.addLink(leo230,s1,intfName1='leo230-eth3',params1={'ip' : '10.11.5.1/24'}, port2=2230)
        self.addLink(leo231,s1,intfName1='leo231-eth3',params1={'ip' : '10.11.6.1/24'}, port2=2231)
        self.addLink(leo232,s1,intfName1='leo232-eth3',params1={'ip' : '10.11.7.1/24'}, port2=2232)
        self.addLink(leo233,s1,intfName1='leo233-eth3',params1={'ip' : '10.11.8.1/24'}, port2=2233)
        self.addLink(leo234,s1,intfName1='leo234-eth3',params1={'ip' : '10.11.9.1/24'}, port2=2234)
        self.addLink(leo235,s1,intfName1='leo235-eth3',params1={'ip' : '10.11.10.1/24'}, port2=2235)
        self.addLink(leo236,s1,intfName1='leo236-eth3',params1={'ip' : '10.11.11.1/24'}, port2=2236)
        self.addLink(leo237,s1,intfName1='leo237-eth3',params1={'ip' : '10.11.12.1/24'}, port2=2237)
        self.addLink(leo238,s1,intfName1='leo238-eth3',params1={'ip' : '10.11.13.1/24'}, port2=2238)
        self.addLink(leo239,s1,intfName1='leo239-eth3',params1={'ip' : '10.11.14.1/24'}, port2=2239)



        station0 = self.addNode('station0', cls = LinuxRouter, ip = '10.0.0.100/24')
        self.addLink(station0, s1, intfName1 = 'station0-eth0', params1 = {'ip' : '10.0.0.100/24'}, port2=240)
        station1 = self.addNode('station1', cls = LinuxRouter, ip = '10.0.2.100/24')
        self.addLink(station1, s1, intfName1 = 'station1-eth0', params1 = {'ip' : '10.0.2.100/24'}, port2=241)
        station2 = self.addNode('station2', cls = LinuxRouter, ip = '10.5.0.100/24')
        self.addLink(station2, s1, intfName1 = 'station2-eth0', params1 = {'ip' : '10.5.0.100/24'}, port2=242)

        self.addLink(station0, s1, intfName1 = 'station0-eth1', params1 = {'ip' : '114.114.114.1/24'}, port2=243)
        self.addLink(station1, s1, intfName1 = 'station1-eth1', params1 = {'ip' : '114.114.114.2/24'}, port2=244)
        self.addLink(station2, s1, intfName1 = 'station2-eth1', params1 = {'ip' : '114.114.114.3/24'}, port2=245)

        stationNAT = self.addNode('stationNAT', cls = LinuxRouter, ip = '114.114.114.114/24')
        self.addLink(stationNAT, s1, intfName1 = 'stationNAT-eth0', params1 = {'ip' : '114.114.114.114/24'}, port2 = 246)



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
        self.leo60=self.getNodeByName('leo60')
        self.leo61=self.getNodeByName('leo61')
        self.leo62=self.getNodeByName('leo62')
        self.leo63=self.getNodeByName('leo63')
        self.leo64=self.getNodeByName('leo64')
        self.leo65=self.getNodeByName('leo65')
        self.leo66=self.getNodeByName('leo66')
        self.leo67=self.getNodeByName('leo67')
        self.leo68=self.getNodeByName('leo68')
        self.leo69=self.getNodeByName('leo69')
        self.leo70=self.getNodeByName('leo70')
        self.leo71=self.getNodeByName('leo71')
        self.leo72=self.getNodeByName('leo72')
        self.leo73=self.getNodeByName('leo73')
        self.leo74=self.getNodeByName('leo74')
        self.leo75=self.getNodeByName('leo75')
        self.leo76=self.getNodeByName('leo76')
        self.leo77=self.getNodeByName('leo77')
        self.leo78=self.getNodeByName('leo78')
        self.leo79=self.getNodeByName('leo79')
        self.leo80=self.getNodeByName('leo80')
        self.leo81=self.getNodeByName('leo81')
        self.leo82=self.getNodeByName('leo82')
        self.leo83=self.getNodeByName('leo83')
        self.leo84=self.getNodeByName('leo84')
        self.leo85=self.getNodeByName('leo85')
        self.leo86=self.getNodeByName('leo86')
        self.leo87=self.getNodeByName('leo87')
        self.leo88=self.getNodeByName('leo88')
        self.leo89=self.getNodeByName('leo89')
        self.leo90=self.getNodeByName('leo90')
        self.leo91=self.getNodeByName('leo91')
        self.leo92=self.getNodeByName('leo92')
        self.leo93=self.getNodeByName('leo93')
        self.leo94=self.getNodeByName('leo94')
        self.leo95=self.getNodeByName('leo95')
        self.leo96=self.getNodeByName('leo96')
        self.leo97=self.getNodeByName('leo97')
        self.leo98=self.getNodeByName('leo98')
        self.leo99=self.getNodeByName('leo99')
        self.leo100=self.getNodeByName('leo100')
        self.leo101=self.getNodeByName('leo101')
        self.leo102=self.getNodeByName('leo102')
        self.leo103=self.getNodeByName('leo103')
        self.leo104=self.getNodeByName('leo104')
        self.leo105=self.getNodeByName('leo105')
        self.leo106=self.getNodeByName('leo106')
        self.leo107=self.getNodeByName('leo107')
        self.leo108=self.getNodeByName('leo108')
        self.leo109=self.getNodeByName('leo109')
        self.leo110=self.getNodeByName('leo110')
        self.leo111=self.getNodeByName('leo111')
        self.leo112=self.getNodeByName('leo112')
        self.leo113=self.getNodeByName('leo113')
        self.leo114=self.getNodeByName('leo114')
        self.leo115=self.getNodeByName('leo115')
        self.leo116=self.getNodeByName('leo116')
        self.leo117=self.getNodeByName('leo117')
        self.leo118=self.getNodeByName('leo118')
        self.leo119=self.getNodeByName('leo119')
        self.leo120=self.getNodeByName('leo120')
        self.leo121=self.getNodeByName('leo121')
        self.leo122=self.getNodeByName('leo122')
        self.leo123=self.getNodeByName('leo123')
        self.leo124=self.getNodeByName('leo124')
        self.leo125=self.getNodeByName('leo125')
        self.leo126=self.getNodeByName('leo126')
        self.leo127=self.getNodeByName('leo127')
        self.leo128=self.getNodeByName('leo128')
        self.leo129=self.getNodeByName('leo129')
        self.leo130=self.getNodeByName('leo130')
        self.leo131=self.getNodeByName('leo131')
        self.leo132=self.getNodeByName('leo132')
        self.leo133=self.getNodeByName('leo133')
        self.leo134=self.getNodeByName('leo134')
        self.leo135=self.getNodeByName('leo135')
        self.leo136=self.getNodeByName('leo136')
        self.leo137=self.getNodeByName('leo137')
        self.leo138=self.getNodeByName('leo138')
        self.leo139=self.getNodeByName('leo139')
        self.leo140=self.getNodeByName('leo140')
        self.leo141=self.getNodeByName('leo141')
        self.leo142=self.getNodeByName('leo142')
        self.leo143=self.getNodeByName('leo143')
        self.leo144=self.getNodeByName('leo144')
        self.leo145=self.getNodeByName('leo145')
        self.leo146=self.getNodeByName('leo146')
        self.leo147=self.getNodeByName('leo147')
        self.leo148=self.getNodeByName('leo148')
        self.leo149=self.getNodeByName('leo149')
        self.leo150=self.getNodeByName('leo150')
        self.leo151=self.getNodeByName('leo151')
        self.leo152=self.getNodeByName('leo152')
        self.leo153=self.getNodeByName('leo153')
        self.leo154=self.getNodeByName('leo154')
        self.leo155=self.getNodeByName('leo155')
        self.leo156=self.getNodeByName('leo156')
        self.leo157=self.getNodeByName('leo157')
        self.leo158=self.getNodeByName('leo158')
        self.leo159=self.getNodeByName('leo159')
        self.leo160=self.getNodeByName('leo160')
        self.leo161=self.getNodeByName('leo161')
        self.leo162=self.getNodeByName('leo162')
        self.leo163=self.getNodeByName('leo163')
        self.leo164=self.getNodeByName('leo164')
        self.leo165=self.getNodeByName('leo165')
        self.leo166=self.getNodeByName('leo166')
        self.leo167=self.getNodeByName('leo167')
        self.leo168=self.getNodeByName('leo168')
        self.leo169=self.getNodeByName('leo169')
        self.leo170=self.getNodeByName('leo170')
        self.leo171=self.getNodeByName('leo171')
        self.leo172=self.getNodeByName('leo172')
        self.leo173=self.getNodeByName('leo173')
        self.leo174=self.getNodeByName('leo174')
        self.leo175=self.getNodeByName('leo175')
        self.leo176=self.getNodeByName('leo176')
        self.leo177=self.getNodeByName('leo177')
        self.leo178=self.getNodeByName('leo178')
        self.leo179=self.getNodeByName('leo179')
        self.leo180=self.getNodeByName('leo180')
        self.leo181=self.getNodeByName('leo181')
        self.leo182=self.getNodeByName('leo182')
        self.leo183=self.getNodeByName('leo183')
        self.leo184=self.getNodeByName('leo184')
        self.leo185=self.getNodeByName('leo185')
        self.leo186=self.getNodeByName('leo186')
        self.leo187=self.getNodeByName('leo187')
        self.leo188=self.getNodeByName('leo188')
        self.leo189=self.getNodeByName('leo189')
        self.leo190=self.getNodeByName('leo190')
        self.leo191=self.getNodeByName('leo191')
        self.leo192=self.getNodeByName('leo192')
        self.leo193=self.getNodeByName('leo193')
        self.leo194=self.getNodeByName('leo194')
        self.leo195=self.getNodeByName('leo195')
        self.leo196=self.getNodeByName('leo196')
        self.leo197=self.getNodeByName('leo197')
        self.leo198=self.getNodeByName('leo198')
        self.leo199=self.getNodeByName('leo199')
        self.leo200=self.getNodeByName('leo200')
        self.leo201=self.getNodeByName('leo201')
        self.leo202=self.getNodeByName('leo202')
        self.leo203=self.getNodeByName('leo203')
        self.leo204=self.getNodeByName('leo204')
        self.leo205=self.getNodeByName('leo205')
        self.leo206=self.getNodeByName('leo206')
        self.leo207=self.getNodeByName('leo207')
        self.leo208=self.getNodeByName('leo208')
        self.leo209=self.getNodeByName('leo209')
        self.leo210=self.getNodeByName('leo210')
        self.leo211=self.getNodeByName('leo211')
        self.leo212=self.getNodeByName('leo212')
        self.leo213=self.getNodeByName('leo213')
        self.leo214=self.getNodeByName('leo214')
        self.leo215=self.getNodeByName('leo215')
        self.leo216=self.getNodeByName('leo216')
        self.leo217=self.getNodeByName('leo217')
        self.leo218=self.getNodeByName('leo218')
        self.leo219=self.getNodeByName('leo219')
        self.leo220=self.getNodeByName('leo220')
        self.leo221=self.getNodeByName('leo221')
        self.leo222=self.getNodeByName('leo222')
        self.leo223=self.getNodeByName('leo223')
        self.leo224=self.getNodeByName('leo224')
        self.leo225=self.getNodeByName('leo225')
        self.leo226=self.getNodeByName('leo226')
        self.leo227=self.getNodeByName('leo227')
        self.leo228=self.getNodeByName('leo228')
        self.leo229=self.getNodeByName('leo229')
        self.leo230=self.getNodeByName('leo230')
        self.leo231=self.getNodeByName('leo231')
        self.leo232=self.getNodeByName('leo232')
        self.leo233=self.getNodeByName('leo233')
        self.leo234=self.getNodeByName('leo234')
        self.leo235=self.getNodeByName('leo235')
        self.leo236=self.getNodeByName('leo236')
        self.leo237=self.getNodeByName('leo237')
        self.leo238=self.getNodeByName('leo238')
        self.leo239=self.getNodeByName('leo239')


        self.n=20
        self.P=12
        self.k=2
        self.phase=0
        self.phaseAll=80

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
        self.leodic[60]=self.leo60
        self.leodic[61]=self.leo61
        self.leodic[62]=self.leo62
        self.leodic[63]=self.leo63
        self.leodic[64]=self.leo64
        self.leodic[65]=self.leo65
        self.leodic[66]=self.leo66
        self.leodic[67]=self.leo67
        self.leodic[68]=self.leo68
        self.leodic[69]=self.leo69
        self.leodic[70]=self.leo70
        self.leodic[71]=self.leo71
        self.leodic[72]=self.leo72
        self.leodic[73]=self.leo73
        self.leodic[74]=self.leo74
        self.leodic[75]=self.leo75
        self.leodic[76]=self.leo76
        self.leodic[77]=self.leo77
        self.leodic[78]=self.leo78
        self.leodic[79]=self.leo79
        self.leodic[80]=self.leo80
        self.leodic[81]=self.leo81
        self.leodic[82]=self.leo82
        self.leodic[83]=self.leo83
        self.leodic[84]=self.leo84
        self.leodic[85]=self.leo85
        self.leodic[86]=self.leo86
        self.leodic[87]=self.leo87
        self.leodic[88]=self.leo88
        self.leodic[89]=self.leo89
        self.leodic[90]=self.leo90
        self.leodic[91]=self.leo91
        self.leodic[92]=self.leo92
        self.leodic[93]=self.leo93
        self.leodic[94]=self.leo94
        self.leodic[95]=self.leo95
        self.leodic[96]=self.leo96
        self.leodic[97]=self.leo97
        self.leodic[98]=self.leo98
        self.leodic[99]=self.leo99
        self.leodic[100]=self.leo100
        self.leodic[101]=self.leo101
        self.leodic[102]=self.leo102
        self.leodic[103]=self.leo103
        self.leodic[104]=self.leo104
        self.leodic[105]=self.leo105
        self.leodic[106]=self.leo106
        self.leodic[107]=self.leo107
        self.leodic[108]=self.leo108
        self.leodic[109]=self.leo109
        self.leodic[110]=self.leo110
        self.leodic[111]=self.leo111
        self.leodic[112]=self.leo112
        self.leodic[113]=self.leo113
        self.leodic[114]=self.leo114
        self.leodic[115]=self.leo115
        self.leodic[116]=self.leo116
        self.leodic[117]=self.leo117
        self.leodic[118]=self.leo118
        self.leodic[119]=self.leo119
        self.leodic[120]=self.leo120
        self.leodic[121]=self.leo121
        self.leodic[122]=self.leo122
        self.leodic[123]=self.leo123
        self.leodic[124]=self.leo124
        self.leodic[125]=self.leo125
        self.leodic[126]=self.leo126
        self.leodic[127]=self.leo127
        self.leodic[128]=self.leo128
        self.leodic[129]=self.leo129
        self.leodic[130]=self.leo130
        self.leodic[131]=self.leo131
        self.leodic[132]=self.leo132
        self.leodic[133]=self.leo133
        self.leodic[134]=self.leo134
        self.leodic[135]=self.leo135
        self.leodic[136]=self.leo136
        self.leodic[137]=self.leo137
        self.leodic[138]=self.leo138
        self.leodic[139]=self.leo139
        self.leodic[140]=self.leo140
        self.leodic[141]=self.leo141
        self.leodic[142]=self.leo142
        self.leodic[143]=self.leo143
        self.leodic[144]=self.leo144
        self.leodic[145]=self.leo145
        self.leodic[146]=self.leo146
        self.leodic[147]=self.leo147
        self.leodic[148]=self.leo148
        self.leodic[149]=self.leo149
        self.leodic[150]=self.leo150
        self.leodic[151]=self.leo151
        self.leodic[152]=self.leo152
        self.leodic[153]=self.leo153
        self.leodic[154]=self.leo154
        self.leodic[155]=self.leo155
        self.leodic[156]=self.leo156
        self.leodic[157]=self.leo157
        self.leodic[158]=self.leo158
        self.leodic[159]=self.leo159
        self.leodic[160]=self.leo160
        self.leodic[161]=self.leo161
        self.leodic[162]=self.leo162
        self.leodic[163]=self.leo163
        self.leodic[164]=self.leo164
        self.leodic[165]=self.leo165
        self.leodic[166]=self.leo166
        self.leodic[167]=self.leo167
        self.leodic[168]=self.leo168
        self.leodic[169]=self.leo169
        self.leodic[170]=self.leo170
        self.leodic[171]=self.leo171
        self.leodic[172]=self.leo172
        self.leodic[173]=self.leo173
        self.leodic[174]=self.leo174
        self.leodic[175]=self.leo175
        self.leodic[176]=self.leo176
        self.leodic[177]=self.leo177
        self.leodic[178]=self.leo178
        self.leodic[179]=self.leo179
        self.leodic[180]=self.leo180
        self.leodic[181]=self.leo181
        self.leodic[182]=self.leo182
        self.leodic[183]=self.leo183
        self.leodic[184]=self.leo184
        self.leodic[185]=self.leo185
        self.leodic[186]=self.leo186
        self.leodic[187]=self.leo187
        self.leodic[188]=self.leo188
        self.leodic[189]=self.leo189
        self.leodic[190]=self.leo190
        self.leodic[191]=self.leo191
        self.leodic[192]=self.leo192
        self.leodic[193]=self.leo193
        self.leodic[194]=self.leo194
        self.leodic[195]=self.leo195
        self.leodic[196]=self.leo196
        self.leodic[197]=self.leo197
        self.leodic[198]=self.leo198
        self.leodic[199]=self.leo199
        self.leodic[200]=self.leo200
        self.leodic[201]=self.leo201
        self.leodic[202]=self.leo202
        self.leodic[203]=self.leo203
        self.leodic[204]=self.leo204
        self.leodic[205]=self.leo205
        self.leodic[206]=self.leo206
        self.leodic[207]=self.leo207
        self.leodic[208]=self.leo208
        self.leodic[209]=self.leo209
        self.leodic[210]=self.leo210
        self.leodic[211]=self.leo211
        self.leodic[212]=self.leo212
        self.leodic[213]=self.leo213
        self.leodic[214]=self.leo214
        self.leodic[215]=self.leo215
        self.leodic[216]=self.leo216
        self.leodic[217]=self.leo217
        self.leodic[218]=self.leo218
        self.leodic[219]=self.leo219
        self.leodic[220]=self.leo220
        self.leodic[221]=self.leo221
        self.leodic[222]=self.leo222
        self.leodic[223]=self.leo223
        self.leodic[224]=self.leo224
        self.leodic[225]=self.leo225
        self.leodic[226]=self.leo226
        self.leodic[227]=self.leo227
        self.leodic[228]=self.leo228
        self.leodic[229]=self.leo229
        self.leodic[230]=self.leo230
        self.leodic[231]=self.leo231
        self.leodic[232]=self.leo232
        self.leodic[233]=self.leo233
        self.leodic[234]=self.leo234
        self.leodic[235]=self.leo235
        self.leodic[236]=self.leo236
        self.leodic[237]=self.leo237
        self.leodic[238]=self.leo238
        self.leodic[239]=self.leo239

        self.se_addr={}
        self.se_addr[0]='10.0.0.1/24'
        self.se_addr[1]='10.0.1.1/24'
        self.se_addr[2]='10.0.2.1/24'
        self.se_addr[3]='10.0.3.1/24'
        self.se_addr[4]='10.0.4.1/24'
        self.se_addr[5]='10.0.5.1/24'
        self.se_addr[6]='10.0.6.1/24'
        self.se_addr[7]='10.0.7.1/24'
        self.se_addr[8]='10.0.8.1/24'
        self.se_addr[9]='10.0.9.1/24'
        self.se_addr[10]='10.0.10.1/24'
        self.se_addr[11]='10.0.11.1/24'
        self.se_addr[12]='10.0.12.1/24'
        self.se_addr[13]='10.0.13.1/24'
        self.se_addr[14]='10.0.14.1/24'
        self.se_addr[15]='10.0.15.1/24'
        self.se_addr[16]='10.0.16.1/24'
        self.se_addr[17]='10.0.17.1/24'
        self.se_addr[18]='10.0.18.1/24'
        self.se_addr[19]='10.0.19.1/24'
        self.se_addr[20]='10.1.0.1/24'
        self.se_addr[21]='10.1.1.1/24'
        self.se_addr[22]='10.1.2.1/24'
        self.se_addr[23]='10.1.3.1/24'
        self.se_addr[24]='10.1.4.1/24'
        self.se_addr[25]='10.1.5.1/24'
        self.se_addr[26]='10.1.6.1/24'
        self.se_addr[27]='10.1.7.1/24'
        self.se_addr[28]='10.1.8.1/24'
        self.se_addr[29]='10.1.9.1/24'
        self.se_addr[30]='10.1.10.1/24'
        self.se_addr[31]='10.1.11.1/24'
        self.se_addr[32]='10.1.12.1/24'
        self.se_addr[33]='10.1.13.1/24'
        self.se_addr[34]='10.1.14.1/24'
        self.se_addr[35]='10.1.15.1/24'
        self.se_addr[36]='10.1.16.1/24'
        self.se_addr[37]='10.1.17.1/24'
        self.se_addr[38]='10.1.18.1/24'
        self.se_addr[39]='10.1.19.1/24'
        self.se_addr[40]='10.2.19.1/24'
        self.se_addr[41]='10.2.0.1/24'
        self.se_addr[42]='10.2.1.1/24'
        self.se_addr[43]='10.2.2.1/24'
        self.se_addr[44]='10.2.3.1/24'
        self.se_addr[45]='10.2.4.1/24'
        self.se_addr[46]='10.2.5.1/24'
        self.se_addr[47]='10.2.6.1/24'
        self.se_addr[48]='10.2.7.1/24'
        self.se_addr[49]='10.2.8.1/24'
        self.se_addr[50]='10.2.9.1/24'
        self.se_addr[51]='10.2.10.1/24'
        self.se_addr[52]='10.2.11.1/24'
        self.se_addr[53]='10.2.12.1/24'
        self.se_addr[54]='10.2.13.1/24'
        self.se_addr[55]='10.2.14.1/24'
        self.se_addr[56]='10.2.15.1/24'
        self.se_addr[57]='10.2.16.1/24'
        self.se_addr[58]='10.2.17.1/24'
        self.se_addr[59]='10.2.18.1/24'
        self.se_addr[60]='10.3.19.1/24'
        self.se_addr[61]='10.3.0.1/24'
        self.se_addr[62]='10.3.1.1/24'
        self.se_addr[63]='10.3.2.1/24'
        self.se_addr[64]='10.3.3.1/24'
        self.se_addr[65]='10.3.4.1/24'
        self.se_addr[66]='10.3.5.1/24'
        self.se_addr[67]='10.3.6.1/24'
        self.se_addr[68]='10.3.7.1/24'
        self.se_addr[69]='10.3.8.1/24'
        self.se_addr[70]='10.3.9.1/24'
        self.se_addr[71]='10.3.10.1/24'
        self.se_addr[72]='10.3.11.1/24'
        self.se_addr[73]='10.3.12.1/24'
        self.se_addr[74]='10.3.13.1/24'
        self.se_addr[75]='10.3.14.1/24'
        self.se_addr[76]='10.3.15.1/24'
        self.se_addr[77]='10.3.16.1/24'
        self.se_addr[78]='10.3.17.1/24'
        self.se_addr[79]='10.3.18.1/24'
        self.se_addr[80]='10.4.18.1/24'
        self.se_addr[81]='10.4.19.1/24'
        self.se_addr[82]='10.4.0.1/24'
        self.se_addr[83]='10.4.1.1/24'
        self.se_addr[84]='10.4.2.1/24'
        self.se_addr[85]='10.4.3.1/24'
        self.se_addr[86]='10.4.4.1/24'
        self.se_addr[87]='10.4.5.1/24'
        self.se_addr[88]='10.4.6.1/24'
        self.se_addr[89]='10.4.7.1/24'
        self.se_addr[90]='10.4.8.1/24'
        self.se_addr[91]='10.4.9.1/24'
        self.se_addr[92]='10.4.10.1/24'
        self.se_addr[93]='10.4.11.1/24'
        self.se_addr[94]='10.4.12.1/24'
        self.se_addr[95]='10.4.13.1/24'
        self.se_addr[96]='10.4.14.1/24'
        self.se_addr[97]='10.4.15.1/24'
        self.se_addr[98]='10.4.16.1/24'
        self.se_addr[99]='10.4.17.1/24'
        self.se_addr[100]='10.5.18.1/24'
        self.se_addr[101]='10.5.19.1/24'
        self.se_addr[102]='10.5.0.1/24'
        self.se_addr[103]='10.5.1.1/24'
        self.se_addr[104]='10.5.2.1/24'
        self.se_addr[105]='10.5.3.1/24'
        self.se_addr[106]='10.5.4.1/24'
        self.se_addr[107]='10.5.5.1/24'
        self.se_addr[108]='10.5.6.1/24'
        self.se_addr[109]='10.5.7.1/24'
        self.se_addr[110]='10.5.8.1/24'
        self.se_addr[111]='10.5.9.1/24'
        self.se_addr[112]='10.5.10.1/24'
        self.se_addr[113]='10.5.11.1/24'
        self.se_addr[114]='10.5.12.1/24'
        self.se_addr[115]='10.5.13.1/24'
        self.se_addr[116]='10.5.14.1/24'
        self.se_addr[117]='10.5.15.1/24'
        self.se_addr[118]='10.5.16.1/24'
        self.se_addr[119]='10.5.17.1/24'
        self.se_addr[120]='10.6.17.1/24'
        self.se_addr[121]='10.6.18.1/24'
        self.se_addr[122]='10.6.19.1/24'
        self.se_addr[123]='10.6.0.1/24'
        self.se_addr[124]='10.6.1.1/24'
        self.se_addr[125]='10.6.2.1/24'
        self.se_addr[126]='10.6.3.1/24'
        self.se_addr[127]='10.6.4.1/24'
        self.se_addr[128]='10.6.5.1/24'
        self.se_addr[129]='10.6.6.1/24'
        self.se_addr[130]='10.6.7.1/24'
        self.se_addr[131]='10.6.8.1/24'
        self.se_addr[132]='10.6.9.1/24'
        self.se_addr[133]='10.6.10.1/24'
        self.se_addr[134]='10.6.11.1/24'
        self.se_addr[135]='10.6.12.1/24'
        self.se_addr[136]='10.6.13.1/24'
        self.se_addr[137]='10.6.14.1/24'
        self.se_addr[138]='10.6.15.1/24'
        self.se_addr[139]='10.6.16.1/24'
        self.se_addr[140]='10.7.17.1/24'
        self.se_addr[141]='10.7.18.1/24'
        self.se_addr[142]='10.7.19.1/24'
        self.se_addr[143]='10.7.0.1/24'
        self.se_addr[144]='10.7.1.1/24'
        self.se_addr[145]='10.7.2.1/24'
        self.se_addr[146]='10.7.3.1/24'
        self.se_addr[147]='10.7.4.1/24'
        self.se_addr[148]='10.7.5.1/24'
        self.se_addr[149]='10.7.6.1/24'
        self.se_addr[150]='10.7.7.1/24'
        self.se_addr[151]='10.7.8.1/24'
        self.se_addr[152]='10.7.9.1/24'
        self.se_addr[153]='10.7.10.1/24'
        self.se_addr[154]='10.7.11.1/24'
        self.se_addr[155]='10.7.12.1/24'
        self.se_addr[156]='10.7.13.1/24'
        self.se_addr[157]='10.7.14.1/24'
        self.se_addr[158]='10.7.15.1/24'
        self.se_addr[159]='10.7.16.1/24'
        self.se_addr[160]='10.8.16.1/24'
        self.se_addr[161]='10.8.17.1/24'
        self.se_addr[162]='10.8.18.1/24'
        self.se_addr[163]='10.8.19.1/24'
        self.se_addr[164]='10.8.0.1/24'
        self.se_addr[165]='10.8.1.1/24'
        self.se_addr[166]='10.8.2.1/24'
        self.se_addr[167]='10.8.3.1/24'
        self.se_addr[168]='10.8.4.1/24'
        self.se_addr[169]='10.8.5.1/24'
        self.se_addr[170]='10.8.6.1/24'
        self.se_addr[171]='10.8.7.1/24'
        self.se_addr[172]='10.8.8.1/24'
        self.se_addr[173]='10.8.9.1/24'
        self.se_addr[174]='10.8.10.1/24'
        self.se_addr[175]='10.8.11.1/24'
        self.se_addr[176]='10.8.12.1/24'
        self.se_addr[177]='10.8.13.1/24'
        self.se_addr[178]='10.8.14.1/24'
        self.se_addr[179]='10.8.15.1/24'
        self.se_addr[180]='10.9.16.1/24'
        self.se_addr[181]='10.9.17.1/24'
        self.se_addr[182]='10.9.18.1/24'
        self.se_addr[183]='10.9.19.1/24'
        self.se_addr[184]='10.9.0.1/24'
        self.se_addr[185]='10.9.1.1/24'
        self.se_addr[186]='10.9.2.1/24'
        self.se_addr[187]='10.9.3.1/24'
        self.se_addr[188]='10.9.4.1/24'
        self.se_addr[189]='10.9.5.1/24'
        self.se_addr[190]='10.9.6.1/24'
        self.se_addr[191]='10.9.7.1/24'
        self.se_addr[192]='10.9.8.1/24'
        self.se_addr[193]='10.9.9.1/24'
        self.se_addr[194]='10.9.10.1/24'
        self.se_addr[195]='10.9.11.1/24'
        self.se_addr[196]='10.9.12.1/24'
        self.se_addr[197]='10.9.13.1/24'
        self.se_addr[198]='10.9.14.1/24'
        self.se_addr[199]='10.9.15.1/24'
        self.se_addr[200]='10.10.15.1/24'
        self.se_addr[201]='10.10.16.1/24'
        self.se_addr[202]='10.10.17.1/24'
        self.se_addr[203]='10.10.18.1/24'
        self.se_addr[204]='10.10.19.1/24'
        self.se_addr[205]='10.10.0.1/24'
        self.se_addr[206]='10.10.1.1/24'
        self.se_addr[207]='10.10.2.1/24'
        self.se_addr[208]='10.10.3.1/24'
        self.se_addr[209]='10.10.4.1/24'
        self.se_addr[210]='10.10.5.1/24'
        self.se_addr[211]='10.10.6.1/24'
        self.se_addr[212]='10.10.7.1/24'
        self.se_addr[213]='10.10.8.1/24'
        self.se_addr[214]='10.10.9.1/24'
        self.se_addr[215]='10.10.10.1/24'
        self.se_addr[216]='10.10.11.1/24'
        self.se_addr[217]='10.10.12.1/24'
        self.se_addr[218]='10.10.13.1/24'
        self.se_addr[219]='10.10.14.1/24'
        self.se_addr[220]='10.11.15.1/24'
        self.se_addr[221]='10.11.16.1/24'
        self.se_addr[222]='10.11.17.1/24'
        self.se_addr[223]='10.11.18.1/24'
        self.se_addr[224]='10.11.19.1/24'
        self.se_addr[225]='10.11.0.1/24'
        self.se_addr[226]='10.11.1.1/24'
        self.se_addr[227]='10.11.2.1/24'
        self.se_addr[228]='10.11.3.1/24'
        self.se_addr[229]='10.11.4.1/24'
        self.se_addr[230]='10.11.5.1/24'
        self.se_addr[231]='10.11.6.1/24'
        self.se_addr[232]='10.11.7.1/24'
        self.se_addr[233]='10.11.8.1/24'
        self.se_addr[234]='10.11.9.1/24'
        self.se_addr[235]='10.11.10.1/24'
        self.se_addr[236]='10.11.11.1/24'
        self.se_addr[237]='10.11.12.1/24'
        self.se_addr[238]='10.11.13.1/24'
        self.se_addr[239]='10.11.14.1/24'

        self.se_ethname={}
        self.se_ethname[0]='leo0-eth3'
        self.se_ethname[1]='leo1-eth3'
        self.se_ethname[2]='leo2-eth3'
        self.se_ethname[3]='leo3-eth3'
        self.se_ethname[4]='leo4-eth3'
        self.se_ethname[5]='leo5-eth3'
        self.se_ethname[6]='leo6-eth3'
        self.se_ethname[7]='leo7-eth3'
        self.se_ethname[8]='leo8-eth3'
        self.se_ethname[9]='leo9-eth3'
        self.se_ethname[10]='leo10-eth3'
        self.se_ethname[11]='leo11-eth3'
        self.se_ethname[12]='leo12-eth3'
        self.se_ethname[13]='leo13-eth3'
        self.se_ethname[14]='leo14-eth3'
        self.se_ethname[15]='leo15-eth3'
        self.se_ethname[16]='leo16-eth3'
        self.se_ethname[17]='leo17-eth3'
        self.se_ethname[18]='leo18-eth3'
        self.se_ethname[19]='leo19-eth3'
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
        self.se_ethname[54]='leo54-eth4'
        self.se_ethname[55]='leo55-eth4'
        self.se_ethname[56]='leo56-eth4'
        self.se_ethname[57]='leo57-eth4'
        self.se_ethname[58]='leo58-eth4'
        self.se_ethname[59]='leo59-eth4'
        self.se_ethname[60]='leo60-eth4'
        self.se_ethname[61]='leo61-eth4'
        self.se_ethname[62]='leo62-eth4'
        self.se_ethname[63]='leo63-eth4'
        self.se_ethname[64]='leo64-eth4'
        self.se_ethname[65]='leo65-eth4'
        self.se_ethname[66]='leo66-eth4'
        self.se_ethname[67]='leo67-eth4'
        self.se_ethname[68]='leo68-eth4'
        self.se_ethname[69]='leo69-eth4'
        self.se_ethname[70]='leo70-eth4'
        self.se_ethname[71]='leo71-eth4'
        self.se_ethname[72]='leo72-eth4'
        self.se_ethname[73]='leo73-eth4'
        self.se_ethname[74]='leo74-eth4'
        self.se_ethname[75]='leo75-eth4'
        self.se_ethname[76]='leo76-eth4'
        self.se_ethname[77]='leo77-eth4'
        self.se_ethname[78]='leo78-eth4'
        self.se_ethname[79]='leo79-eth4'
        self.se_ethname[80]='leo80-eth4'
        self.se_ethname[81]='leo81-eth4'
        self.se_ethname[82]='leo82-eth4'
        self.se_ethname[83]='leo83-eth4'
        self.se_ethname[84]='leo84-eth4'
        self.se_ethname[85]='leo85-eth4'
        self.se_ethname[86]='leo86-eth4'
        self.se_ethname[87]='leo87-eth4'
        self.se_ethname[88]='leo88-eth4'
        self.se_ethname[89]='leo89-eth4'
        self.se_ethname[90]='leo90-eth4'
        self.se_ethname[91]='leo91-eth4'
        self.se_ethname[92]='leo92-eth4'
        self.se_ethname[93]='leo93-eth4'
        self.se_ethname[94]='leo94-eth4'
        self.se_ethname[95]='leo95-eth4'
        self.se_ethname[96]='leo96-eth4'
        self.se_ethname[97]='leo97-eth4'
        self.se_ethname[98]='leo98-eth4'
        self.se_ethname[99]='leo99-eth4'
        self.se_ethname[100]='leo100-eth4'
        self.se_ethname[101]='leo101-eth4'
        self.se_ethname[102]='leo102-eth4'
        self.se_ethname[103]='leo103-eth4'
        self.se_ethname[104]='leo104-eth4'
        self.se_ethname[105]='leo105-eth4'
        self.se_ethname[106]='leo106-eth4'
        self.se_ethname[107]='leo107-eth4'
        self.se_ethname[108]='leo108-eth4'
        self.se_ethname[109]='leo109-eth4'
        self.se_ethname[110]='leo110-eth4'
        self.se_ethname[111]='leo111-eth4'
        self.se_ethname[112]='leo112-eth4'
        self.se_ethname[113]='leo113-eth4'
        self.se_ethname[114]='leo114-eth4'
        self.se_ethname[115]='leo115-eth4'
        self.se_ethname[116]='leo116-eth4'
        self.se_ethname[117]='leo117-eth4'
        self.se_ethname[118]='leo118-eth4'
        self.se_ethname[119]='leo119-eth4'
        self.se_ethname[120]='leo120-eth4'
        self.se_ethname[121]='leo121-eth4'
        self.se_ethname[122]='leo122-eth4'
        self.se_ethname[123]='leo123-eth4'
        self.se_ethname[124]='leo124-eth4'
        self.se_ethname[125]='leo125-eth4'
        self.se_ethname[126]='leo126-eth4'
        self.se_ethname[127]='leo127-eth4'
        self.se_ethname[128]='leo128-eth4'
        self.se_ethname[129]='leo129-eth4'
        self.se_ethname[130]='leo130-eth4'
        self.se_ethname[131]='leo131-eth4'
        self.se_ethname[132]='leo132-eth4'
        self.se_ethname[133]='leo133-eth4'
        self.se_ethname[134]='leo134-eth4'
        self.se_ethname[135]='leo135-eth4'
        self.se_ethname[136]='leo136-eth4'
        self.se_ethname[137]='leo137-eth4'
        self.se_ethname[138]='leo138-eth4'
        self.se_ethname[139]='leo139-eth4'
        self.se_ethname[140]='leo140-eth4'
        self.se_ethname[141]='leo141-eth4'
        self.se_ethname[142]='leo142-eth4'
        self.se_ethname[143]='leo143-eth4'
        self.se_ethname[144]='leo144-eth4'
        self.se_ethname[145]='leo145-eth4'
        self.se_ethname[146]='leo146-eth4'
        self.se_ethname[147]='leo147-eth4'
        self.se_ethname[148]='leo148-eth4'
        self.se_ethname[149]='leo149-eth4'
        self.se_ethname[150]='leo150-eth4'
        self.se_ethname[151]='leo151-eth4'
        self.se_ethname[152]='leo152-eth4'
        self.se_ethname[153]='leo153-eth4'
        self.se_ethname[154]='leo154-eth4'
        self.se_ethname[155]='leo155-eth4'
        self.se_ethname[156]='leo156-eth4'
        self.se_ethname[157]='leo157-eth4'
        self.se_ethname[158]='leo158-eth4'
        self.se_ethname[159]='leo159-eth4'
        self.se_ethname[160]='leo160-eth4'
        self.se_ethname[161]='leo161-eth4'
        self.se_ethname[162]='leo162-eth4'
        self.se_ethname[163]='leo163-eth4'
        self.se_ethname[164]='leo164-eth4'
        self.se_ethname[165]='leo165-eth4'
        self.se_ethname[166]='leo166-eth4'
        self.se_ethname[167]='leo167-eth4'
        self.se_ethname[168]='leo168-eth4'
        self.se_ethname[169]='leo169-eth4'
        self.se_ethname[170]='leo170-eth4'
        self.se_ethname[171]='leo171-eth4'
        self.se_ethname[172]='leo172-eth4'
        self.se_ethname[173]='leo173-eth4'
        self.se_ethname[174]='leo174-eth4'
        self.se_ethname[175]='leo175-eth4'
        self.se_ethname[176]='leo176-eth4'
        self.se_ethname[177]='leo177-eth4'
        self.se_ethname[178]='leo178-eth4'
        self.se_ethname[179]='leo179-eth4'
        self.se_ethname[180]='leo180-eth4'
        self.se_ethname[181]='leo181-eth4'
        self.se_ethname[182]='leo182-eth4'
        self.se_ethname[183]='leo183-eth4'
        self.se_ethname[184]='leo184-eth4'
        self.se_ethname[185]='leo185-eth4'
        self.se_ethname[186]='leo186-eth4'
        self.se_ethname[187]='leo187-eth4'
        self.se_ethname[188]='leo188-eth4'
        self.se_ethname[189]='leo189-eth4'
        self.se_ethname[190]='leo190-eth4'
        self.se_ethname[191]='leo191-eth4'
        self.se_ethname[192]='leo192-eth4'
        self.se_ethname[193]='leo193-eth4'
        self.se_ethname[194]='leo194-eth4'
        self.se_ethname[195]='leo195-eth4'
        self.se_ethname[196]='leo196-eth4'
        self.se_ethname[197]='leo197-eth4'
        self.se_ethname[198]='leo198-eth4'
        self.se_ethname[199]='leo199-eth4'
        self.se_ethname[200]='leo200-eth4'
        self.se_ethname[201]='leo201-eth4'
        self.se_ethname[202]='leo202-eth4'
        self.se_ethname[203]='leo203-eth4'
        self.se_ethname[204]='leo204-eth4'
        self.se_ethname[205]='leo205-eth4'
        self.se_ethname[206]='leo206-eth4'
        self.se_ethname[207]='leo207-eth4'
        self.se_ethname[208]='leo208-eth4'
        self.se_ethname[209]='leo209-eth4'
        self.se_ethname[210]='leo210-eth4'
        self.se_ethname[211]='leo211-eth4'
        self.se_ethname[212]='leo212-eth4'
        self.se_ethname[213]='leo213-eth4'
        self.se_ethname[214]='leo214-eth4'
        self.se_ethname[215]='leo215-eth4'
        self.se_ethname[216]='leo216-eth4'
        self.se_ethname[217]='leo217-eth4'
        self.se_ethname[218]='leo218-eth4'
        self.se_ethname[219]='leo219-eth4'
        self.se_ethname[220]='leo220-eth3'
        self.se_ethname[221]='leo221-eth3'
        self.se_ethname[222]='leo222-eth3'
        self.se_ethname[223]='leo223-eth3'
        self.se_ethname[224]='leo224-eth3'
        self.se_ethname[225]='leo225-eth3'
        self.se_ethname[226]='leo226-eth3'
        self.se_ethname[227]='leo227-eth3'
        self.se_ethname[228]='leo228-eth3'
        self.se_ethname[229]='leo229-eth3'
        self.se_ethname[230]='leo230-eth3'
        self.se_ethname[231]='leo231-eth3'
        self.se_ethname[232]='leo232-eth3'
        self.se_ethname[233]='leo233-eth3'
        self.se_ethname[234]='leo234-eth3'
        self.se_ethname[235]='leo235-eth3'
        self.se_ethname[236]='leo236-eth3'
        self.se_ethname[237]='leo237-eth3'
        self.se_ethname[238]='leo238-eth3'
        self.se_ethname[239]='leo239-eth3'

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
        self.orbit_k[10]=0
        self.orbit_k[11]=1


        self.tc_info_array={}
        self.tc_info_array[0]=tc_info(0,20,'leo0-eth2','leo20-eth2',[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        self.tc_info_array[1]=tc_info(1,21,'leo1-eth2','leo21-eth2',[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[2]=tc_info(2,22,'leo2-eth2','leo22-eth2',[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[3]=tc_info(3,23,'leo3-eth2','leo23-eth2',[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[4]=tc_info(4,24,'leo4-eth2','leo24-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[5]=tc_info(5,25,'leo5-eth2','leo25-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
        self.tc_info_array[6]=tc_info(6,26,'leo6-eth2','leo26-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
        self.tc_info_array[7]=tc_info(7,27,'leo7-eth2','leo27-eth2',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[8]=tc_info(8,28,'leo8-eth2','leo28-eth2',[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[9]=tc_info(9,29,'leo9-eth2','leo29-eth2',[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])
        self.tc_info_array[10]=tc_info(10,30,'leo10-eth2','leo30-eth2',[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        self.tc_info_array[11]=tc_info(11,31,'leo11-eth2','leo31-eth2',[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[12]=tc_info(12,32,'leo12-eth2','leo32-eth2',[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[13]=tc_info(13,33,'leo13-eth2','leo33-eth2',[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[14]=tc_info(14,34,'leo14-eth2','leo34-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[15]=tc_info(15,35,'leo15-eth2','leo35-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
        self.tc_info_array[16]=tc_info(16,36,'leo16-eth2','leo36-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
        self.tc_info_array[17]=tc_info(17,37,'leo17-eth2','leo37-eth2',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[18]=tc_info(18,38,'leo18-eth2','leo38-eth2',[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[19]=tc_info(19,39,'leo19-eth2','leo39-eth2',[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])
        self.tc_info_array[20]=tc_info(20,40,'leo20-eth3','leo40-eth3',[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1])
        self.tc_info_array[21]=tc_info(21,41,'leo21-eth3','leo41-eth3',[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[22]=tc_info(22,42,'leo22-eth3','leo42-eth3',[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[23]=tc_info(23,43,'leo23-eth3','leo43-eth3',[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[24]=tc_info(24,44,'leo24-eth3','leo44-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[25]=tc_info(25,45,'leo25-eth3','leo45-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[26]=tc_info(26,46,'leo26-eth3','leo46-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0])
        self.tc_info_array[27]=tc_info(27,47,'leo27-eth3','leo47-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
        self.tc_info_array[28]=tc_info(28,48,'leo28-eth3','leo48-eth3',[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[29]=tc_info(29,49,'leo29-eth3','leo49-eth3',[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1])
        self.tc_info_array[30]=tc_info(30,50,'leo30-eth3','leo50-eth3',[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1])
        self.tc_info_array[31]=tc_info(31,51,'leo31-eth3','leo51-eth3',[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[32]=tc_info(32,52,'leo32-eth3','leo52-eth3',[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[33]=tc_info(33,53,'leo33-eth3','leo53-eth3',[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[34]=tc_info(34,54,'leo34-eth3','leo54-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[35]=tc_info(35,55,'leo35-eth3','leo55-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[36]=tc_info(36,56,'leo36-eth3','leo56-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0])
        self.tc_info_array[37]=tc_info(37,57,'leo37-eth3','leo57-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
        self.tc_info_array[38]=tc_info(38,58,'leo38-eth3','leo58-eth3',[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[39]=tc_info(39,59,'leo39-eth3','leo59-eth3',[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1])
        self.tc_info_array[40]=tc_info(40,60,'leo40-eth2','leo60-eth2',[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[41]=tc_info(41,61,'leo41-eth2','leo61-eth2',[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])
        self.tc_info_array[42]=tc_info(42,62,'leo42-eth2','leo62-eth2',[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        self.tc_info_array[43]=tc_info(43,63,'leo43-eth2','leo63-eth2',[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[44]=tc_info(44,64,'leo44-eth2','leo64-eth2',[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[45]=tc_info(45,65,'leo45-eth2','leo65-eth2',[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[46]=tc_info(46,66,'leo46-eth2','leo66-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[47]=tc_info(47,67,'leo47-eth2','leo67-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
        self.tc_info_array[48]=tc_info(48,68,'leo48-eth2','leo68-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
        self.tc_info_array[49]=tc_info(49,69,'leo49-eth2','leo69-eth2',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[50]=tc_info(50,70,'leo50-eth2','leo70-eth2',[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[51]=tc_info(51,71,'leo51-eth2','leo71-eth2',[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])
        self.tc_info_array[52]=tc_info(52,72,'leo52-eth2','leo72-eth2',[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        self.tc_info_array[53]=tc_info(53,73,'leo53-eth2','leo73-eth2',[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[54]=tc_info(54,74,'leo54-eth2','leo74-eth2',[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[55]=tc_info(55,75,'leo55-eth2','leo75-eth2',[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[56]=tc_info(56,76,'leo56-eth2','leo76-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[57]=tc_info(57,77,'leo57-eth2','leo77-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
        self.tc_info_array[58]=tc_info(58,78,'leo58-eth2','leo78-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
        self.tc_info_array[59]=tc_info(59,79,'leo59-eth2','leo79-eth2',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[60]=tc_info(60,80,'leo60-eth3','leo80-eth3',[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[61]=tc_info(61,81,'leo61-eth3','leo81-eth3',[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1])
        self.tc_info_array[62]=tc_info(62,82,'leo62-eth3','leo82-eth3',[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1])
        self.tc_info_array[63]=tc_info(63,83,'leo63-eth3','leo83-eth3',[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[64]=tc_info(64,84,'leo64-eth3','leo84-eth3',[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[65]=tc_info(65,85,'leo65-eth3','leo85-eth3',[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[66]=tc_info(66,86,'leo66-eth3','leo86-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[67]=tc_info(67,87,'leo67-eth3','leo87-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[68]=tc_info(68,88,'leo68-eth3','leo88-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0])
        self.tc_info_array[69]=tc_info(69,89,'leo69-eth3','leo89-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
        self.tc_info_array[70]=tc_info(70,90,'leo70-eth3','leo90-eth3',[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[71]=tc_info(71,91,'leo71-eth3','leo91-eth3',[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1])
        self.tc_info_array[72]=tc_info(72,92,'leo72-eth3','leo92-eth3',[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1])
        self.tc_info_array[73]=tc_info(73,93,'leo73-eth3','leo93-eth3',[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[74]=tc_info(74,94,'leo74-eth3','leo94-eth3',[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[75]=tc_info(75,95,'leo75-eth3','leo95-eth3',[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[76]=tc_info(76,96,'leo76-eth3','leo96-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[77]=tc_info(77,97,'leo77-eth3','leo97-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[78]=tc_info(78,98,'leo78-eth3','leo98-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0])
        self.tc_info_array[79]=tc_info(79,99,'leo79-eth3','leo99-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
        self.tc_info_array[80]=tc_info(80,100,'leo80-eth2','leo100-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
        self.tc_info_array[81]=tc_info(81,101,'leo81-eth2','leo101-eth2',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[82]=tc_info(82,102,'leo82-eth2','leo102-eth2',[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[83]=tc_info(83,103,'leo83-eth2','leo103-eth2',[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])
        self.tc_info_array[84]=tc_info(84,104,'leo84-eth2','leo104-eth2',[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        self.tc_info_array[85]=tc_info(85,105,'leo85-eth2','leo105-eth2',[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[86]=tc_info(86,106,'leo86-eth2','leo106-eth2',[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[87]=tc_info(87,107,'leo87-eth2','leo107-eth2',[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[88]=tc_info(88,108,'leo88-eth2','leo108-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[89]=tc_info(89,109,'leo89-eth2','leo109-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
        self.tc_info_array[90]=tc_info(90,110,'leo90-eth2','leo110-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
        self.tc_info_array[91]=tc_info(91,111,'leo91-eth2','leo111-eth2',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[92]=tc_info(92,112,'leo92-eth2','leo112-eth2',[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[93]=tc_info(93,113,'leo93-eth2','leo113-eth2',[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])
        self.tc_info_array[94]=tc_info(94,114,'leo94-eth2','leo114-eth2',[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        self.tc_info_array[95]=tc_info(95,115,'leo95-eth2','leo115-eth2',[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[96]=tc_info(96,116,'leo96-eth2','leo116-eth2',[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[97]=tc_info(97,117,'leo97-eth2','leo117-eth2',[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[98]=tc_info(98,118,'leo98-eth2','leo118-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[99]=tc_info(99,119,'leo99-eth2','leo119-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
        self.tc_info_array[100]=tc_info(100,120,'leo100-eth3','leo120-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0])
        self.tc_info_array[101]=tc_info(101,121,'leo101-eth3','leo121-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
        self.tc_info_array[102]=tc_info(102,122,'leo102-eth3','leo122-eth3',[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[103]=tc_info(103,123,'leo103-eth3','leo123-eth3',[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1])
        self.tc_info_array[104]=tc_info(104,124,'leo104-eth3','leo124-eth3',[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1])
        self.tc_info_array[105]=tc_info(105,125,'leo105-eth3','leo125-eth3',[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[106]=tc_info(106,126,'leo106-eth3','leo126-eth3',[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[107]=tc_info(107,127,'leo107-eth3','leo127-eth3',[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[108]=tc_info(108,128,'leo108-eth3','leo128-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[109]=tc_info(109,129,'leo109-eth3','leo129-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[110]=tc_info(110,130,'leo110-eth3','leo130-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0])
        self.tc_info_array[111]=tc_info(111,131,'leo111-eth3','leo131-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
        self.tc_info_array[112]=tc_info(112,132,'leo112-eth3','leo132-eth3',[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[113]=tc_info(113,133,'leo113-eth3','leo133-eth3',[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1])
        self.tc_info_array[114]=tc_info(114,134,'leo114-eth3','leo134-eth3',[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1])
        self.tc_info_array[115]=tc_info(115,135,'leo115-eth3','leo135-eth3',[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[116]=tc_info(116,136,'leo116-eth3','leo136-eth3',[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[117]=tc_info(117,137,'leo117-eth3','leo137-eth3',[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[118]=tc_info(118,138,'leo118-eth3','leo138-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[119]=tc_info(119,139,'leo119-eth3','leo139-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[120]=tc_info(120,140,'leo120-eth2','leo140-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[121]=tc_info(121,141,'leo121-eth2','leo141-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
        self.tc_info_array[122]=tc_info(122,142,'leo122-eth2','leo142-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
        self.tc_info_array[123]=tc_info(123,143,'leo123-eth2','leo143-eth2',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[124]=tc_info(124,144,'leo124-eth2','leo144-eth2',[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[125]=tc_info(125,145,'leo125-eth2','leo145-eth2',[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])
        self.tc_info_array[126]=tc_info(126,146,'leo126-eth2','leo146-eth2',[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        self.tc_info_array[127]=tc_info(127,147,'leo127-eth2','leo147-eth2',[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[128]=tc_info(128,148,'leo128-eth2','leo148-eth2',[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[129]=tc_info(129,149,'leo129-eth2','leo149-eth2',[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[130]=tc_info(130,150,'leo130-eth2','leo150-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[131]=tc_info(131,151,'leo131-eth2','leo151-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
        self.tc_info_array[132]=tc_info(132,152,'leo132-eth2','leo152-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
        self.tc_info_array[133]=tc_info(133,153,'leo133-eth2','leo153-eth2',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[134]=tc_info(134,154,'leo134-eth2','leo154-eth2',[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[135]=tc_info(135,155,'leo135-eth2','leo155-eth2',[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])
        self.tc_info_array[136]=tc_info(136,156,'leo136-eth2','leo156-eth2',[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        self.tc_info_array[137]=tc_info(137,157,'leo137-eth2','leo157-eth2',[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[138]=tc_info(138,158,'leo138-eth2','leo158-eth2',[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[139]=tc_info(139,159,'leo139-eth2','leo159-eth2',[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[140]=tc_info(140,160,'leo140-eth3','leo160-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[141]=tc_info(141,161,'leo141-eth3','leo161-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[142]=tc_info(142,162,'leo142-eth3','leo162-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0])
        self.tc_info_array[143]=tc_info(143,163,'leo143-eth3','leo163-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
        self.tc_info_array[144]=tc_info(144,164,'leo144-eth3','leo164-eth3',[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[145]=tc_info(145,165,'leo145-eth3','leo165-eth3',[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1])
        self.tc_info_array[146]=tc_info(146,166,'leo146-eth3','leo166-eth3',[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1])
        self.tc_info_array[147]=tc_info(147,167,'leo147-eth3','leo167-eth3',[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[148]=tc_info(148,168,'leo148-eth3','leo168-eth3',[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[149]=tc_info(149,169,'leo149-eth3','leo169-eth3',[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[150]=tc_info(150,170,'leo150-eth3','leo170-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[151]=tc_info(151,171,'leo151-eth3','leo171-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[152]=tc_info(152,172,'leo152-eth3','leo172-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0])
        self.tc_info_array[153]=tc_info(153,173,'leo153-eth3','leo173-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
        self.tc_info_array[154]=tc_info(154,174,'leo154-eth3','leo174-eth3',[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[155]=tc_info(155,175,'leo155-eth3','leo175-eth3',[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1])
        self.tc_info_array[156]=tc_info(156,176,'leo156-eth3','leo176-eth3',[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1])
        self.tc_info_array[157]=tc_info(157,177,'leo157-eth3','leo177-eth3',[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[158]=tc_info(158,178,'leo158-eth3','leo178-eth3',[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[159]=tc_info(159,179,'leo159-eth3','leo179-eth3',[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[160]=tc_info(160,180,'leo160-eth2','leo180-eth2',[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[161]=tc_info(161,181,'leo161-eth2','leo181-eth2',[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[162]=tc_info(162,182,'leo162-eth2','leo182-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[163]=tc_info(163,183,'leo163-eth2','leo183-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
        self.tc_info_array[164]=tc_info(164,184,'leo164-eth2','leo184-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
        self.tc_info_array[165]=tc_info(165,185,'leo165-eth2','leo185-eth2',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[166]=tc_info(166,186,'leo166-eth2','leo186-eth2',[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[167]=tc_info(167,187,'leo167-eth2','leo187-eth2',[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])
        self.tc_info_array[168]=tc_info(168,188,'leo168-eth2','leo188-eth2',[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        self.tc_info_array[169]=tc_info(169,189,'leo169-eth2','leo189-eth2',[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[170]=tc_info(170,190,'leo170-eth2','leo190-eth2',[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[171]=tc_info(171,191,'leo171-eth2','leo191-eth2',[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[172]=tc_info(172,192,'leo172-eth2','leo192-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[173]=tc_info(173,193,'leo173-eth2','leo193-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
        self.tc_info_array[174]=tc_info(174,194,'leo174-eth2','leo194-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
        self.tc_info_array[175]=tc_info(175,195,'leo175-eth2','leo195-eth2',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[176]=tc_info(176,196,'leo176-eth2','leo196-eth2',[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[177]=tc_info(177,197,'leo177-eth2','leo197-eth2',[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])
        self.tc_info_array[178]=tc_info(178,198,'leo178-eth2','leo198-eth2',[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        self.tc_info_array[179]=tc_info(179,199,'leo179-eth2','leo199-eth2',[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[180]=tc_info(180,200,'leo180-eth3','leo200-eth3',[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[181]=tc_info(181,201,'leo181-eth3','leo201-eth3',[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[182]=tc_info(182,202,'leo182-eth3','leo202-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[183]=tc_info(183,203,'leo183-eth3','leo203-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[184]=tc_info(184,204,'leo184-eth3','leo204-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0])
        self.tc_info_array[185]=tc_info(185,205,'leo185-eth3','leo205-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
        self.tc_info_array[186]=tc_info(186,206,'leo186-eth3','leo206-eth3',[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[187]=tc_info(187,207,'leo187-eth3','leo207-eth3',[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1])
        self.tc_info_array[188]=tc_info(188,208,'leo188-eth3','leo208-eth3',[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1])
        self.tc_info_array[189]=tc_info(189,209,'leo189-eth3','leo209-eth3',[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[190]=tc_info(190,210,'leo190-eth3','leo210-eth3',[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[191]=tc_info(191,211,'leo191-eth3','leo211-eth3',[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[192]=tc_info(192,212,'leo192-eth3','leo212-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[193]=tc_info(193,213,'leo193-eth3','leo213-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[194]=tc_info(194,214,'leo194-eth3','leo214-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0])
        self.tc_info_array[195]=tc_info(195,215,'leo195-eth3','leo215-eth3',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0])
        self.tc_info_array[196]=tc_info(196,216,'leo196-eth3','leo216-eth3',[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[197]=tc_info(197,217,'leo197-eth3','leo217-eth3',[1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1])
        self.tc_info_array[198]=tc_info(198,218,'leo198-eth3','leo218-eth3',[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1])
        self.tc_info_array[199]=tc_info(199,219,'leo199-eth3','leo219-eth3',[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[200]=tc_info(200,220,'leo200-eth2','leo220-eth2',[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        self.tc_info_array[201]=tc_info(201,221,'leo201-eth2','leo221-eth2',[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[202]=tc_info(202,222,'leo202-eth2','leo222-eth2',[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[203]=tc_info(203,223,'leo203-eth2','leo223-eth2',[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[204]=tc_info(204,224,'leo204-eth2','leo224-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[205]=tc_info(205,225,'leo205-eth2','leo225-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
        self.tc_info_array[206]=tc_info(206,226,'leo206-eth2','leo226-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
        self.tc_info_array[207]=tc_info(207,227,'leo207-eth2','leo227-eth2',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[208]=tc_info(208,228,'leo208-eth2','leo228-eth2',[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[209]=tc_info(209,229,'leo209-eth2','leo229-eth2',[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])
        self.tc_info_array[210]=tc_info(210,230,'leo210-eth2','leo230-eth2',[1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
        self.tc_info_array[211]=tc_info(211,231,'leo211-eth2','leo231-eth2',[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[212]=tc_info(212,232,'leo212-eth2','leo232-eth2',[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[213]=tc_info(213,233,'leo213-eth2','leo233-eth2',[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[214]=tc_info(214,234,'leo214-eth2','leo234-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0])
        self.tc_info_array[215]=tc_info(215,235,'leo215-eth2','leo235-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0])
        self.tc_info_array[216]=tc_info(216,236,'leo216-eth2','leo236-eth2',[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0])
        self.tc_info_array[217]=tc_info(217,237,'leo217-eth2','leo237-eth2',[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[218]=tc_info(218,238,'leo218-eth2','leo238-eth2',[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1])
        self.tc_info_array[219]=tc_info(219,239,'leo219-eth2','leo239-eth2',[1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1])



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
                cmd_y = 'vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/se_add_y.conf -w /home/wyc/vtyzebra'+ str(i*self.n+j) +'.api -q /home/wyc/vtyospfd'+ str(i*self.n+j)  +'.api -r'
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
                cmd_x = 'vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/se_add_x.conf -w /home/wyc/vtyzebra'+ str(leo_num) +'.api -q /home/wyc/vtyospfd'+ str(leo_num)  +'.api -r'
                self.leodic[leo_num].cmd(cmd_x)
                print(cmd_x)


    def oa(self):
        self.leo0.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa0.conf -w /home/wyc/vtyzebra0.api -q /home/wyc/vtyospfd0.api -r")
        self.leo1.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa1.conf -w /home/wyc/vtyzebra1.api -q /home/wyc/vtyospfd1.api -r")
        self.leo2.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa2.conf -w /home/wyc/vtyzebra2.api -q /home/wyc/vtyospfd2.api -r")
        self.leo3.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa3.conf -w /home/wyc/vtyzebra3.api -q /home/wyc/vtyospfd3.api -r")
        self.leo4.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa4.conf -w /home/wyc/vtyzebra4.api -q /home/wyc/vtyospfd4.api -r")
        self.leo5.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa5.conf -w /home/wyc/vtyzebra5.api -q /home/wyc/vtyospfd5.api -r")
        self.leo6.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa6.conf -w /home/wyc/vtyzebra6.api -q /home/wyc/vtyospfd6.api -r")
        self.leo7.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa7.conf -w /home/wyc/vtyzebra7.api -q /home/wyc/vtyospfd7.api -r")
        self.leo8.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa8.conf -w /home/wyc/vtyzebra8.api -q /home/wyc/vtyospfd8.api -r")
        self.leo9.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa9.conf -w /home/wyc/vtyzebra9.api -q /home/wyc/vtyospfd9.api -r")
        self.leo10.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa10.conf -w /home/wyc/vtyzebra10.api -q /home/wyc/vtyospfd10.api -r")
        self.leo11.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa11.conf -w /home/wyc/vtyzebra11.api -q /home/wyc/vtyospfd11.api -r")
        self.leo12.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa12.conf -w /home/wyc/vtyzebra12.api -q /home/wyc/vtyospfd12.api -r")
        self.leo13.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa13.conf -w /home/wyc/vtyzebra13.api -q /home/wyc/vtyospfd13.api -r")
        self.leo14.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa14.conf -w /home/wyc/vtyzebra14.api -q /home/wyc/vtyospfd14.api -r")
        self.leo15.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa15.conf -w /home/wyc/vtyzebra15.api -q /home/wyc/vtyospfd15.api -r")
        self.leo16.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa16.conf -w /home/wyc/vtyzebra16.api -q /home/wyc/vtyospfd16.api -r")
        self.leo17.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa17.conf -w /home/wyc/vtyzebra17.api -q /home/wyc/vtyospfd17.api -r")
        self.leo18.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa18.conf -w /home/wyc/vtyzebra18.api -q /home/wyc/vtyospfd18.api -r")
        self.leo19.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa19.conf -w /home/wyc/vtyzebra19.api -q /home/wyc/vtyospfd19.api -r")
        self.leo20.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa20.conf -w /home/wyc/vtyzebra20.api -q /home/wyc/vtyospfd20.api -r")
        self.leo21.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa21.conf -w /home/wyc/vtyzebra21.api -q /home/wyc/vtyospfd21.api -r")
        self.leo22.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa22.conf -w /home/wyc/vtyzebra22.api -q /home/wyc/vtyospfd22.api -r")
        self.leo23.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa23.conf -w /home/wyc/vtyzebra23.api -q /home/wyc/vtyospfd23.api -r")
        self.leo24.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa24.conf -w /home/wyc/vtyzebra24.api -q /home/wyc/vtyospfd24.api -r")
        self.leo25.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa25.conf -w /home/wyc/vtyzebra25.api -q /home/wyc/vtyospfd25.api -r")
        self.leo26.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa26.conf -w /home/wyc/vtyzebra26.api -q /home/wyc/vtyospfd26.api -r")
        self.leo27.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa27.conf -w /home/wyc/vtyzebra27.api -q /home/wyc/vtyospfd27.api -r")
        self.leo28.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa28.conf -w /home/wyc/vtyzebra28.api -q /home/wyc/vtyospfd28.api -r")
        self.leo29.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa29.conf -w /home/wyc/vtyzebra29.api -q /home/wyc/vtyospfd29.api -r")
        self.leo30.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa30.conf -w /home/wyc/vtyzebra30.api -q /home/wyc/vtyospfd30.api -r")
        self.leo31.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa31.conf -w /home/wyc/vtyzebra31.api -q /home/wyc/vtyospfd31.api -r")
        self.leo32.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa32.conf -w /home/wyc/vtyzebra32.api -q /home/wyc/vtyospfd32.api -r")
        self.leo33.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa33.conf -w /home/wyc/vtyzebra33.api -q /home/wyc/vtyospfd33.api -r")
        self.leo34.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa34.conf -w /home/wyc/vtyzebra34.api -q /home/wyc/vtyospfd34.api -r")
        self.leo35.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa35.conf -w /home/wyc/vtyzebra35.api -q /home/wyc/vtyospfd35.api -r")
        self.leo36.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa36.conf -w /home/wyc/vtyzebra36.api -q /home/wyc/vtyospfd36.api -r")
        self.leo37.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa37.conf -w /home/wyc/vtyzebra37.api -q /home/wyc/vtyospfd37.api -r")
        self.leo38.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa38.conf -w /home/wyc/vtyzebra38.api -q /home/wyc/vtyospfd38.api -r")
        self.leo39.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa39.conf -w /home/wyc/vtyzebra39.api -q /home/wyc/vtyospfd39.api -r")
        self.leo40.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa40.conf -w /home/wyc/vtyzebra40.api -q /home/wyc/vtyospfd40.api -r")
        self.leo41.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa41.conf -w /home/wyc/vtyzebra41.api -q /home/wyc/vtyospfd41.api -r")
        self.leo42.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa42.conf -w /home/wyc/vtyzebra42.api -q /home/wyc/vtyospfd42.api -r")
        self.leo43.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa43.conf -w /home/wyc/vtyzebra43.api -q /home/wyc/vtyospfd43.api -r")
        self.leo44.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa44.conf -w /home/wyc/vtyzebra44.api -q /home/wyc/vtyospfd44.api -r")
        self.leo45.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa45.conf -w /home/wyc/vtyzebra45.api -q /home/wyc/vtyospfd45.api -r")
        self.leo46.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa46.conf -w /home/wyc/vtyzebra46.api -q /home/wyc/vtyospfd46.api -r")
        self.leo47.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa47.conf -w /home/wyc/vtyzebra47.api -q /home/wyc/vtyospfd47.api -r")
        self.leo48.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa48.conf -w /home/wyc/vtyzebra48.api -q /home/wyc/vtyospfd48.api -r")
        self.leo49.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa49.conf -w /home/wyc/vtyzebra49.api -q /home/wyc/vtyospfd49.api -r")
        self.leo50.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa50.conf -w /home/wyc/vtyzebra50.api -q /home/wyc/vtyospfd50.api -r")
        self.leo51.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa51.conf -w /home/wyc/vtyzebra51.api -q /home/wyc/vtyospfd51.api -r")
        self.leo52.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa52.conf -w /home/wyc/vtyzebra52.api -q /home/wyc/vtyospfd52.api -r")
        self.leo53.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa53.conf -w /home/wyc/vtyzebra53.api -q /home/wyc/vtyospfd53.api -r")
        self.leo54.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa54.conf -w /home/wyc/vtyzebra54.api -q /home/wyc/vtyospfd54.api -r")
        self.leo55.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa55.conf -w /home/wyc/vtyzebra55.api -q /home/wyc/vtyospfd55.api -r")
        self.leo56.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa56.conf -w /home/wyc/vtyzebra56.api -q /home/wyc/vtyospfd56.api -r")
        self.leo57.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa57.conf -w /home/wyc/vtyzebra57.api -q /home/wyc/vtyospfd57.api -r")
        self.leo58.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa58.conf -w /home/wyc/vtyzebra58.api -q /home/wyc/vtyospfd58.api -r")
        self.leo59.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa59.conf -w /home/wyc/vtyzebra59.api -q /home/wyc/vtyospfd59.api -r")
        self.leo60.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa60.conf -w /home/wyc/vtyzebra60.api -q /home/wyc/vtyospfd60.api -r")
        self.leo61.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa61.conf -w /home/wyc/vtyzebra61.api -q /home/wyc/vtyospfd61.api -r")
        self.leo62.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa62.conf -w /home/wyc/vtyzebra62.api -q /home/wyc/vtyospfd62.api -r")
        self.leo63.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa63.conf -w /home/wyc/vtyzebra63.api -q /home/wyc/vtyospfd63.api -r")
        self.leo64.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa64.conf -w /home/wyc/vtyzebra64.api -q /home/wyc/vtyospfd64.api -r")
        self.leo65.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa65.conf -w /home/wyc/vtyzebra65.api -q /home/wyc/vtyospfd65.api -r")
        self.leo66.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa66.conf -w /home/wyc/vtyzebra66.api -q /home/wyc/vtyospfd66.api -r")
        self.leo67.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa67.conf -w /home/wyc/vtyzebra67.api -q /home/wyc/vtyospfd67.api -r")
        self.leo68.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa68.conf -w /home/wyc/vtyzebra68.api -q /home/wyc/vtyospfd68.api -r")
        self.leo69.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa69.conf -w /home/wyc/vtyzebra69.api -q /home/wyc/vtyospfd69.api -r")
        self.leo70.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa70.conf -w /home/wyc/vtyzebra70.api -q /home/wyc/vtyospfd70.api -r")
        self.leo71.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa71.conf -w /home/wyc/vtyzebra71.api -q /home/wyc/vtyospfd71.api -r")
        self.leo72.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa72.conf -w /home/wyc/vtyzebra72.api -q /home/wyc/vtyospfd72.api -r")
        self.leo73.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa73.conf -w /home/wyc/vtyzebra73.api -q /home/wyc/vtyospfd73.api -r")
        self.leo74.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa74.conf -w /home/wyc/vtyzebra74.api -q /home/wyc/vtyospfd74.api -r")
        self.leo75.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa75.conf -w /home/wyc/vtyzebra75.api -q /home/wyc/vtyospfd75.api -r")
        self.leo76.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa76.conf -w /home/wyc/vtyzebra76.api -q /home/wyc/vtyospfd76.api -r")
        self.leo77.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa77.conf -w /home/wyc/vtyzebra77.api -q /home/wyc/vtyospfd77.api -r")
        self.leo78.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa78.conf -w /home/wyc/vtyzebra78.api -q /home/wyc/vtyospfd78.api -r")
        self.leo79.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa79.conf -w /home/wyc/vtyzebra79.api -q /home/wyc/vtyospfd79.api -r")
        self.leo80.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa80.conf -w /home/wyc/vtyzebra80.api -q /home/wyc/vtyospfd80.api -r")
        self.leo81.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa81.conf -w /home/wyc/vtyzebra81.api -q /home/wyc/vtyospfd81.api -r")
        self.leo82.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa82.conf -w /home/wyc/vtyzebra82.api -q /home/wyc/vtyospfd82.api -r")
        self.leo83.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa83.conf -w /home/wyc/vtyzebra83.api -q /home/wyc/vtyospfd83.api -r")
        self.leo84.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa84.conf -w /home/wyc/vtyzebra84.api -q /home/wyc/vtyospfd84.api -r")
        self.leo85.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa85.conf -w /home/wyc/vtyzebra85.api -q /home/wyc/vtyospfd85.api -r")
        self.leo86.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa86.conf -w /home/wyc/vtyzebra86.api -q /home/wyc/vtyospfd86.api -r")
        self.leo87.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa87.conf -w /home/wyc/vtyzebra87.api -q /home/wyc/vtyospfd87.api -r")
        self.leo88.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa88.conf -w /home/wyc/vtyzebra88.api -q /home/wyc/vtyospfd88.api -r")
        self.leo89.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa89.conf -w /home/wyc/vtyzebra89.api -q /home/wyc/vtyospfd89.api -r")
        self.leo90.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa90.conf -w /home/wyc/vtyzebra90.api -q /home/wyc/vtyospfd90.api -r")
        self.leo91.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa91.conf -w /home/wyc/vtyzebra91.api -q /home/wyc/vtyospfd91.api -r")
        self.leo92.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa92.conf -w /home/wyc/vtyzebra92.api -q /home/wyc/vtyospfd92.api -r")
        self.leo93.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa93.conf -w /home/wyc/vtyzebra93.api -q /home/wyc/vtyospfd93.api -r")
        self.leo94.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa94.conf -w /home/wyc/vtyzebra94.api -q /home/wyc/vtyospfd94.api -r")
        self.leo95.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa95.conf -w /home/wyc/vtyzebra95.api -q /home/wyc/vtyospfd95.api -r")
        self.leo96.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa96.conf -w /home/wyc/vtyzebra96.api -q /home/wyc/vtyospfd96.api -r")
        self.leo97.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa97.conf -w /home/wyc/vtyzebra97.api -q /home/wyc/vtyospfd97.api -r")
        self.leo98.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa98.conf -w /home/wyc/vtyzebra98.api -q /home/wyc/vtyospfd98.api -r")
        self.leo99.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa99.conf -w /home/wyc/vtyzebra99.api -q /home/wyc/vtyospfd99.api -r")
        self.leo100.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa100.conf -w /home/wyc/vtyzebra100.api -q /home/wyc/vtyospfd100.api -r")
        self.leo101.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa101.conf -w /home/wyc/vtyzebra101.api -q /home/wyc/vtyospfd101.api -r")
        self.leo102.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa102.conf -w /home/wyc/vtyzebra102.api -q /home/wyc/vtyospfd102.api -r")
        self.leo103.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa103.conf -w /home/wyc/vtyzebra103.api -q /home/wyc/vtyospfd103.api -r")
        self.leo104.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa104.conf -w /home/wyc/vtyzebra104.api -q /home/wyc/vtyospfd104.api -r")
        self.leo105.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa105.conf -w /home/wyc/vtyzebra105.api -q /home/wyc/vtyospfd105.api -r")
        self.leo106.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa106.conf -w /home/wyc/vtyzebra106.api -q /home/wyc/vtyospfd106.api -r")
        self.leo107.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa107.conf -w /home/wyc/vtyzebra107.api -q /home/wyc/vtyospfd107.api -r")
        self.leo108.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa108.conf -w /home/wyc/vtyzebra108.api -q /home/wyc/vtyospfd108.api -r")
        self.leo109.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa109.conf -w /home/wyc/vtyzebra109.api -q /home/wyc/vtyospfd109.api -r")
        self.leo110.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa110.conf -w /home/wyc/vtyzebra110.api -q /home/wyc/vtyospfd110.api -r")
        self.leo111.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa111.conf -w /home/wyc/vtyzebra111.api -q /home/wyc/vtyospfd111.api -r")
        self.leo112.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa112.conf -w /home/wyc/vtyzebra112.api -q /home/wyc/vtyospfd112.api -r")
        self.leo113.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa113.conf -w /home/wyc/vtyzebra113.api -q /home/wyc/vtyospfd113.api -r")
        self.leo114.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa114.conf -w /home/wyc/vtyzebra114.api -q /home/wyc/vtyospfd114.api -r")
        self.leo115.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa115.conf -w /home/wyc/vtyzebra115.api -q /home/wyc/vtyospfd115.api -r")
        self.leo116.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa116.conf -w /home/wyc/vtyzebra116.api -q /home/wyc/vtyospfd116.api -r")
        self.leo117.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa117.conf -w /home/wyc/vtyzebra117.api -q /home/wyc/vtyospfd117.api -r")
        self.leo118.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa118.conf -w /home/wyc/vtyzebra118.api -q /home/wyc/vtyospfd118.api -r")
        self.leo119.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa119.conf -w /home/wyc/vtyzebra119.api -q /home/wyc/vtyospfd119.api -r")
        self.leo120.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa120.conf -w /home/wyc/vtyzebra120.api -q /home/wyc/vtyospfd120.api -r")
        self.leo121.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa121.conf -w /home/wyc/vtyzebra121.api -q /home/wyc/vtyospfd121.api -r")
        self.leo122.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa122.conf -w /home/wyc/vtyzebra122.api -q /home/wyc/vtyospfd122.api -r")
        self.leo123.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa123.conf -w /home/wyc/vtyzebra123.api -q /home/wyc/vtyospfd123.api -r")
        self.leo124.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa124.conf -w /home/wyc/vtyzebra124.api -q /home/wyc/vtyospfd124.api -r")
        self.leo125.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa125.conf -w /home/wyc/vtyzebra125.api -q /home/wyc/vtyospfd125.api -r")
        self.leo126.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa126.conf -w /home/wyc/vtyzebra126.api -q /home/wyc/vtyospfd126.api -r")
        self.leo127.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa127.conf -w /home/wyc/vtyzebra127.api -q /home/wyc/vtyospfd127.api -r")
        self.leo128.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa128.conf -w /home/wyc/vtyzebra128.api -q /home/wyc/vtyospfd128.api -r")
        self.leo129.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa129.conf -w /home/wyc/vtyzebra129.api -q /home/wyc/vtyospfd129.api -r")
        self.leo130.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa130.conf -w /home/wyc/vtyzebra130.api -q /home/wyc/vtyospfd130.api -r")
        self.leo131.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa131.conf -w /home/wyc/vtyzebra131.api -q /home/wyc/vtyospfd131.api -r")
        self.leo132.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa132.conf -w /home/wyc/vtyzebra132.api -q /home/wyc/vtyospfd132.api -r")
        self.leo133.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa133.conf -w /home/wyc/vtyzebra133.api -q /home/wyc/vtyospfd133.api -r")
        self.leo134.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa134.conf -w /home/wyc/vtyzebra134.api -q /home/wyc/vtyospfd134.api -r")
        self.leo135.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa135.conf -w /home/wyc/vtyzebra135.api -q /home/wyc/vtyospfd135.api -r")
        self.leo136.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa136.conf -w /home/wyc/vtyzebra136.api -q /home/wyc/vtyospfd136.api -r")
        self.leo137.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa137.conf -w /home/wyc/vtyzebra137.api -q /home/wyc/vtyospfd137.api -r")
        self.leo138.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa138.conf -w /home/wyc/vtyzebra138.api -q /home/wyc/vtyospfd138.api -r")
        self.leo139.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa139.conf -w /home/wyc/vtyzebra139.api -q /home/wyc/vtyospfd139.api -r")
        self.leo140.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa140.conf -w /home/wyc/vtyzebra140.api -q /home/wyc/vtyospfd140.api -r")
        self.leo141.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa141.conf -w /home/wyc/vtyzebra141.api -q /home/wyc/vtyospfd141.api -r")
        self.leo142.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa142.conf -w /home/wyc/vtyzebra142.api -q /home/wyc/vtyospfd142.api -r")
        self.leo143.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa143.conf -w /home/wyc/vtyzebra143.api -q /home/wyc/vtyospfd143.api -r")
        self.leo144.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa144.conf -w /home/wyc/vtyzebra144.api -q /home/wyc/vtyospfd144.api -r")
        self.leo145.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa145.conf -w /home/wyc/vtyzebra145.api -q /home/wyc/vtyospfd145.api -r")
        self.leo146.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa146.conf -w /home/wyc/vtyzebra146.api -q /home/wyc/vtyospfd146.api -r")
        self.leo147.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa147.conf -w /home/wyc/vtyzebra147.api -q /home/wyc/vtyospfd147.api -r")
        self.leo148.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa148.conf -w /home/wyc/vtyzebra148.api -q /home/wyc/vtyospfd148.api -r")
        self.leo149.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa149.conf -w /home/wyc/vtyzebra149.api -q /home/wyc/vtyospfd149.api -r")
        self.leo150.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa150.conf -w /home/wyc/vtyzebra150.api -q /home/wyc/vtyospfd150.api -r")
        self.leo151.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa151.conf -w /home/wyc/vtyzebra151.api -q /home/wyc/vtyospfd151.api -r")
        self.leo152.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa152.conf -w /home/wyc/vtyzebra152.api -q /home/wyc/vtyospfd152.api -r")
        self.leo153.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa153.conf -w /home/wyc/vtyzebra153.api -q /home/wyc/vtyospfd153.api -r")
        self.leo154.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa154.conf -w /home/wyc/vtyzebra154.api -q /home/wyc/vtyospfd154.api -r")
        self.leo155.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa155.conf -w /home/wyc/vtyzebra155.api -q /home/wyc/vtyospfd155.api -r")
        self.leo156.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa156.conf -w /home/wyc/vtyzebra156.api -q /home/wyc/vtyospfd156.api -r")
        self.leo157.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa157.conf -w /home/wyc/vtyzebra157.api -q /home/wyc/vtyospfd157.api -r")
        self.leo158.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa158.conf -w /home/wyc/vtyzebra158.api -q /home/wyc/vtyospfd158.api -r")
        self.leo159.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa159.conf -w /home/wyc/vtyzebra159.api -q /home/wyc/vtyospfd159.api -r")
        self.leo160.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa160.conf -w /home/wyc/vtyzebra160.api -q /home/wyc/vtyospfd160.api -r")
        self.leo161.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa161.conf -w /home/wyc/vtyzebra161.api -q /home/wyc/vtyospfd161.api -r")
        self.leo162.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa162.conf -w /home/wyc/vtyzebra162.api -q /home/wyc/vtyospfd162.api -r")
        self.leo163.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa163.conf -w /home/wyc/vtyzebra163.api -q /home/wyc/vtyospfd163.api -r")
        self.leo164.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa164.conf -w /home/wyc/vtyzebra164.api -q /home/wyc/vtyospfd164.api -r")
        self.leo165.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa165.conf -w /home/wyc/vtyzebra165.api -q /home/wyc/vtyospfd165.api -r")
        self.leo166.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa166.conf -w /home/wyc/vtyzebra166.api -q /home/wyc/vtyospfd166.api -r")
        self.leo167.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa167.conf -w /home/wyc/vtyzebra167.api -q /home/wyc/vtyospfd167.api -r")
        self.leo168.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa168.conf -w /home/wyc/vtyzebra168.api -q /home/wyc/vtyospfd168.api -r")
        self.leo169.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa169.conf -w /home/wyc/vtyzebra169.api -q /home/wyc/vtyospfd169.api -r")
        self.leo170.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa170.conf -w /home/wyc/vtyzebra170.api -q /home/wyc/vtyospfd170.api -r")
        self.leo171.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa171.conf -w /home/wyc/vtyzebra171.api -q /home/wyc/vtyospfd171.api -r")
        self.leo172.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa172.conf -w /home/wyc/vtyzebra172.api -q /home/wyc/vtyospfd172.api -r")
        self.leo173.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa173.conf -w /home/wyc/vtyzebra173.api -q /home/wyc/vtyospfd173.api -r")
        self.leo174.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa174.conf -w /home/wyc/vtyzebra174.api -q /home/wyc/vtyospfd174.api -r")
        self.leo175.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa175.conf -w /home/wyc/vtyzebra175.api -q /home/wyc/vtyospfd175.api -r")
        self.leo176.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa176.conf -w /home/wyc/vtyzebra176.api -q /home/wyc/vtyospfd176.api -r")
        self.leo177.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa177.conf -w /home/wyc/vtyzebra177.api -q /home/wyc/vtyospfd177.api -r")
        self.leo178.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa178.conf -w /home/wyc/vtyzebra178.api -q /home/wyc/vtyospfd178.api -r")
        self.leo179.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa179.conf -w /home/wyc/vtyzebra179.api -q /home/wyc/vtyospfd179.api -r")
        self.leo180.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa180.conf -w /home/wyc/vtyzebra180.api -q /home/wyc/vtyospfd180.api -r")
        self.leo181.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa181.conf -w /home/wyc/vtyzebra181.api -q /home/wyc/vtyospfd181.api -r")
        self.leo182.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa182.conf -w /home/wyc/vtyzebra182.api -q /home/wyc/vtyospfd182.api -r")
        self.leo183.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa183.conf -w /home/wyc/vtyzebra183.api -q /home/wyc/vtyospfd183.api -r")
        self.leo184.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa184.conf -w /home/wyc/vtyzebra184.api -q /home/wyc/vtyospfd184.api -r")
        self.leo185.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa185.conf -w /home/wyc/vtyzebra185.api -q /home/wyc/vtyospfd185.api -r")
        self.leo186.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa186.conf -w /home/wyc/vtyzebra186.api -q /home/wyc/vtyospfd186.api -r")
        self.leo187.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa187.conf -w /home/wyc/vtyzebra187.api -q /home/wyc/vtyospfd187.api -r")
        self.leo188.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa188.conf -w /home/wyc/vtyzebra188.api -q /home/wyc/vtyospfd188.api -r")
        self.leo189.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa189.conf -w /home/wyc/vtyzebra189.api -q /home/wyc/vtyospfd189.api -r")
        self.leo190.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa190.conf -w /home/wyc/vtyzebra190.api -q /home/wyc/vtyospfd190.api -r")
        self.leo191.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa191.conf -w /home/wyc/vtyzebra191.api -q /home/wyc/vtyospfd191.api -r")
        self.leo192.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa192.conf -w /home/wyc/vtyzebra192.api -q /home/wyc/vtyospfd192.api -r")
        self.leo193.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa193.conf -w /home/wyc/vtyzebra193.api -q /home/wyc/vtyospfd193.api -r")
        self.leo194.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa194.conf -w /home/wyc/vtyzebra194.api -q /home/wyc/vtyospfd194.api -r")
        self.leo195.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa195.conf -w /home/wyc/vtyzebra195.api -q /home/wyc/vtyospfd195.api -r")
        self.leo196.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa196.conf -w /home/wyc/vtyzebra196.api -q /home/wyc/vtyospfd196.api -r")
        self.leo197.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa197.conf -w /home/wyc/vtyzebra197.api -q /home/wyc/vtyospfd197.api -r")
        self.leo198.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa198.conf -w /home/wyc/vtyzebra198.api -q /home/wyc/vtyospfd198.api -r")
        self.leo199.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa199.conf -w /home/wyc/vtyzebra199.api -q /home/wyc/vtyospfd199.api -r")
        self.leo200.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa200.conf -w /home/wyc/vtyzebra200.api -q /home/wyc/vtyospfd200.api -r")
        self.leo201.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa201.conf -w /home/wyc/vtyzebra201.api -q /home/wyc/vtyospfd201.api -r")
        self.leo202.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa202.conf -w /home/wyc/vtyzebra202.api -q /home/wyc/vtyospfd202.api -r")
        self.leo203.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa203.conf -w /home/wyc/vtyzebra203.api -q /home/wyc/vtyospfd203.api -r")
        self.leo204.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa204.conf -w /home/wyc/vtyzebra204.api -q /home/wyc/vtyospfd204.api -r")
        self.leo205.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa205.conf -w /home/wyc/vtyzebra205.api -q /home/wyc/vtyospfd205.api -r")
        self.leo206.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa206.conf -w /home/wyc/vtyzebra206.api -q /home/wyc/vtyospfd206.api -r")
        self.leo207.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa207.conf -w /home/wyc/vtyzebra207.api -q /home/wyc/vtyospfd207.api -r")
        self.leo208.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa208.conf -w /home/wyc/vtyzebra208.api -q /home/wyc/vtyospfd208.api -r")
        self.leo209.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa209.conf -w /home/wyc/vtyzebra209.api -q /home/wyc/vtyospfd209.api -r")
        self.leo210.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa210.conf -w /home/wyc/vtyzebra210.api -q /home/wyc/vtyospfd210.api -r")
        self.leo211.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa211.conf -w /home/wyc/vtyzebra211.api -q /home/wyc/vtyospfd211.api -r")
        self.leo212.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa212.conf -w /home/wyc/vtyzebra212.api -q /home/wyc/vtyospfd212.api -r")
        self.leo213.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa213.conf -w /home/wyc/vtyzebra213.api -q /home/wyc/vtyospfd213.api -r")
        self.leo214.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa214.conf -w /home/wyc/vtyzebra214.api -q /home/wyc/vtyospfd214.api -r")
        self.leo215.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa215.conf -w /home/wyc/vtyzebra215.api -q /home/wyc/vtyospfd215.api -r")
        self.leo216.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa216.conf -w /home/wyc/vtyzebra216.api -q /home/wyc/vtyospfd216.api -r")
        self.leo217.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa217.conf -w /home/wyc/vtyzebra217.api -q /home/wyc/vtyospfd217.api -r")
        self.leo218.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa218.conf -w /home/wyc/vtyzebra218.api -q /home/wyc/vtyospfd218.api -r")
        self.leo219.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa219.conf -w /home/wyc/vtyzebra219.api -q /home/wyc/vtyospfd219.api -r")
        self.leo220.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa220.conf -w /home/wyc/vtyzebra220.api -q /home/wyc/vtyospfd220.api -r")
        self.leo221.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa221.conf -w /home/wyc/vtyzebra221.api -q /home/wyc/vtyospfd221.api -r")
        self.leo222.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa222.conf -w /home/wyc/vtyzebra222.api -q /home/wyc/vtyospfd222.api -r")
        self.leo223.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa223.conf -w /home/wyc/vtyzebra223.api -q /home/wyc/vtyospfd223.api -r")
        self.leo224.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa224.conf -w /home/wyc/vtyzebra224.api -q /home/wyc/vtyospfd224.api -r")
        self.leo225.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa225.conf -w /home/wyc/vtyzebra225.api -q /home/wyc/vtyospfd225.api -r")
        self.leo226.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa226.conf -w /home/wyc/vtyzebra226.api -q /home/wyc/vtyospfd226.api -r")
        self.leo227.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa227.conf -w /home/wyc/vtyzebra227.api -q /home/wyc/vtyospfd227.api -r")
        self.leo228.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa228.conf -w /home/wyc/vtyzebra228.api -q /home/wyc/vtyospfd228.api -r")
        self.leo229.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa229.conf -w /home/wyc/vtyzebra229.api -q /home/wyc/vtyospfd229.api -r")
        self.leo230.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa230.conf -w /home/wyc/vtyzebra230.api -q /home/wyc/vtyospfd230.api -r")
        self.leo231.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa231.conf -w /home/wyc/vtyzebra231.api -q /home/wyc/vtyospfd231.api -r")
        self.leo232.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa232.conf -w /home/wyc/vtyzebra232.api -q /home/wyc/vtyospfd232.api -r")
        self.leo233.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa233.conf -w /home/wyc/vtyzebra233.api -q /home/wyc/vtyospfd233.api -r")
        self.leo234.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa234.conf -w /home/wyc/vtyzebra234.api -q /home/wyc/vtyospfd234.api -r")
        self.leo235.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa235.conf -w /home/wyc/vtyzebra235.api -q /home/wyc/vtyospfd235.api -r")
        self.leo236.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa236.conf -w /home/wyc/vtyzebra236.api -q /home/wyc/vtyospfd236.api -r")
        self.leo237.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa237.conf -w /home/wyc/vtyzebra237.api -q /home/wyc/vtyospfd237.api -r")
        self.leo238.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa238.conf -w /home/wyc/vtyzebra238.api -q /home/wyc/vtyospfd238.api -r")
        self.leo239.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/inter_oa/inter_oa239.conf -w /home/wyc/vtyzebra239.api -q /home/wyc/vtyospfd239.api -r")


    def load(self):
        self.leo0.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra0.api -q /home/wyc/vtyospfd0.api -r")
        self.leo1.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra1.api -q /home/wyc/vtyospfd1.api -r")
        self.leo2.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra2.api -q /home/wyc/vtyospfd2.api -r")
        self.leo3.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra3.api -q /home/wyc/vtyospfd3.api -r")
        self.leo4.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra4.api -q /home/wyc/vtyospfd4.api -r")
        self.leo5.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra5.api -q /home/wyc/vtyospfd5.api -r")
        self.leo6.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra6.api -q /home/wyc/vtyospfd6.api -r")
        self.leo7.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra7.api -q /home/wyc/vtyospfd7.api -r")
        self.leo8.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra8.api -q /home/wyc/vtyospfd8.api -r")
        self.leo9.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra9.api -q /home/wyc/vtyospfd9.api -r")
        self.leo10.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra10.api -q /home/wyc/vtyospfd10.api -r")
        self.leo11.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra11.api -q /home/wyc/vtyospfd11.api -r")
        self.leo12.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra12.api -q /home/wyc/vtyospfd12.api -r")
        self.leo13.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra13.api -q /home/wyc/vtyospfd13.api -r")
        self.leo14.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra14.api -q /home/wyc/vtyospfd14.api -r")
        self.leo15.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra15.api -q /home/wyc/vtyospfd15.api -r")
        self.leo16.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra16.api -q /home/wyc/vtyospfd16.api -r")
        self.leo17.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra17.api -q /home/wyc/vtyospfd17.api -r")
        self.leo18.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra18.api -q /home/wyc/vtyospfd18.api -r")
        self.leo19.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra19.api -q /home/wyc/vtyospfd19.api -r")
        self.leo20.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra20.api -q /home/wyc/vtyospfd20.api -r")
        self.leo21.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra21.api -q /home/wyc/vtyospfd21.api -r")
        self.leo22.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra22.api -q /home/wyc/vtyospfd22.api -r")
        self.leo23.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra23.api -q /home/wyc/vtyospfd23.api -r")
        self.leo24.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra24.api -q /home/wyc/vtyospfd24.api -r")
        self.leo25.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra25.api -q /home/wyc/vtyospfd25.api -r")
        self.leo26.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra26.api -q /home/wyc/vtyospfd26.api -r")
        self.leo27.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra27.api -q /home/wyc/vtyospfd27.api -r")
        self.leo28.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra28.api -q /home/wyc/vtyospfd28.api -r")
        self.leo29.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra29.api -q /home/wyc/vtyospfd29.api -r")
        self.leo30.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra30.api -q /home/wyc/vtyospfd30.api -r")
        self.leo31.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra31.api -q /home/wyc/vtyospfd31.api -r")
        self.leo32.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra32.api -q /home/wyc/vtyospfd32.api -r")
        self.leo33.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra33.api -q /home/wyc/vtyospfd33.api -r")
        self.leo34.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra34.api -q /home/wyc/vtyospfd34.api -r")
        self.leo35.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra35.api -q /home/wyc/vtyospfd35.api -r")
        self.leo36.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra36.api -q /home/wyc/vtyospfd36.api -r")
        self.leo37.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra37.api -q /home/wyc/vtyospfd37.api -r")
        self.leo38.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra38.api -q /home/wyc/vtyospfd38.api -r")
        self.leo39.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra39.api -q /home/wyc/vtyospfd39.api -r")
        self.leo40.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra40.api -q /home/wyc/vtyospfd40.api -r")
        self.leo41.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra41.api -q /home/wyc/vtyospfd41.api -r")
        self.leo42.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra42.api -q /home/wyc/vtyospfd42.api -r")
        self.leo43.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra43.api -q /home/wyc/vtyospfd43.api -r")
        self.leo44.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra44.api -q /home/wyc/vtyospfd44.api -r")
        self.leo45.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra45.api -q /home/wyc/vtyospfd45.api -r")
        self.leo46.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra46.api -q /home/wyc/vtyospfd46.api -r")
        self.leo47.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra47.api -q /home/wyc/vtyospfd47.api -r")
        self.leo48.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra48.api -q /home/wyc/vtyospfd48.api -r")
        self.leo49.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra49.api -q /home/wyc/vtyospfd49.api -r")
        self.leo50.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra50.api -q /home/wyc/vtyospfd50.api -r")
        self.leo51.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra51.api -q /home/wyc/vtyospfd51.api -r")
        self.leo52.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra52.api -q /home/wyc/vtyospfd52.api -r")
        self.leo53.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra53.api -q /home/wyc/vtyospfd53.api -r")
        self.leo54.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra54.api -q /home/wyc/vtyospfd54.api -r")
        self.leo55.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra55.api -q /home/wyc/vtyospfd55.api -r")
        self.leo56.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra56.api -q /home/wyc/vtyospfd56.api -r")
        self.leo57.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra57.api -q /home/wyc/vtyospfd57.api -r")
        self.leo58.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra58.api -q /home/wyc/vtyospfd58.api -r")
        self.leo59.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra59.api -q /home/wyc/vtyospfd59.api -r")
        self.leo60.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra60.api -q /home/wyc/vtyospfd60.api -r")
        self.leo61.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra61.api -q /home/wyc/vtyospfd61.api -r")
        self.leo62.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra62.api -q /home/wyc/vtyospfd62.api -r")
        self.leo63.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra63.api -q /home/wyc/vtyospfd63.api -r")
        self.leo64.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra64.api -q /home/wyc/vtyospfd64.api -r")
        self.leo65.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra65.api -q /home/wyc/vtyospfd65.api -r")
        self.leo66.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra66.api -q /home/wyc/vtyospfd66.api -r")
        self.leo67.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra67.api -q /home/wyc/vtyospfd67.api -r")
        self.leo68.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra68.api -q /home/wyc/vtyospfd68.api -r")
        self.leo69.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra69.api -q /home/wyc/vtyospfd69.api -r")
        self.leo70.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra70.api -q /home/wyc/vtyospfd70.api -r")
        self.leo71.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra71.api -q /home/wyc/vtyospfd71.api -r")
        self.leo72.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra72.api -q /home/wyc/vtyospfd72.api -r")
        self.leo73.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra73.api -q /home/wyc/vtyospfd73.api -r")
        self.leo74.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra74.api -q /home/wyc/vtyospfd74.api -r")
        self.leo75.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra75.api -q /home/wyc/vtyospfd75.api -r")
        self.leo76.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra76.api -q /home/wyc/vtyospfd76.api -r")
        self.leo77.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra77.api -q /home/wyc/vtyospfd77.api -r")
        self.leo78.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra78.api -q /home/wyc/vtyospfd78.api -r")
        self.leo79.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra79.api -q /home/wyc/vtyospfd79.api -r")
        self.leo80.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra80.api -q /home/wyc/vtyospfd80.api -r")
        self.leo81.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra81.api -q /home/wyc/vtyospfd81.api -r")
        self.leo82.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra82.api -q /home/wyc/vtyospfd82.api -r")
        self.leo83.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra83.api -q /home/wyc/vtyospfd83.api -r")
        self.leo84.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra84.api -q /home/wyc/vtyospfd84.api -r")
        self.leo85.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra85.api -q /home/wyc/vtyospfd85.api -r")
        self.leo86.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra86.api -q /home/wyc/vtyospfd86.api -r")
        self.leo87.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra87.api -q /home/wyc/vtyospfd87.api -r")
        self.leo88.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra88.api -q /home/wyc/vtyospfd88.api -r")
        self.leo89.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra89.api -q /home/wyc/vtyospfd89.api -r")
        self.leo90.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra90.api -q /home/wyc/vtyospfd90.api -r")
        self.leo91.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra91.api -q /home/wyc/vtyospfd91.api -r")
        self.leo92.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra92.api -q /home/wyc/vtyospfd92.api -r")
        self.leo93.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra93.api -q /home/wyc/vtyospfd93.api -r")
        self.leo94.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra94.api -q /home/wyc/vtyospfd94.api -r")
        self.leo95.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra95.api -q /home/wyc/vtyospfd95.api -r")
        self.leo96.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra96.api -q /home/wyc/vtyospfd96.api -r")
        self.leo97.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra97.api -q /home/wyc/vtyospfd97.api -r")
        self.leo98.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra98.api -q /home/wyc/vtyospfd98.api -r")
        self.leo99.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra99.api -q /home/wyc/vtyospfd99.api -r")
        self.leo100.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra100.api -q /home/wyc/vtyospfd100.api -r")
        self.leo101.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra101.api -q /home/wyc/vtyospfd101.api -r")
        self.leo102.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra102.api -q /home/wyc/vtyospfd102.api -r")
        self.leo103.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra103.api -q /home/wyc/vtyospfd103.api -r")
        self.leo104.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra104.api -q /home/wyc/vtyospfd104.api -r")
        self.leo105.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra105.api -q /home/wyc/vtyospfd105.api -r")
        self.leo106.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra106.api -q /home/wyc/vtyospfd106.api -r")
        self.leo107.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra107.api -q /home/wyc/vtyospfd107.api -r")
        self.leo108.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra108.api -q /home/wyc/vtyospfd108.api -r")
        self.leo109.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra109.api -q /home/wyc/vtyospfd109.api -r")
        self.leo110.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra110.api -q /home/wyc/vtyospfd110.api -r")
        self.leo111.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra111.api -q /home/wyc/vtyospfd111.api -r")
        self.leo112.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra112.api -q /home/wyc/vtyospfd112.api -r")
        self.leo113.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra113.api -q /home/wyc/vtyospfd113.api -r")
        self.leo114.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra114.api -q /home/wyc/vtyospfd114.api -r")
        self.leo115.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra115.api -q /home/wyc/vtyospfd115.api -r")
        self.leo116.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra116.api -q /home/wyc/vtyospfd116.api -r")
        self.leo117.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra117.api -q /home/wyc/vtyospfd117.api -r")
        self.leo118.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra118.api -q /home/wyc/vtyospfd118.api -r")
        self.leo119.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra119.api -q /home/wyc/vtyospfd119.api -r")
        self.leo120.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra120.api -q /home/wyc/vtyospfd120.api -r")
        self.leo121.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra121.api -q /home/wyc/vtyospfd121.api -r")
        self.leo122.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra122.api -q /home/wyc/vtyospfd122.api -r")
        self.leo123.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra123.api -q /home/wyc/vtyospfd123.api -r")
        self.leo124.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra124.api -q /home/wyc/vtyospfd124.api -r")
        self.leo125.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra125.api -q /home/wyc/vtyospfd125.api -r")
        self.leo126.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra126.api -q /home/wyc/vtyospfd126.api -r")
        self.leo127.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra127.api -q /home/wyc/vtyospfd127.api -r")
        self.leo128.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra128.api -q /home/wyc/vtyospfd128.api -r")
        self.leo129.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra129.api -q /home/wyc/vtyospfd129.api -r")
        self.leo130.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra130.api -q /home/wyc/vtyospfd130.api -r")
        self.leo131.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra131.api -q /home/wyc/vtyospfd131.api -r")
        self.leo132.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra132.api -q /home/wyc/vtyospfd132.api -r")
        self.leo133.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra133.api -q /home/wyc/vtyospfd133.api -r")
        self.leo134.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra134.api -q /home/wyc/vtyospfd134.api -r")
        self.leo135.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra135.api -q /home/wyc/vtyospfd135.api -r")
        self.leo136.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra136.api -q /home/wyc/vtyospfd136.api -r")
        self.leo137.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra137.api -q /home/wyc/vtyospfd137.api -r")
        self.leo138.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra138.api -q /home/wyc/vtyospfd138.api -r")
        self.leo139.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra139.api -q /home/wyc/vtyospfd139.api -r")
        self.leo140.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra140.api -q /home/wyc/vtyospfd140.api -r")
        self.leo141.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra141.api -q /home/wyc/vtyospfd141.api -r")
        self.leo142.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra142.api -q /home/wyc/vtyospfd142.api -r")
        self.leo143.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra143.api -q /home/wyc/vtyospfd143.api -r")
        self.leo144.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra144.api -q /home/wyc/vtyospfd144.api -r")
        self.leo145.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra145.api -q /home/wyc/vtyospfd145.api -r")
        self.leo146.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra146.api -q /home/wyc/vtyospfd146.api -r")
        self.leo147.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra147.api -q /home/wyc/vtyospfd147.api -r")
        self.leo148.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra148.api -q /home/wyc/vtyospfd148.api -r")
        self.leo149.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra149.api -q /home/wyc/vtyospfd149.api -r")
        self.leo150.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra150.api -q /home/wyc/vtyospfd150.api -r")
        self.leo151.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra151.api -q /home/wyc/vtyospfd151.api -r")
        self.leo152.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra152.api -q /home/wyc/vtyospfd152.api -r")
        self.leo153.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra153.api -q /home/wyc/vtyospfd153.api -r")
        self.leo154.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra154.api -q /home/wyc/vtyospfd154.api -r")
        self.leo155.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra155.api -q /home/wyc/vtyospfd155.api -r")
        self.leo156.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra156.api -q /home/wyc/vtyospfd156.api -r")
        self.leo157.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra157.api -q /home/wyc/vtyospfd157.api -r")
        self.leo158.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra158.api -q /home/wyc/vtyospfd158.api -r")
        self.leo159.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra159.api -q /home/wyc/vtyospfd159.api -r")
        self.leo160.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra160.api -q /home/wyc/vtyospfd160.api -r")
        self.leo161.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra161.api -q /home/wyc/vtyospfd161.api -r")
        self.leo162.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra162.api -q /home/wyc/vtyospfd162.api -r")
        self.leo163.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra163.api -q /home/wyc/vtyospfd163.api -r")
        self.leo164.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra164.api -q /home/wyc/vtyospfd164.api -r")
        self.leo165.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra165.api -q /home/wyc/vtyospfd165.api -r")
        self.leo166.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra166.api -q /home/wyc/vtyospfd166.api -r")
        self.leo167.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra167.api -q /home/wyc/vtyospfd167.api -r")
        self.leo168.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra168.api -q /home/wyc/vtyospfd168.api -r")
        self.leo169.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra169.api -q /home/wyc/vtyospfd169.api -r")
        self.leo170.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra170.api -q /home/wyc/vtyospfd170.api -r")
        self.leo171.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra171.api -q /home/wyc/vtyospfd171.api -r")
        self.leo172.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra172.api -q /home/wyc/vtyospfd172.api -r")
        self.leo173.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra173.api -q /home/wyc/vtyospfd173.api -r")
        self.leo174.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra174.api -q /home/wyc/vtyospfd174.api -r")
        self.leo175.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra175.api -q /home/wyc/vtyospfd175.api -r")
        self.leo176.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra176.api -q /home/wyc/vtyospfd176.api -r")
        self.leo177.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra177.api -q /home/wyc/vtyospfd177.api -r")
        self.leo178.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra178.api -q /home/wyc/vtyospfd178.api -r")
        self.leo179.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra179.api -q /home/wyc/vtyospfd179.api -r")
        self.leo180.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra180.api -q /home/wyc/vtyospfd180.api -r")
        self.leo181.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra181.api -q /home/wyc/vtyospfd181.api -r")
        self.leo182.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra182.api -q /home/wyc/vtyospfd182.api -r")
        self.leo183.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra183.api -q /home/wyc/vtyospfd183.api -r")
        self.leo184.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra184.api -q /home/wyc/vtyospfd184.api -r")
        self.leo185.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra185.api -q /home/wyc/vtyospfd185.api -r")
        self.leo186.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra186.api -q /home/wyc/vtyospfd186.api -r")
        self.leo187.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra187.api -q /home/wyc/vtyospfd187.api -r")
        self.leo188.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra188.api -q /home/wyc/vtyospfd188.api -r")
        self.leo189.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra189.api -q /home/wyc/vtyospfd189.api -r")
        self.leo190.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra190.api -q /home/wyc/vtyospfd190.api -r")
        self.leo191.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra191.api -q /home/wyc/vtyospfd191.api -r")
        self.leo192.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra192.api -q /home/wyc/vtyospfd192.api -r")
        self.leo193.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra193.api -q /home/wyc/vtyospfd193.api -r")
        self.leo194.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra194.api -q /home/wyc/vtyospfd194.api -r")
        self.leo195.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra195.api -q /home/wyc/vtyospfd195.api -r")
        self.leo196.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra196.api -q /home/wyc/vtyospfd196.api -r")
        self.leo197.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra197.api -q /home/wyc/vtyospfd197.api -r")
        self.leo198.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra198.api -q /home/wyc/vtyospfd198.api -r")
        self.leo199.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra199.api -q /home/wyc/vtyospfd199.api -r")
        self.leo200.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra200.api -q /home/wyc/vtyospfd200.api -r")
        self.leo201.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra201.api -q /home/wyc/vtyospfd201.api -r")
        self.leo202.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra202.api -q /home/wyc/vtyospfd202.api -r")
        self.leo203.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra203.api -q /home/wyc/vtyospfd203.api -r")
        self.leo204.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra204.api -q /home/wyc/vtyospfd204.api -r")
        self.leo205.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra205.api -q /home/wyc/vtyospfd205.api -r")
        self.leo206.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra206.api -q /home/wyc/vtyospfd206.api -r")
        self.leo207.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra207.api -q /home/wyc/vtyospfd207.api -r")
        self.leo208.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra208.api -q /home/wyc/vtyospfd208.api -r")
        self.leo209.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra209.api -q /home/wyc/vtyospfd209.api -r")
        self.leo210.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra210.api -q /home/wyc/vtyospfd210.api -r")
        self.leo211.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra211.api -q /home/wyc/vtyospfd211.api -r")
        self.leo212.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra212.api -q /home/wyc/vtyospfd212.api -r")
        self.leo213.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra213.api -q /home/wyc/vtyospfd213.api -r")
        self.leo214.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra214.api -q /home/wyc/vtyospfd214.api -r")
        self.leo215.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra215.api -q /home/wyc/vtyospfd215.api -r")
        self.leo216.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra216.api -q /home/wyc/vtyospfd216.api -r")
        self.leo217.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra217.api -q /home/wyc/vtyospfd217.api -r")
        self.leo218.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra218.api -q /home/wyc/vtyospfd218.api -r")
        self.leo219.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra219.api -q /home/wyc/vtyospfd219.api -r")
        self.leo220.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra220.api -q /home/wyc/vtyospfd220.api -r")
        self.leo221.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra221.api -q /home/wyc/vtyospfd221.api -r")
        self.leo222.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra222.api -q /home/wyc/vtyospfd222.api -r")
        self.leo223.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra223.api -q /home/wyc/vtyospfd223.api -r")
        self.leo224.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra224.api -q /home/wyc/vtyospfd224.api -r")
        self.leo225.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra225.api -q /home/wyc/vtyospfd225.api -r")
        self.leo226.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra226.api -q /home/wyc/vtyospfd226.api -r")
        self.leo227.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra227.api -q /home/wyc/vtyospfd227.api -r")
        self.leo228.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra228.api -q /home/wyc/vtyospfd228.api -r")
        self.leo229.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra229.api -q /home/wyc/vtyospfd229.api -r")
        self.leo230.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra230.api -q /home/wyc/vtyospfd230.api -r")
        self.leo231.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra231.api -q /home/wyc/vtyospfd231.api -r")
        self.leo232.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra232.api -q /home/wyc/vtyospfd232.api -r")
        self.leo233.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra233.api -q /home/wyc/vtyospfd233.api -r")
        self.leo234.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra234.api -q /home/wyc/vtyospfd234.api -r")
        self.leo235.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra235.api -q /home/wyc/vtyospfd235.api -r")
        self.leo236.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra236.api -q /home/wyc/vtyospfd236.api -r")
        self.leo237.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra237.api -q /home/wyc/vtyospfd237.api -r")
        self.leo238.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra238.api -q /home/wyc/vtyospfd238.api -r")
        self.leo239.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/loadlsdb.conf -w /home/wyc/vtyzebra239.api -q /home/wyc/vtyospfd239.api -r")


    def add_phase(self):
        last_phase=self.phase
        self.phase+=1
        if self.phase>=self.phaseAll:
            self.phase=0
        print(str(self.phase)+","+str(last_phase))
        self.leo0.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra0.api -q /home/wyc/vtyospfd0.api -r")
        self.leo1.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra1.api -q /home/wyc/vtyospfd1.api -r")
        self.leo2.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra2.api -q /home/wyc/vtyospfd2.api -r")
        self.leo3.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra3.api -q /home/wyc/vtyospfd3.api -r")
        self.leo4.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra4.api -q /home/wyc/vtyospfd4.api -r")
        self.leo5.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra5.api -q /home/wyc/vtyospfd5.api -r")
        self.leo6.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra6.api -q /home/wyc/vtyospfd6.api -r")
        self.leo7.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra7.api -q /home/wyc/vtyospfd7.api -r")
        self.leo8.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra8.api -q /home/wyc/vtyospfd8.api -r")
        self.leo9.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra9.api -q /home/wyc/vtyospfd9.api -r")
        self.leo10.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra10.api -q /home/wyc/vtyospfd10.api -r")
        self.leo11.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra11.api -q /home/wyc/vtyospfd11.api -r")
        self.leo12.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra12.api -q /home/wyc/vtyospfd12.api -r")
        self.leo13.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra13.api -q /home/wyc/vtyospfd13.api -r")
        self.leo14.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra14.api -q /home/wyc/vtyospfd14.api -r")
        self.leo15.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra15.api -q /home/wyc/vtyospfd15.api -r")
        self.leo16.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra16.api -q /home/wyc/vtyospfd16.api -r")
        self.leo17.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra17.api -q /home/wyc/vtyospfd17.api -r")
        self.leo18.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra18.api -q /home/wyc/vtyospfd18.api -r")
        self.leo19.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra19.api -q /home/wyc/vtyospfd19.api -r")
        self.leo20.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra20.api -q /home/wyc/vtyospfd20.api -r")
        self.leo21.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra21.api -q /home/wyc/vtyospfd21.api -r")
        self.leo22.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra22.api -q /home/wyc/vtyospfd22.api -r")
        self.leo23.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra23.api -q /home/wyc/vtyospfd23.api -r")
        self.leo24.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra24.api -q /home/wyc/vtyospfd24.api -r")
        self.leo25.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra25.api -q /home/wyc/vtyospfd25.api -r")
        self.leo26.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra26.api -q /home/wyc/vtyospfd26.api -r")
        self.leo27.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra27.api -q /home/wyc/vtyospfd27.api -r")
        self.leo28.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra28.api -q /home/wyc/vtyospfd28.api -r")
        self.leo29.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra29.api -q /home/wyc/vtyospfd29.api -r")
        self.leo30.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra30.api -q /home/wyc/vtyospfd30.api -r")
        self.leo31.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra31.api -q /home/wyc/vtyospfd31.api -r")
        self.leo32.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra32.api -q /home/wyc/vtyospfd32.api -r")
        self.leo33.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra33.api -q /home/wyc/vtyospfd33.api -r")
        self.leo34.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra34.api -q /home/wyc/vtyospfd34.api -r")
        self.leo35.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra35.api -q /home/wyc/vtyospfd35.api -r")
        self.leo36.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra36.api -q /home/wyc/vtyospfd36.api -r")
        self.leo37.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra37.api -q /home/wyc/vtyospfd37.api -r")
        self.leo38.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra38.api -q /home/wyc/vtyospfd38.api -r")
        self.leo39.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra39.api -q /home/wyc/vtyospfd39.api -r")
        self.leo40.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra40.api -q /home/wyc/vtyospfd40.api -r")
        self.leo41.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra41.api -q /home/wyc/vtyospfd41.api -r")
        self.leo42.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra42.api -q /home/wyc/vtyospfd42.api -r")
        self.leo43.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra43.api -q /home/wyc/vtyospfd43.api -r")
        self.leo44.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra44.api -q /home/wyc/vtyospfd44.api -r")
        self.leo45.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra45.api -q /home/wyc/vtyospfd45.api -r")
        self.leo46.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra46.api -q /home/wyc/vtyospfd46.api -r")
        self.leo47.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra47.api -q /home/wyc/vtyospfd47.api -r")
        self.leo48.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra48.api -q /home/wyc/vtyospfd48.api -r")
        self.leo49.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra49.api -q /home/wyc/vtyospfd49.api -r")
        self.leo50.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra50.api -q /home/wyc/vtyospfd50.api -r")
        self.leo51.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra51.api -q /home/wyc/vtyospfd51.api -r")
        self.leo52.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra52.api -q /home/wyc/vtyospfd52.api -r")
        self.leo53.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra53.api -q /home/wyc/vtyospfd53.api -r")
        self.leo54.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra54.api -q /home/wyc/vtyospfd54.api -r")
        self.leo55.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra55.api -q /home/wyc/vtyospfd55.api -r")
        self.leo56.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra56.api -q /home/wyc/vtyospfd56.api -r")
        self.leo57.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra57.api -q /home/wyc/vtyospfd57.api -r")
        self.leo58.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra58.api -q /home/wyc/vtyospfd58.api -r")
        self.leo59.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra59.api -q /home/wyc/vtyospfd59.api -r")
        self.leo60.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra60.api -q /home/wyc/vtyospfd60.api -r")
        self.leo61.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra61.api -q /home/wyc/vtyospfd61.api -r")
        self.leo62.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra62.api -q /home/wyc/vtyospfd62.api -r")
        self.leo63.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra63.api -q /home/wyc/vtyospfd63.api -r")
        self.leo64.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra64.api -q /home/wyc/vtyospfd64.api -r")
        self.leo65.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra65.api -q /home/wyc/vtyospfd65.api -r")
        self.leo66.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra66.api -q /home/wyc/vtyospfd66.api -r")
        self.leo67.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra67.api -q /home/wyc/vtyospfd67.api -r")
        self.leo68.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra68.api -q /home/wyc/vtyospfd68.api -r")
        self.leo69.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra69.api -q /home/wyc/vtyospfd69.api -r")
        self.leo70.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra70.api -q /home/wyc/vtyospfd70.api -r")
        self.leo71.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra71.api -q /home/wyc/vtyospfd71.api -r")
        self.leo72.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra72.api -q /home/wyc/vtyospfd72.api -r")
        self.leo73.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra73.api -q /home/wyc/vtyospfd73.api -r")
        self.leo74.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra74.api -q /home/wyc/vtyospfd74.api -r")
        self.leo75.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra75.api -q /home/wyc/vtyospfd75.api -r")
        self.leo76.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra76.api -q /home/wyc/vtyospfd76.api -r")
        self.leo77.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra77.api -q /home/wyc/vtyospfd77.api -r")
        self.leo78.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra78.api -q /home/wyc/vtyospfd78.api -r")
        self.leo79.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra79.api -q /home/wyc/vtyospfd79.api -r")
        self.leo80.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra80.api -q /home/wyc/vtyospfd80.api -r")
        self.leo81.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra81.api -q /home/wyc/vtyospfd81.api -r")
        self.leo82.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra82.api -q /home/wyc/vtyospfd82.api -r")
        self.leo83.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra83.api -q /home/wyc/vtyospfd83.api -r")
        self.leo84.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra84.api -q /home/wyc/vtyospfd84.api -r")
        self.leo85.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra85.api -q /home/wyc/vtyospfd85.api -r")
        self.leo86.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra86.api -q /home/wyc/vtyospfd86.api -r")
        self.leo87.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra87.api -q /home/wyc/vtyospfd87.api -r")
        self.leo88.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra88.api -q /home/wyc/vtyospfd88.api -r")
        self.leo89.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra89.api -q /home/wyc/vtyospfd89.api -r")
        self.leo90.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra90.api -q /home/wyc/vtyospfd90.api -r")
        self.leo91.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra91.api -q /home/wyc/vtyospfd91.api -r")
        self.leo92.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra92.api -q /home/wyc/vtyospfd92.api -r")
        self.leo93.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra93.api -q /home/wyc/vtyospfd93.api -r")
        self.leo94.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra94.api -q /home/wyc/vtyospfd94.api -r")
        self.leo95.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra95.api -q /home/wyc/vtyospfd95.api -r")
        self.leo96.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra96.api -q /home/wyc/vtyospfd96.api -r")
        self.leo97.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra97.api -q /home/wyc/vtyospfd97.api -r")
        self.leo98.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra98.api -q /home/wyc/vtyospfd98.api -r")
        self.leo99.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra99.api -q /home/wyc/vtyospfd99.api -r")
        self.leo100.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra100.api -q /home/wyc/vtyospfd100.api -r")
        self.leo101.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra101.api -q /home/wyc/vtyospfd101.api -r")
        self.leo102.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra102.api -q /home/wyc/vtyospfd102.api -r")
        self.leo103.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra103.api -q /home/wyc/vtyospfd103.api -r")
        self.leo104.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra104.api -q /home/wyc/vtyospfd104.api -r")
        self.leo105.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra105.api -q /home/wyc/vtyospfd105.api -r")
        self.leo106.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra106.api -q /home/wyc/vtyospfd106.api -r")
        self.leo107.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra107.api -q /home/wyc/vtyospfd107.api -r")
        self.leo108.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra108.api -q /home/wyc/vtyospfd108.api -r")
        self.leo109.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra109.api -q /home/wyc/vtyospfd109.api -r")
        self.leo110.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra110.api -q /home/wyc/vtyospfd110.api -r")
        self.leo111.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra111.api -q /home/wyc/vtyospfd111.api -r")
        self.leo112.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra112.api -q /home/wyc/vtyospfd112.api -r")
        self.leo113.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra113.api -q /home/wyc/vtyospfd113.api -r")
        self.leo114.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra114.api -q /home/wyc/vtyospfd114.api -r")
        self.leo115.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra115.api -q /home/wyc/vtyospfd115.api -r")
        self.leo116.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra116.api -q /home/wyc/vtyospfd116.api -r")
        self.leo117.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra117.api -q /home/wyc/vtyospfd117.api -r")
        self.leo118.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra118.api -q /home/wyc/vtyospfd118.api -r")
        self.leo119.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra119.api -q /home/wyc/vtyospfd119.api -r")
        self.leo120.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra120.api -q /home/wyc/vtyospfd120.api -r")
        self.leo121.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra121.api -q /home/wyc/vtyospfd121.api -r")
        self.leo122.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra122.api -q /home/wyc/vtyospfd122.api -r")
        self.leo123.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra123.api -q /home/wyc/vtyospfd123.api -r")
        self.leo124.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra124.api -q /home/wyc/vtyospfd124.api -r")
        self.leo125.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra125.api -q /home/wyc/vtyospfd125.api -r")
        self.leo126.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra126.api -q /home/wyc/vtyospfd126.api -r")
        self.leo127.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra127.api -q /home/wyc/vtyospfd127.api -r")
        self.leo128.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra128.api -q /home/wyc/vtyospfd128.api -r")
        self.leo129.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra129.api -q /home/wyc/vtyospfd129.api -r")
        self.leo130.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra130.api -q /home/wyc/vtyospfd130.api -r")
        self.leo131.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra131.api -q /home/wyc/vtyospfd131.api -r")
        self.leo132.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra132.api -q /home/wyc/vtyospfd132.api -r")
        self.leo133.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra133.api -q /home/wyc/vtyospfd133.api -r")
        self.leo134.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra134.api -q /home/wyc/vtyospfd134.api -r")
        self.leo135.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra135.api -q /home/wyc/vtyospfd135.api -r")
        self.leo136.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra136.api -q /home/wyc/vtyospfd136.api -r")
        self.leo137.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra137.api -q /home/wyc/vtyospfd137.api -r")
        self.leo138.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra138.api -q /home/wyc/vtyospfd138.api -r")
        self.leo139.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra139.api -q /home/wyc/vtyospfd139.api -r")
        self.leo140.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra140.api -q /home/wyc/vtyospfd140.api -r")
        self.leo141.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra141.api -q /home/wyc/vtyospfd141.api -r")
        self.leo142.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra142.api -q /home/wyc/vtyospfd142.api -r")
        self.leo143.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra143.api -q /home/wyc/vtyospfd143.api -r")
        self.leo144.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra144.api -q /home/wyc/vtyospfd144.api -r")
        self.leo145.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra145.api -q /home/wyc/vtyospfd145.api -r")
        self.leo146.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra146.api -q /home/wyc/vtyospfd146.api -r")
        self.leo147.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra147.api -q /home/wyc/vtyospfd147.api -r")
        self.leo148.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra148.api -q /home/wyc/vtyospfd148.api -r")
        self.leo149.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra149.api -q /home/wyc/vtyospfd149.api -r")
        self.leo150.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra150.api -q /home/wyc/vtyospfd150.api -r")
        self.leo151.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra151.api -q /home/wyc/vtyospfd151.api -r")
        self.leo152.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra152.api -q /home/wyc/vtyospfd152.api -r")
        self.leo153.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra153.api -q /home/wyc/vtyospfd153.api -r")
        self.leo154.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra154.api -q /home/wyc/vtyospfd154.api -r")
        self.leo155.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra155.api -q /home/wyc/vtyospfd155.api -r")
        self.leo156.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra156.api -q /home/wyc/vtyospfd156.api -r")
        self.leo157.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra157.api -q /home/wyc/vtyospfd157.api -r")
        self.leo158.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra158.api -q /home/wyc/vtyospfd158.api -r")
        self.leo159.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra159.api -q /home/wyc/vtyospfd159.api -r")
        self.leo160.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra160.api -q /home/wyc/vtyospfd160.api -r")
        self.leo161.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra161.api -q /home/wyc/vtyospfd161.api -r")
        self.leo162.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra162.api -q /home/wyc/vtyospfd162.api -r")
        self.leo163.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra163.api -q /home/wyc/vtyospfd163.api -r")
        self.leo164.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra164.api -q /home/wyc/vtyospfd164.api -r")
        self.leo165.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra165.api -q /home/wyc/vtyospfd165.api -r")
        self.leo166.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra166.api -q /home/wyc/vtyospfd166.api -r")
        self.leo167.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra167.api -q /home/wyc/vtyospfd167.api -r")
        self.leo168.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra168.api -q /home/wyc/vtyospfd168.api -r")
        self.leo169.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra169.api -q /home/wyc/vtyospfd169.api -r")
        self.leo170.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra170.api -q /home/wyc/vtyospfd170.api -r")
        self.leo171.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra171.api -q /home/wyc/vtyospfd171.api -r")
        self.leo172.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra172.api -q /home/wyc/vtyospfd172.api -r")
        self.leo173.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra173.api -q /home/wyc/vtyospfd173.api -r")
        self.leo174.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra174.api -q /home/wyc/vtyospfd174.api -r")
        self.leo175.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra175.api -q /home/wyc/vtyospfd175.api -r")
        self.leo176.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra176.api -q /home/wyc/vtyospfd176.api -r")
        self.leo177.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra177.api -q /home/wyc/vtyospfd177.api -r")
        self.leo178.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra178.api -q /home/wyc/vtyospfd178.api -r")
        self.leo179.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra179.api -q /home/wyc/vtyospfd179.api -r")
        self.leo180.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra180.api -q /home/wyc/vtyospfd180.api -r")
        self.leo181.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra181.api -q /home/wyc/vtyospfd181.api -r")
        self.leo182.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra182.api -q /home/wyc/vtyospfd182.api -r")
        self.leo183.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra183.api -q /home/wyc/vtyospfd183.api -r")
        self.leo184.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra184.api -q /home/wyc/vtyospfd184.api -r")
        self.leo185.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra185.api -q /home/wyc/vtyospfd185.api -r")
        self.leo186.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra186.api -q /home/wyc/vtyospfd186.api -r")
        self.leo187.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra187.api -q /home/wyc/vtyospfd187.api -r")
        self.leo188.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra188.api -q /home/wyc/vtyospfd188.api -r")
        self.leo189.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra189.api -q /home/wyc/vtyospfd189.api -r")
        self.leo190.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra190.api -q /home/wyc/vtyospfd190.api -r")
        self.leo191.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra191.api -q /home/wyc/vtyospfd191.api -r")
        self.leo192.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra192.api -q /home/wyc/vtyospfd192.api -r")
        self.leo193.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra193.api -q /home/wyc/vtyospfd193.api -r")
        self.leo194.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra194.api -q /home/wyc/vtyospfd194.api -r")
        self.leo195.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra195.api -q /home/wyc/vtyospfd195.api -r")
        self.leo196.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra196.api -q /home/wyc/vtyospfd196.api -r")
        self.leo197.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra197.api -q /home/wyc/vtyospfd197.api -r")
        self.leo198.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra198.api -q /home/wyc/vtyospfd198.api -r")
        self.leo199.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra199.api -q /home/wyc/vtyospfd199.api -r")
        self.leo200.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra200.api -q /home/wyc/vtyospfd200.api -r")
        self.leo201.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra201.api -q /home/wyc/vtyospfd201.api -r")
        self.leo202.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra202.api -q /home/wyc/vtyospfd202.api -r")
        self.leo203.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra203.api -q /home/wyc/vtyospfd203.api -r")
        self.leo204.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra204.api -q /home/wyc/vtyospfd204.api -r")
        self.leo205.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra205.api -q /home/wyc/vtyospfd205.api -r")
        self.leo206.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra206.api -q /home/wyc/vtyospfd206.api -r")
        self.leo207.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra207.api -q /home/wyc/vtyospfd207.api -r")
        self.leo208.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra208.api -q /home/wyc/vtyospfd208.api -r")
        self.leo209.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra209.api -q /home/wyc/vtyospfd209.api -r")
        self.leo210.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra210.api -q /home/wyc/vtyospfd210.api -r")
        self.leo211.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra211.api -q /home/wyc/vtyospfd211.api -r")
        self.leo212.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra212.api -q /home/wyc/vtyospfd212.api -r")
        self.leo213.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra213.api -q /home/wyc/vtyospfd213.api -r")
        self.leo214.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra214.api -q /home/wyc/vtyospfd214.api -r")
        self.leo215.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra215.api -q /home/wyc/vtyospfd215.api -r")
        self.leo216.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra216.api -q /home/wyc/vtyospfd216.api -r")
        self.leo217.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra217.api -q /home/wyc/vtyospfd217.api -r")
        self.leo218.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra218.api -q /home/wyc/vtyospfd218.api -r")
        self.leo219.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra219.api -q /home/wyc/vtyospfd219.api -r")
        self.leo220.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra220.api -q /home/wyc/vtyospfd220.api -r")
        self.leo221.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra221.api -q /home/wyc/vtyospfd221.api -r")
        self.leo222.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra222.api -q /home/wyc/vtyospfd222.api -r")
        self.leo223.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra223.api -q /home/wyc/vtyospfd223.api -r")
        self.leo224.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra224.api -q /home/wyc/vtyospfd224.api -r")
        self.leo225.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra225.api -q /home/wyc/vtyospfd225.api -r")
        self.leo226.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra226.api -q /home/wyc/vtyospfd226.api -r")
        self.leo227.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra227.api -q /home/wyc/vtyospfd227.api -r")
        self.leo228.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra228.api -q /home/wyc/vtyospfd228.api -r")
        self.leo229.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra229.api -q /home/wyc/vtyospfd229.api -r")
        self.leo230.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra230.api -q /home/wyc/vtyospfd230.api -r")
        self.leo231.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra231.api -q /home/wyc/vtyospfd231.api -r")
        self.leo232.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra232.api -q /home/wyc/vtyospfd232.api -r")
        self.leo233.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra233.api -q /home/wyc/vtyospfd233.api -r")
        self.leo234.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra234.api -q /home/wyc/vtyospfd234.api -r")
        self.leo235.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra235.api -q /home/wyc/vtyospfd235.api -r")
        self.leo236.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra236.api -q /home/wyc/vtyospfd236.api -r")
        self.leo237.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra237.api -q /home/wyc/vtyospfd237.api -r")
        self.leo238.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra238.api -q /home/wyc/vtyospfd238.api -r")
        self.leo239.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/add_phase.conf -w /home/wyc/vtyzebra239.api -q /home/wyc/vtyospfd239.api -r")
        time.sleep(10)


    def begin_running(self):
        self.leo0.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra0.api -q /home/wyc/vtyospfd0.api -r")
        self.leo1.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra1.api -q /home/wyc/vtyospfd1.api -r")
        self.leo2.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra2.api -q /home/wyc/vtyospfd2.api -r")
        self.leo3.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra3.api -q /home/wyc/vtyospfd3.api -r")
        self.leo4.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra4.api -q /home/wyc/vtyospfd4.api -r")
        self.leo5.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra5.api -q /home/wyc/vtyospfd5.api -r")
        self.leo6.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra6.api -q /home/wyc/vtyospfd6.api -r")
        self.leo7.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra7.api -q /home/wyc/vtyospfd7.api -r")
        self.leo8.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra8.api -q /home/wyc/vtyospfd8.api -r")
        self.leo9.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra9.api -q /home/wyc/vtyospfd9.api -r")
        self.leo10.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra10.api -q /home/wyc/vtyospfd10.api -r")
        self.leo11.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra11.api -q /home/wyc/vtyospfd11.api -r")
        self.leo12.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra12.api -q /home/wyc/vtyospfd12.api -r")
        self.leo13.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra13.api -q /home/wyc/vtyospfd13.api -r")
        self.leo14.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra14.api -q /home/wyc/vtyospfd14.api -r")
        self.leo15.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra15.api -q /home/wyc/vtyospfd15.api -r")
        self.leo16.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra16.api -q /home/wyc/vtyospfd16.api -r")
        self.leo17.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra17.api -q /home/wyc/vtyospfd17.api -r")
        self.leo18.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra18.api -q /home/wyc/vtyospfd18.api -r")
        self.leo19.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra19.api -q /home/wyc/vtyospfd19.api -r")
        self.leo20.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra20.api -q /home/wyc/vtyospfd20.api -r")
        self.leo21.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra21.api -q /home/wyc/vtyospfd21.api -r")
        self.leo22.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra22.api -q /home/wyc/vtyospfd22.api -r")
        self.leo23.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra23.api -q /home/wyc/vtyospfd23.api -r")
        self.leo24.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra24.api -q /home/wyc/vtyospfd24.api -r")
        self.leo25.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra25.api -q /home/wyc/vtyospfd25.api -r")
        self.leo26.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra26.api -q /home/wyc/vtyospfd26.api -r")
        self.leo27.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra27.api -q /home/wyc/vtyospfd27.api -r")
        self.leo28.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra28.api -q /home/wyc/vtyospfd28.api -r")
        self.leo29.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra29.api -q /home/wyc/vtyospfd29.api -r")
        self.leo30.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra30.api -q /home/wyc/vtyospfd30.api -r")
        self.leo31.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra31.api -q /home/wyc/vtyospfd31.api -r")
        self.leo32.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra32.api -q /home/wyc/vtyospfd32.api -r")
        self.leo33.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra33.api -q /home/wyc/vtyospfd33.api -r")
        self.leo34.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra34.api -q /home/wyc/vtyospfd34.api -r")
        self.leo35.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra35.api -q /home/wyc/vtyospfd35.api -r")
        self.leo36.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra36.api -q /home/wyc/vtyospfd36.api -r")
        self.leo37.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra37.api -q /home/wyc/vtyospfd37.api -r")
        self.leo38.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra38.api -q /home/wyc/vtyospfd38.api -r")
        self.leo39.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra39.api -q /home/wyc/vtyospfd39.api -r")
        self.leo40.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra40.api -q /home/wyc/vtyospfd40.api -r")
        self.leo41.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra41.api -q /home/wyc/vtyospfd41.api -r")
        self.leo42.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra42.api -q /home/wyc/vtyospfd42.api -r")
        self.leo43.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra43.api -q /home/wyc/vtyospfd43.api -r")
        self.leo44.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra44.api -q /home/wyc/vtyospfd44.api -r")
        self.leo45.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra45.api -q /home/wyc/vtyospfd45.api -r")
        self.leo46.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra46.api -q /home/wyc/vtyospfd46.api -r")
        self.leo47.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra47.api -q /home/wyc/vtyospfd47.api -r")
        self.leo48.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra48.api -q /home/wyc/vtyospfd48.api -r")
        self.leo49.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra49.api -q /home/wyc/vtyospfd49.api -r")
        self.leo50.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra50.api -q /home/wyc/vtyospfd50.api -r")
        self.leo51.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra51.api -q /home/wyc/vtyospfd51.api -r")
        self.leo52.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra52.api -q /home/wyc/vtyospfd52.api -r")
        self.leo53.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra53.api -q /home/wyc/vtyospfd53.api -r")
        self.leo54.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra54.api -q /home/wyc/vtyospfd54.api -r")
        self.leo55.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra55.api -q /home/wyc/vtyospfd55.api -r")
        self.leo56.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra56.api -q /home/wyc/vtyospfd56.api -r")
        self.leo57.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra57.api -q /home/wyc/vtyospfd57.api -r")
        self.leo58.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra58.api -q /home/wyc/vtyospfd58.api -r")
        self.leo59.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra59.api -q /home/wyc/vtyospfd59.api -r")
        self.leo60.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra60.api -q /home/wyc/vtyospfd60.api -r")
        self.leo61.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra61.api -q /home/wyc/vtyospfd61.api -r")
        self.leo62.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra62.api -q /home/wyc/vtyospfd62.api -r")
        self.leo63.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra63.api -q /home/wyc/vtyospfd63.api -r")
        self.leo64.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra64.api -q /home/wyc/vtyospfd64.api -r")
        self.leo65.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra65.api -q /home/wyc/vtyospfd65.api -r")
        self.leo66.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra66.api -q /home/wyc/vtyospfd66.api -r")
        self.leo67.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra67.api -q /home/wyc/vtyospfd67.api -r")
        self.leo68.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra68.api -q /home/wyc/vtyospfd68.api -r")
        self.leo69.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra69.api -q /home/wyc/vtyospfd69.api -r")
        self.leo70.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra70.api -q /home/wyc/vtyospfd70.api -r")
        self.leo71.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra71.api -q /home/wyc/vtyospfd71.api -r")
        self.leo72.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra72.api -q /home/wyc/vtyospfd72.api -r")
        self.leo73.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra73.api -q /home/wyc/vtyospfd73.api -r")
        self.leo74.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra74.api -q /home/wyc/vtyospfd74.api -r")
        self.leo75.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra75.api -q /home/wyc/vtyospfd75.api -r")
        self.leo76.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra76.api -q /home/wyc/vtyospfd76.api -r")
        self.leo77.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra77.api -q /home/wyc/vtyospfd77.api -r")
        self.leo78.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra78.api -q /home/wyc/vtyospfd78.api -r")
        self.leo79.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra79.api -q /home/wyc/vtyospfd79.api -r")
        self.leo80.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra80.api -q /home/wyc/vtyospfd80.api -r")
        self.leo81.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra81.api -q /home/wyc/vtyospfd81.api -r")
        self.leo82.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra82.api -q /home/wyc/vtyospfd82.api -r")
        self.leo83.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra83.api -q /home/wyc/vtyospfd83.api -r")
        self.leo84.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra84.api -q /home/wyc/vtyospfd84.api -r")
        self.leo85.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra85.api -q /home/wyc/vtyospfd85.api -r")
        self.leo86.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra86.api -q /home/wyc/vtyospfd86.api -r")
        self.leo87.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra87.api -q /home/wyc/vtyospfd87.api -r")
        self.leo88.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra88.api -q /home/wyc/vtyospfd88.api -r")
        self.leo89.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra89.api -q /home/wyc/vtyospfd89.api -r")
        self.leo90.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra90.api -q /home/wyc/vtyospfd90.api -r")
        self.leo91.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra91.api -q /home/wyc/vtyospfd91.api -r")
        self.leo92.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra92.api -q /home/wyc/vtyospfd92.api -r")
        self.leo93.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra93.api -q /home/wyc/vtyospfd93.api -r")
        self.leo94.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra94.api -q /home/wyc/vtyospfd94.api -r")
        self.leo95.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra95.api -q /home/wyc/vtyospfd95.api -r")
        self.leo96.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra96.api -q /home/wyc/vtyospfd96.api -r")
        self.leo97.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra97.api -q /home/wyc/vtyospfd97.api -r")
        self.leo98.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra98.api -q /home/wyc/vtyospfd98.api -r")
        self.leo99.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra99.api -q /home/wyc/vtyospfd99.api -r")
        self.leo100.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra100.api -q /home/wyc/vtyospfd100.api -r")
        self.leo101.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra101.api -q /home/wyc/vtyospfd101.api -r")
        self.leo102.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra102.api -q /home/wyc/vtyospfd102.api -r")
        self.leo103.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra103.api -q /home/wyc/vtyospfd103.api -r")
        self.leo104.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra104.api -q /home/wyc/vtyospfd104.api -r")
        self.leo105.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra105.api -q /home/wyc/vtyospfd105.api -r")
        self.leo106.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra106.api -q /home/wyc/vtyospfd106.api -r")
        self.leo107.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra107.api -q /home/wyc/vtyospfd107.api -r")
        self.leo108.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra108.api -q /home/wyc/vtyospfd108.api -r")
        self.leo109.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra109.api -q /home/wyc/vtyospfd109.api -r")
        self.leo110.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra110.api -q /home/wyc/vtyospfd110.api -r")
        self.leo111.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra111.api -q /home/wyc/vtyospfd111.api -r")
        self.leo112.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra112.api -q /home/wyc/vtyospfd112.api -r")
        self.leo113.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra113.api -q /home/wyc/vtyospfd113.api -r")
        self.leo114.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra114.api -q /home/wyc/vtyospfd114.api -r")
        self.leo115.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra115.api -q /home/wyc/vtyospfd115.api -r")
        self.leo116.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra116.api -q /home/wyc/vtyospfd116.api -r")
        self.leo117.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra117.api -q /home/wyc/vtyospfd117.api -r")
        self.leo118.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra118.api -q /home/wyc/vtyospfd118.api -r")
        self.leo119.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra119.api -q /home/wyc/vtyospfd119.api -r")
        self.leo120.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra120.api -q /home/wyc/vtyospfd120.api -r")
        self.leo121.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra121.api -q /home/wyc/vtyospfd121.api -r")
        self.leo122.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra122.api -q /home/wyc/vtyospfd122.api -r")
        self.leo123.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra123.api -q /home/wyc/vtyospfd123.api -r")
        self.leo124.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra124.api -q /home/wyc/vtyospfd124.api -r")
        self.leo125.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra125.api -q /home/wyc/vtyospfd125.api -r")
        self.leo126.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra126.api -q /home/wyc/vtyospfd126.api -r")
        self.leo127.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra127.api -q /home/wyc/vtyospfd127.api -r")
        self.leo128.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra128.api -q /home/wyc/vtyospfd128.api -r")
        self.leo129.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra129.api -q /home/wyc/vtyospfd129.api -r")
        self.leo130.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra130.api -q /home/wyc/vtyospfd130.api -r")
        self.leo131.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra131.api -q /home/wyc/vtyospfd131.api -r")
        self.leo132.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra132.api -q /home/wyc/vtyospfd132.api -r")
        self.leo133.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra133.api -q /home/wyc/vtyospfd133.api -r")
        self.leo134.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra134.api -q /home/wyc/vtyospfd134.api -r")
        self.leo135.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra135.api -q /home/wyc/vtyospfd135.api -r")
        self.leo136.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra136.api -q /home/wyc/vtyospfd136.api -r")
        self.leo137.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra137.api -q /home/wyc/vtyospfd137.api -r")
        self.leo138.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra138.api -q /home/wyc/vtyospfd138.api -r")
        self.leo139.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra139.api -q /home/wyc/vtyospfd139.api -r")
        self.leo140.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra140.api -q /home/wyc/vtyospfd140.api -r")
        self.leo141.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra141.api -q /home/wyc/vtyospfd141.api -r")
        self.leo142.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra142.api -q /home/wyc/vtyospfd142.api -r")
        self.leo143.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra143.api -q /home/wyc/vtyospfd143.api -r")
        self.leo144.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra144.api -q /home/wyc/vtyospfd144.api -r")
        self.leo145.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra145.api -q /home/wyc/vtyospfd145.api -r")
        self.leo146.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra146.api -q /home/wyc/vtyospfd146.api -r")
        self.leo147.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra147.api -q /home/wyc/vtyospfd147.api -r")
        self.leo148.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra148.api -q /home/wyc/vtyospfd148.api -r")
        self.leo149.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra149.api -q /home/wyc/vtyospfd149.api -r")
        self.leo150.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra150.api -q /home/wyc/vtyospfd150.api -r")
        self.leo151.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra151.api -q /home/wyc/vtyospfd151.api -r")
        self.leo152.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra152.api -q /home/wyc/vtyospfd152.api -r")
        self.leo153.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra153.api -q /home/wyc/vtyospfd153.api -r")
        self.leo154.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra154.api -q /home/wyc/vtyospfd154.api -r")
        self.leo155.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra155.api -q /home/wyc/vtyospfd155.api -r")
        self.leo156.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra156.api -q /home/wyc/vtyospfd156.api -r")
        self.leo157.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra157.api -q /home/wyc/vtyospfd157.api -r")
        self.leo158.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra158.api -q /home/wyc/vtyospfd158.api -r")
        self.leo159.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra159.api -q /home/wyc/vtyospfd159.api -r")
        self.leo160.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra160.api -q /home/wyc/vtyospfd160.api -r")
        self.leo161.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra161.api -q /home/wyc/vtyospfd161.api -r")
        self.leo162.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra162.api -q /home/wyc/vtyospfd162.api -r")
        self.leo163.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra163.api -q /home/wyc/vtyospfd163.api -r")
        self.leo164.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra164.api -q /home/wyc/vtyospfd164.api -r")
        self.leo165.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra165.api -q /home/wyc/vtyospfd165.api -r")
        self.leo166.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra166.api -q /home/wyc/vtyospfd166.api -r")
        self.leo167.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra167.api -q /home/wyc/vtyospfd167.api -r")
        self.leo168.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra168.api -q /home/wyc/vtyospfd168.api -r")
        self.leo169.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra169.api -q /home/wyc/vtyospfd169.api -r")
        self.leo170.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra170.api -q /home/wyc/vtyospfd170.api -r")
        self.leo171.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra171.api -q /home/wyc/vtyospfd171.api -r")
        self.leo172.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra172.api -q /home/wyc/vtyospfd172.api -r")
        self.leo173.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra173.api -q /home/wyc/vtyospfd173.api -r")
        self.leo174.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra174.api -q /home/wyc/vtyospfd174.api -r")
        self.leo175.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra175.api -q /home/wyc/vtyospfd175.api -r")
        self.leo176.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra176.api -q /home/wyc/vtyospfd176.api -r")
        self.leo177.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra177.api -q /home/wyc/vtyospfd177.api -r")
        self.leo178.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra178.api -q /home/wyc/vtyospfd178.api -r")
        self.leo179.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra179.api -q /home/wyc/vtyospfd179.api -r")
        self.leo180.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra180.api -q /home/wyc/vtyospfd180.api -r")
        self.leo181.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra181.api -q /home/wyc/vtyospfd181.api -r")
        self.leo182.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra182.api -q /home/wyc/vtyospfd182.api -r")
        self.leo183.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra183.api -q /home/wyc/vtyospfd183.api -r")
        self.leo184.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra184.api -q /home/wyc/vtyospfd184.api -r")
        self.leo185.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra185.api -q /home/wyc/vtyospfd185.api -r")
        self.leo186.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra186.api -q /home/wyc/vtyospfd186.api -r")
        self.leo187.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra187.api -q /home/wyc/vtyospfd187.api -r")
        self.leo188.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra188.api -q /home/wyc/vtyospfd188.api -r")
        self.leo189.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra189.api -q /home/wyc/vtyospfd189.api -r")
        self.leo190.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra190.api -q /home/wyc/vtyospfd190.api -r")
        self.leo191.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra191.api -q /home/wyc/vtyospfd191.api -r")
        self.leo192.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra192.api -q /home/wyc/vtyospfd192.api -r")
        self.leo193.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra193.api -q /home/wyc/vtyospfd193.api -r")
        self.leo194.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra194.api -q /home/wyc/vtyospfd194.api -r")
        self.leo195.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra195.api -q /home/wyc/vtyospfd195.api -r")
        self.leo196.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra196.api -q /home/wyc/vtyospfd196.api -r")
        self.leo197.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra197.api -q /home/wyc/vtyospfd197.api -r")
        self.leo198.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra198.api -q /home/wyc/vtyospfd198.api -r")
        self.leo199.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra199.api -q /home/wyc/vtyospfd199.api -r")
        self.leo200.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra200.api -q /home/wyc/vtyospfd200.api -r")
        self.leo201.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra201.api -q /home/wyc/vtyospfd201.api -r")
        self.leo202.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra202.api -q /home/wyc/vtyospfd202.api -r")
        self.leo203.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra203.api -q /home/wyc/vtyospfd203.api -r")
        self.leo204.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra204.api -q /home/wyc/vtyospfd204.api -r")
        self.leo205.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra205.api -q /home/wyc/vtyospfd205.api -r")
        self.leo206.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra206.api -q /home/wyc/vtyospfd206.api -r")
        self.leo207.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra207.api -q /home/wyc/vtyospfd207.api -r")
        self.leo208.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra208.api -q /home/wyc/vtyospfd208.api -r")
        self.leo209.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra209.api -q /home/wyc/vtyospfd209.api -r")
        self.leo210.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra210.api -q /home/wyc/vtyospfd210.api -r")
        self.leo211.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra211.api -q /home/wyc/vtyospfd211.api -r")
        self.leo212.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra212.api -q /home/wyc/vtyospfd212.api -r")
        self.leo213.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra213.api -q /home/wyc/vtyospfd213.api -r")
        self.leo214.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra214.api -q /home/wyc/vtyospfd214.api -r")
        self.leo215.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra215.api -q /home/wyc/vtyospfd215.api -r")
        self.leo216.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra216.api -q /home/wyc/vtyospfd216.api -r")
        self.leo217.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra217.api -q /home/wyc/vtyospfd217.api -r")
        self.leo218.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra218.api -q /home/wyc/vtyospfd218.api -r")
        self.leo219.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra219.api -q /home/wyc/vtyospfd219.api -r")
        self.leo220.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra220.api -q /home/wyc/vtyospfd220.api -r")
        self.leo221.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra221.api -q /home/wyc/vtyospfd221.api -r")
        self.leo222.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra222.api -q /home/wyc/vtyospfd222.api -r")
        self.leo223.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra223.api -q /home/wyc/vtyospfd223.api -r")
        self.leo224.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra224.api -q /home/wyc/vtyospfd224.api -r")
        self.leo225.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra225.api -q /home/wyc/vtyospfd225.api -r")
        self.leo226.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra226.api -q /home/wyc/vtyospfd226.api -r")
        self.leo227.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra227.api -q /home/wyc/vtyospfd227.api -r")
        self.leo228.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra228.api -q /home/wyc/vtyospfd228.api -r")
        self.leo229.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra229.api -q /home/wyc/vtyospfd229.api -r")
        self.leo230.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra230.api -q /home/wyc/vtyospfd230.api -r")
        self.leo231.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra231.api -q /home/wyc/vtyospfd231.api -r")
        self.leo232.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra232.api -q /home/wyc/vtyospfd232.api -r")
        self.leo233.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra233.api -q /home/wyc/vtyospfd233.api -r")
        self.leo234.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra234.api -q /home/wyc/vtyospfd234.api -r")
        self.leo235.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra235.api -q /home/wyc/vtyospfd235.api -r")
        self.leo236.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra236.api -q /home/wyc/vtyospfd236.api -r")
        self.leo237.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra237.api -q /home/wyc/vtyospfd237.api -r")
        self.leo238.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra238.api -q /home/wyc/vtyospfd238.api -r")
        self.leo239.cmd("vtysh -f /mnt/hgfs/vm_new/test_data/AS_240_6/cmd/begin_running.conf -w /home/wyc/vtyzebra239.api -q /home/wyc/vtyospfd239.api -r")
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
    leo60=net.getNodeByName('leo60')
    leo61=net.getNodeByName('leo61')
    leo62=net.getNodeByName('leo62')
    leo63=net.getNodeByName('leo63')
    leo64=net.getNodeByName('leo64')
    leo65=net.getNodeByName('leo65')
    leo66=net.getNodeByName('leo66')
    leo67=net.getNodeByName('leo67')
    leo68=net.getNodeByName('leo68')
    leo69=net.getNodeByName('leo69')
    leo70=net.getNodeByName('leo70')
    leo71=net.getNodeByName('leo71')
    leo72=net.getNodeByName('leo72')
    leo73=net.getNodeByName('leo73')
    leo74=net.getNodeByName('leo74')
    leo75=net.getNodeByName('leo75')
    leo76=net.getNodeByName('leo76')
    leo77=net.getNodeByName('leo77')
    leo78=net.getNodeByName('leo78')
    leo79=net.getNodeByName('leo79')
    leo80=net.getNodeByName('leo80')
    leo81=net.getNodeByName('leo81')
    leo82=net.getNodeByName('leo82')
    leo83=net.getNodeByName('leo83')
    leo84=net.getNodeByName('leo84')
    leo85=net.getNodeByName('leo85')
    leo86=net.getNodeByName('leo86')
    leo87=net.getNodeByName('leo87')
    leo88=net.getNodeByName('leo88')
    leo89=net.getNodeByName('leo89')
    leo90=net.getNodeByName('leo90')
    leo91=net.getNodeByName('leo91')
    leo92=net.getNodeByName('leo92')
    leo93=net.getNodeByName('leo93')
    leo94=net.getNodeByName('leo94')
    leo95=net.getNodeByName('leo95')
    leo96=net.getNodeByName('leo96')
    leo97=net.getNodeByName('leo97')
    leo98=net.getNodeByName('leo98')
    leo99=net.getNodeByName('leo99')
    leo100=net.getNodeByName('leo100')
    leo101=net.getNodeByName('leo101')
    leo102=net.getNodeByName('leo102')
    leo103=net.getNodeByName('leo103')
    leo104=net.getNodeByName('leo104')
    leo105=net.getNodeByName('leo105')
    leo106=net.getNodeByName('leo106')
    leo107=net.getNodeByName('leo107')
    leo108=net.getNodeByName('leo108')
    leo109=net.getNodeByName('leo109')
    leo110=net.getNodeByName('leo110')
    leo111=net.getNodeByName('leo111')
    leo112=net.getNodeByName('leo112')
    leo113=net.getNodeByName('leo113')
    leo114=net.getNodeByName('leo114')
    leo115=net.getNodeByName('leo115')
    leo116=net.getNodeByName('leo116')
    leo117=net.getNodeByName('leo117')
    leo118=net.getNodeByName('leo118')
    leo119=net.getNodeByName('leo119')
    leo120=net.getNodeByName('leo120')
    leo121=net.getNodeByName('leo121')
    leo122=net.getNodeByName('leo122')
    leo123=net.getNodeByName('leo123')
    leo124=net.getNodeByName('leo124')
    leo125=net.getNodeByName('leo125')
    leo126=net.getNodeByName('leo126')
    leo127=net.getNodeByName('leo127')
    leo128=net.getNodeByName('leo128')
    leo129=net.getNodeByName('leo129')
    leo130=net.getNodeByName('leo130')
    leo131=net.getNodeByName('leo131')
    leo132=net.getNodeByName('leo132')
    leo133=net.getNodeByName('leo133')
    leo134=net.getNodeByName('leo134')
    leo135=net.getNodeByName('leo135')
    leo136=net.getNodeByName('leo136')
    leo137=net.getNodeByName('leo137')
    leo138=net.getNodeByName('leo138')
    leo139=net.getNodeByName('leo139')
    leo140=net.getNodeByName('leo140')
    leo141=net.getNodeByName('leo141')
    leo142=net.getNodeByName('leo142')
    leo143=net.getNodeByName('leo143')
    leo144=net.getNodeByName('leo144')
    leo145=net.getNodeByName('leo145')
    leo146=net.getNodeByName('leo146')
    leo147=net.getNodeByName('leo147')
    leo148=net.getNodeByName('leo148')
    leo149=net.getNodeByName('leo149')
    leo150=net.getNodeByName('leo150')
    leo151=net.getNodeByName('leo151')
    leo152=net.getNodeByName('leo152')
    leo153=net.getNodeByName('leo153')
    leo154=net.getNodeByName('leo154')
    leo155=net.getNodeByName('leo155')
    leo156=net.getNodeByName('leo156')
    leo157=net.getNodeByName('leo157')
    leo158=net.getNodeByName('leo158')
    leo159=net.getNodeByName('leo159')
    leo160=net.getNodeByName('leo160')
    leo161=net.getNodeByName('leo161')
    leo162=net.getNodeByName('leo162')
    leo163=net.getNodeByName('leo163')
    leo164=net.getNodeByName('leo164')
    leo165=net.getNodeByName('leo165')
    leo166=net.getNodeByName('leo166')
    leo167=net.getNodeByName('leo167')
    leo168=net.getNodeByName('leo168')
    leo169=net.getNodeByName('leo169')
    leo170=net.getNodeByName('leo170')
    leo171=net.getNodeByName('leo171')
    leo172=net.getNodeByName('leo172')
    leo173=net.getNodeByName('leo173')
    leo174=net.getNodeByName('leo174')
    leo175=net.getNodeByName('leo175')
    leo176=net.getNodeByName('leo176')
    leo177=net.getNodeByName('leo177')
    leo178=net.getNodeByName('leo178')
    leo179=net.getNodeByName('leo179')
    leo180=net.getNodeByName('leo180')
    leo181=net.getNodeByName('leo181')
    leo182=net.getNodeByName('leo182')
    leo183=net.getNodeByName('leo183')
    leo184=net.getNodeByName('leo184')
    leo185=net.getNodeByName('leo185')
    leo186=net.getNodeByName('leo186')
    leo187=net.getNodeByName('leo187')
    leo188=net.getNodeByName('leo188')
    leo189=net.getNodeByName('leo189')
    leo190=net.getNodeByName('leo190')
    leo191=net.getNodeByName('leo191')
    leo192=net.getNodeByName('leo192')
    leo193=net.getNodeByName('leo193')
    leo194=net.getNodeByName('leo194')
    leo195=net.getNodeByName('leo195')
    leo196=net.getNodeByName('leo196')
    leo197=net.getNodeByName('leo197')
    leo198=net.getNodeByName('leo198')
    leo199=net.getNodeByName('leo199')
    leo200=net.getNodeByName('leo200')
    leo201=net.getNodeByName('leo201')
    leo202=net.getNodeByName('leo202')
    leo203=net.getNodeByName('leo203')
    leo204=net.getNodeByName('leo204')
    leo205=net.getNodeByName('leo205')
    leo206=net.getNodeByName('leo206')
    leo207=net.getNodeByName('leo207')
    leo208=net.getNodeByName('leo208')
    leo209=net.getNodeByName('leo209')
    leo210=net.getNodeByName('leo210')
    leo211=net.getNodeByName('leo211')
    leo212=net.getNodeByName('leo212')
    leo213=net.getNodeByName('leo213')
    leo214=net.getNodeByName('leo214')
    leo215=net.getNodeByName('leo215')
    leo216=net.getNodeByName('leo216')
    leo217=net.getNodeByName('leo217')
    leo218=net.getNodeByName('leo218')
    leo219=net.getNodeByName('leo219')
    leo220=net.getNodeByName('leo220')
    leo221=net.getNodeByName('leo221')
    leo222=net.getNodeByName('leo222')
    leo223=net.getNodeByName('leo223')
    leo224=net.getNodeByName('leo224')
    leo225=net.getNodeByName('leo225')
    leo226=net.getNodeByName('leo226')
    leo227=net.getNodeByName('leo227')
    leo228=net.getNodeByName('leo228')
    leo229=net.getNodeByName('leo229')
    leo230=net.getNodeByName('leo230')
    leo231=net.getNodeByName('leo231')
    leo232=net.getNodeByName('leo232')
    leo233=net.getNodeByName('leo233')
    leo234=net.getNodeByName('leo234')
    leo235=net.getNodeByName('leo235')
    leo236=net.getNodeByName('leo236')
    leo237=net.getNodeByName('leo237')
    leo238=net.getNodeByName('leo238')
    leo239=net.getNodeByName('leo239')
    station0=net.getNodeByName('station0')
    station1=net.getNodeByName('station1')
    station2=net.getNodeByName('station2')
    leo0.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo0zebra.conf -d -z /home/wyc/leo0zebra.api -i /home/wyc/leo0zebra.interface -w /home/wyc/vtyzebra0.api')
    leo1.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo1zebra.conf -d -z /home/wyc/leo1zebra.api -i /home/wyc/leo1zebra.interface -w /home/wyc/vtyzebra1.api')
    leo2.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo2zebra.conf -d -z /home/wyc/leo2zebra.api -i /home/wyc/leo2zebra.interface -w /home/wyc/vtyzebra2.api')
    leo3.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo3zebra.conf -d -z /home/wyc/leo3zebra.api -i /home/wyc/leo3zebra.interface -w /home/wyc/vtyzebra3.api')
    leo4.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo4zebra.conf -d -z /home/wyc/leo4zebra.api -i /home/wyc/leo4zebra.interface -w /home/wyc/vtyzebra4.api')
    leo5.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo5zebra.conf -d -z /home/wyc/leo5zebra.api -i /home/wyc/leo5zebra.interface -w /home/wyc/vtyzebra5.api')
    leo6.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo6zebra.conf -d -z /home/wyc/leo6zebra.api -i /home/wyc/leo6zebra.interface -w /home/wyc/vtyzebra6.api')
    leo7.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo7zebra.conf -d -z /home/wyc/leo7zebra.api -i /home/wyc/leo7zebra.interface -w /home/wyc/vtyzebra7.api')
    leo8.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo8zebra.conf -d -z /home/wyc/leo8zebra.api -i /home/wyc/leo8zebra.interface -w /home/wyc/vtyzebra8.api')
    leo9.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo9zebra.conf -d -z /home/wyc/leo9zebra.api -i /home/wyc/leo9zebra.interface -w /home/wyc/vtyzebra9.api')
    leo10.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo10zebra.conf -d -z /home/wyc/leo10zebra.api -i /home/wyc/leo10zebra.interface -w /home/wyc/vtyzebra10.api')
    leo11.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo11zebra.conf -d -z /home/wyc/leo11zebra.api -i /home/wyc/leo11zebra.interface -w /home/wyc/vtyzebra11.api')
    leo12.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo12zebra.conf -d -z /home/wyc/leo12zebra.api -i /home/wyc/leo12zebra.interface -w /home/wyc/vtyzebra12.api')
    leo13.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo13zebra.conf -d -z /home/wyc/leo13zebra.api -i /home/wyc/leo13zebra.interface -w /home/wyc/vtyzebra13.api')
    leo14.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo14zebra.conf -d -z /home/wyc/leo14zebra.api -i /home/wyc/leo14zebra.interface -w /home/wyc/vtyzebra14.api')
    leo15.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo15zebra.conf -d -z /home/wyc/leo15zebra.api -i /home/wyc/leo15zebra.interface -w /home/wyc/vtyzebra15.api')
    leo16.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo16zebra.conf -d -z /home/wyc/leo16zebra.api -i /home/wyc/leo16zebra.interface -w /home/wyc/vtyzebra16.api')
    leo17.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo17zebra.conf -d -z /home/wyc/leo17zebra.api -i /home/wyc/leo17zebra.interface -w /home/wyc/vtyzebra17.api')
    leo18.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo18zebra.conf -d -z /home/wyc/leo18zebra.api -i /home/wyc/leo18zebra.interface -w /home/wyc/vtyzebra18.api')
    leo19.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo19zebra.conf -d -z /home/wyc/leo19zebra.api -i /home/wyc/leo19zebra.interface -w /home/wyc/vtyzebra19.api')
    leo20.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo20zebra.conf -d -z /home/wyc/leo20zebra.api -i /home/wyc/leo20zebra.interface -w /home/wyc/vtyzebra20.api')
    leo21.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo21zebra.conf -d -z /home/wyc/leo21zebra.api -i /home/wyc/leo21zebra.interface -w /home/wyc/vtyzebra21.api')
    leo22.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo22zebra.conf -d -z /home/wyc/leo22zebra.api -i /home/wyc/leo22zebra.interface -w /home/wyc/vtyzebra22.api')
    leo23.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo23zebra.conf -d -z /home/wyc/leo23zebra.api -i /home/wyc/leo23zebra.interface -w /home/wyc/vtyzebra23.api')
    leo24.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo24zebra.conf -d -z /home/wyc/leo24zebra.api -i /home/wyc/leo24zebra.interface -w /home/wyc/vtyzebra24.api')
    leo25.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo25zebra.conf -d -z /home/wyc/leo25zebra.api -i /home/wyc/leo25zebra.interface -w /home/wyc/vtyzebra25.api')
    leo26.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo26zebra.conf -d -z /home/wyc/leo26zebra.api -i /home/wyc/leo26zebra.interface -w /home/wyc/vtyzebra26.api')
    leo27.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo27zebra.conf -d -z /home/wyc/leo27zebra.api -i /home/wyc/leo27zebra.interface -w /home/wyc/vtyzebra27.api')
    leo28.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo28zebra.conf -d -z /home/wyc/leo28zebra.api -i /home/wyc/leo28zebra.interface -w /home/wyc/vtyzebra28.api')
    leo29.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo29zebra.conf -d -z /home/wyc/leo29zebra.api -i /home/wyc/leo29zebra.interface -w /home/wyc/vtyzebra29.api')
    leo30.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo30zebra.conf -d -z /home/wyc/leo30zebra.api -i /home/wyc/leo30zebra.interface -w /home/wyc/vtyzebra30.api')
    leo31.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo31zebra.conf -d -z /home/wyc/leo31zebra.api -i /home/wyc/leo31zebra.interface -w /home/wyc/vtyzebra31.api')
    leo32.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo32zebra.conf -d -z /home/wyc/leo32zebra.api -i /home/wyc/leo32zebra.interface -w /home/wyc/vtyzebra32.api')
    leo33.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo33zebra.conf -d -z /home/wyc/leo33zebra.api -i /home/wyc/leo33zebra.interface -w /home/wyc/vtyzebra33.api')
    leo34.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo34zebra.conf -d -z /home/wyc/leo34zebra.api -i /home/wyc/leo34zebra.interface -w /home/wyc/vtyzebra34.api')
    leo35.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo35zebra.conf -d -z /home/wyc/leo35zebra.api -i /home/wyc/leo35zebra.interface -w /home/wyc/vtyzebra35.api')
    leo36.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo36zebra.conf -d -z /home/wyc/leo36zebra.api -i /home/wyc/leo36zebra.interface -w /home/wyc/vtyzebra36.api')
    leo37.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo37zebra.conf -d -z /home/wyc/leo37zebra.api -i /home/wyc/leo37zebra.interface -w /home/wyc/vtyzebra37.api')
    leo38.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo38zebra.conf -d -z /home/wyc/leo38zebra.api -i /home/wyc/leo38zebra.interface -w /home/wyc/vtyzebra38.api')
    leo39.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo39zebra.conf -d -z /home/wyc/leo39zebra.api -i /home/wyc/leo39zebra.interface -w /home/wyc/vtyzebra39.api')
    leo40.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo40zebra.conf -d -z /home/wyc/leo40zebra.api -i /home/wyc/leo40zebra.interface -w /home/wyc/vtyzebra40.api')
    leo41.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo41zebra.conf -d -z /home/wyc/leo41zebra.api -i /home/wyc/leo41zebra.interface -w /home/wyc/vtyzebra41.api')
    leo42.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo42zebra.conf -d -z /home/wyc/leo42zebra.api -i /home/wyc/leo42zebra.interface -w /home/wyc/vtyzebra42.api')
    leo43.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo43zebra.conf -d -z /home/wyc/leo43zebra.api -i /home/wyc/leo43zebra.interface -w /home/wyc/vtyzebra43.api')
    leo44.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo44zebra.conf -d -z /home/wyc/leo44zebra.api -i /home/wyc/leo44zebra.interface -w /home/wyc/vtyzebra44.api')
    leo45.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo45zebra.conf -d -z /home/wyc/leo45zebra.api -i /home/wyc/leo45zebra.interface -w /home/wyc/vtyzebra45.api')
    leo46.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo46zebra.conf -d -z /home/wyc/leo46zebra.api -i /home/wyc/leo46zebra.interface -w /home/wyc/vtyzebra46.api')
    leo47.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo47zebra.conf -d -z /home/wyc/leo47zebra.api -i /home/wyc/leo47zebra.interface -w /home/wyc/vtyzebra47.api')
    leo48.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo48zebra.conf -d -z /home/wyc/leo48zebra.api -i /home/wyc/leo48zebra.interface -w /home/wyc/vtyzebra48.api')
    leo49.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo49zebra.conf -d -z /home/wyc/leo49zebra.api -i /home/wyc/leo49zebra.interface -w /home/wyc/vtyzebra49.api')
    leo50.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo50zebra.conf -d -z /home/wyc/leo50zebra.api -i /home/wyc/leo50zebra.interface -w /home/wyc/vtyzebra50.api')
    leo51.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo51zebra.conf -d -z /home/wyc/leo51zebra.api -i /home/wyc/leo51zebra.interface -w /home/wyc/vtyzebra51.api')
    leo52.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo52zebra.conf -d -z /home/wyc/leo52zebra.api -i /home/wyc/leo52zebra.interface -w /home/wyc/vtyzebra52.api')
    leo53.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo53zebra.conf -d -z /home/wyc/leo53zebra.api -i /home/wyc/leo53zebra.interface -w /home/wyc/vtyzebra53.api')
    leo54.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo54zebra.conf -d -z /home/wyc/leo54zebra.api -i /home/wyc/leo54zebra.interface -w /home/wyc/vtyzebra54.api')
    leo55.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo55zebra.conf -d -z /home/wyc/leo55zebra.api -i /home/wyc/leo55zebra.interface -w /home/wyc/vtyzebra55.api')
    leo56.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo56zebra.conf -d -z /home/wyc/leo56zebra.api -i /home/wyc/leo56zebra.interface -w /home/wyc/vtyzebra56.api')
    leo57.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo57zebra.conf -d -z /home/wyc/leo57zebra.api -i /home/wyc/leo57zebra.interface -w /home/wyc/vtyzebra57.api')
    leo58.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo58zebra.conf -d -z /home/wyc/leo58zebra.api -i /home/wyc/leo58zebra.interface -w /home/wyc/vtyzebra58.api')
    leo59.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo59zebra.conf -d -z /home/wyc/leo59zebra.api -i /home/wyc/leo59zebra.interface -w /home/wyc/vtyzebra59.api')
    leo60.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo60zebra.conf -d -z /home/wyc/leo60zebra.api -i /home/wyc/leo60zebra.interface -w /home/wyc/vtyzebra60.api')
    leo61.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo61zebra.conf -d -z /home/wyc/leo61zebra.api -i /home/wyc/leo61zebra.interface -w /home/wyc/vtyzebra61.api')
    leo62.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo62zebra.conf -d -z /home/wyc/leo62zebra.api -i /home/wyc/leo62zebra.interface -w /home/wyc/vtyzebra62.api')
    leo63.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo63zebra.conf -d -z /home/wyc/leo63zebra.api -i /home/wyc/leo63zebra.interface -w /home/wyc/vtyzebra63.api')
    leo64.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo64zebra.conf -d -z /home/wyc/leo64zebra.api -i /home/wyc/leo64zebra.interface -w /home/wyc/vtyzebra64.api')
    leo65.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo65zebra.conf -d -z /home/wyc/leo65zebra.api -i /home/wyc/leo65zebra.interface -w /home/wyc/vtyzebra65.api')
    leo66.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo66zebra.conf -d -z /home/wyc/leo66zebra.api -i /home/wyc/leo66zebra.interface -w /home/wyc/vtyzebra66.api')
    leo67.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo67zebra.conf -d -z /home/wyc/leo67zebra.api -i /home/wyc/leo67zebra.interface -w /home/wyc/vtyzebra67.api')
    leo68.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo68zebra.conf -d -z /home/wyc/leo68zebra.api -i /home/wyc/leo68zebra.interface -w /home/wyc/vtyzebra68.api')
    leo69.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo69zebra.conf -d -z /home/wyc/leo69zebra.api -i /home/wyc/leo69zebra.interface -w /home/wyc/vtyzebra69.api')
    leo70.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo70zebra.conf -d -z /home/wyc/leo70zebra.api -i /home/wyc/leo70zebra.interface -w /home/wyc/vtyzebra70.api')
    leo71.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo71zebra.conf -d -z /home/wyc/leo71zebra.api -i /home/wyc/leo71zebra.interface -w /home/wyc/vtyzebra71.api')
    leo72.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo72zebra.conf -d -z /home/wyc/leo72zebra.api -i /home/wyc/leo72zebra.interface -w /home/wyc/vtyzebra72.api')
    leo73.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo73zebra.conf -d -z /home/wyc/leo73zebra.api -i /home/wyc/leo73zebra.interface -w /home/wyc/vtyzebra73.api')
    leo74.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo74zebra.conf -d -z /home/wyc/leo74zebra.api -i /home/wyc/leo74zebra.interface -w /home/wyc/vtyzebra74.api')
    leo75.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo75zebra.conf -d -z /home/wyc/leo75zebra.api -i /home/wyc/leo75zebra.interface -w /home/wyc/vtyzebra75.api')
    leo76.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo76zebra.conf -d -z /home/wyc/leo76zebra.api -i /home/wyc/leo76zebra.interface -w /home/wyc/vtyzebra76.api')
    leo77.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo77zebra.conf -d -z /home/wyc/leo77zebra.api -i /home/wyc/leo77zebra.interface -w /home/wyc/vtyzebra77.api')
    leo78.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo78zebra.conf -d -z /home/wyc/leo78zebra.api -i /home/wyc/leo78zebra.interface -w /home/wyc/vtyzebra78.api')
    leo79.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo79zebra.conf -d -z /home/wyc/leo79zebra.api -i /home/wyc/leo79zebra.interface -w /home/wyc/vtyzebra79.api')
    leo80.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo80zebra.conf -d -z /home/wyc/leo80zebra.api -i /home/wyc/leo80zebra.interface -w /home/wyc/vtyzebra80.api')
    leo81.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo81zebra.conf -d -z /home/wyc/leo81zebra.api -i /home/wyc/leo81zebra.interface -w /home/wyc/vtyzebra81.api')
    leo82.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo82zebra.conf -d -z /home/wyc/leo82zebra.api -i /home/wyc/leo82zebra.interface -w /home/wyc/vtyzebra82.api')
    leo83.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo83zebra.conf -d -z /home/wyc/leo83zebra.api -i /home/wyc/leo83zebra.interface -w /home/wyc/vtyzebra83.api')
    leo84.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo84zebra.conf -d -z /home/wyc/leo84zebra.api -i /home/wyc/leo84zebra.interface -w /home/wyc/vtyzebra84.api')
    leo85.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo85zebra.conf -d -z /home/wyc/leo85zebra.api -i /home/wyc/leo85zebra.interface -w /home/wyc/vtyzebra85.api')
    leo86.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo86zebra.conf -d -z /home/wyc/leo86zebra.api -i /home/wyc/leo86zebra.interface -w /home/wyc/vtyzebra86.api')
    leo87.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo87zebra.conf -d -z /home/wyc/leo87zebra.api -i /home/wyc/leo87zebra.interface -w /home/wyc/vtyzebra87.api')
    leo88.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo88zebra.conf -d -z /home/wyc/leo88zebra.api -i /home/wyc/leo88zebra.interface -w /home/wyc/vtyzebra88.api')
    leo89.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo89zebra.conf -d -z /home/wyc/leo89zebra.api -i /home/wyc/leo89zebra.interface -w /home/wyc/vtyzebra89.api')
    leo90.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo90zebra.conf -d -z /home/wyc/leo90zebra.api -i /home/wyc/leo90zebra.interface -w /home/wyc/vtyzebra90.api')
    leo91.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo91zebra.conf -d -z /home/wyc/leo91zebra.api -i /home/wyc/leo91zebra.interface -w /home/wyc/vtyzebra91.api')
    leo92.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo92zebra.conf -d -z /home/wyc/leo92zebra.api -i /home/wyc/leo92zebra.interface -w /home/wyc/vtyzebra92.api')
    leo93.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo93zebra.conf -d -z /home/wyc/leo93zebra.api -i /home/wyc/leo93zebra.interface -w /home/wyc/vtyzebra93.api')
    leo94.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo94zebra.conf -d -z /home/wyc/leo94zebra.api -i /home/wyc/leo94zebra.interface -w /home/wyc/vtyzebra94.api')
    leo95.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo95zebra.conf -d -z /home/wyc/leo95zebra.api -i /home/wyc/leo95zebra.interface -w /home/wyc/vtyzebra95.api')
    leo96.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo96zebra.conf -d -z /home/wyc/leo96zebra.api -i /home/wyc/leo96zebra.interface -w /home/wyc/vtyzebra96.api')
    leo97.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo97zebra.conf -d -z /home/wyc/leo97zebra.api -i /home/wyc/leo97zebra.interface -w /home/wyc/vtyzebra97.api')
    leo98.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo98zebra.conf -d -z /home/wyc/leo98zebra.api -i /home/wyc/leo98zebra.interface -w /home/wyc/vtyzebra98.api')
    leo99.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo99zebra.conf -d -z /home/wyc/leo99zebra.api -i /home/wyc/leo99zebra.interface -w /home/wyc/vtyzebra99.api')
    leo100.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo100zebra.conf -d -z /home/wyc/leo100zebra.api -i /home/wyc/leo100zebra.interface -w /home/wyc/vtyzebra100.api')
    leo101.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo101zebra.conf -d -z /home/wyc/leo101zebra.api -i /home/wyc/leo101zebra.interface -w /home/wyc/vtyzebra101.api')
    leo102.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo102zebra.conf -d -z /home/wyc/leo102zebra.api -i /home/wyc/leo102zebra.interface -w /home/wyc/vtyzebra102.api')
    leo103.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo103zebra.conf -d -z /home/wyc/leo103zebra.api -i /home/wyc/leo103zebra.interface -w /home/wyc/vtyzebra103.api')
    leo104.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo104zebra.conf -d -z /home/wyc/leo104zebra.api -i /home/wyc/leo104zebra.interface -w /home/wyc/vtyzebra104.api')
    leo105.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo105zebra.conf -d -z /home/wyc/leo105zebra.api -i /home/wyc/leo105zebra.interface -w /home/wyc/vtyzebra105.api')
    leo106.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo106zebra.conf -d -z /home/wyc/leo106zebra.api -i /home/wyc/leo106zebra.interface -w /home/wyc/vtyzebra106.api')
    leo107.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo107zebra.conf -d -z /home/wyc/leo107zebra.api -i /home/wyc/leo107zebra.interface -w /home/wyc/vtyzebra107.api')
    leo108.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo108zebra.conf -d -z /home/wyc/leo108zebra.api -i /home/wyc/leo108zebra.interface -w /home/wyc/vtyzebra108.api')
    leo109.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo109zebra.conf -d -z /home/wyc/leo109zebra.api -i /home/wyc/leo109zebra.interface -w /home/wyc/vtyzebra109.api')
    leo110.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo110zebra.conf -d -z /home/wyc/leo110zebra.api -i /home/wyc/leo110zebra.interface -w /home/wyc/vtyzebra110.api')
    leo111.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo111zebra.conf -d -z /home/wyc/leo111zebra.api -i /home/wyc/leo111zebra.interface -w /home/wyc/vtyzebra111.api')
    leo112.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo112zebra.conf -d -z /home/wyc/leo112zebra.api -i /home/wyc/leo112zebra.interface -w /home/wyc/vtyzebra112.api')
    leo113.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo113zebra.conf -d -z /home/wyc/leo113zebra.api -i /home/wyc/leo113zebra.interface -w /home/wyc/vtyzebra113.api')
    leo114.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo114zebra.conf -d -z /home/wyc/leo114zebra.api -i /home/wyc/leo114zebra.interface -w /home/wyc/vtyzebra114.api')
    leo115.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo115zebra.conf -d -z /home/wyc/leo115zebra.api -i /home/wyc/leo115zebra.interface -w /home/wyc/vtyzebra115.api')
    leo116.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo116zebra.conf -d -z /home/wyc/leo116zebra.api -i /home/wyc/leo116zebra.interface -w /home/wyc/vtyzebra116.api')
    leo117.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo117zebra.conf -d -z /home/wyc/leo117zebra.api -i /home/wyc/leo117zebra.interface -w /home/wyc/vtyzebra117.api')
    leo118.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo118zebra.conf -d -z /home/wyc/leo118zebra.api -i /home/wyc/leo118zebra.interface -w /home/wyc/vtyzebra118.api')
    leo119.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo119zebra.conf -d -z /home/wyc/leo119zebra.api -i /home/wyc/leo119zebra.interface -w /home/wyc/vtyzebra119.api')
    leo120.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo120zebra.conf -d -z /home/wyc/leo120zebra.api -i /home/wyc/leo120zebra.interface -w /home/wyc/vtyzebra120.api')
    leo121.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo121zebra.conf -d -z /home/wyc/leo121zebra.api -i /home/wyc/leo121zebra.interface -w /home/wyc/vtyzebra121.api')
    leo122.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo122zebra.conf -d -z /home/wyc/leo122zebra.api -i /home/wyc/leo122zebra.interface -w /home/wyc/vtyzebra122.api')
    leo123.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo123zebra.conf -d -z /home/wyc/leo123zebra.api -i /home/wyc/leo123zebra.interface -w /home/wyc/vtyzebra123.api')
    leo124.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo124zebra.conf -d -z /home/wyc/leo124zebra.api -i /home/wyc/leo124zebra.interface -w /home/wyc/vtyzebra124.api')
    leo125.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo125zebra.conf -d -z /home/wyc/leo125zebra.api -i /home/wyc/leo125zebra.interface -w /home/wyc/vtyzebra125.api')
    leo126.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo126zebra.conf -d -z /home/wyc/leo126zebra.api -i /home/wyc/leo126zebra.interface -w /home/wyc/vtyzebra126.api')
    leo127.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo127zebra.conf -d -z /home/wyc/leo127zebra.api -i /home/wyc/leo127zebra.interface -w /home/wyc/vtyzebra127.api')
    leo128.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo128zebra.conf -d -z /home/wyc/leo128zebra.api -i /home/wyc/leo128zebra.interface -w /home/wyc/vtyzebra128.api')
    leo129.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo129zebra.conf -d -z /home/wyc/leo129zebra.api -i /home/wyc/leo129zebra.interface -w /home/wyc/vtyzebra129.api')
    leo130.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo130zebra.conf -d -z /home/wyc/leo130zebra.api -i /home/wyc/leo130zebra.interface -w /home/wyc/vtyzebra130.api')
    leo131.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo131zebra.conf -d -z /home/wyc/leo131zebra.api -i /home/wyc/leo131zebra.interface -w /home/wyc/vtyzebra131.api')
    leo132.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo132zebra.conf -d -z /home/wyc/leo132zebra.api -i /home/wyc/leo132zebra.interface -w /home/wyc/vtyzebra132.api')
    leo133.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo133zebra.conf -d -z /home/wyc/leo133zebra.api -i /home/wyc/leo133zebra.interface -w /home/wyc/vtyzebra133.api')
    leo134.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo134zebra.conf -d -z /home/wyc/leo134zebra.api -i /home/wyc/leo134zebra.interface -w /home/wyc/vtyzebra134.api')
    leo135.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo135zebra.conf -d -z /home/wyc/leo135zebra.api -i /home/wyc/leo135zebra.interface -w /home/wyc/vtyzebra135.api')
    leo136.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo136zebra.conf -d -z /home/wyc/leo136zebra.api -i /home/wyc/leo136zebra.interface -w /home/wyc/vtyzebra136.api')
    leo137.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo137zebra.conf -d -z /home/wyc/leo137zebra.api -i /home/wyc/leo137zebra.interface -w /home/wyc/vtyzebra137.api')
    leo138.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo138zebra.conf -d -z /home/wyc/leo138zebra.api -i /home/wyc/leo138zebra.interface -w /home/wyc/vtyzebra138.api')
    leo139.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo139zebra.conf -d -z /home/wyc/leo139zebra.api -i /home/wyc/leo139zebra.interface -w /home/wyc/vtyzebra139.api')
    leo140.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo140zebra.conf -d -z /home/wyc/leo140zebra.api -i /home/wyc/leo140zebra.interface -w /home/wyc/vtyzebra140.api')
    leo141.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo141zebra.conf -d -z /home/wyc/leo141zebra.api -i /home/wyc/leo141zebra.interface -w /home/wyc/vtyzebra141.api')
    leo142.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo142zebra.conf -d -z /home/wyc/leo142zebra.api -i /home/wyc/leo142zebra.interface -w /home/wyc/vtyzebra142.api')
    leo143.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo143zebra.conf -d -z /home/wyc/leo143zebra.api -i /home/wyc/leo143zebra.interface -w /home/wyc/vtyzebra143.api')
    leo144.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo144zebra.conf -d -z /home/wyc/leo144zebra.api -i /home/wyc/leo144zebra.interface -w /home/wyc/vtyzebra144.api')
    leo145.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo145zebra.conf -d -z /home/wyc/leo145zebra.api -i /home/wyc/leo145zebra.interface -w /home/wyc/vtyzebra145.api')
    leo146.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo146zebra.conf -d -z /home/wyc/leo146zebra.api -i /home/wyc/leo146zebra.interface -w /home/wyc/vtyzebra146.api')
    leo147.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo147zebra.conf -d -z /home/wyc/leo147zebra.api -i /home/wyc/leo147zebra.interface -w /home/wyc/vtyzebra147.api')
    leo148.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo148zebra.conf -d -z /home/wyc/leo148zebra.api -i /home/wyc/leo148zebra.interface -w /home/wyc/vtyzebra148.api')
    leo149.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo149zebra.conf -d -z /home/wyc/leo149zebra.api -i /home/wyc/leo149zebra.interface -w /home/wyc/vtyzebra149.api')
    leo150.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo150zebra.conf -d -z /home/wyc/leo150zebra.api -i /home/wyc/leo150zebra.interface -w /home/wyc/vtyzebra150.api')
    leo151.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo151zebra.conf -d -z /home/wyc/leo151zebra.api -i /home/wyc/leo151zebra.interface -w /home/wyc/vtyzebra151.api')
    leo152.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo152zebra.conf -d -z /home/wyc/leo152zebra.api -i /home/wyc/leo152zebra.interface -w /home/wyc/vtyzebra152.api')
    leo153.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo153zebra.conf -d -z /home/wyc/leo153zebra.api -i /home/wyc/leo153zebra.interface -w /home/wyc/vtyzebra153.api')
    leo154.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo154zebra.conf -d -z /home/wyc/leo154zebra.api -i /home/wyc/leo154zebra.interface -w /home/wyc/vtyzebra154.api')
    leo155.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo155zebra.conf -d -z /home/wyc/leo155zebra.api -i /home/wyc/leo155zebra.interface -w /home/wyc/vtyzebra155.api')
    leo156.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo156zebra.conf -d -z /home/wyc/leo156zebra.api -i /home/wyc/leo156zebra.interface -w /home/wyc/vtyzebra156.api')
    leo157.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo157zebra.conf -d -z /home/wyc/leo157zebra.api -i /home/wyc/leo157zebra.interface -w /home/wyc/vtyzebra157.api')
    leo158.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo158zebra.conf -d -z /home/wyc/leo158zebra.api -i /home/wyc/leo158zebra.interface -w /home/wyc/vtyzebra158.api')
    leo159.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo159zebra.conf -d -z /home/wyc/leo159zebra.api -i /home/wyc/leo159zebra.interface -w /home/wyc/vtyzebra159.api')
    leo160.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo160zebra.conf -d -z /home/wyc/leo160zebra.api -i /home/wyc/leo160zebra.interface -w /home/wyc/vtyzebra160.api')
    leo161.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo161zebra.conf -d -z /home/wyc/leo161zebra.api -i /home/wyc/leo161zebra.interface -w /home/wyc/vtyzebra161.api')
    leo162.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo162zebra.conf -d -z /home/wyc/leo162zebra.api -i /home/wyc/leo162zebra.interface -w /home/wyc/vtyzebra162.api')
    leo163.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo163zebra.conf -d -z /home/wyc/leo163zebra.api -i /home/wyc/leo163zebra.interface -w /home/wyc/vtyzebra163.api')
    leo164.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo164zebra.conf -d -z /home/wyc/leo164zebra.api -i /home/wyc/leo164zebra.interface -w /home/wyc/vtyzebra164.api')
    leo165.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo165zebra.conf -d -z /home/wyc/leo165zebra.api -i /home/wyc/leo165zebra.interface -w /home/wyc/vtyzebra165.api')
    leo166.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo166zebra.conf -d -z /home/wyc/leo166zebra.api -i /home/wyc/leo166zebra.interface -w /home/wyc/vtyzebra166.api')
    leo167.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo167zebra.conf -d -z /home/wyc/leo167zebra.api -i /home/wyc/leo167zebra.interface -w /home/wyc/vtyzebra167.api')
    leo168.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo168zebra.conf -d -z /home/wyc/leo168zebra.api -i /home/wyc/leo168zebra.interface -w /home/wyc/vtyzebra168.api')
    leo169.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo169zebra.conf -d -z /home/wyc/leo169zebra.api -i /home/wyc/leo169zebra.interface -w /home/wyc/vtyzebra169.api')
    leo170.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo170zebra.conf -d -z /home/wyc/leo170zebra.api -i /home/wyc/leo170zebra.interface -w /home/wyc/vtyzebra170.api')
    leo171.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo171zebra.conf -d -z /home/wyc/leo171zebra.api -i /home/wyc/leo171zebra.interface -w /home/wyc/vtyzebra171.api')
    leo172.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo172zebra.conf -d -z /home/wyc/leo172zebra.api -i /home/wyc/leo172zebra.interface -w /home/wyc/vtyzebra172.api')
    leo173.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo173zebra.conf -d -z /home/wyc/leo173zebra.api -i /home/wyc/leo173zebra.interface -w /home/wyc/vtyzebra173.api')
    leo174.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo174zebra.conf -d -z /home/wyc/leo174zebra.api -i /home/wyc/leo174zebra.interface -w /home/wyc/vtyzebra174.api')
    leo175.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo175zebra.conf -d -z /home/wyc/leo175zebra.api -i /home/wyc/leo175zebra.interface -w /home/wyc/vtyzebra175.api')
    leo176.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo176zebra.conf -d -z /home/wyc/leo176zebra.api -i /home/wyc/leo176zebra.interface -w /home/wyc/vtyzebra176.api')
    leo177.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo177zebra.conf -d -z /home/wyc/leo177zebra.api -i /home/wyc/leo177zebra.interface -w /home/wyc/vtyzebra177.api')
    leo178.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo178zebra.conf -d -z /home/wyc/leo178zebra.api -i /home/wyc/leo178zebra.interface -w /home/wyc/vtyzebra178.api')
    leo179.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo179zebra.conf -d -z /home/wyc/leo179zebra.api -i /home/wyc/leo179zebra.interface -w /home/wyc/vtyzebra179.api')
    leo180.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo180zebra.conf -d -z /home/wyc/leo180zebra.api -i /home/wyc/leo180zebra.interface -w /home/wyc/vtyzebra180.api')
    leo181.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo181zebra.conf -d -z /home/wyc/leo181zebra.api -i /home/wyc/leo181zebra.interface -w /home/wyc/vtyzebra181.api')
    leo182.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo182zebra.conf -d -z /home/wyc/leo182zebra.api -i /home/wyc/leo182zebra.interface -w /home/wyc/vtyzebra182.api')
    leo183.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo183zebra.conf -d -z /home/wyc/leo183zebra.api -i /home/wyc/leo183zebra.interface -w /home/wyc/vtyzebra183.api')
    leo184.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo184zebra.conf -d -z /home/wyc/leo184zebra.api -i /home/wyc/leo184zebra.interface -w /home/wyc/vtyzebra184.api')
    leo185.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo185zebra.conf -d -z /home/wyc/leo185zebra.api -i /home/wyc/leo185zebra.interface -w /home/wyc/vtyzebra185.api')
    leo186.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo186zebra.conf -d -z /home/wyc/leo186zebra.api -i /home/wyc/leo186zebra.interface -w /home/wyc/vtyzebra186.api')
    leo187.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo187zebra.conf -d -z /home/wyc/leo187zebra.api -i /home/wyc/leo187zebra.interface -w /home/wyc/vtyzebra187.api')
    leo188.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo188zebra.conf -d -z /home/wyc/leo188zebra.api -i /home/wyc/leo188zebra.interface -w /home/wyc/vtyzebra188.api')
    leo189.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo189zebra.conf -d -z /home/wyc/leo189zebra.api -i /home/wyc/leo189zebra.interface -w /home/wyc/vtyzebra189.api')
    leo190.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo190zebra.conf -d -z /home/wyc/leo190zebra.api -i /home/wyc/leo190zebra.interface -w /home/wyc/vtyzebra190.api')
    leo191.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo191zebra.conf -d -z /home/wyc/leo191zebra.api -i /home/wyc/leo191zebra.interface -w /home/wyc/vtyzebra191.api')
    leo192.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo192zebra.conf -d -z /home/wyc/leo192zebra.api -i /home/wyc/leo192zebra.interface -w /home/wyc/vtyzebra192.api')
    leo193.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo193zebra.conf -d -z /home/wyc/leo193zebra.api -i /home/wyc/leo193zebra.interface -w /home/wyc/vtyzebra193.api')
    leo194.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo194zebra.conf -d -z /home/wyc/leo194zebra.api -i /home/wyc/leo194zebra.interface -w /home/wyc/vtyzebra194.api')
    leo195.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo195zebra.conf -d -z /home/wyc/leo195zebra.api -i /home/wyc/leo195zebra.interface -w /home/wyc/vtyzebra195.api')
    leo196.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo196zebra.conf -d -z /home/wyc/leo196zebra.api -i /home/wyc/leo196zebra.interface -w /home/wyc/vtyzebra196.api')
    leo197.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo197zebra.conf -d -z /home/wyc/leo197zebra.api -i /home/wyc/leo197zebra.interface -w /home/wyc/vtyzebra197.api')
    leo198.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo198zebra.conf -d -z /home/wyc/leo198zebra.api -i /home/wyc/leo198zebra.interface -w /home/wyc/vtyzebra198.api')
    leo199.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo199zebra.conf -d -z /home/wyc/leo199zebra.api -i /home/wyc/leo199zebra.interface -w /home/wyc/vtyzebra199.api')
    leo200.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo200zebra.conf -d -z /home/wyc/leo200zebra.api -i /home/wyc/leo200zebra.interface -w /home/wyc/vtyzebra200.api')
    leo201.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo201zebra.conf -d -z /home/wyc/leo201zebra.api -i /home/wyc/leo201zebra.interface -w /home/wyc/vtyzebra201.api')
    leo202.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo202zebra.conf -d -z /home/wyc/leo202zebra.api -i /home/wyc/leo202zebra.interface -w /home/wyc/vtyzebra202.api')
    leo203.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo203zebra.conf -d -z /home/wyc/leo203zebra.api -i /home/wyc/leo203zebra.interface -w /home/wyc/vtyzebra203.api')
    leo204.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo204zebra.conf -d -z /home/wyc/leo204zebra.api -i /home/wyc/leo204zebra.interface -w /home/wyc/vtyzebra204.api')
    leo205.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo205zebra.conf -d -z /home/wyc/leo205zebra.api -i /home/wyc/leo205zebra.interface -w /home/wyc/vtyzebra205.api')
    leo206.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo206zebra.conf -d -z /home/wyc/leo206zebra.api -i /home/wyc/leo206zebra.interface -w /home/wyc/vtyzebra206.api')
    leo207.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo207zebra.conf -d -z /home/wyc/leo207zebra.api -i /home/wyc/leo207zebra.interface -w /home/wyc/vtyzebra207.api')
    leo208.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo208zebra.conf -d -z /home/wyc/leo208zebra.api -i /home/wyc/leo208zebra.interface -w /home/wyc/vtyzebra208.api')
    leo209.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo209zebra.conf -d -z /home/wyc/leo209zebra.api -i /home/wyc/leo209zebra.interface -w /home/wyc/vtyzebra209.api')
    leo210.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo210zebra.conf -d -z /home/wyc/leo210zebra.api -i /home/wyc/leo210zebra.interface -w /home/wyc/vtyzebra210.api')
    leo211.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo211zebra.conf -d -z /home/wyc/leo211zebra.api -i /home/wyc/leo211zebra.interface -w /home/wyc/vtyzebra211.api')
    leo212.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo212zebra.conf -d -z /home/wyc/leo212zebra.api -i /home/wyc/leo212zebra.interface -w /home/wyc/vtyzebra212.api')
    leo213.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo213zebra.conf -d -z /home/wyc/leo213zebra.api -i /home/wyc/leo213zebra.interface -w /home/wyc/vtyzebra213.api')
    leo214.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo214zebra.conf -d -z /home/wyc/leo214zebra.api -i /home/wyc/leo214zebra.interface -w /home/wyc/vtyzebra214.api')
    leo215.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo215zebra.conf -d -z /home/wyc/leo215zebra.api -i /home/wyc/leo215zebra.interface -w /home/wyc/vtyzebra215.api')
    leo216.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo216zebra.conf -d -z /home/wyc/leo216zebra.api -i /home/wyc/leo216zebra.interface -w /home/wyc/vtyzebra216.api')
    leo217.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo217zebra.conf -d -z /home/wyc/leo217zebra.api -i /home/wyc/leo217zebra.interface -w /home/wyc/vtyzebra217.api')
    leo218.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo218zebra.conf -d -z /home/wyc/leo218zebra.api -i /home/wyc/leo218zebra.interface -w /home/wyc/vtyzebra218.api')
    leo219.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo219zebra.conf -d -z /home/wyc/leo219zebra.api -i /home/wyc/leo219zebra.interface -w /home/wyc/vtyzebra219.api')
    leo220.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo220zebra.conf -d -z /home/wyc/leo220zebra.api -i /home/wyc/leo220zebra.interface -w /home/wyc/vtyzebra220.api')
    leo221.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo221zebra.conf -d -z /home/wyc/leo221zebra.api -i /home/wyc/leo221zebra.interface -w /home/wyc/vtyzebra221.api')
    leo222.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo222zebra.conf -d -z /home/wyc/leo222zebra.api -i /home/wyc/leo222zebra.interface -w /home/wyc/vtyzebra222.api')
    leo223.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo223zebra.conf -d -z /home/wyc/leo223zebra.api -i /home/wyc/leo223zebra.interface -w /home/wyc/vtyzebra223.api')
    leo224.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo224zebra.conf -d -z /home/wyc/leo224zebra.api -i /home/wyc/leo224zebra.interface -w /home/wyc/vtyzebra224.api')
    leo225.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo225zebra.conf -d -z /home/wyc/leo225zebra.api -i /home/wyc/leo225zebra.interface -w /home/wyc/vtyzebra225.api')
    leo226.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo226zebra.conf -d -z /home/wyc/leo226zebra.api -i /home/wyc/leo226zebra.interface -w /home/wyc/vtyzebra226.api')
    leo227.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo227zebra.conf -d -z /home/wyc/leo227zebra.api -i /home/wyc/leo227zebra.interface -w /home/wyc/vtyzebra227.api')
    leo228.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo228zebra.conf -d -z /home/wyc/leo228zebra.api -i /home/wyc/leo228zebra.interface -w /home/wyc/vtyzebra228.api')
    leo229.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo229zebra.conf -d -z /home/wyc/leo229zebra.api -i /home/wyc/leo229zebra.interface -w /home/wyc/vtyzebra229.api')
    leo230.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo230zebra.conf -d -z /home/wyc/leo230zebra.api -i /home/wyc/leo230zebra.interface -w /home/wyc/vtyzebra230.api')
    leo231.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo231zebra.conf -d -z /home/wyc/leo231zebra.api -i /home/wyc/leo231zebra.interface -w /home/wyc/vtyzebra231.api')
    leo232.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo232zebra.conf -d -z /home/wyc/leo232zebra.api -i /home/wyc/leo232zebra.interface -w /home/wyc/vtyzebra232.api')
    leo233.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo233zebra.conf -d -z /home/wyc/leo233zebra.api -i /home/wyc/leo233zebra.interface -w /home/wyc/vtyzebra233.api')
    leo234.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo234zebra.conf -d -z /home/wyc/leo234zebra.api -i /home/wyc/leo234zebra.interface -w /home/wyc/vtyzebra234.api')
    leo235.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo235zebra.conf -d -z /home/wyc/leo235zebra.api -i /home/wyc/leo235zebra.interface -w /home/wyc/vtyzebra235.api')
    leo236.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo236zebra.conf -d -z /home/wyc/leo236zebra.api -i /home/wyc/leo236zebra.interface -w /home/wyc/vtyzebra236.api')
    leo237.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo237zebra.conf -d -z /home/wyc/leo237zebra.api -i /home/wyc/leo237zebra.interface -w /home/wyc/vtyzebra237.api')
    leo238.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo238zebra.conf -d -z /home/wyc/leo238zebra.api -i /home/wyc/leo238zebra.interface -w /home/wyc/vtyzebra238.api')
    leo239.cmd('zebra -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo239zebra.conf -d -z /home/wyc/leo239zebra.api -i /home/wyc/leo239zebra.interface -w /home/wyc/vtyzebra239.api')
    time.sleep(2)
    leo0.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo0ospfd.conf -d -z /home/wyc/leo0zebra.api -i /home/wyc/leo0ospfd.interface -q /home/wyc/vtyospfd0.api')
    leo1.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo1ospfd.conf -d -z /home/wyc/leo1zebra.api -i /home/wyc/leo1ospfd.interface -q /home/wyc/vtyospfd1.api')
    leo2.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo2ospfd.conf -d -z /home/wyc/leo2zebra.api -i /home/wyc/leo2ospfd.interface -q /home/wyc/vtyospfd2.api')
    leo3.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo3ospfd.conf -d -z /home/wyc/leo3zebra.api -i /home/wyc/leo3ospfd.interface -q /home/wyc/vtyospfd3.api')
    leo4.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo4ospfd.conf -d -z /home/wyc/leo4zebra.api -i /home/wyc/leo4ospfd.interface -q /home/wyc/vtyospfd4.api')
    leo5.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo5ospfd.conf -d -z /home/wyc/leo5zebra.api -i /home/wyc/leo5ospfd.interface -q /home/wyc/vtyospfd5.api')
    leo6.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo6ospfd.conf -d -z /home/wyc/leo6zebra.api -i /home/wyc/leo6ospfd.interface -q /home/wyc/vtyospfd6.api')
    leo7.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo7ospfd.conf -d -z /home/wyc/leo7zebra.api -i /home/wyc/leo7ospfd.interface -q /home/wyc/vtyospfd7.api')
    leo8.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo8ospfd.conf -d -z /home/wyc/leo8zebra.api -i /home/wyc/leo8ospfd.interface -q /home/wyc/vtyospfd8.api')
    leo9.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo9ospfd.conf -d -z /home/wyc/leo9zebra.api -i /home/wyc/leo9ospfd.interface -q /home/wyc/vtyospfd9.api')
    leo10.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo10ospfd.conf -d -z /home/wyc/leo10zebra.api -i /home/wyc/leo10ospfd.interface -q /home/wyc/vtyospfd10.api')
    leo11.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo11ospfd.conf -d -z /home/wyc/leo11zebra.api -i /home/wyc/leo11ospfd.interface -q /home/wyc/vtyospfd11.api')
    leo12.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo12ospfd.conf -d -z /home/wyc/leo12zebra.api -i /home/wyc/leo12ospfd.interface -q /home/wyc/vtyospfd12.api')
    leo13.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo13ospfd.conf -d -z /home/wyc/leo13zebra.api -i /home/wyc/leo13ospfd.interface -q /home/wyc/vtyospfd13.api')
    leo14.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo14ospfd.conf -d -z /home/wyc/leo14zebra.api -i /home/wyc/leo14ospfd.interface -q /home/wyc/vtyospfd14.api')
    leo15.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo15ospfd.conf -d -z /home/wyc/leo15zebra.api -i /home/wyc/leo15ospfd.interface -q /home/wyc/vtyospfd15.api')
    leo16.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo16ospfd.conf -d -z /home/wyc/leo16zebra.api -i /home/wyc/leo16ospfd.interface -q /home/wyc/vtyospfd16.api')
    leo17.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo17ospfd.conf -d -z /home/wyc/leo17zebra.api -i /home/wyc/leo17ospfd.interface -q /home/wyc/vtyospfd17.api')
    leo18.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo18ospfd.conf -d -z /home/wyc/leo18zebra.api -i /home/wyc/leo18ospfd.interface -q /home/wyc/vtyospfd18.api')
    leo19.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo19ospfd.conf -d -z /home/wyc/leo19zebra.api -i /home/wyc/leo19ospfd.interface -q /home/wyc/vtyospfd19.api')
    leo20.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo20ospfd.conf -d -z /home/wyc/leo20zebra.api -i /home/wyc/leo20ospfd.interface -q /home/wyc/vtyospfd20.api')
    leo21.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo21ospfd.conf -d -z /home/wyc/leo21zebra.api -i /home/wyc/leo21ospfd.interface -q /home/wyc/vtyospfd21.api')
    leo22.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo22ospfd.conf -d -z /home/wyc/leo22zebra.api -i /home/wyc/leo22ospfd.interface -q /home/wyc/vtyospfd22.api')
    leo23.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo23ospfd.conf -d -z /home/wyc/leo23zebra.api -i /home/wyc/leo23ospfd.interface -q /home/wyc/vtyospfd23.api')
    leo24.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo24ospfd.conf -d -z /home/wyc/leo24zebra.api -i /home/wyc/leo24ospfd.interface -q /home/wyc/vtyospfd24.api')
    leo25.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo25ospfd.conf -d -z /home/wyc/leo25zebra.api -i /home/wyc/leo25ospfd.interface -q /home/wyc/vtyospfd25.api')
    leo26.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo26ospfd.conf -d -z /home/wyc/leo26zebra.api -i /home/wyc/leo26ospfd.interface -q /home/wyc/vtyospfd26.api')
    leo27.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo27ospfd.conf -d -z /home/wyc/leo27zebra.api -i /home/wyc/leo27ospfd.interface -q /home/wyc/vtyospfd27.api')
    leo28.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo28ospfd.conf -d -z /home/wyc/leo28zebra.api -i /home/wyc/leo28ospfd.interface -q /home/wyc/vtyospfd28.api')
    leo29.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo29ospfd.conf -d -z /home/wyc/leo29zebra.api -i /home/wyc/leo29ospfd.interface -q /home/wyc/vtyospfd29.api')
    leo30.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo30ospfd.conf -d -z /home/wyc/leo30zebra.api -i /home/wyc/leo30ospfd.interface -q /home/wyc/vtyospfd30.api')
    leo31.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo31ospfd.conf -d -z /home/wyc/leo31zebra.api -i /home/wyc/leo31ospfd.interface -q /home/wyc/vtyospfd31.api')
    leo32.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo32ospfd.conf -d -z /home/wyc/leo32zebra.api -i /home/wyc/leo32ospfd.interface -q /home/wyc/vtyospfd32.api')
    leo33.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo33ospfd.conf -d -z /home/wyc/leo33zebra.api -i /home/wyc/leo33ospfd.interface -q /home/wyc/vtyospfd33.api')
    leo34.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo34ospfd.conf -d -z /home/wyc/leo34zebra.api -i /home/wyc/leo34ospfd.interface -q /home/wyc/vtyospfd34.api')
    leo35.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo35ospfd.conf -d -z /home/wyc/leo35zebra.api -i /home/wyc/leo35ospfd.interface -q /home/wyc/vtyospfd35.api')
    leo36.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo36ospfd.conf -d -z /home/wyc/leo36zebra.api -i /home/wyc/leo36ospfd.interface -q /home/wyc/vtyospfd36.api')
    leo37.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo37ospfd.conf -d -z /home/wyc/leo37zebra.api -i /home/wyc/leo37ospfd.interface -q /home/wyc/vtyospfd37.api')
    leo38.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo38ospfd.conf -d -z /home/wyc/leo38zebra.api -i /home/wyc/leo38ospfd.interface -q /home/wyc/vtyospfd38.api')
    leo39.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo39ospfd.conf -d -z /home/wyc/leo39zebra.api -i /home/wyc/leo39ospfd.interface -q /home/wyc/vtyospfd39.api')
    leo40.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo40ospfd.conf -d -z /home/wyc/leo40zebra.api -i /home/wyc/leo40ospfd.interface -q /home/wyc/vtyospfd40.api')
    leo41.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo41ospfd.conf -d -z /home/wyc/leo41zebra.api -i /home/wyc/leo41ospfd.interface -q /home/wyc/vtyospfd41.api')
    leo42.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo42ospfd.conf -d -z /home/wyc/leo42zebra.api -i /home/wyc/leo42ospfd.interface -q /home/wyc/vtyospfd42.api')
    leo43.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo43ospfd.conf -d -z /home/wyc/leo43zebra.api -i /home/wyc/leo43ospfd.interface -q /home/wyc/vtyospfd43.api')
    leo44.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo44ospfd.conf -d -z /home/wyc/leo44zebra.api -i /home/wyc/leo44ospfd.interface -q /home/wyc/vtyospfd44.api')
    leo45.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo45ospfd.conf -d -z /home/wyc/leo45zebra.api -i /home/wyc/leo45ospfd.interface -q /home/wyc/vtyospfd45.api')
    leo46.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo46ospfd.conf -d -z /home/wyc/leo46zebra.api -i /home/wyc/leo46ospfd.interface -q /home/wyc/vtyospfd46.api')
    leo47.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo47ospfd.conf -d -z /home/wyc/leo47zebra.api -i /home/wyc/leo47ospfd.interface -q /home/wyc/vtyospfd47.api')
    leo48.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo48ospfd.conf -d -z /home/wyc/leo48zebra.api -i /home/wyc/leo48ospfd.interface -q /home/wyc/vtyospfd48.api')
    leo49.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo49ospfd.conf -d -z /home/wyc/leo49zebra.api -i /home/wyc/leo49ospfd.interface -q /home/wyc/vtyospfd49.api')
    leo50.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo50ospfd.conf -d -z /home/wyc/leo50zebra.api -i /home/wyc/leo50ospfd.interface -q /home/wyc/vtyospfd50.api')
    leo51.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo51ospfd.conf -d -z /home/wyc/leo51zebra.api -i /home/wyc/leo51ospfd.interface -q /home/wyc/vtyospfd51.api')
    leo52.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo52ospfd.conf -d -z /home/wyc/leo52zebra.api -i /home/wyc/leo52ospfd.interface -q /home/wyc/vtyospfd52.api')
    leo53.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo53ospfd.conf -d -z /home/wyc/leo53zebra.api -i /home/wyc/leo53ospfd.interface -q /home/wyc/vtyospfd53.api')
    leo54.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo54ospfd.conf -d -z /home/wyc/leo54zebra.api -i /home/wyc/leo54ospfd.interface -q /home/wyc/vtyospfd54.api')
    leo55.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo55ospfd.conf -d -z /home/wyc/leo55zebra.api -i /home/wyc/leo55ospfd.interface -q /home/wyc/vtyospfd55.api')
    leo56.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo56ospfd.conf -d -z /home/wyc/leo56zebra.api -i /home/wyc/leo56ospfd.interface -q /home/wyc/vtyospfd56.api')
    leo57.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo57ospfd.conf -d -z /home/wyc/leo57zebra.api -i /home/wyc/leo57ospfd.interface -q /home/wyc/vtyospfd57.api')
    leo58.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo58ospfd.conf -d -z /home/wyc/leo58zebra.api -i /home/wyc/leo58ospfd.interface -q /home/wyc/vtyospfd58.api')
    leo59.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo59ospfd.conf -d -z /home/wyc/leo59zebra.api -i /home/wyc/leo59ospfd.interface -q /home/wyc/vtyospfd59.api')
    leo60.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo60ospfd.conf -d -z /home/wyc/leo60zebra.api -i /home/wyc/leo60ospfd.interface -q /home/wyc/vtyospfd60.api')
    leo61.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo61ospfd.conf -d -z /home/wyc/leo61zebra.api -i /home/wyc/leo61ospfd.interface -q /home/wyc/vtyospfd61.api')
    leo62.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo62ospfd.conf -d -z /home/wyc/leo62zebra.api -i /home/wyc/leo62ospfd.interface -q /home/wyc/vtyospfd62.api')
    leo63.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo63ospfd.conf -d -z /home/wyc/leo63zebra.api -i /home/wyc/leo63ospfd.interface -q /home/wyc/vtyospfd63.api')
    leo64.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo64ospfd.conf -d -z /home/wyc/leo64zebra.api -i /home/wyc/leo64ospfd.interface -q /home/wyc/vtyospfd64.api')
    leo65.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo65ospfd.conf -d -z /home/wyc/leo65zebra.api -i /home/wyc/leo65ospfd.interface -q /home/wyc/vtyospfd65.api')
    leo66.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo66ospfd.conf -d -z /home/wyc/leo66zebra.api -i /home/wyc/leo66ospfd.interface -q /home/wyc/vtyospfd66.api')
    leo67.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo67ospfd.conf -d -z /home/wyc/leo67zebra.api -i /home/wyc/leo67ospfd.interface -q /home/wyc/vtyospfd67.api')
    leo68.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo68ospfd.conf -d -z /home/wyc/leo68zebra.api -i /home/wyc/leo68ospfd.interface -q /home/wyc/vtyospfd68.api')
    leo69.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo69ospfd.conf -d -z /home/wyc/leo69zebra.api -i /home/wyc/leo69ospfd.interface -q /home/wyc/vtyospfd69.api')
    leo70.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo70ospfd.conf -d -z /home/wyc/leo70zebra.api -i /home/wyc/leo70ospfd.interface -q /home/wyc/vtyospfd70.api')
    leo71.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo71ospfd.conf -d -z /home/wyc/leo71zebra.api -i /home/wyc/leo71ospfd.interface -q /home/wyc/vtyospfd71.api')
    leo72.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo72ospfd.conf -d -z /home/wyc/leo72zebra.api -i /home/wyc/leo72ospfd.interface -q /home/wyc/vtyospfd72.api')
    leo73.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo73ospfd.conf -d -z /home/wyc/leo73zebra.api -i /home/wyc/leo73ospfd.interface -q /home/wyc/vtyospfd73.api')
    leo74.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo74ospfd.conf -d -z /home/wyc/leo74zebra.api -i /home/wyc/leo74ospfd.interface -q /home/wyc/vtyospfd74.api')
    leo75.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo75ospfd.conf -d -z /home/wyc/leo75zebra.api -i /home/wyc/leo75ospfd.interface -q /home/wyc/vtyospfd75.api')
    leo76.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo76ospfd.conf -d -z /home/wyc/leo76zebra.api -i /home/wyc/leo76ospfd.interface -q /home/wyc/vtyospfd76.api')
    leo77.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo77ospfd.conf -d -z /home/wyc/leo77zebra.api -i /home/wyc/leo77ospfd.interface -q /home/wyc/vtyospfd77.api')
    leo78.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo78ospfd.conf -d -z /home/wyc/leo78zebra.api -i /home/wyc/leo78ospfd.interface -q /home/wyc/vtyospfd78.api')
    leo79.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo79ospfd.conf -d -z /home/wyc/leo79zebra.api -i /home/wyc/leo79ospfd.interface -q /home/wyc/vtyospfd79.api')
    leo80.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo80ospfd.conf -d -z /home/wyc/leo80zebra.api -i /home/wyc/leo80ospfd.interface -q /home/wyc/vtyospfd80.api')
    leo81.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo81ospfd.conf -d -z /home/wyc/leo81zebra.api -i /home/wyc/leo81ospfd.interface -q /home/wyc/vtyospfd81.api')
    leo82.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo82ospfd.conf -d -z /home/wyc/leo82zebra.api -i /home/wyc/leo82ospfd.interface -q /home/wyc/vtyospfd82.api')
    leo83.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo83ospfd.conf -d -z /home/wyc/leo83zebra.api -i /home/wyc/leo83ospfd.interface -q /home/wyc/vtyospfd83.api')
    leo84.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo84ospfd.conf -d -z /home/wyc/leo84zebra.api -i /home/wyc/leo84ospfd.interface -q /home/wyc/vtyospfd84.api')
    leo85.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo85ospfd.conf -d -z /home/wyc/leo85zebra.api -i /home/wyc/leo85ospfd.interface -q /home/wyc/vtyospfd85.api')
    leo86.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo86ospfd.conf -d -z /home/wyc/leo86zebra.api -i /home/wyc/leo86ospfd.interface -q /home/wyc/vtyospfd86.api')
    leo87.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo87ospfd.conf -d -z /home/wyc/leo87zebra.api -i /home/wyc/leo87ospfd.interface -q /home/wyc/vtyospfd87.api')
    leo88.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo88ospfd.conf -d -z /home/wyc/leo88zebra.api -i /home/wyc/leo88ospfd.interface -q /home/wyc/vtyospfd88.api')
    leo89.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo89ospfd.conf -d -z /home/wyc/leo89zebra.api -i /home/wyc/leo89ospfd.interface -q /home/wyc/vtyospfd89.api')
    leo90.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo90ospfd.conf -d -z /home/wyc/leo90zebra.api -i /home/wyc/leo90ospfd.interface -q /home/wyc/vtyospfd90.api')
    leo91.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo91ospfd.conf -d -z /home/wyc/leo91zebra.api -i /home/wyc/leo91ospfd.interface -q /home/wyc/vtyospfd91.api')
    leo92.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo92ospfd.conf -d -z /home/wyc/leo92zebra.api -i /home/wyc/leo92ospfd.interface -q /home/wyc/vtyospfd92.api')
    leo93.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo93ospfd.conf -d -z /home/wyc/leo93zebra.api -i /home/wyc/leo93ospfd.interface -q /home/wyc/vtyospfd93.api')
    leo94.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo94ospfd.conf -d -z /home/wyc/leo94zebra.api -i /home/wyc/leo94ospfd.interface -q /home/wyc/vtyospfd94.api')
    leo95.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo95ospfd.conf -d -z /home/wyc/leo95zebra.api -i /home/wyc/leo95ospfd.interface -q /home/wyc/vtyospfd95.api')
    leo96.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo96ospfd.conf -d -z /home/wyc/leo96zebra.api -i /home/wyc/leo96ospfd.interface -q /home/wyc/vtyospfd96.api')
    leo97.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo97ospfd.conf -d -z /home/wyc/leo97zebra.api -i /home/wyc/leo97ospfd.interface -q /home/wyc/vtyospfd97.api')
    leo98.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo98ospfd.conf -d -z /home/wyc/leo98zebra.api -i /home/wyc/leo98ospfd.interface -q /home/wyc/vtyospfd98.api')
    leo99.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo99ospfd.conf -d -z /home/wyc/leo99zebra.api -i /home/wyc/leo99ospfd.interface -q /home/wyc/vtyospfd99.api')
    leo100.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo100ospfd.conf -d -z /home/wyc/leo100zebra.api -i /home/wyc/leo100ospfd.interface -q /home/wyc/vtyospfd100.api')
    leo101.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo101ospfd.conf -d -z /home/wyc/leo101zebra.api -i /home/wyc/leo101ospfd.interface -q /home/wyc/vtyospfd101.api')
    leo102.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo102ospfd.conf -d -z /home/wyc/leo102zebra.api -i /home/wyc/leo102ospfd.interface -q /home/wyc/vtyospfd102.api')
    leo103.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo103ospfd.conf -d -z /home/wyc/leo103zebra.api -i /home/wyc/leo103ospfd.interface -q /home/wyc/vtyospfd103.api')
    leo104.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo104ospfd.conf -d -z /home/wyc/leo104zebra.api -i /home/wyc/leo104ospfd.interface -q /home/wyc/vtyospfd104.api')
    leo105.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo105ospfd.conf -d -z /home/wyc/leo105zebra.api -i /home/wyc/leo105ospfd.interface -q /home/wyc/vtyospfd105.api')
    leo106.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo106ospfd.conf -d -z /home/wyc/leo106zebra.api -i /home/wyc/leo106ospfd.interface -q /home/wyc/vtyospfd106.api')
    leo107.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo107ospfd.conf -d -z /home/wyc/leo107zebra.api -i /home/wyc/leo107ospfd.interface -q /home/wyc/vtyospfd107.api')
    leo108.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo108ospfd.conf -d -z /home/wyc/leo108zebra.api -i /home/wyc/leo108ospfd.interface -q /home/wyc/vtyospfd108.api')
    leo109.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo109ospfd.conf -d -z /home/wyc/leo109zebra.api -i /home/wyc/leo109ospfd.interface -q /home/wyc/vtyospfd109.api')
    leo110.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo110ospfd.conf -d -z /home/wyc/leo110zebra.api -i /home/wyc/leo110ospfd.interface -q /home/wyc/vtyospfd110.api')
    leo111.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo111ospfd.conf -d -z /home/wyc/leo111zebra.api -i /home/wyc/leo111ospfd.interface -q /home/wyc/vtyospfd111.api')
    leo112.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo112ospfd.conf -d -z /home/wyc/leo112zebra.api -i /home/wyc/leo112ospfd.interface -q /home/wyc/vtyospfd112.api')
    leo113.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo113ospfd.conf -d -z /home/wyc/leo113zebra.api -i /home/wyc/leo113ospfd.interface -q /home/wyc/vtyospfd113.api')
    leo114.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo114ospfd.conf -d -z /home/wyc/leo114zebra.api -i /home/wyc/leo114ospfd.interface -q /home/wyc/vtyospfd114.api')
    leo115.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo115ospfd.conf -d -z /home/wyc/leo115zebra.api -i /home/wyc/leo115ospfd.interface -q /home/wyc/vtyospfd115.api')
    leo116.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo116ospfd.conf -d -z /home/wyc/leo116zebra.api -i /home/wyc/leo116ospfd.interface -q /home/wyc/vtyospfd116.api')
    leo117.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo117ospfd.conf -d -z /home/wyc/leo117zebra.api -i /home/wyc/leo117ospfd.interface -q /home/wyc/vtyospfd117.api')
    leo118.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo118ospfd.conf -d -z /home/wyc/leo118zebra.api -i /home/wyc/leo118ospfd.interface -q /home/wyc/vtyospfd118.api')
    leo119.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo119ospfd.conf -d -z /home/wyc/leo119zebra.api -i /home/wyc/leo119ospfd.interface -q /home/wyc/vtyospfd119.api')
    leo120.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo120ospfd.conf -d -z /home/wyc/leo120zebra.api -i /home/wyc/leo120ospfd.interface -q /home/wyc/vtyospfd120.api')
    leo121.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo121ospfd.conf -d -z /home/wyc/leo121zebra.api -i /home/wyc/leo121ospfd.interface -q /home/wyc/vtyospfd121.api')
    leo122.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo122ospfd.conf -d -z /home/wyc/leo122zebra.api -i /home/wyc/leo122ospfd.interface -q /home/wyc/vtyospfd122.api')
    leo123.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo123ospfd.conf -d -z /home/wyc/leo123zebra.api -i /home/wyc/leo123ospfd.interface -q /home/wyc/vtyospfd123.api')
    leo124.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo124ospfd.conf -d -z /home/wyc/leo124zebra.api -i /home/wyc/leo124ospfd.interface -q /home/wyc/vtyospfd124.api')
    leo125.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo125ospfd.conf -d -z /home/wyc/leo125zebra.api -i /home/wyc/leo125ospfd.interface -q /home/wyc/vtyospfd125.api')
    leo126.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo126ospfd.conf -d -z /home/wyc/leo126zebra.api -i /home/wyc/leo126ospfd.interface -q /home/wyc/vtyospfd126.api')
    leo127.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo127ospfd.conf -d -z /home/wyc/leo127zebra.api -i /home/wyc/leo127ospfd.interface -q /home/wyc/vtyospfd127.api')
    leo128.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo128ospfd.conf -d -z /home/wyc/leo128zebra.api -i /home/wyc/leo128ospfd.interface -q /home/wyc/vtyospfd128.api')
    leo129.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo129ospfd.conf -d -z /home/wyc/leo129zebra.api -i /home/wyc/leo129ospfd.interface -q /home/wyc/vtyospfd129.api')
    leo130.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo130ospfd.conf -d -z /home/wyc/leo130zebra.api -i /home/wyc/leo130ospfd.interface -q /home/wyc/vtyospfd130.api')
    leo131.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo131ospfd.conf -d -z /home/wyc/leo131zebra.api -i /home/wyc/leo131ospfd.interface -q /home/wyc/vtyospfd131.api')
    leo132.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo132ospfd.conf -d -z /home/wyc/leo132zebra.api -i /home/wyc/leo132ospfd.interface -q /home/wyc/vtyospfd132.api')
    leo133.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo133ospfd.conf -d -z /home/wyc/leo133zebra.api -i /home/wyc/leo133ospfd.interface -q /home/wyc/vtyospfd133.api')
    leo134.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo134ospfd.conf -d -z /home/wyc/leo134zebra.api -i /home/wyc/leo134ospfd.interface -q /home/wyc/vtyospfd134.api')
    leo135.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo135ospfd.conf -d -z /home/wyc/leo135zebra.api -i /home/wyc/leo135ospfd.interface -q /home/wyc/vtyospfd135.api')
    leo136.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo136ospfd.conf -d -z /home/wyc/leo136zebra.api -i /home/wyc/leo136ospfd.interface -q /home/wyc/vtyospfd136.api')
    leo137.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo137ospfd.conf -d -z /home/wyc/leo137zebra.api -i /home/wyc/leo137ospfd.interface -q /home/wyc/vtyospfd137.api')
    leo138.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo138ospfd.conf -d -z /home/wyc/leo138zebra.api -i /home/wyc/leo138ospfd.interface -q /home/wyc/vtyospfd138.api')
    leo139.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo139ospfd.conf -d -z /home/wyc/leo139zebra.api -i /home/wyc/leo139ospfd.interface -q /home/wyc/vtyospfd139.api')
    leo140.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo140ospfd.conf -d -z /home/wyc/leo140zebra.api -i /home/wyc/leo140ospfd.interface -q /home/wyc/vtyospfd140.api')
    leo141.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo141ospfd.conf -d -z /home/wyc/leo141zebra.api -i /home/wyc/leo141ospfd.interface -q /home/wyc/vtyospfd141.api')
    leo142.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo142ospfd.conf -d -z /home/wyc/leo142zebra.api -i /home/wyc/leo142ospfd.interface -q /home/wyc/vtyospfd142.api')
    leo143.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo143ospfd.conf -d -z /home/wyc/leo143zebra.api -i /home/wyc/leo143ospfd.interface -q /home/wyc/vtyospfd143.api')
    leo144.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo144ospfd.conf -d -z /home/wyc/leo144zebra.api -i /home/wyc/leo144ospfd.interface -q /home/wyc/vtyospfd144.api')
    leo145.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo145ospfd.conf -d -z /home/wyc/leo145zebra.api -i /home/wyc/leo145ospfd.interface -q /home/wyc/vtyospfd145.api')
    leo146.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo146ospfd.conf -d -z /home/wyc/leo146zebra.api -i /home/wyc/leo146ospfd.interface -q /home/wyc/vtyospfd146.api')
    leo147.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo147ospfd.conf -d -z /home/wyc/leo147zebra.api -i /home/wyc/leo147ospfd.interface -q /home/wyc/vtyospfd147.api')
    leo148.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo148ospfd.conf -d -z /home/wyc/leo148zebra.api -i /home/wyc/leo148ospfd.interface -q /home/wyc/vtyospfd148.api')
    leo149.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo149ospfd.conf -d -z /home/wyc/leo149zebra.api -i /home/wyc/leo149ospfd.interface -q /home/wyc/vtyospfd149.api')
    leo150.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo150ospfd.conf -d -z /home/wyc/leo150zebra.api -i /home/wyc/leo150ospfd.interface -q /home/wyc/vtyospfd150.api')
    leo151.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo151ospfd.conf -d -z /home/wyc/leo151zebra.api -i /home/wyc/leo151ospfd.interface -q /home/wyc/vtyospfd151.api')
    leo152.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo152ospfd.conf -d -z /home/wyc/leo152zebra.api -i /home/wyc/leo152ospfd.interface -q /home/wyc/vtyospfd152.api')
    leo153.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo153ospfd.conf -d -z /home/wyc/leo153zebra.api -i /home/wyc/leo153ospfd.interface -q /home/wyc/vtyospfd153.api')
    leo154.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo154ospfd.conf -d -z /home/wyc/leo154zebra.api -i /home/wyc/leo154ospfd.interface -q /home/wyc/vtyospfd154.api')
    leo155.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo155ospfd.conf -d -z /home/wyc/leo155zebra.api -i /home/wyc/leo155ospfd.interface -q /home/wyc/vtyospfd155.api')
    leo156.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo156ospfd.conf -d -z /home/wyc/leo156zebra.api -i /home/wyc/leo156ospfd.interface -q /home/wyc/vtyospfd156.api')
    leo157.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo157ospfd.conf -d -z /home/wyc/leo157zebra.api -i /home/wyc/leo157ospfd.interface -q /home/wyc/vtyospfd157.api')
    leo158.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo158ospfd.conf -d -z /home/wyc/leo158zebra.api -i /home/wyc/leo158ospfd.interface -q /home/wyc/vtyospfd158.api')
    leo159.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo159ospfd.conf -d -z /home/wyc/leo159zebra.api -i /home/wyc/leo159ospfd.interface -q /home/wyc/vtyospfd159.api')
    leo160.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo160ospfd.conf -d -z /home/wyc/leo160zebra.api -i /home/wyc/leo160ospfd.interface -q /home/wyc/vtyospfd160.api')
    leo161.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo161ospfd.conf -d -z /home/wyc/leo161zebra.api -i /home/wyc/leo161ospfd.interface -q /home/wyc/vtyospfd161.api')
    leo162.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo162ospfd.conf -d -z /home/wyc/leo162zebra.api -i /home/wyc/leo162ospfd.interface -q /home/wyc/vtyospfd162.api')
    leo163.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo163ospfd.conf -d -z /home/wyc/leo163zebra.api -i /home/wyc/leo163ospfd.interface -q /home/wyc/vtyospfd163.api')
    leo164.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo164ospfd.conf -d -z /home/wyc/leo164zebra.api -i /home/wyc/leo164ospfd.interface -q /home/wyc/vtyospfd164.api')
    leo165.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo165ospfd.conf -d -z /home/wyc/leo165zebra.api -i /home/wyc/leo165ospfd.interface -q /home/wyc/vtyospfd165.api')
    leo166.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo166ospfd.conf -d -z /home/wyc/leo166zebra.api -i /home/wyc/leo166ospfd.interface -q /home/wyc/vtyospfd166.api')
    leo167.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo167ospfd.conf -d -z /home/wyc/leo167zebra.api -i /home/wyc/leo167ospfd.interface -q /home/wyc/vtyospfd167.api')
    leo168.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo168ospfd.conf -d -z /home/wyc/leo168zebra.api -i /home/wyc/leo168ospfd.interface -q /home/wyc/vtyospfd168.api')
    leo169.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo169ospfd.conf -d -z /home/wyc/leo169zebra.api -i /home/wyc/leo169ospfd.interface -q /home/wyc/vtyospfd169.api')
    leo170.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo170ospfd.conf -d -z /home/wyc/leo170zebra.api -i /home/wyc/leo170ospfd.interface -q /home/wyc/vtyospfd170.api')
    leo171.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo171ospfd.conf -d -z /home/wyc/leo171zebra.api -i /home/wyc/leo171ospfd.interface -q /home/wyc/vtyospfd171.api')
    leo172.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo172ospfd.conf -d -z /home/wyc/leo172zebra.api -i /home/wyc/leo172ospfd.interface -q /home/wyc/vtyospfd172.api')
    leo173.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo173ospfd.conf -d -z /home/wyc/leo173zebra.api -i /home/wyc/leo173ospfd.interface -q /home/wyc/vtyospfd173.api')
    leo174.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo174ospfd.conf -d -z /home/wyc/leo174zebra.api -i /home/wyc/leo174ospfd.interface -q /home/wyc/vtyospfd174.api')
    leo175.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo175ospfd.conf -d -z /home/wyc/leo175zebra.api -i /home/wyc/leo175ospfd.interface -q /home/wyc/vtyospfd175.api')
    leo176.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo176ospfd.conf -d -z /home/wyc/leo176zebra.api -i /home/wyc/leo176ospfd.interface -q /home/wyc/vtyospfd176.api')
    leo177.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo177ospfd.conf -d -z /home/wyc/leo177zebra.api -i /home/wyc/leo177ospfd.interface -q /home/wyc/vtyospfd177.api')
    leo178.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo178ospfd.conf -d -z /home/wyc/leo178zebra.api -i /home/wyc/leo178ospfd.interface -q /home/wyc/vtyospfd178.api')
    leo179.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo179ospfd.conf -d -z /home/wyc/leo179zebra.api -i /home/wyc/leo179ospfd.interface -q /home/wyc/vtyospfd179.api')
    leo180.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo180ospfd.conf -d -z /home/wyc/leo180zebra.api -i /home/wyc/leo180ospfd.interface -q /home/wyc/vtyospfd180.api')
    leo181.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo181ospfd.conf -d -z /home/wyc/leo181zebra.api -i /home/wyc/leo181ospfd.interface -q /home/wyc/vtyospfd181.api')
    leo182.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo182ospfd.conf -d -z /home/wyc/leo182zebra.api -i /home/wyc/leo182ospfd.interface -q /home/wyc/vtyospfd182.api')
    leo183.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo183ospfd.conf -d -z /home/wyc/leo183zebra.api -i /home/wyc/leo183ospfd.interface -q /home/wyc/vtyospfd183.api')
    leo184.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo184ospfd.conf -d -z /home/wyc/leo184zebra.api -i /home/wyc/leo184ospfd.interface -q /home/wyc/vtyospfd184.api')
    leo185.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo185ospfd.conf -d -z /home/wyc/leo185zebra.api -i /home/wyc/leo185ospfd.interface -q /home/wyc/vtyospfd185.api')
    leo186.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo186ospfd.conf -d -z /home/wyc/leo186zebra.api -i /home/wyc/leo186ospfd.interface -q /home/wyc/vtyospfd186.api')
    leo187.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo187ospfd.conf -d -z /home/wyc/leo187zebra.api -i /home/wyc/leo187ospfd.interface -q /home/wyc/vtyospfd187.api')
    leo188.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo188ospfd.conf -d -z /home/wyc/leo188zebra.api -i /home/wyc/leo188ospfd.interface -q /home/wyc/vtyospfd188.api')
    leo189.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo189ospfd.conf -d -z /home/wyc/leo189zebra.api -i /home/wyc/leo189ospfd.interface -q /home/wyc/vtyospfd189.api')
    leo190.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo190ospfd.conf -d -z /home/wyc/leo190zebra.api -i /home/wyc/leo190ospfd.interface -q /home/wyc/vtyospfd190.api')
    leo191.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo191ospfd.conf -d -z /home/wyc/leo191zebra.api -i /home/wyc/leo191ospfd.interface -q /home/wyc/vtyospfd191.api')
    leo192.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo192ospfd.conf -d -z /home/wyc/leo192zebra.api -i /home/wyc/leo192ospfd.interface -q /home/wyc/vtyospfd192.api')
    leo193.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo193ospfd.conf -d -z /home/wyc/leo193zebra.api -i /home/wyc/leo193ospfd.interface -q /home/wyc/vtyospfd193.api')
    leo194.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo194ospfd.conf -d -z /home/wyc/leo194zebra.api -i /home/wyc/leo194ospfd.interface -q /home/wyc/vtyospfd194.api')
    leo195.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo195ospfd.conf -d -z /home/wyc/leo195zebra.api -i /home/wyc/leo195ospfd.interface -q /home/wyc/vtyospfd195.api')
    leo196.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo196ospfd.conf -d -z /home/wyc/leo196zebra.api -i /home/wyc/leo196ospfd.interface -q /home/wyc/vtyospfd196.api')
    leo197.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo197ospfd.conf -d -z /home/wyc/leo197zebra.api -i /home/wyc/leo197ospfd.interface -q /home/wyc/vtyospfd197.api')
    leo198.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo198ospfd.conf -d -z /home/wyc/leo198zebra.api -i /home/wyc/leo198ospfd.interface -q /home/wyc/vtyospfd198.api')
    leo199.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo199ospfd.conf -d -z /home/wyc/leo199zebra.api -i /home/wyc/leo199ospfd.interface -q /home/wyc/vtyospfd199.api')
    leo200.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo200ospfd.conf -d -z /home/wyc/leo200zebra.api -i /home/wyc/leo200ospfd.interface -q /home/wyc/vtyospfd200.api')
    leo201.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo201ospfd.conf -d -z /home/wyc/leo201zebra.api -i /home/wyc/leo201ospfd.interface -q /home/wyc/vtyospfd201.api')
    leo202.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo202ospfd.conf -d -z /home/wyc/leo202zebra.api -i /home/wyc/leo202ospfd.interface -q /home/wyc/vtyospfd202.api')
    leo203.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo203ospfd.conf -d -z /home/wyc/leo203zebra.api -i /home/wyc/leo203ospfd.interface -q /home/wyc/vtyospfd203.api')
    leo204.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo204ospfd.conf -d -z /home/wyc/leo204zebra.api -i /home/wyc/leo204ospfd.interface -q /home/wyc/vtyospfd204.api')
    leo205.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo205ospfd.conf -d -z /home/wyc/leo205zebra.api -i /home/wyc/leo205ospfd.interface -q /home/wyc/vtyospfd205.api')
    leo206.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo206ospfd.conf -d -z /home/wyc/leo206zebra.api -i /home/wyc/leo206ospfd.interface -q /home/wyc/vtyospfd206.api')
    leo207.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo207ospfd.conf -d -z /home/wyc/leo207zebra.api -i /home/wyc/leo207ospfd.interface -q /home/wyc/vtyospfd207.api')
    leo208.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo208ospfd.conf -d -z /home/wyc/leo208zebra.api -i /home/wyc/leo208ospfd.interface -q /home/wyc/vtyospfd208.api')
    leo209.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo209ospfd.conf -d -z /home/wyc/leo209zebra.api -i /home/wyc/leo209ospfd.interface -q /home/wyc/vtyospfd209.api')
    leo210.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo210ospfd.conf -d -z /home/wyc/leo210zebra.api -i /home/wyc/leo210ospfd.interface -q /home/wyc/vtyospfd210.api')
    leo211.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo211ospfd.conf -d -z /home/wyc/leo211zebra.api -i /home/wyc/leo211ospfd.interface -q /home/wyc/vtyospfd211.api')
    leo212.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo212ospfd.conf -d -z /home/wyc/leo212zebra.api -i /home/wyc/leo212ospfd.interface -q /home/wyc/vtyospfd212.api')
    leo213.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo213ospfd.conf -d -z /home/wyc/leo213zebra.api -i /home/wyc/leo213ospfd.interface -q /home/wyc/vtyospfd213.api')
    leo214.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo214ospfd.conf -d -z /home/wyc/leo214zebra.api -i /home/wyc/leo214ospfd.interface -q /home/wyc/vtyospfd214.api')
    leo215.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo215ospfd.conf -d -z /home/wyc/leo215zebra.api -i /home/wyc/leo215ospfd.interface -q /home/wyc/vtyospfd215.api')
    leo216.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo216ospfd.conf -d -z /home/wyc/leo216zebra.api -i /home/wyc/leo216ospfd.interface -q /home/wyc/vtyospfd216.api')
    leo217.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo217ospfd.conf -d -z /home/wyc/leo217zebra.api -i /home/wyc/leo217ospfd.interface -q /home/wyc/vtyospfd217.api')
    leo218.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo218ospfd.conf -d -z /home/wyc/leo218zebra.api -i /home/wyc/leo218ospfd.interface -q /home/wyc/vtyospfd218.api')
    leo219.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo219ospfd.conf -d -z /home/wyc/leo219zebra.api -i /home/wyc/leo219ospfd.interface -q /home/wyc/vtyospfd219.api')
    leo220.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo220ospfd.conf -d -z /home/wyc/leo220zebra.api -i /home/wyc/leo220ospfd.interface -q /home/wyc/vtyospfd220.api')
    leo221.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo221ospfd.conf -d -z /home/wyc/leo221zebra.api -i /home/wyc/leo221ospfd.interface -q /home/wyc/vtyospfd221.api')
    leo222.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo222ospfd.conf -d -z /home/wyc/leo222zebra.api -i /home/wyc/leo222ospfd.interface -q /home/wyc/vtyospfd222.api')
    leo223.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo223ospfd.conf -d -z /home/wyc/leo223zebra.api -i /home/wyc/leo223ospfd.interface -q /home/wyc/vtyospfd223.api')
    leo224.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo224ospfd.conf -d -z /home/wyc/leo224zebra.api -i /home/wyc/leo224ospfd.interface -q /home/wyc/vtyospfd224.api')
    leo225.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo225ospfd.conf -d -z /home/wyc/leo225zebra.api -i /home/wyc/leo225ospfd.interface -q /home/wyc/vtyospfd225.api')
    leo226.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo226ospfd.conf -d -z /home/wyc/leo226zebra.api -i /home/wyc/leo226ospfd.interface -q /home/wyc/vtyospfd226.api')
    leo227.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo227ospfd.conf -d -z /home/wyc/leo227zebra.api -i /home/wyc/leo227ospfd.interface -q /home/wyc/vtyospfd227.api')
    leo228.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo228ospfd.conf -d -z /home/wyc/leo228zebra.api -i /home/wyc/leo228ospfd.interface -q /home/wyc/vtyospfd228.api')
    leo229.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo229ospfd.conf -d -z /home/wyc/leo229zebra.api -i /home/wyc/leo229ospfd.interface -q /home/wyc/vtyospfd229.api')
    leo230.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo230ospfd.conf -d -z /home/wyc/leo230zebra.api -i /home/wyc/leo230ospfd.interface -q /home/wyc/vtyospfd230.api')
    leo231.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo231ospfd.conf -d -z /home/wyc/leo231zebra.api -i /home/wyc/leo231ospfd.interface -q /home/wyc/vtyospfd231.api')
    leo232.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo232ospfd.conf -d -z /home/wyc/leo232zebra.api -i /home/wyc/leo232ospfd.interface -q /home/wyc/vtyospfd232.api')
    leo233.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo233ospfd.conf -d -z /home/wyc/leo233zebra.api -i /home/wyc/leo233ospfd.interface -q /home/wyc/vtyospfd233.api')
    leo234.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo234ospfd.conf -d -z /home/wyc/leo234zebra.api -i /home/wyc/leo234ospfd.interface -q /home/wyc/vtyospfd234.api')
    leo235.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo235ospfd.conf -d -z /home/wyc/leo235zebra.api -i /home/wyc/leo235ospfd.interface -q /home/wyc/vtyospfd235.api')
    leo236.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo236ospfd.conf -d -z /home/wyc/leo236zebra.api -i /home/wyc/leo236ospfd.interface -q /home/wyc/vtyospfd236.api')
    leo237.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo237ospfd.conf -d -z /home/wyc/leo237zebra.api -i /home/wyc/leo237ospfd.interface -q /home/wyc/vtyospfd237.api')
    leo238.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo238ospfd.conf -d -z /home/wyc/leo238zebra.api -i /home/wyc/leo238ospfd.interface -q /home/wyc/vtyospfd238.api')
    leo239.cmd('ospfd -f /mnt/hgfs/vm_new/test_data/AS_240_6/ospf_conf/leo239ospfd.conf -d -z /home/wyc/leo239zebra.api -i /home/wyc/leo239ospfd.interface -q /home/wyc/vtyospfd239.api')

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
