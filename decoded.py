import subprocess
import platform as plat
from pystyle import Center, Anime, Colors, Colorate, System,Write
import time
import sys
import os


BL   = '\033[01;30m'
R     = '\033[01;31m'
G   = '\033[01;32m'
Y  = '\033[01;33m'
B    = '\033[01;34m'
M = '\033[01;35m'
C    = '\033[01;36m'
W   = '\033[01;37m'
E   = '\033[01;39m'

def update():
    print(R+"Updataing WIFI-Hack....."+E)
    os.system("python update.py")

def get_password():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    print("{:<40} | {:<}".format(B+"\n   Wi-Fi Name"+E,M+"    "+"Password"))
    print(C+"-----------------------------------------\n")
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            i='\033[01;31m'+i
            try:
                if results == " ":print("No Password")
                print("{:<35} \033[01;34m>  {:<}".format('\n'+i,'\033[01;33m'+ results[0]+E))
            except IndexError:
                print (R+i, "")
        except subprocess.CalledProcessError:
            print (B+i,R+ "ENCODING ERROR")
    input('')
            
get_os=plat.system()
System.Clear()
System.Title("EthicalHackingLK")
System.Size(140, 40)
 


main = r"""                                                                      
               /                                                      
    /  /#(#%@@@@@                                                     
,*@@/@@ @@ . ,/**@/                               ,* /.*  ,%* * *     
 %/@@%@@ @@   , &@@/            ,@@@@@            *# #@,  ./*(/#(#,   
  @ @@@@@**@@@@@@.*          %@/*****//(@(        %%   #(((           
   #/.,,                    @/**, @@ *(//(@       &@                  
    .                      @**,@/    .//@/(@      .#   (        .     
                         .@** .   ///////&/(@         ,,/    /.@*(    
     (                   @**. *//////////#@//@                        
                        @**///////////////////@                       
                        @*/////@////(///@/////@                       
                      @@@@//////@@@@@@@@/////@@@@                     
                    @(////&///////&@@@//////@////#@                   
                  @@///@@%///////////////#///// /((@@                 
                 @#///////@@////////////////  /(((((&@                
                   &@@@#/////////////////////((%@@@&                  
                           #@@@@&%#(((%@@@@(                          
                                                                      
                                                                      
                                                                      
                           ##/        ###  ###                        
                           ##/        ### ###                         
                           ##/        ##### (                         
                           ##/####    ###  ###                        
                                                                      
                                                                      
"""[1:]

menu_note="""

 ██╗       ██╗██╗███████╗██╗      ██╗  ██╗ █████╗  █████╗ ██╗  ██╗
 ██║  ██╗  ██║██║██╔════╝██║      ██║  ██║██╔══██╗██╔══██╗██║ ██╔╝
 ╚██╗████╗██╔╝██║█████╗  ██║█████╗███████║███████║██║  ╚═╝█████═╝ 
  ████╔═████║ ██║██╔══╝  ██║╚════╝██╔══██║██╔══██║██║  ██╗██╔═██╗ 
  ╚██╔╝ ╚██╔╝ ██║██║     ██║      ██║  ██║██║  ██║╚█████╔╝██║ ╚██╗
   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝

"""
make="""
─══════════════════════════════ቐቐ════════════════════════════════════─
                    Tool By Ethical Hacking LK
─══════════════════════════════ቐቐ════════════════════════════════════─

"""
menuu="""
\033[01;39m[\033[01;31m01\033[01;39m]\033[01;32m Get Save Wifi Password                            \033[01;39m[\033[01;31m02\033[01;39m]\033[01;32m Auther
\033[01;39m[\033[01;31m03\033[01;39m]\033[01;32m Update                                            \033[01;39m[\033[01;31m04\033[01;39m]\033[01;32m Exit\033[01;39m"""

auther_note="""
    Auther : Ethical Hacking LK
    About : Save Wifi Password Show Tool
    
    """[1:]

def auther():
    Write.Print(auther_note,Colors.red_to_yellow)
    return menu()


def menu():
    os.system("cls")
    print(Colorate.Horizontal(Colors.yellow_to_green, menu_note, 1))
    print(Colorate.Horizontal(Colors.red_to_blue, make, 1))
    print(menuu)
    lk=int(input(W+"\n\n[\033[01;31m+\033[39m]\033[33m WIFI-HACK"+E+" >>  "))
    if(lk==1):
        get_password() 
    elif(lk==2):
        auther()
    elif(lk==3):
        update()
    elif(lk==4):
        Write.Print("Exiting......",Colors.red_to_purple, interval=0.09)
        os.system("cls")
        Write.Print("Exiting......",Colors.red_to_purple, interval=0.09)
        os.system("cls")
        Write.Print("Exiting......",Colors.red_to_purple, interval=0.09)
        os.system("cls")
        Write.Print("Exiting......",Colors.red_to_purple, interval=0.09)
        os.system("cls")
        exit
    else:
        print(R+"Worng Input"+E)
        time.sleep(3)
        return menu()
    
    


if __name__=="__main__":
    if get_os == "Windows":
        None
    else :
        print(R+"\nThis Tool is Not Support",get_os+W)
        time.sleep(3)
        sys.exit()
    Anime.Fade(Center.Center(main), Colors.blue_to_white, Colorate.Vertical, enter=True)
    menu()
    
