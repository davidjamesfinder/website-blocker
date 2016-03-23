import sys
import time
from gi.repository import Notify
import timeConvert.py
import os
import ast
import threading
from gi.repository import AppIndicator3 as Appindicator
from gi.repository import Gtk
#commands
    #block <URL>
    #block <URL> <MIN TIME>
    #multi-block <URL> <URL> ...
    #multi-block <URL> <URL> ... <MIN TIME>

    #block-file <FILE-NAME>
    #block-file <FILE-NAME> <MIN Time>

    #block-set <TEMPLATE NAME>
    #block-set <TEMPLATE NAME>
    #block-set-create <TEMPLATE NAME>
    #block-set-destroy <TEMPLATE NAME>

    #block-template <TEMPLATE NAME>
    #block-template-create <TEMPLATE NAME>
    #block-template-destroy <TEMPLATE NAME>

    #unblock <URL>
    #unblock-all

    #refresh-blocks

    #list-blocks
    #help

#flags(Go at the end):
    #-a: Sets an alert to go off at that time.
        #Only applies to Block, multiblock, block-until, 

#formatting: 

#Times are all done in the format of #d#h#m


#Alerts: Run as their own thread

#Files:
    #locktiming


#print(str(sys.argv[0]))
#print(len(sys.argv))
if(len(sys.argv)=1):
    print("No arguments given!\n")
    print("Run with the help argument to see options\n")
else:
    length=len(sys.argv)
    command=sys.argv[1]
    flagArg=(sys.argv[length-1]=="-a")

    if(command=="block"):
        #If command is block, 3rd arg is url, 4th argument is time if not the time flag.
        URL=sys.argv[2]
        if length-flagarg>4:
            print("Uh oh, too many arguments")
        else:
            if(length-flagarg=3):#We don't have a time.
                block(url,"0d1h0m")
            if(length-flagarg=4):#We have a time.
                block(URL,sys.argv[3])
            if(flagarg): #Flag arg, but not 
                unlock_alert(URL,timeTIME)

    if(command=="block-file"):
        filePath=sys.argv[2] #validity check on file name
        if os.path.exists(filePath):
            
            if length-flagarg>4:
                print("That's not a valid argument list")
            else:
                if(length-flagarg=3):#We don't have a time.
                    file_block(filePath,"0d1h0m")
                if(length-flagarg=4):#We have a time.
                    file_block(filePath,sys.argv[3])

        else:
            print("That's not a valid location!"))
        


    if(command=="unblock"):

    if(command=="unblock-all"):

    if(command=="list-blocks"):
    
    if(command=="refresh-blocks")

    if(command=="help"):
        help()


def unlock_alert(URL, TIME): #Accepts a URL and a UNIX time
    alert_thread=threading.Thread(target=unlock_alert_thread,args=(URL,time.time(),TIME))
    alert_thread.start()
def unlock_alert_thread(URL,START_TIME, DEL_TIME):

    if(lessthanTime(START_TIME))


    #Give an option to reset the time? But this qould require using GTK.


def help():
    print("Help:\n\n")
    print("Commands:\n")
    print("block <URL>: blocks a specific url indefinitely(Min: 1 hour))\n")
    print("block <URL> <TIME>: blocks a specific url with a timer(With manual unblocking)\n")
    print("unblock <URL>: Unblocks a URL\n")
    print("unblock-all: Unblocks all currently blocked websites\n") 
    print("block-file <FILE-NAME>: Blocks all websites listed in a file\n")
    print("refresh-blocks: Refreshes all blocks")
    print("refresh-blocks<TIME>: Refreshes all blocks for another timer period")
    print("list-blocks: Lists all active blocks\n")
    print("help: Displays this page\n")
    print("Date Format: #d#h#m, where # corresponds to the number of units, d for days, h for hours, m for minutes.")

def less_than_time(endTime):
    if endTime<time.time():
        return false
    return true

def block(URL,endTime):
    block_site(URL)
    #Do time stuff

    
def block_site(URL):
    #Blocks a website
    if url.startsWith("http"):
        url=url.split("//")[2]
    if url.startsWith("www"):
        shortenedURL=url.split(".")[2]
    else:
        shortenedURL=url
        url="www."+url
    if not site_blocked(shortenedURL):
        with open("/etc/hosts","a") as hostsFile:
            hostsFile.write("127.0.0.1 "+shortenedURL)
    #if website starts with www
        #block removing "www."URL
    #else, block for with www and current URL
def site_blocked(URL):#Determines if a website has been blocked already
    hostsFile=open("/etc/hosts")
    for line in hostsFile:
        if (URL in line)and ("127.0.0.1" in line) and "#" not in line:
            hostsFile.close()
            return true
    hostsFile.close()
    return false 
def unblock_all_sites():
    with open("/etc/hosts","r+") as hostsFile:
        for line in hostsFile:
            if("127.0.0.1" in line and "#" not in line and "localhost" not in line):
                line="#"+line




#def removeCommentedSites():
    #with open("/etc/hosts","r+") as hostsFile:
        #newHostsFile=file.new())
        #for line in hostsFile:
            #if("127.0.0.1" in line and line.startsWith("#")):
                ##Remove LIne
