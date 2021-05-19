#!/usr/bin/python3

import os, sys
import colorama
from colorama import Fore, Style


def printUsage():
    print('Usage: ./devdiscover.py --ip-start=[ip] --ip-end=[ip] --wait-response=[secs] --iface=[interface] \
[--verbose] [--show-names] [--show-macs]')
    print('./devdiscover.py --help for additional help')

def help():
    print()
    print(Fore.LIGHTBLUE_EX)
    print('''devdiscover is a simple utility that can discover all LAN/WLAN devices in specified IP Range.
Usage: ./devdiscover.py --ip-start=[ip] --ip-end=[ip] --wait-response=[secs] --iface=[interface]
[--verbose] [--show-names] [--show-macs]

--ip-start=[ip]	                Start bound of IP range	                            (*)
--ip-end=[ip]	                End bound of IP range                               (*)
--show-macs	                Show MAC addresses?	
--show-names	                Show names of devices?	
--verbose	                Show all scanned IP addresses	
--wait-response=[seconds]	How much time should I wait for response?           (*)
--iface=[interface]	        Which interface should I use to scan IP addresses?  (*)
''')
    print(Style.RESET_ALL)


def check(myArgs):
    foundArgs = 0
    startIP,endIP,waitInterval,iface,verbose,macs,names = '','',0,'',False,False,False
    for argument in myArgs:
        # --ip-start, --ip-end, --wait-response, --iface   // it exists? //
        if argument.find('--ip-start=') != -1 or argument.find('--ip-end=') != -1:
            if len(argument[argument.index('=')+1:].split('.')) == 4:  # all is ok
                foundArgs += 1
                if argument.find('--ip-start=') != -1:
                    _startIP = argument[argument.index('=')+1:]
                    startIP = _startIP
                else:
                    _endIP = argument[argument.index('=')+1:]
                    endIP = _endIP
            else:  # we've got --ip-start / --ip-end, but specified IP is not IP
                print(Fore.RED + 'Incorrect usage of argument --ip-start / --ip-end')
                print(Style.RESET_ALL)
                printUsage()
                exit()
        elif argument.find('--wait-response=') != -1:
            if len(argument[argument.index('=')+1:]) > 0:
                foundArgs += 1
                waitInterval = argument[argument.index('=')+1:]
            else:
                print(Fore.RED + 'Incorrect usage of argument --wait-response')
                print(Style.RESET_ALL)
                printUsage()
                exit()
        elif argument.find('--iface=') != -1:
            _ifaces = os.popen('ls /sys/class/net/')
            ifaces = _ifaces.read().split('\n')
            specifiedIface = argument[argument.index('=')+1:]
            if specifiedIface in ifaces:
                foundArgs += 1
                iface = specifiedIface
            else:
                print(Fore.RED + 'Specified network interface does not exist at the moment')
                print(Style.RESET_ALL)
                printUsage()
                exit()
        elif argument == '--verbose' or argument == '--show-macs' or argument == '--show-names':
            if argument == '--verbose':
                verbose = True
            elif argument == '--show-macs':
                macs = True
            elif argument == '--show-names':
                names = True
            foundArgs += 1

    if foundArgs >= 4:
        if '.'.join(_startIP.split('.')[0:3]) == '.'.join(_endIP.split('.')[0:3]):
            if int(max(_startIP.split('.'))) <= 255 and int(max(_endIP.split('.'))) <= 255:
                if int(min(_startIP.split('.'))) >= 0 and int(min(_endIP.split('.'))) >= 0:
                    if int(_startIP.split('.')[-1]) < int(_endIP.split('.')[-1]):
                        return (startIP,endIP,waitInterval,iface,verbose,macs,names)
                    else:  # start bound is < end bound
                        print(Fore.RED + 'Incorrect usage of argument --ip-start / --ip-end')
                        print(Style.RESET_ALL)
                        printUsage()
                        exit()
                else:  # one of IP blocks is < 0
                    print(Fore.RED + 'Incorrect usage of argument --ip-start / --ip-end')
                    print(Style.RESET_ALL)
                    printUsage()
                    exit()
            else:  # one of IP blocks is > 255
                print(Fore.RED + 'Incorrect usage of argument --ip-start / --ip-end')
                print(Style.RESET_ALL)
                printUsage()
                exit()
        else:  # xxx.xxx.xxx.??? != xxx.xxx.xxx.???
            print(Fore.RED + 'Incorrect usage of argument --ip-start / --ip-end')
            print(Style.RESET_ALL)
            printUsage()
            exit()
    else:
        print(Fore.RED + 'Not all necessary arguments were found.')
        print(Style.RESET_ALL)
        printUsage()
        exit()


def work(startIP, endIP, waitInterval, iface, verbose, macs, names):
    avaliableHosts = []
    for last_block in range(int(startIP.split('.')[-1]), int(endIP.split('.')[-1])):
        ipaddr = '.'.join(startIP.split('.')[0:3]) + '.' + str(last_block)
        ping_stream = os.popen('ping ' + ipaddr + ' -c 1 -W ' + waitInterval + ' -I ' + iface)
        ping_data = ping_stream.read()
        if 'bytes from' in ping_data:
            avaliableHosts.append(ipaddr)
            if verbose:
                print(Fore.GREEN + '[+] ' + ipaddr + ': FOUND' + Style.RESET_ALL)
        else:
            if verbose:
                print(Fore.RED + '[-] ' + ipaddr + ': no such host' + Style.RESET_ALL)

    print(Fore.LIGHTBLUE_EX + '[i] Getting summary information...')

    for host in avaliableHosts:
        print('IP: ' + host, end='     ')
        if names:
            nslookup_stream = os.popen('nslookup ' + host)
            nslookup_data = nslookup_stream.read()
            try:
                print('Name: ' + nslookup_data[nslookup_data.index('=')+2:-3], end='     ')
            except:
                print('Name: UNKNOWN (report this!)', end='     ')
        if macs:
            arp_stream = os.popen('arp -a ' + host)
            arp_data = arp_stream.read()
            try:
                print('MAC: ' + arp_data[arp_data.index('at')+3:arp_data.index('[')-1], end='     ')
            except:
                print('MAC: UNKNOWN (report this!)', end='     ')
        print()

    print(Fore.GREEN + '[+] Job done!' + Style.RESET_ALL)


def main():
    print(Fore.YELLOW)
    os.system('figlet devdiscover')
    print('v. 0.1')
    print('thm, 2021')
    print('https://github.com/thm-unix/devdiscover/')
    #print(Style.RESET_ALL)

    myArgs = sys.argv

    if '--help' in myArgs:
        help()
        exit()

    # checking if arguments are typed correctly and setting them
    startIP,endIP,waitInterval,iface,verbose,macs,names = check(myArgs)

    print(Fore.LIGHTBLUE_EX)
    print('[i] IP Start Bound: ' + startIP)
    print('[i] IP End Bound: ' + endIP)
    print('[i] Wait Response Interval: ' + str(waitInterval) + ' secs')
    print('[i] Interface: ' + iface)
    print('[i] Verbose: ' + str(verbose))
    print('[i] Show MAC addresses: ' + str(macs))
    print('[i] Show names of devices: ' + str(names))

    print(Fore.GREEN + '\nStarting...')
    print(Fore.RED + 'Please be patient, it can take a couple of minutes.' + Style.RESET_ALL)
    work(startIP, endIP, waitInterval, iface, verbose, macs, names)


main()

