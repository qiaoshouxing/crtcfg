# $language = "Python"
# $interface = "1.0"

'''
    crt script, go to shell
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

    crt.Screen.Send('enable\r\n')
    crt.Screen.Send('admin\r\n')
    crt.Screen.Send('configure terminal\r\n')
    crt.Screen.Send('__hide\r\n')
    crt.Screen.Send('_hide\r\n')
    crt.Screen.Send('shell\r\n')
    crt.Screen.Send('cd /tmp\r\n')

main()        
