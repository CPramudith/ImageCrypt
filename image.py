import pyfiglet, os, base64
from datetime import *
from pathlib import Path
from cryptography.fernet import Fernet
import time as T

i = 0
rec = "bkjwgdu24357485dkjtdfgytytfk5l" #Used to identify when the added code starts in the file.
erec = rec.encode("utf-8")
now=datetime.now()
dt=now.strftime("%b-%d-%Y at %H:%M:%S")
head = pyfiglet.figlet_format("Image.Py")
home = str(Path.home())

os.system("clear")
print(head)
print("Author  : CPramudith")
print("Executed on  : ",dt)
print("================================================\n")

option = input(str("Select the option [write/read] : "))

def write():
    print("\nSelect the image file : ")
    file = input(home+"\\")
    ffile = home+"\\"+file

    with open(ffile, "rb")as f:
        stuff = [line.rstrip() for line in f]

    if erec in stuff:
        print("\nFile already used. Use a new file.")
        EndWithAnError #Used to generate an error and exit

    key = Fernet.generate_key()
    ekey = key.decode("utf-8")

    os.system("echo  >> "+ffile)
    os.system("echo "+rec+" >> "+ffile)
    os.system("echo "+ekey+" >> "+ffile)

    ps = input("\nInput a password to secure the file : ")
    print("Type your text here. Type 'exit()' to leave the editor")
    while i == 0:
        text = input(">> ")
        if text == "exit()":
            eps = Fernet(key).encrypt(ps.encode("utf-8"))
            deps = eps.decode("utf-8")
            os.system("echo "+deps+" >> "+ffile)
            break
        else:
            etext = Fernet(key).encrypt(text.encode("utf-8"))
            detext = etext.decode("utf-8")
            os.system("echo "+detext+" >> "+ffile)
            continue
    print("\n[+]Text embeded to the file")

def read():
    print("\nSelect the image file : ")
    file = input(home+"\\")
    ffile = home+"\\"+file

    with open(ffile, "rb")as f:
        stuff = [line.rstrip() for line in f]

    for x in stuff:
        if x == erec :
            break
        else :
            for x in stuff:
                stuff.pop(0)

    for x in stuff :
        stuff.pop(0)
        break

    ps = input("\n[+]Enter the password : ")
    for x in stuff :
        key = x
        stuff.pop(0)
        break

    c = len(stuff)
    d = c -1

    for x in stuff:
        cat = stuff[d]
        stuff.pop(d)
        break
    
    text = []
    pas = Fernet(key).decrypt(cat)
    tpas = pas.decode("utf-8")
    if tpas == ps :
        print("[+]Password Accepted\n")
        for x in stuff:
            txt = Fernet(key).decrypt(x)
            dtxt = txt.decode("utf-8")
            text.append(dtxt)
            continue
        print("[+]Embeded text identified :\n")
        for x in text:
            print(">>> "+x)
    else :
        print("[+]Invalid Password")


if option == "write" :
    try :
        write()
    except :
        print("\n[+]Cannot edit this file :(")
if option == "read" :
    try :
        read()
    except :
        print("\n[+]Cannot read this file. Looks like a corrupted file :(")
        
print("\n=================================================")
print("Press Enter to exit...")
input()
