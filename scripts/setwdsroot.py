# $language = "Python"
# $interface = "1.0"

'''
    crt script, set wds root
'''
import os
__author__ = 'sxqiao'


crt.Screen.Synchronous = True

def main():  
    crt.Screen.Send('./wds -l 1 -D eth0\r\n')

main()        
