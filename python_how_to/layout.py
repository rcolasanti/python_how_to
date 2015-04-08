#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2015  <ric.colasanti@gmail.com>
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
from Tkinter import Tk, Text, BOTH, W, N, E, S,Y,RIGHT,LEFT,YES,Scrollbar,Listbox
from ttk import Frame, Button, Label, Style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure 


class TkinterGraph(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.figure = Figure(figsize=(10,10), dpi=50)
        self.graph_a = self.figure.add_subplot(111)
        self.graph_a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])



        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.show()
        self.canvas._tkcanvas.pack(fill=BOTH, expand=1)


class ScrolledList(Frame):
    def __init__(self, master,d_list,a_function):
        Frame.__init__(self,master)
        
        scrl_bar = Scrollbar(self)
        self.listbox = Listbox(self)
        
        scrl_bar.config(command=self.listbox.yview)                   
        scrl_bar.pack(side=RIGHT, fill=Y)                     
        
        self.listbox.config(yscrollcommand=scrl_bar.set)              
        self.listbox.pack(side=LEFT, expand=YES, fill=BOTH)       
        
        #load the listbox
        idx = 0
        for item in d_list:      
            fparts = item.split('.')
            # DEBUG print fparts
            if fparts[-1] == 'csv':
                self.listbox.insert(idx, item)                       
                idx += 1

        # link double click to the processList
        self.listbox.bind('<Double-1>', self.processList)  
        # attach a function passed form the master
        # not this si done as passd function so it could be anything       
        self.passed_function = a_function
        
    # get the index of the double clicked itenm and pass the item to
    # the passed function    
    def processList(self, event):
        index = self.listbox.curselection()               
        label = self.listbox.get(index)  
        self.passed_function((index,label))
        
class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Graphs")
        self.style = Style()
        self.style.theme_use("clam")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(6, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        
        lbl = Label(self, text="Graphs")
        lbl.grid(sticky=W, pady=4, padx=5)
        
        area1 =  ScrolledList(self,['a','b,','c','d','e'],lambda x: self.load_hunt_data(x))
        area1.grid(row=1, column=0, columnspan=3, rowspan=4, 
            padx=5, sticky=E+W+S+N)

        area2 = TkinterGraph(self)
        area2.grid(row=1, column=3, columnspan=2, rowspan=4, 
            padx=5, sticky=E+W+S+N)
        
        btn1 = Button(self, text="Left")
        btn1.grid(row=1, column=6)

        btn2 = Button(self, text="Right")
        btn2.grid(row=2, column=6, pady=4)
        
        btn3 = Button(self, text="csv")
        btn3.grid(row=5, column=0, padx=5)
        
        btn5 = Button(self, text="dat")
        btn5.grid(row=5, column=2, padx=5)

        btn4 = Button(self, text="OK")
        btn4.grid(row=5, column=6) 
               
    def load_hunt_data(self,selection):
        pass
                    

def main():
  
    root = Tk()
    root.geometry("850x500+500+500")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  
