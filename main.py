#THIS SCRIPT WAS TESTED ON THE PYTHON VERSION 3.12.6
#IT MAY NOT WORK ON VERSIONS LATER
#
#PLEASE, INSTALL ALL PACKAGES
#    pip install uuid
#    pip install requests
#    pip install psutil
#OR 
#    pip install uuid requests psutil
#
#IF CODE DOESN'T WORK, PLEASE, WRITE TO ME: felibog@bk.ru


#imports
import getpass
import os
import time
import platform
import socket
import requests
import subprocess
from uuid import getnode as getmac
import psutil
import winreg
import json

#functions
def correct_size(bts): #convert bits
    size = 1024
    for item in ["", "Kb", "Mb", "Gb", "Tb", "Pb"]:
        if bts < size:
            return f"{bts:.2f}{item}"
        bts /= size
timeout = 1

def is_cnx_active(): #checking internet connection
    try:
        requests.head("https://google.com")
        return True
    except: 
        return False
while True: #waiting for internet connection
    if is_cnx_active() is True:
        break
    else:
        pass
      
#system data
osinfo = platform.uname()
architecture = platform.architecture()
name = getpass.getuser()
host = osinfo.node
ip = socket.gethostbyname(host)
osname = osinfo.system
processor = osinfo.machine
release = osinfo.release
version = osinfo.version
mac = getmac()
biosSN = subprocess.check_output("WMIC BIOS GET SERIALNUMBER").decode('utf-8').replace("SerialNumber", "")
biosMF = subprocess.check_output("WMIC BIOS GET Manufacturer").decode('utf-8').replace("urer", "")
biosV = subprocess.check_output("WMIC BIOS GET Version").decode('utf-8').replace("Version", "")
Dir = subprocess.check_output("WMIC BOOTCONFIG GET BootDirectory").decode('utf-8').replace("BootDirectory", "")
processorfrq = psutil.cpu_freq()
timezone = psutil.boot_time()
C = psutil.disk_usage("/")
Path = winreg.HKEY_LOCAL_MACHINE
ProductKeyPath = winreg.OpenKeyEx(Path, r"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\SoftwareProtectionPlatform")
ProductKey = winreg.QueryValueEx(ProductKeyPath, "BackupProductKeyDefault")
ipinfo = json.loads(requests.get('http://ipinfo.io/json').text)
vpnapiio_key = "" #key from vpnapi.io
vpninfo = json.loads(requests.get(f"https://vpnapi.io/api/{ipinfo['ip']}?key={vpnapiio_key}").text)

#full information of system
all = {
"OSname" : osname,
"OSrelease" : release,
"OS Version" : version,
"OS Product Key" : ProductKey[0],
"User" : name,
"Local IP" : ip,
"Public IP" : ipinfo["ip"],
"Host" : host,
"MAC" : mac,
"VPN" : vpninfo["security"]["vpn"],
"Proxy" : vpninfo["security"]["proxy"],
"Country" : ipinfo["country"],
"Region" : ipinfo["region"],
"City" : ipinfo["city"],
"Postal code" : ipinfo["postal"],
"Timezone" : ipinfo["timezone"],
"Hostname" : ipinfo["hostname"],
"Processor" : processor,
"Architecture" : architecture[0],
"Current Processor Frequency" : processorfrq.current,
"Min Processor Frequency" : processorfrq.min,
"Max Processor Frequency" : processorfrq.max,
"BIOS SerialNumber" : biosSN[8:len(biosSN)-4],
"BIOS Manufacturer" : biosMF[40:len(biosMF)-4],
"BIOS Version" : biosV[14:len(biosV)-4],
"System Directory" : Dir[5:len(Dir)-4],
"System Disk Total" : correct_size(C.total),
"System Disk Used" : correct_size(C.used),
"System Disk Free" : correct_size(C.free)
}

#output to the console
print("Windows-View \nCopyright (c) 2024 Felix Bogomolov \nGitHub: https://github.com/FeliBog/Windows-View/tree/main-latest \n \nOS:")
print("    OS:", all["OSname"], all["OSrelease"], f"({all['OS Version']})")
print(f"    {all['OSname']} Product Key:", all["OS Product Key"])
print("Users:")
print("    This User:", all["User"])
print("Connections:")
print("    Local IP:", all["Local IP"])
print("    Public IP:", all["Public IP"])
print("    Host:", all["Host"])
print("    MAC:", all["MAC"])
print("    VPN:", all["VPN"])
print("    Proxy:", all["Proxy"])
print("Public IP Info:")
print("    Country:", all["Country"])
print("    Region:", all["Region"])
print("    City:", all["City"])
print("    Timezone:", all["Timezone"])
print("    Hostname:", all["Hostname"])
print("Processor:")
print("    Processor:", all["Processor"])
print("    Architectre:", all["Architecture"])
print("    Processor frequency:")
print("        Current:", all["Current Processor Frequency"])
print("        Min:", all["Min Processor Frequency"])
print("        Max:", all["Max Processor Frequency"])
print("BIOS:")
print("    BIOS SerialNumber:", all["BIOS SerialNumber"])
print("    BIOS Manufacturer:", all["BIOS Manufacturer"])
print("    BIOS Version:", all["BIOS Version"])
print("System:")
print("    System Directory:", all["System Directory"])
print("    System Disk:")
print("        Total:", all["System Disk Total"])
print("        Used:", all["System Disk Used"])
print("        Free:", all["System Disk Free"])
