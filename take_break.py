"""
take break of 2 minutes for every 20 minutes of work and a break of 10 minutes for every one hour.
"""
import time
import subprocess

TIME = 20
BREAK1 = 2
BREAK2 = 10
COUNT = 3

def verify_pkg():

    #check if package is installed on the server
    check_pkg = subprocess.Popen(["apt", "-qq", "list", "gnome-screensaver"], stdout=subprocess.PIPE)
    pkg_avil = "installed" in check_pkg.communicate()[0]

    #if not installed, install the package
    if not pkg_avil:

        install_pkg = subprocess.Popen(["apt-get", "install", "-y", "gnome-screensaver"], stdout=subprocess.PIPE)
        check_pkg = "Setting up gnome-screensaver"    
        if check_pkg in install_pkg.communicate()[0]:
            return True

    elif pkg_avil:
        return True

def start_timer(timer):
    while timer:
        print(time.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(60)
        timer -= 1
    return 0

def take_break(break_time):
    if verify_pkg(): 

        print("TAKE A BREAK OF {} minutes".format(break_time)) 

        #lock the screen 
        lock = subprocess.call(["/usr/bin/gnome-screensaver-command", "-l"])
        start_timer(break_time)        

        #unlock the screen
        unlock = subprocess.call(["/usr/bin/gnome-screensaver-command", "-d"])


if __name__ == "__main__":

    count = 1 
    while True:
        print("20 minute timer started with break {} minutes".format(BREAK1))
        start_timer(TIME)

        #count of 3 will make an hour. i.e 20*3=60 min
        if count == COUNT:
            print("HOUR timer started with break {} minutes".format(BREAK2))
            take_break(BREAK2)
            #intialize the count to 1 after the hourly break
            count = 1
        else:

            take_break(BREAK1)
            count += 1
