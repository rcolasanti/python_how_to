#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2015  <code.colasanti@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from Tkinter import Tk, LEFT, Menu,Label
from tkFileDialog   import askopenfilename
from os.path import join,split
"""A stub program for a tk interface fro a python program"""
class TkStub:
    def __init__(self):
        root = Tk()
        root.title("tk_stub")
        root.geometry("400x200")
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Load data",command = self.do_this)
        self.notifcation = Label(root,text="")
        self.notifcation.grid(row=0,column=0)

        root.mainloop()
        
    def do_this(self):
        name = askopenfilename() 
        (d_path,d_name)=split(name)
        self.notifcation.config(text=join(d_path,d_name))
        
        
def main():
    TkStub()
    return 0

if __name__ == '__main__':
    main()

