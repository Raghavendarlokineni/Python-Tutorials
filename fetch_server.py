import paramiko

#ip_list input values : ["IP_ADDR", "USERNAME", "PASSWD", "ROOT_PASSWD"]
ip_list = [
    ["192.168.11.44", "root", "radisys", "radisys"],
    ["192.168.11.8", "root", "root123", "radisys"],
    ["192.168.11.30", "root", "root123", "radisys"],
    ["192.168.11.6", "radisys", "radisys", "radisys"]
]
os_check_list = ["DISTRIB_DESCRIPTION"]
hard_disks = [
             'sda', 'sdb', 'sdc', 'sdd', 'sde', 'sdf', 'sdg',
             'sdh', 'sdi', 'sdj', 'sdk', 'sdl', 'sdm', 'sdn',
             'sdo', 'sdp', 'sdq', 'sdr', 'sds'
             ]
os = None

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for ip in ip_list:
    ssh.connect(ip[0], username = ip[1], password = ip[2])

    print("\n \n   ************************************************************ \
           \n   IP ADDR = {}                SYSTEM INFO                           \
          \n  ******************************************************************". format(ip[0]))
    stdin, stdout, stderr = ssh.exec_command("cat /etc/*release")
    stdin.write(ip[3]+"\n")
    for line in stdout.readlines():
       if any(x in line for x in os_check_list):
           os_dist = line.split("=")
           os = os_dist[1]
           print(" Operating System is {}" .format(os))
    if not os:
           stdin, stdout, stderr = ssh.exec_command("cat /etc/system-release")
           for line in stdout.readlines():
               os = line
               print(" Operating System is {}" .format(os))

    os = None

    stdin, stdout, stderr = ssh.exec_command("sudo -k udisksctl status", get_pty = True)
    stdin.write(ip[3]+"\n")
    for line in stdout.readlines():
        if any(x in line for x in hard_disks):
            print(line)
        elif "command not found" in line:
            print("udisksctl not installed on target server")

    stdin, stdout, stderr = ssh.exec_command("sudo dmidecode -t 0 | grep -i version", get_pty = True)
    stdin.write(ip[3]+"\n")
    for line in stdout.readlines():
        if "Version" in line:
            print(line)
        elif "command not found" in line:
            print("dmidecode not installed on target server")
