# $language = "Python"
# $interface = "1.0"

'''
    crt script, update image 
'''
import os
__author__ = 'sxqiao'


crt.Screen.Synchronous = True

def main():  
    crt.Screen.Send('\r\n')
    crt.Screen.Send('exit\r\n')
    crt.Screen.Send('\r\n')
    crt.Screen.Send('quit\r\n')
    crt.Screen.Send('\r\n')

    crt.Screen.Send('enable\n')
    crt.Screen.Send('admin\n')
    crt.Screen.Send('configure terminal\r\n')

    crt.Screen.Send('info-center terminal logging level debugging  \n')
    crt.Screen.Send('info-center terminal logging enable\n')
    crt.Screen.Send('terminal logging\n')

    crt.Screen.Send('terminal debugging setting level detail\n')
    crt.Screen.Send('terminal debugging \n')

    crt.Screen.Send('debugging wds\n')
    crt.Screen.Send('debugging wds link\n')

    crt.Screen.Send('dot11 authentication mac-acl qsx\n')
    crt.Screen.Send('mac-list 34:CD:6D:03:45:30\n')
    crt.Screen.Send('mac-list 34:CD:6D:F6:23:B0\n')
    crt.Screen.Send('mac-list 34:CD:6D:00:00:10\n')
    crt.Screen.Send('policy permit\n')
    crt.Screen.Send('exit\n')

    crt.Screen.Send('dot11 wds\n')
    crt.Screen.Send('root config\n')
    crt.Screen.Send('auto-repeater default-backhaul 5g\n')
    #crt.Screen.Send('auto-repeater ap 34:CD:6D:03:45:30 uplinkap 34:CD:6D:03:83:10\n') 
    #crt.Screen.Send('auto-repeater ap 34:CD:6D:00:00:10 uplinkap 34:CD:6D:03:45:30\n') 
    #crt.Screen.Send('auto-repeater acl maclist 0\n') 
    crt.Screen.Send('auto-repeater link-secure simple passphase 12345678\n') 
    crt.Screen.Send('netid 1wds_test\n')
    crt.Screen.Send('exit\n')
    crt.Screen.Send('wds mode root\n')



main()        
