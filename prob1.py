#Quiz 3 lab1
#Anne-Marie SMith
#do 2 functions 
from datetime import datetime
import time

def filename(): # get the timestamp and make a name for the file
    ts = time.time()
    value = "parsed_log"+ str(ts)+".txt"
    return value
    
def closing(f, e): # close all files opened
    f.close()
    e.close()
    

    
logList = ["chrome.log", "firefox.log", "gedit.log", "gimp.log", "pycharm.log"]
logLevel = input("Enter Log Level: ['Debug', 'Fatal', 'Critical', 'Warn', 'Info']: ")
username = input("Enter user from the list: ['root', 'ubuntu', 'wheel', 'vbox', 'syslog', 'arty']: ")
name = filename()  
e = open(name, "a")

#open all logs and read them, write to the screen only the loglevel and username chose by the user
for x in logList:
    f = open(x, "r")
    names = str(x)+"\n"
    e.write(names)
    print(x)
    for x in f:
        if username in x and logLevel in x:
            #splitting the lines to only the content needed(log level, username, datetime, error message)
            a = x.split(":")[-1][:-1] #log level
            b = x.split(":")[1] #username
            first = x.split(":")[0]
            firstHalf = int(first.split(".")[0]) 
            second = ":"+ first.split(".")[1] #seconds
            c = datetime.fromtimestamp(firstHalf) #datetime
            d = x.split(":")[-2] #error message
            half = ' '+ str(a) + str(b)
            andhalf = str(c) + str(second) + str(d) 
            final = str(half) + str(andhalf) + "\n"
            #write only the content sellected to the file
            e.write(final)
            #also print it to the screen (optional)
            print(a, b, c, second, d)
            
closing(f, e)



