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

tn.write("conf t\n")
tn.write("hostname SW1\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
