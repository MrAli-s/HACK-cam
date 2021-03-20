from time import sleep as timeout

import time

import sys

import os

def t(nn,t_):

        print(t_)

        print('')

        for i in range(0,33):

                i+=1

                txt='\033[1;32m▒'*41

                f=i*'\033[1;31m▊'

                tt=i*3+1

                ttt=str(tt)

                print(txt+'┊'+ttt+'%',end='\r')

                print('MrAli  ┊{}'.format(f),end='\r')

                time.sleep(nn)

        print('')

t(0.10,'\n\t   \033[1;35m[ ..... PLEASE WAIT .... ]')

print (' ')

time.sleep(0.2)
