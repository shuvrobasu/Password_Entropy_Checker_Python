import os
from time import sleep

def prRedE(skk):
    print("\u274c \033[91m {}\033[00m" .format(skk))

def prGreenE(skk):
    print("\u2705 \033[92m {}\033[00m" .format(skk))

def prLightPurple(skk):
    print("\033[36m {}\033[00m" .format(skk)) #94 to 36


def prPurple(skk):
    print("\033[95m {}\033[00m" .format(skk))


def prCyan(skk):
    print("\033[96m {}\033[00m" .format(skk))


def prLightGray(skk):
    print("\033[97m {}\033[00m" .format(skk))


def prRed(skk): print\
    ("\033[91m {}\033[00m" .format(skk))


def prGreen(skk):
    print("\033[92m {}\033[00m" .format(skk))


def prYellow(skk):
    print("\033[93m {}\033[00m" .format(skk))

def clear():

    osname = os.name
    # for windows 
    if osname == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 
  

# sleep for 2 seconds after printing output 
sleep(2) 