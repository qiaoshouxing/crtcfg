# $language = "Python"
# $interface = "1.0"

'''
    crt script, set wds root
'''
import os
__author__ = 'sxqiao'


crt.Screen.Synchronous = True

def main():  
    crt.Screen.Send('./wds -l 3 -T 1 -U eth0 -A 34:CD:6D:E0:10:27\r\n')

main()        
