import os

raw = input("Enter the Service name: ")
s='systemctl is-active '  + raww
status = os.system(s)
print(status) 
