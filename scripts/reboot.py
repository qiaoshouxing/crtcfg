# $language = "Python"
# $interface = "1.0"

'''
    crt script, reboot
'''

import os
__author__ = 'sxqiao'


crt.Screen.Synchronous = True

def main():  
    username = crt.Dialog.Prompt("Enter your username:", "Logon Script", "", False)
    if username == "":
        crt.Dialog.MessageBox("username can't NULL")
      # User clicked Cancel button

    password = crt.Dialog.Prompt("Enter your password:", "Logon Script", "", True)
    if password == "":
        crt.Dialog.MessageBox("password can't NULL")
      # User clicked Cancel button

    times = crt.Dialog.Prompt("Enter reboot times:", "Logon Script", "200", False)
    if times == "":
        crt.Dialog.MessageBox("times can't NULL")
      # User clicked Cancel button

    while (True) :
        if (crt.Screen.WaitForString("ogin:", 1000000) != True):
            crt.Dialog.MessageBox("Failed to detect login!")
        crt.Screen.Send('kylin\n')
        crt.Screen.Send('123123\n')
        crt.Screen.Send('\r\n')
        crt.Screen.Send('\r\n')
        crt.Screen.Send('sudo su -')
        crt.Screen.Send('123123\n')




main()        
