#!/usr/bin/python
 
from gi.repository import AppIndicator3 as Appindicator
from gi.repository import Notify
from gi.repository import Gtk
import pdb
import os
import json
import jsonpickle
import ast
import time
import thread


class LockoutIndicator(object):
        def __init__(self):
            self.ind = Appindicator.Indicator.new("Lockout",
                    'badge-small', Appindicator.IndicatorCategory.APPLICATION_STATUS)
            self.ind.set_label("Lockout","LockoutIndicator") 
            self.ind.set_status (Appindicator.IndicatorStatus.ACTIVE)
            self.render()
        def render(self):
            self.menu = Gtk.Menu()
            lockoutMenu = Gtk.MenuItem("Lock myself out for...")
            lockoutMenuSub = Gtk.Menu()
            lockoutMenu.set_submenu(lockoutMenuSub)
            oneHourQuickOption = Gtk.MenuItem("One hour")
            oneDayQuickOption = Gtk.MenuItem("One day")
            customOption = Gtk.MenuItem("Custom time")
            lockoutMenuSub.append(oneHourQuickOption)
            lockoutMenuSub.append(oneDayQuickOption)
            lockoutMenuSub.append(customOption)
            self.menu.append(lockoutMenu)

            exit = Gtk.MenuItem("Exit")
            exit.connect('activate', Gtk.main_quit)

            self.menu.append(exit);
            self.menu.show_all()
            self.ind.set_menu(self.menu)


indicator = LockoutIndicator()

Gtk.main()
