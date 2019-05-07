# Importing necessary libraries
import netmiko
import getpass

#Opening text files, includes list of commands and devices 

f = open ("a", "r")
devices = f.read().splitlines()
f.close()
h = open ("c", "r")
commands = h.read().splitlines()

ssh_user = input("Enter username: ")
ssh_pw = input('SSH Password: ')

for device in devices:
    try:
        ssh_session = netmiko.ConnectHandler(device_type='cisco_ios', host=device, username=ssh_user, password=ssh_pw)
        print ("Login to " + devices + " Successful")
        for command in commands:
            print(ssh_session.send_command(command) + "\n")
        ssh_session.disconnect()
        print("Successfully disconnected from " + device + "\n")

    except (netmiko.ssh_exception.NetMikoTimeoutException,
            netmiko.ssh_exception.NetMikoAuthenticationException,
            paramiko.ssh_exception.SSHException) as s_error:
        print(s_error)
