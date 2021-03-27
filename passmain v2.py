import re, math
import os
from time import sleep
from term_color import prPurple, prRed, prYellow, prGreen, prLightGray, prLightPurple, clear, prCyan, prRedE, prGreenE

"""
#TGREEN = '\033[32m'  # Green Text
#TRED   = '\31[m'     # Red Text
#TYLLW = '\033[33m'  # Yellow Text
"""
"""
Entropy
Type	                Pool of Characters Possible
Lowercase                            26
Lower & Upper Case                   52
Alphanumeric                         36
Alphanumeric & Upper Case            62
Common ASCII Characters              30
E=log2(R)^L
E=Entropy
R=Pool of chars
R^L=Possible combinations
log2(R^L) = Entropy
< 28 bits = Very Weak; might keep out family members
28 - 35 bits = Weak; should keep out most people, often good for desktop login passwords
36 - 59 bits = Reasonable; fairly secure passwords for network and company passwords
60 - 127 bits = Strong; can be good for guarding financial information
128+ bits = Very Strong; often overkill
"""
CBOLD = '\33[1m'
ENDC = '\033[m'      # Reset
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
UNDERLINE = '\033[4m'
CSELECTED = '\33[7m'
CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'

# global g_uplength
# global g_lowlength
# global g_pwdlength
# global g_numlength
# global g_nonalphas
# global g_special
# global g_poolchar

# def prLightPurple(skk):
#     print("\033[94m {}\033[00m" .format(skk))


# def prPurple(skk):
#     print("\033[95m {}\033[00m" .format(skk))


# def prCyan(skk):
#     print("\033[96m {}\033[00m" .format(skk))


# def prLightGray(skk):
#     print("\033[97m {}\033[00m" .format(skk))


# def prRed(skk): print\
#     ("\033[91m {}\033[00m" .format(skk))


# def prGreen(skk):
#     print("\033[92m {}\033[00m" .format(skk))


# def prYellow(skk):
#     print("\033[93m {}\033[00m" .format(skk))

# prCyan("Hello World, ")
# print (TGREEN + "Das ist es!" , ENDC)


def check_entropy(password):
    poolchar = 0
    entropy = 0.0
    pwdlength = 0
    pwdlength =  len(password)

    if pwdlength == 0:
        prRed("\u274c Password is BLANK" + ENDC)
        exit(0)
    elif pwdlength < 8:
        prRed("\u274c Password is less than 8 characters" + ENDC)
    else:
        prGreen("\u2705 You password is greater or equal to 8 characters" + ENDC)

    uplength = 0
    uplength = len(re.findall(r'[A-Z]', password))
    # print(uplength)
    # print(str(uplength.count())
    # print(str(len(re.findall(r'[A-Z]',password))))
    if uplength >= 1:
        prGreen("\u2705 You have {" + str(uplength) + "} uppercase characters in your password" + ENDC)
    else:
        prRed("\u274c You do not have any uppercase characters")

    lowlength = 0
    lowlength = len(re.findall(r'[a-z]', password))

    if lowlength > 1:
        prGreen("\u2705 You have {" + str(lowlength) + "} lower characters in your password" + ENDC)
    else:
        prRed("\u274c You do not have any lowercase characters" + ENDC)

    numlength = 0
    numlength = len(re.findall(r'[0-9]', password))

    if numlength > 1:
        prGreen("\u2705 You have {" + str(numlength) + "} numerical characters in your password" + ENDC)
    else:
        prRed("\u274c You do not have any numerical characters" + ENDC)

    regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')

    if regex.search(password) == None:
        prRed("\u274c No special characters found")
    else:
        prGreen("\u2705 Special characters found!")
    
    specialc = 0
    for i in range(len(password)):
        if (password[i].isalpha()):
            # alphabets = alphabets + 1
            pass
        elif (password[i].isdigit()):
            # digits = digits + 1
            pass
        else:
            specialc += 1

    if specialc > 0:
        prGreen("[+] # of special characters : " + str(specialc))
    else:
        prRed("\u274c No special characters found.")
        
    if uplength > 0:
        poolchar += uplength

    if lowlength > 0:
        poolchar += lowlength
    
    if specialc > 0:
        poolchar += specialc

    if numlength > 0:
        poolchar += numlength
    
    
    prYellow("Pool of password is :" + str(poolchar))
    prYellow("Pass length: " + str(pwdlength))
    entropy = math.log2(poolchar ** pwdlength)

    prLightGray("Entropy of password is : " + str(round(entropy)))

    if entropy < 28:
        prRed("\u274c Password is very very weak. May keep you safe from friend and family only. \n Suitable for non-critical applications")
    elif entropy >= 28 and entropy <= 35:
        prRed("\u274c Very weak password. May be suitable for login into desktop/laptor or phone.")
    elif entropy >= 35 and entropy <= 59:
        prCyan("\u2705 Reasonably strong password. Can be used for company / network apps or systems")
    elif entropy >= 60 and entropy <= 127:
        prPurple("\u2705 \u2705 Very STRONG password. Can you be used to safegaurd information very critical like financial, health data etc.")
    elif entropy >= 128:
        prGreen("\u2705 \u2705 \u2705 This is the STRONGEST possible password you could have. It won't be cracked easily.")
    else:
        prLightGray("Entropy is invalid")
    
    

