import subprocess
import getpass
import re
import config
###########################
print('___________________________________________________________________')
print('#######################   ######          #########      ##     ##   ##  ##      ##')
print('#######################  ###  ###          ##            ##    ##        ##      ##')
print('         ###            ###    ###            ##         ##  ##      ##  ##      ##')
print('         ###           ###      ###              ##      ##          ##  ##      ##')
print('         ###          ###  ####  ###           ##        ##  ##      ##  ##      ##')
print('         ###         ###          ###        ##          ##   ##     ##  ##      ##')
print('         ###        ###            ###   ######          ##    ##    ##  ######  ######')
print('___________________________________________________________________')
print('This script to get and kill tasks that running on a remote host in domain environment ')
print('Auther: Hamed Adel')
print('GitHub: github.com/hamedeg')
print('___________________________________________________________________')
if config.AdAdmin == 'default' or config.AdDomain == 'default':
    print("Please edit config file first !")
else:
    ip=input('IP Address:')
    if not re.match(r'[0-9]+(?:\.[0-9]+){3}', ip):
        print('Invalid IP Address ',ip)
    else:
        pwd = getpass.getpass(prompt = 'Administrator password: ')
        getTasks = subprocess.call(['tasklist','/s',ip,'/u',str(config.AdDomain)+'\\'+str(config.AdAdmin),'/p',pwd])
        print(getTasks)
        print('++++++++++++++++++++++++++++++++++++++++++++++++++')
        if getTasks == 1:
            print('Username or password invalid')
        else:
            print('0: To kill task using task name')
            print('1: To kill task using task PID')
            killBy = int(input("What's your choice: "))
            if(killBy==0):
                taskName = input('Enter Task Name: ')
                killTaskName = subprocess.Popen(['taskkill','/s',ip,'/u',str(config.AdDomain)+'\\'+str(config.AdAdmin),'/p',pwd,'/IM',taskName]).communicate()[0]
            elif(killBy==1):
                taskPID = input('Enter Task PID: ')
                killTaskPID = subprocess.Popen(['taskkill','/s',ip,'/u',str(config.AdDomain)+'\\'+str(config.AdAdmin),'/p',pwd,'/PID',taskPID]).communicate()[0]
            else:
                print('Incorrect input')
