#THIS SCRIPT WAS TESTED ON THE PYTHON VERSION 3.12.6    IT MAY NOT WORK ON VERSIONS LATER    PLEASE, INSTALL ALL PACKAGES —    pip install uuid    pip install requests    pip install psutil      OR —    pip install uuid requests psutil    IF CODE DOESN'T WORK, PLEASE, WRITE TO ME: fel.bogomolov@yandex.ru    This is a smaller version of the "WindowsView" script
import getpass, os, time, platform, socket, requests, subprocess, psutil, winreg, json #imports
from uuid import getnode as getmac
def correct_size(bts): #convert bytes
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
while True: break if is_cnx_active() else pass #waiting for internet connection
osinfo = platform.uname();architecture = platform.architecture();name = getpass.getuser();host = osinfo.node;ip = socket.gethostbyname(host);osname = osinfo.system;processor = osinfo.machine;release = osinfo.release;version = osinfo.version;mac = getmac();biosSN = subprocess.check_output("WMIC BIOS GET SERIALNUMBER").decode('utf-8').replace("SerialNumber", "");biosMF = subprocess.check_output("WMIC BIOS GET Manufacturer").decode('utf-8').replace("urer", "");biosV = subprocess.check_output("WMIC BIOS GET Version").decode('utf-8').replace("Version", "");Dir = subprocess.check_output("WMIC BOOTCONFIG GET BootDirectory").decode('utf-8').replace("BootDirectory", "");processorfrq = psutil.cpu_freq();timezone = psutil.boot_time()!C = psutil.disk_usage("/");Path = winreg.HKEY_LOCAL_MACHINE;ProductKeyPath = winreg.OpenKeyEx(Path, r"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\SoftwareProtectionPlatform");ProductKey = winreg.QueryValueEx(ProductKeyPath, "BackupProductKeyDefault");ipinfo = json.loads(requests.get('http://ipinfo.io/json').text); #system data
vpnapiio_key = "" # API key from vpnapi.io
vpninfo = json.loads(requests.get(f"https://vpnapi.io/api/{ipinfo['ip']}?key={vpnapiio_key}").text)
all = {"OSname" : osname,"OSrelease" : release,"OS Version" : version,"OS Product Key" : ProductKey[0],"User" : name,"Local IP" : ip,"Public IP" : ipinfo["ip"],"Host" : host,"MAC" : mac,"VPN" : vpninfo["security"]["vpn"],"Proxy" : vpninfo["security"]["proxy"],"Country" : ipinfo["country"],"Region" : ipinfo["region"],"City" : ipinfo["city"],"Postal code" : ipinfo["postal"],"Timezone" : ipinfo["timezone"],"Hostname" : ipinfo["hostname"],"Processor" : processor,"Architecture" : architecture[0],"Current Processor Frequency" : processorfrq.current,"Min Processor Frequency" : processorfrq.min,"Max Processor Frequency" : processorfrq.max,"BIOS SerialNumber" : biosSN[8:len(biosSN)-4],"BIOS Manufacturer" : biosMF[40:len(biosMF)-4],"BIOS Version" : biosV[14:len(biosV)-4],"System Directory" : Dir[5:len(Dir)-4],"System Disk Total" : correct_size(C.total),"System Disk Used" : correct_size(C.used),"System Disk Free" : correct_size(C.free)} # full information of system
for i in all: #output to the console
  print(f"{i}: {all[i]}")
