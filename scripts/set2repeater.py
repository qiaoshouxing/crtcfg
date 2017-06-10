# $language = "Python"
# $interface = "1.0"

'''
    crt script, set wds root
'''
import os
__author__ = 'sxqiao'


crt.Screen.Synchronous = True

def main():  
    crt.Screen.Send('./wds -l 2 -U eth0 -T 1 -D eth1 -A 34:CD:6D:00:00:67\r\n')

main()        
