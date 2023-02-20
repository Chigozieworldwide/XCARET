#coding=utf-8
import os, sys, platform
try:
    import bs4
except:
    os.system('pip install bs4')
os.system('xdg-open https://chat.whatsapp.com/F9uCvPXPJml891R0KETB6y')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf XCARET.so XCARET32.so')
except:
    pass
os.system('rm -rf XCARET.so XCARET32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('XCARET.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/sxs/blob/main/XCARET.cpython-311.so?raw=true -o XCARET.so') 
        __import__("XCARET").keyx()
    else:
        __import__("XCARET").keyx()

elif bit == '32bit':
    if not os.path.isfile('XCARET32.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/sxs/blob/main/XCARET32.cpython-311.so?raw=true -o XCARET32.so') 
        __import__("XCARET32").keyx()
    else:
        __import__("XCARET32").keyx()
