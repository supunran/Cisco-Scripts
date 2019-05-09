# Cisco-Scripts
Using cisco_exec_commands.py file
You can use this script to run exec commands (no config line commands) in multiple devices
Create a plain file named "a" with the list of devices you need to run the commands
Create a plain file named "c" with the list of commands
Then execute the script - python cisco_exec_commands.py

eg:
file "a" 
Router01
Router02

file "c"
show ip interface brief
show version

Using the cisco_config.py file
You can use this script to run configuration commands in a cisco device (you will be landed on the config mode on the device)
Create a plain file named "a" with the list of devices you need to run the commands
Create a plain file named "c" with the list of commands
Then execute the script - python cisco_config.py

eg:
file "a" 
Router01
Router02


file "c"
hostname test-router
end
wr

