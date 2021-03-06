from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto import rfc1902


def GetPortStatus(ip, comm, oid):
    rez = None
    try:
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData(comm),
                   UdpTransportTarget(
                       (ip, 161), timeout=2.0, retries=0
                   ),
                   ContextData(),
                   ObjectType(ObjectIdentity(oid)))
        )

        if errorIndication:
            error = errorIndication
            print(errorIndication)
            return rez, error
        elif errorStatus:
            error = ('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
            return rez, error
        else:
            for varBind in varBinds:
                if str(varBind).find("up") > 0: rez = 1;
                if str(varBind).find("down") > 0: rez = 2;
                if rez == None:
                    zx = str(varBind).split("=");
                    rez = zx[1].replace(" ", "");

    except:
        rez = None
    return rez



def SetPortStatus(ip, comm, oid, status):
    rez = None
    error = None
    try:
        cmdGen = cmdgen.CommandGenerator()
        errorIndication, errorStatus, errorIndex, varBinds = cmdGen.setCmd(
            cmdgen.CommunityData(comm, mpModel=1),
            cmdgen.UdpTransportTarget((ip, 161)),
            (oid, rfc1902.Integer(status)),
        )
        # Check for errors and print out results
        if errorIndication:
            error = errorIndication
            print(errorIndication)
            return error
        else:
            if errorStatus:
                error = ('%s at %s' % (
                    errorStatus.prettyPrint(),
                    errorIndex and varBinds[int(errorIndex) - 1] or '?'
                )
                         )
                print('%s at %s' % (
                    errorStatus.prettyPrint(),
                    errorIndex and varBinds[int(errorIndex) - 1] or '?'
                )
                      )
                rez = None
            else:
                for name, val in varBinds:
                    error = ('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                    print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
                    rez = True
    except:
        rez = None
    return rez, error