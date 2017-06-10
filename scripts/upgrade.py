# $language = "Python"
# $interface = "1.0"

'''
    crt script, update image 
'''
import os
__author__ = 'sxqiao'


crt.Screen.Synchronous = True

def main():  
    crt.Screen.Send('\n')
    crt.Screen.Send('exit\n')
    crt.Screen.Send('\n')
    crt.Screen.Send('quit\n')
    crt.Screen.Send('\n')
    crt.Screen.WaitForString('>')
    crt.Screen.Clear()

    crt.Screen.Send('enable\n')
    crt.Screen.Send('admin\n')
    crt.Screen.Send('configure terminal\n')
    crt.Screen.Send('__hide\n')
    crt.Screen.Send('shell\n')
    crt.Screen.WaitForString('/ #')
    crt.Screen.Send("fw_readmanu | grep model | awk -F '=' '{print $2}'\n")
    crt.Screen.WaitForString('\n')
    product = crt.Screen.ReadString('/ #', 10)  

    crt.Screen.Send('\n')
    crt.Screen.Send('exit\n')
    crt.Screen.Send('\n')
    crt.Screen.Send('quit\n')
    crt.Screen.Send('\n')
    crt.Screen.WaitForString('>')
    crt.Screen.Clear()

    crt.Screen.Send('enable\n')
    crt.Screen.Send('admin\n')
    crt.Screen.Send('configure terminal\n')
    crt.Screen.Send('image-upgrade tftp\n')
    crt.Screen.Send('192.168.1.104\n')
    crt.Screen.Send(product.strip('\r\n') + '.app\n')
    crt.Screen.Send('y\n')
    crt.Screen.Send('\r\n')


main()        
