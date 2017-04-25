"""
this module demonstrates how to fetch the system info like, OS version,
hard disks attached to it and also BIOS version.
"""
import paramiko
import string
from collections import namedtuple

Server = namedtuple("Server", "ipaddr username passwd root_passwd")

ip_list = [
    Server("192.168.11.11", "radisys", "radisys", "radisys"),
    Server("192.168.11.118", "radisys", "radisys", "radisys")
]

#using this list to find out the version
os_check_list = ["DISTRIB_DESCRIPTION"]

#list comprises of hard disk names, like sda, sdb...sds
hard_disks = [ 'sd{}'.format(i) for i in string.ascii_lowercase[:19]]

HEADER = """
             ************************************************************

              IP ADDR = {}                SYSTEM INFO                           

             ************************************************************* 
         """
#executes the command and returns the output
def execute_command(command, ip):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip.ipaddr, username=ip.username, password=ip.passwd)

    stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
    stdin.write(ip.root_passwd +"\n")
    
    return stdout.readlines()

#for fetching OS version
def check_os(output):

    for line in output:
       if any(x in line for x in os_check_list):
           print(" Operating System is {}" .format(line.split("=")[1]))

#for fetching disk information
def disk_status(output):
    for line in output:
        if any(x in line for x in hard_disks):
            print(line)
        elif "command not found" in line:
            print("udisksctl not installed on target server")

#for fetching BIOS version
def bios_version(output):
    for line in output:
        if "Version" in line:
            print(line)
        elif "command not found" in line:
            print("dmidecode not installed on target server")

if __name__ == "__main__":
     for ip in ip_list:
         print(HEADER.format(ip.ipaddr))
         check_os(execute_command("cat /etc/*release", ip))
         disk_status(execute_command("sudo -k udisksctl status", ip))
         bios_version(execute_command("sudo dmidecode -t 0 | grep -i version", ip))
