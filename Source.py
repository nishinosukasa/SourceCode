## Source Code
# TakeScript Deface In Sites 
# Import Folder Script In Android
# mv Codename.html /storage/emulated/0/ 
# Check Folder Script TakeScript In Memory Internal Name Files Codename.html
# Special Thanks To :* TheChoyon
import urllib
import os
import sys
import time
import random

#Clear
os.system ('clear')
#Wallpaper
print ('''
\033[91m
  _______                                         _______              __         
 |   _   | .-----. .--.--. .----. .----. .-----. |   _   | .-----. .--|  | .-----.
 |   1___| |  _  | |  |  | |   _| |  __| |  -__| |.  1___| |  _  | |  _  | |  -__|
 |____   | |_____| |_____| |__|   |____| |_____| |.  |___  |_____| |_____| |_____|
 |:  1   |                                       |:  1   |                        
 |::.. . |                                       |::.. . |                        
 `-------'                                       `-------'                      
                                                                                
                   \033[92m[\033[91m127.0.0.1\033[92m]\033[0m|_|\033[92m[\033[91m127.217.21.78\033[92m]
                       \033[92m[\033[91mCodec By Codename\033[92m]
''')
target = raw_input('http://: ')
try:
    openurl = urllib.urlopen(target)
    read = openurl.read()
except IOError:
    print '\033[91mCheck Connection Internet. With Protocol http dont https'
    input("press enter to exit ...")
print '\033[92mSource Code Successful Save...'
file_save = open('codename.html', 'w')
file_save.write(read)
print '\033[93mSource Code Save as codename.html'
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)
mengetik('^_^ Done TakeScript...')
key = raw_input("ENTER To exit")
