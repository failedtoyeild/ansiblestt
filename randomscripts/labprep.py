#!/usr/bin/env python
from netmiko import ConnectHandler

deviceCount = int(raw_input("How many devices would you like configured? "))
startingPort = int(raw_input("What is the starting telnet port? "))
startingIP = raw_input("What is the starting management IP? ")
commandSet = ['username admin priv 15 secret cisco', 'ip domain-name lyons103.lab', 'crypto key generate rsa mod 1024', 'ip route 10.242.2.0 255.255.255.0 10.0.0.1' ,
 'line vty 0 4', 'transport input ssh', 'login local', 'int e0/3', 'no sw', 'temp', 'no shut']


for x in range(0, deviceCount):
	telnet_device = {
		'device_type': 'cisco_ios_telnet',
		'ip': '10.0.0.100',
		'port': str((startingPort + x))
	}
	managementIP = startingIP.split(".")
	managementIP[3] = str(int(managementIP[3]) + x)
	managementIP = ".".join(managementIP)
	commandSet[9] = 'ip add ' + managementIP + " 255.255.255.0"
	print '-' * 50
	print "Configuring Device #" + str(x) + " with " + commandSet[9]
	print "Connecting to device ....."
	device = ConnectHandler(**telnet_device)
	print "Connected"
	device.enable()
	print "Entering Global Configuration Mode ....."
	device.config_mode()
	print "Sending Configuration Set ....."
	print device.send_config_set(commandSet)
	device.exit_config_mode()
	device.send_command('wr')
	print "Device Configured and Configuration saved/n/n/n"



