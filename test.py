import getpass
import sys
import telnetlib

HOST = "192.168.122.100"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")
'''
tn.write("enable\n")
password1 = getpass.getpass()
if password1:
    tn.read_until("Password: ")
    tn.write(password1 + "\n")
'''
tn.write("show run\n")
tn.write("exit\n")

print tn.read_all()
