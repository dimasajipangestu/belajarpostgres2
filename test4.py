from pysnmp.hlapi import *
from pysnmp import hlapi
import quicksnmp

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public', mpModel=0),
           UdpTransportTarget(('180.250.156.138', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysUpTime', 0)))
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))
        print(varBind)
        print(x/100/60/60/24)
print("\n\n")
print(varBinds)
print('')

'''
#uptime
uptime = quicksnmp.get('demo.snmplabs.com', ['.1.3.6.1.2.1.1.3.0'], hlapi.CommunityData('public', mpModel=0))
for k, v in uptime.items():
    print(("Up Time: {} days").format(v/60/60/24))
# We leave a blank line between the output of each interface
print('')
#quicksnmp.set('demo.snmplabs.com', {'.1.3.6.1.2.1.1.1.0': 'Test'}, hlapi.CommunityData('public', mpModel=0))

location = quicksnmp.get('demo.snmplabs.com', ['.1.3.6.1.2.1.1.6.0'], hlapi.CommunityData('public', mpModel=0))
for k, v in location.items():
    print(("Location: {}").format(v))
# We leave a blank line between the output of each interface
print('')
its = quicksnmp.get_bulk_auto('demo.snmplabs.com', ['1.3.6.1.2.1.2.2.1.2', '1.3.6.1.2.1.31.1.1.1.18'], hlapi.CommunityData('public', mpModel=0), '1.3.6.1.2.1.2.1.0')
for it in its:
    for k, v in it.items():
        print("{0}={1}".format(k, v))
    print('')

test = quicksnmp.get_bulk_auto('180.250.156.138', hlapi.CommunityData('public', mpModel=0))
'''