# def clear():

#     osname = os.name
#     # for windows 
#     if osname == 'nt': 
#         _ = os.system('cls') 
  
#     # for mac and linux(here, os.name is 'posix') 
#     else: 
#         _ = os.system('clear') 
  

# sleep for 2 seconds after printing output 
sleep(2) 


def main():
    ans = ""
    clear()

    while True:

        # prGreen("(_____ \                                    | |  (_______)       _                            (_______| |               | |                ")
        # prYellow(" _____) _____  ___  ___ _ _ _  ___   ____ __| |   _____   ____ _| |_  ____ ___  ____  _   _    _      | |__  _____  ____| |  _ _____  ____ ")
        # prRed("|  ____(____ |/___)/___| | | |/ _ \ / ___/ _  |  |  ___) |  _ (_   _)/ ___/ _ \|  _ \| | | |  | |     |  _ \| ___ |/ ___| |_/ | ___ |/ ___)")
        # prCyan("| |    / ___ |___ |___ | | | | |_| | |  ( (_| |  | |_____| | | || |_| |  | |_| | |_| | |_| |  | |_____| | | | ____( (___|  _ (| ____| |    ")
        # prPurple("|_|    \_____(___/(___/ \___/ \___/|_|   \____|  |_______|_| |_| \__|_|   \___/|  __/ \__  |   \______|_| |_|_____)\____|_| \_|_____|_|    ")
        # prLightPurple("(c) Shuvro Basu, 2021.                                                         | _ | (____ / ")
        # prLightGray("<<==========================================================================================================================================>>")
        print(CBOLD)
        prGreen(" ;-.                              .   ,--.     .                      ,-. .           ,")    
        prYellow(" |  )                             |   |        |                     /    |           |")
        prRed(" |-'  ,-: ,-. ,-. , , , ,-. ;-. ,-|   |-   ;-. |-  ;-. ,-. ;-. . .   |    |-. ,-. ,-. | , ,-. ;-. ")
        prCyan(" |    | | `-. `-. |/|/  | | |   | |   |    | | |   |   | | | | | |   \    | | |-' |   |<  |-' |")
        prPurple(" '    `-` `-' `-' ' '   `-' '   `-'   `--' ' ' `-' '   `-' |-' `-|    `-' ' ' `-' `-' ' ` `-' '") 
        prLightPurple("                                                           '   `-'                              ")        
        print(CBOLD + CITALIC + " (c) Shuvro Basu, 2021 " + ENDC)  
        prLightGray("<<==================================================================================================>>" + ENDC) 


        password = input(" Enter your password : ")
       
        if password == "":
            prRedE(" Quitting..." + ENDC)
            break
        
        prYellow("Checking password... ->" + password)
        check_entropy(password)

        prCyan("Password check done.")
        prPurple("Thank You For Using The Password Entropy Checker Tool.")

        sleep(3)
        #clear()
        ans = input("Continue ? Y/N) ")
        
        if ans == "N" or ans == "n" or ans =="NO" or ans == "no":
            break

if __name__ == '__main__':
    main()

