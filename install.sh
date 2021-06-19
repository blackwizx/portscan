#! /usr/bin/bash

#check root

# color codes
N="\033[0m"    # Reset
B="\033[1m"    # Bold
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
M="\033[1;35m" # Magenta
C="\033[1;36m" # Cyan


if [ "$EUID" -ne 0 ]

    then echo -e "$Y Please run as root & try Again$Y"
    echo -e "$R Exiting install.sh $R"
    exit
    
    else
    echo -e "$C root login detected... $C"
    sleep 2
    echo -e "$M script  can proceed with installation $M"
    sleep 1
fi

#install python dependencies

apt-get update && apt-get install pip
echo -e "$C pip install succesfully $C "
pip install plyer;pip install colr
echo -e "\n"
echo -e "$C plyer install succesfuly$C"
sleep 2
echo -e "$C colr install succesfully$C"
clear
cp portscan.py /usr/bin/portscan
chmod 755 /usr/bin/portscan


echo -e " $CB INSTALATION HAS BEEN DONE $CB" 
sleep 4
echo -e "\n"
echo -e "$YB *enter 'portscan -h' for more info $YB"
sleep 3
clear -x























