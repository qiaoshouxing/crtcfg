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



    crt.Screen.Send('no terminal debugging\n')
    crt.Screen.Send('no terminal logging\n')



main()        
