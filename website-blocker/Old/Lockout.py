#Lockout
#By David Finder
import time
from gi.repository import AppIndicator3 as Appindicator
from gi.repository import Notify
from gi.repository import Gtk
import pdb
import os
import json
import jsonpickle
import ast
import threading
import LockoutEnforcer.py

## Get time to end
def Lockout(endTime):
    #Check to see if there's already an instance 
    #of this running? or should that go in menu?

    ## get settings
    with open("~/appBlackList") as f:
        appBlackList=f.readLines()
    with open("~/webBlackList") as f:
        appBlackList=f.readLines()
    ## Don't need hashes for the blacklists, because we only read them once.
    ## Set up a chron job respawn self.
    ## Spawn lockout enforcer
    warnings=0
    enforcer=threading.Thread(target=LockoutEnforcer.Enforcer,args=(appBlackList,webBlackList,))
    enforcer.start()
    while lessThanTime(endTime): ## Change to while time is less than stop time.
        ## If LockoutEnforcer doesn't exist
        if not enforcer.isAlive():
            ## respawn it
            enforcer.start()
            ## Give the user a warning
            warnings++
            userWarning=threading.Thread(target=warnUser)
            userWarning.start()
                
    ## If the user is warned enough, restart unity
    if(warnings>5):
        os.system('unity&')

    ## If the chron job doesn't exist
    ## Respawn it

## Disable the chronjob.


def lessThanTime(endTime):
    if endTime<time.time():
        return false
    return true

class warnUser(Gtk.Window):
    def __init__(self):
        super(warnUser,self).__init__()
        self.setPosition(Gtk.WindowPosition.CENTER)
        self.set_title("No, stop that")
        self.set_border_width(20)
        self.connect('delete-event',self.quit)
        self.box=Gtk.HBox(spacing=6)
        self.button=Gtk.Button(label="Ok...")
        self.button.connect('clicked',self.quit)
        self.showall()
    def quit(self,window,connection):
        Gtk.Widget.destroy(self)

def closeApp(processName):
    pass
