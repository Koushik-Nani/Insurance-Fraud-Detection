#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Sep 28, 2023 07:27:58 PM IST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import Gui

_debug = True # False to eliminate debug printing from callback functions.

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = Gui.Toplevel1(_top1)
    
    root.mainloop()

if __name__ == '__main__':
    Gui.start_up()




