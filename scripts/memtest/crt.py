# $language = "Python"
# $interface = "1.0"

'''
    crt script, get process memory
'''

__author__ = 'sxqiao'

import os
import re
import csv
import time


USER = 'exit' + chr(10) + 'quit' + chr(10)
SYSTEM = USER + 'enable' + chr(10) + 'admin' + chr(10)
CONFIG = SYSTEM + 'configure terminal' + chr(10)
SHELL = CONFIG + '_hide' + chr(10) +  'shell' + chr(10)

HOME_PATH = os.path.split(crt.ScriptFullName)
HOME_DIR = HOME_PATH[0]
FILE_PATH = os.path.join(HOME_DIR, 'cmd.txt')
EXCEL_PATH = os.path.join(HOME_DIR, 'summary.csv')

crt.Screen.Synchronous = True

# 获取进程内存
def get_process_mem(process_name):
    crt.Screen.Send(SHELL) 
    crt.Screen.WaitForString('/ #')
    crt.Screen.Send('ps | grep /usr/bin/' + process_name + " | grep -v grep | awk '{print $1}'"+ chr(10)) 
    crt.Screen.WaitForString(chr(10))   
    pid = crt.Screen.ReadString('/ #', 10)  
        
    crt.Screen.Send('cat /proc/' + pid.strip('\r\n') + "/status | grep VmRSS | awk '{print $2}'" + chr(10))   
    crt.Screen.WaitForString(chr(10))    
    mem = crt.Screen.ReadString('/ #', 10)
    mem = mem.strip('\r\n')
    
    return mem

# 获取总内存
def get_total_mem():
    crt.Screen.Send(SHELL) 
    crt.Screen.WaitForString('/ #')
    crt.Screen.Send("free | grep Mem | awk '{print $3}'"+ chr(10)) 
    crt.Screen.WaitForString(chr(10))   
    mem = crt.Screen.ReadString('/ #', 10)
    mem = mem.strip('\r\n')  
    
    return mem 

def main():  
    crt.Dialog.MessageBox ('make sure cmd.txt have common!', 'NOTE')
    intervalstr = crt.Dialog.Prompt("Please input count time interval(ms):", "time interval", "5000", False)
    interval = int(intervalstr)
    process = crt.Dialog.Prompt("Please input proccess name(ms):", "process name", "dnsmasq", False)
        
    excelobj = open(EXCEL_PATH, 'wb')
    worksheet = csv.writer(excelobj)
    worksheet.writerow(['', process, 'total']);  
    while True :
        cmdobj = open(FILE_PATH)  
        for line in cmdobj.readlines():
            crt.Screen.Send(line)
        cmdobj.close()
            
        mem1 = get_process_mem(process)
        mem2 = get_total_mem()
        worksheet.writerow([time.strftime('%X'), mem1, mem2])
    
        crt.Sleep(interval)
        
    excelobj.close()



main()        
 

